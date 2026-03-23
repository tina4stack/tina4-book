# Chapter 11: Queues

## 1. Not Everything Should Happen Right Now

Some tasks are too slow for an HTTP request. Sending an email: 2 seconds. Generating a PDF report: 10 seconds. Processing a large CSV upload: a minute. Run these inside a route handler and the user stares at a spinner. Or the request times out.

Queues solve this. Push a message describing the work. A separate worker picks it up and does the job in the background. The user gets an instant response: "Your report is being generated."

Picture a store that sends order confirmations, generates invoices, and syncs inventory with a warehouse. None of these should block checkout. Each one becomes a queue message. A worker processes it on its own schedule.

---

## 2. Queue Configuration

Tina4 Python includes a built-in database-backed queue that requires zero additional setup. It uses your existing database connection to store queue messages.

### Default (Database Queue)

The database queue works out of the box with no extra configuration:

```env
# No TINA4_QUEUE_BACKEND needed -- database is the default
DATABASE_URL=sqlite:///data/app.db
```

The first time you push a message, Tina4 automatically creates the `tina4_queue` table.

### Switching to RabbitMQ

When your application outgrows the database queue (millions of messages, multiple services, pub/sub patterns), switch to RabbitMQ by changing the config:

```env
TINA4_QUEUE_BACKEND=rabbitmq
RABBITMQ_URL=amqp://user:pass@localhost:5672
```

Install the client library:

```bash
uv add pika
```

### Switching to Kafka

For stream processing, event sourcing, or very high throughput:

```env
TINA4_QUEUE_BACKEND=kafka
KAFKA_BROKERS=localhost:9092
KAFKA_GROUP_ID=tina4-workers
```

Install the client library:

```bash
uv add confluent-kafka
```

### Switching to MongoDB

```env
TINA4_QUEUE_BACKEND=mongodb
TINA4_MONGO_HOST=localhost
TINA4_MONGO_PORT=27017
TINA4_MONGO_DB=tina4
TINA4_MONGO_COLLECTION=tina4_queue
# Or use a full URI:
# TINA4_MONGO_URI=mongodb://user:pass@host:27017/tina4
```

MongoDB uses `findOneAndUpdate` for atomic job claiming -- no double-processing. Install the driver:

```bash
uv add pymongo
```

The key point: your code stays the same. `Queue`, `push`, `pop`, and `worker` work identically whether the backend is SQLite, PostgreSQL, RabbitMQ, Kafka, or MongoDB.

---

## 3. Pushing Messages

```python
from tina4_python.queue import Queue

queue = Queue("emails")

# Push a message
message_id = queue.push("emails", {
    "to": "alice@example.com",
    "subject": "Order Confirmation",
    "body": "Your order #1234 has been confirmed."
})
```

The first argument is the queue name. The second is the payload -- any dictionary that can be serialized to JSON.

### Priority

Higher priority messages are processed first:

```python
# Normal priority (default: 0)
queue.push("emails", {"to": "user@example.com", "subject": "Newsletter"})

# High priority
queue.push("emails", {"to": "user@example.com", "subject": "Password Reset"}, priority=10)
```

### Delayed Messages

Schedule a message to be processed later:

```python
# Process in 5 minutes
queue.push("reminders", {
    "user_id": 42,
    "message": "Your trial expires tomorrow"
}, delay=300)

# Process at a specific time
queue.push("reports", {
    "report_type": "monthly",
    "month": "2026-03"
}, available_at="2026-04-01T00:00:00Z")
```

### Max Attempts

Control how many times a failed message is retried:

```python
queue.push("emails", payload, max_attempts=5)  # Default is 3
```

---

## 4. Consuming Messages

### Simple Worker

```python
from tina4_python.queue import Queue

queue = Queue("emails")

@queue.worker(concurrency=1, poll_interval=1)
def process_email(message):
    payload = message.payload
    send_email(payload["to"], payload["subject"], payload["body"])
    # Returning without error = auto-complete
    # Raising an exception = auto-fail with retry
```

The worker polls the queue every `poll_interval` seconds, pops a message, and calls your function. If the function returns normally, the message is marked as completed. If it raises an exception, the message is marked as failed and retried (up to `max_attempts`).

### Manual Pop

For more control, pop messages manually:

```python
message = queue.pop("emails")

if message is not None:
    try:
        send_email(message.payload["to"], message.payload["subject"])
        queue.complete(message)
    except Exception as e:
        queue.fail(message, str(e))
```

### Batch Processing

Pop multiple messages at once:

```python
messages = queue.pop_batch("emails", count=10)

for msg in messages:
    try:
        process(msg.payload)
        queue.complete(msg)
    except Exception as e:
        queue.fail(msg, str(e))
```

---

## 5. Message Lifecycle

A message moves through these statuses:

```
push() → PENDING → pop() → RESERVED → complete() → COMPLETED
                                     → fail() → FAILED
                                                   ↓
                                              retry (auto)
                                                   ↓
                                              PENDING (retry)
                                                   ↓
                                         max attempts exceeded
                                                   ↓
                                            DEAD_LETTER
```

### Status Definitions

| Status | Description |
|--------|-------------|
| `pending` | Waiting to be processed |
| `reserved` | Claimed by a worker, being processed |
| `completed` | Successfully processed |
| `failed` | Processing failed, will be retried |
| `dead_letter` | Failed too many times, requires manual intervention |

### Inspecting Messages

```python
# Get a specific message by ID
message = queue.get(message_id)
print(message.status)      # "pending", "reserved", "completed", etc.
print(message.attempts)    # How many times it has been tried
print(message.error)       # Last error message if failed

# Search messages
pending = queue.find("emails", status="pending")
failed = queue.find("emails", status="failed", limit=50)
```

---

## 6. Retry and Dead Letters

### Automatic Retry with Exponential Backoff

When a message fails, Tina4 retries it with exponential backoff:

```
Attempt 1 fails → retry in 30 seconds
Attempt 2 fails → retry in 120 seconds
Attempt 3 fails → moved to dead letter queue
```

The backoff formula is: `delay = base_delay * (2 ^ (attempt - 1))`

Default base delay is 30 seconds.

### Dead Letter Queue

Messages that exceed `max_attempts` are moved to dead letter status. They are not retried automatically -- you must handle them manually.

```python
# List dead letter messages
dead_messages = queue.dead_letter("emails")

for msg in dead_messages:
    print(f"Failed message: {msg.id}")
    print(f"  Payload: {msg.payload}")
    print(f"  Error: {msg.error}")
    print(f"  Attempts: {msg.attempts}")
```

### Manual Retry

You can manually retry a dead letter message:

```python
# Retry a single message (resets attempts, moves back to pending)
queue.retry(message)
```

### Purging Dead Letters

```python
queue.purge("emails")  # Remove all messages from the queue
```

---

## 7. Queue in Route Handlers

The most common pattern is pushing messages from route handlers:

```python
from tina4_python.core.router import post
from tina4_python.queue import Queue

@post("/api/orders")
async def create_order(request, response):
    body = request.body
    db = Database()

    # Create the order in the database
    db.execute(
        "INSERT INTO orders (user_id, total, status) VALUES (:user_id, :total, :status)",
        {"user_id": body["user_id"], "total": body["total"], "status": "confirmed"}
    )

    order = db.fetch_one("SELECT * FROM orders WHERE id = last_insert_rowid()")

    # Queue background tasks
    queue = Queue()

    # Send confirmation email
    queue.push("emails", {
        "type": "order_confirmation",
        "to": body["email"],
        "order_id": order["id"],
        "total": order["total"]
    })

    # Generate invoice PDF
    queue.push("invoices", {
        "order_id": order["id"],
        "format": "pdf"
    }, delay=5)  # Small delay to ensure order is fully saved

    # Sync with warehouse
    queue.push("warehouse_sync", {
        "order_id": order["id"],
        "items": body["items"]
    }, priority=5)

    return response.json({
        "message": "Order created",
        "order": order
    }, 201)
```

The user gets an instant response. The email, invoice, and warehouse sync happen in the background.

---

## 8. Switching Backends via .env

Switching backends is a config change, not a code change.

### Development: SQLite

```env
DATABASE_URL=sqlite:///data/app.db
# No TINA4_QUEUE_BACKEND needed -- database is default
```

### Staging: PostgreSQL Database Queue

```env
DATABASE_URL=postgresql://user:pass@localhost:5432/myapp
# Still using database queue, but now with PostgreSQL's FOR UPDATE SKIP LOCKED
# for safe concurrent workers
```

### Production: RabbitMQ

```env
TINA4_QUEUE_BACKEND=rabbitmq
RABBITMQ_URL=amqp://user:pass@rabbitmq.internal:5672
```

### High-Scale Production: Kafka

```env
TINA4_QUEUE_BACKEND=kafka
KAFKA_BROKERS=kafka-1:9092,kafka-2:9092,kafka-3:9092
KAFKA_GROUP_ID=tina4-workers
```

### Production: MongoDB

```env
TINA4_QUEUE_BACKEND=mongodb
TINA4_MONGO_URI=mongodb://user:pass@mongo.internal:27017/tina4
TINA4_MONGO_COLLECTION=tina4_queue
```

Your queue code does not change at all. The same `queue.push()` and `@queue.worker()` calls work with every backend.

### Fallback Configuration

If your RabbitMQ goes down, Tina4 can fall back to the database queue automatically:

```env
TINA4_QUEUE_BACKEND=rabbitmq
RABBITMQ_URL=amqp://user:pass@rabbitmq.internal:5672
QUEUE_FALLBACK_DRIVER=database
```

When RabbitMQ is unreachable, messages are stored in the database queue. When RabbitMQ comes back, processing resumes normally. Your application never stops accepting work.

---

## 9. Stale Job Recovery

If a worker crashes while processing a message, the message stays in `reserved` status forever. Tina4 automatically recovers these stale messages with a background sweep that runs every 60 seconds:

Messages stuck in `reserved` for longer than 5 minutes (configurable) are moved back to `pending` so another worker can pick them up.

```env
TINA4_QUEUE_STALE_TIMEOUT=300  # 5 minutes (default)
```

---

## 10. Exercise: Build an Email Queue

Build an email queue system that sends emails in the background.

### Requirements

1. Create these endpoints:

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/emails/send` | Queue an email for sending |
| `GET` | `/api/emails/status/{id}` | Check the status of a queued email |
| `GET` | `/api/emails/queue` | List pending and failed emails |
| `POST` | `/api/emails/retry/{id}` | Retry a failed email |

2. The email payload should include: `to` (required), `subject` (required), `body` (required), `priority` ("low", "normal", "high")

3. Map priority strings to numeric values: low=0, normal=5, high=10

4. The status endpoint should return the message status, attempts, and error (if any)

5. Create a simulated email worker that "sends" emails by printing to the console and waiting 1 second

### Test with:

```bash
# Queue an email
curl -X POST http://localhost:7145/api/emails/send \
  -H "Content-Type: application/json" \
  -d '{"to": "alice@example.com", "subject": "Welcome!", "body": "Thanks for signing up.", "priority": "high"}'

# Check status
curl http://localhost:7145/api/emails/status/MESSAGE_ID_HERE

# List queue
curl http://localhost:7145/api/emails/queue

# Retry failed
curl -X POST http://localhost:7145/api/emails/retry/MESSAGE_ID_HERE
```

---

## 11. Solution

Create `src/routes/email_queue.py`:

```python
from tina4_python.core.router import get, post
from tina4_python.queue import Queue

queue = Queue()

PRIORITY_MAP = {
    "low": 0,
    "normal": 5,
    "high": 10
}


@post("/api/emails/send")
async def queue_email(request, response):
    body = request.body

    errors = []
    if not body.get("to"):
        errors.append("'to' is required")
    if not body.get("subject"):
        errors.append("'subject' is required")
    if not body.get("body"):
        errors.append("'body' is required")

    priority_name = body.get("priority", "normal")
    if priority_name not in PRIORITY_MAP:
        errors.append(f"'priority' must be one of: {', '.join(PRIORITY_MAP.keys())}")

    if errors:
        return response.json({"errors": errors}, 400)

    priority = PRIORITY_MAP[priority_name]

    message_id = queue.push("emails", {
        "to": body["to"],
        "subject": body["subject"],
        "body": body["body"],
        "priority_name": priority_name
    }, priority=priority)

    return response.json({
        "message": "Email queued for sending",
        "message_id": message_id,
        "priority": priority_name
    }, 201)


@get("/api/emails/status/{id}")
async def email_status(request, response):
    message_id = request.params["id"]

    message = queue.get(message_id)

    if message is None:
        return response.json({"error": "Message not found"}, 404)

    return response.json({
        "id": message.id,
        "status": message.status,
        "queue": message.queue,
        "payload": message.payload,
        "attempts": message.attempts,
        "max_attempts": message.max_attempts,
        "error": message.error,
        "created_at": message.created_at,
        "completed_at": message.completed_at,
        "failed_at": message.failed_at
    })


@get("/api/emails/queue")
async def list_email_queue(request, response):
    status_filter = request.query.get("status", "pending")

    messages = queue.find("emails", status=status_filter, limit=50)

    items = []
    for msg in messages:
        items.append({
            "id": msg.id,
            "to": msg.payload.get("to"),
            "subject": msg.payload.get("subject"),
            "status": msg.status,
            "attempts": msg.attempts,
            "error": msg.error,
            "created_at": msg.created_at
        })

    queue_size = queue.size("emails")

    return response.json({
        "messages": items,
        "count": len(items),
        "total_queue_size": queue_size
    })


@post("/api/emails/retry/{id}")
async def retry_email(request, response):
    message_id = request.params["id"]

    message = queue.get(message_id)

    if message is None:
        return response.json({"error": "Message not found"}, 404)

    if message.status not in ("failed", "dead_letter"):
        return response.json({
            "error": f"Cannot retry a message with status '{message.status}'. Only 'failed' or 'dead_letter' messages can be retried."
        }, 400)

    queue.retry(message)

    return response.json({
        "message": "Email queued for retry",
        "id": message_id
    })
```

Create a separate worker file `src/workers/email_worker.py`:

```python
from tina4_python.queue import Queue
import time

queue = Queue()

@queue.worker(concurrency=1, poll_interval=2)
def send_email(message):
    payload = message.payload

    print(f"Sending email to {payload['to']}...")
    print(f"  Subject: {payload['subject']}")
    print(f"  Body: {payload['body'][:50]}...")

    # Simulate sending (replace with real email sending)
    time.sleep(1)

    print(f"  Email sent to {payload['to']} successfully!")
```

**Expected output for queuing an email:**

```json
{
  "message": "Email queued for sending",
  "message_id": "550e8400-e29b-41d4-a716-446655440000",
  "priority": "high"
}
```

(Status: `201 Created`)

**Expected output for checking status (before processing):**

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "pending",
  "queue": "emails",
  "payload": {
    "to": "alice@example.com",
    "subject": "Welcome!",
    "body": "Thanks for signing up.",
    "priority_name": "high"
  },
  "attempts": 0,
  "max_attempts": 3,
  "error": null,
  "created_at": "2026-03-22T16:00:00Z",
  "completed_at": null,
  "failed_at": null
}
```

**Expected output for checking status (after processing):**

```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "completed",
  "attempts": 1,
  "completed_at": "2026-03-22T16:00:02Z"
}
```

---

## 12. Gotchas

### 1. Queue table not created

**Problem:** Pushing a message fails with a "table not found" error.

**Cause:** The `tina4_queue` table has not been created yet. This usually happens when using a new database.

**Fix:** Tina4 auto-creates the queue table on first use. If that fails, run a migration or create the table manually. Check that your `DATABASE_URL` is correct and the database is accessible.

### 2. Worker not picking up messages

**Problem:** Messages are pushed but nothing happens -- the worker is not processing them.

**Cause:** The worker process is not running, or it is polling a different queue name.

**Fix:** Make sure the worker is running (`python src/workers/email_worker.py` or via the Tina4 CLI). Check that the queue name in `queue.push("emails", ...)` matches the queue name in `@queue.worker()`.

### 3. Message processed twice

**Problem:** A message is processed by two workers simultaneously.

**Cause:** If using SQLite without WAL mode, concurrent access can cause race conditions.

**Fix:** For production with multiple workers, use PostgreSQL (which has `FOR UPDATE SKIP LOCKED`), RabbitMQ, or MongoDB. SQLite is fine for single-worker setups. Enable WAL mode for SQLite: `PRAGMA journal_mode=WAL;`

### 4. Payload too large

**Problem:** Pushing a message with a large payload fails or is slow.

**Cause:** The payload is serialized to JSON and stored in the database. Very large payloads (multiple MB) slow down the queue.

**Fix:** Keep payloads small. Instead of putting file contents in the payload, store the file on disk or in object storage and put the file path in the payload. Payloads should be metadata, not data.

### 5. Dead letters pile up

**Problem:** The dead letter queue grows indefinitely.

**Cause:** Failed messages that exceed max_attempts move to dead letter status but are never cleaned up.

**Fix:** Monitor your dead letter queue. Set up an alert when dead letters exceed a threshold. Either fix the underlying issue and retry them, or purge them after investigation. Completed messages older than 7 days are automatically purged by default.

### 6. Environment-specific queue name collision

**Problem:** Your development and staging environments process each other's queue messages.

**Cause:** Both environments use the same database or RabbitMQ instance and the same queue names.

**Fix:** Prefix queue names with the environment: `queue.push("dev_emails", ...)` or use separate database/RabbitMQ instances per environment. The simplest approach is separate databases.

### 7. Blocking the event loop

**Problem:** Your async Tina4 server becomes unresponsive while the queue worker is processing.

**Cause:** The queue worker's `time.sleep()` or CPU-intensive work blocks the async event loop.

**Fix:** Run queue workers as separate processes, not inside the web server process. Use `python src/workers/email_worker.py` as a separate command, or use Tina4's CLI: `tina4 worker emails`. For CPU-intensive work inside async handlers, use `asyncio.to_thread()` to run blocking code in a thread pool.
