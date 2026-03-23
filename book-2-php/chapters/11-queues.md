# Chapter 11: Queue System

## 1. Do Not Make the User Wait

Your app sends welcome emails on signup, generates PDF invoices, and resizes uploaded images. Each task takes 2 to 30 seconds. Do them inside the HTTP request and the user stares at a spinner while the server processes. That is a broken experience.

Queues move slow work to a background process. The handler drops a job onto a queue and responds immediately. A separate consumer picks it up. The user sees "Welcome -- check your email." in under 100 milliseconds. The email arrives 5 seconds later.

Tina4 has a built-in queue system. Works out of the box with SQLite. No Redis. No RabbitMQ. No external services. Add jobs. Process them.

---

## 2. Why Queues Matter

Without queues:

```
User clicks "Sign Up"
  -> Server validates input (10ms)
  -> Server creates user in database (20ms)
  -> Server sends welcome email (3000ms)
  -> Server generates PDF welcome kit (2000ms)
  -> Server resizes avatar (1500ms)
  -> User sees response (6530ms later)
```

With queues:

```
User clicks "Sign Up"
  -> Server validates input (10ms)
  -> Server creates user in database (20ms)
  -> Server queues: send welcome email (1ms)
  -> Server queues: generate PDF (1ms)
  -> Server queues: resize avatar (1ms)
  -> User sees response (33ms later)

Meanwhile, in the background:
  -> Consumer sends welcome email
  -> Consumer generates PDF
  -> Consumer resizes avatar
```

6.5 seconds becomes 33 milliseconds. The work still happens. Just not during the HTTP request.

Beyond speed, queues provide:

- **Retry logic**: Email server down. Job retries automatically.
- **Rate limiting**: Process at a controlled pace. Do not overwhelm external services.
- **Fault isolation**: A failed PDF does not crash the signup request.
- **Scaling**: More consumers for higher load.

---

## 3. SQLite Queue (Default)

SQLite backend by default. No configuration. First job creates `data/queue.db` automatically.

### Producing a Job

```php
<?php
use Tina4Router;
use Tina4\Queue;

Router::post("/api/register", function ($request, $response) {
    $body = $request->body;

    // Create the user (database logic)
    $userId = 42; // Simulated

    // Queue a welcome email
    Queue::produce("send-welcome-email", [
        "user_id" => $userId,
        "email" => $body["email"],
        "name" => $body["name"]
    ]);

    return $response->json([
        "message" => "Registration successful. Welcome email will arrive shortly.",
        "user_id" => $userId
    ], 201);
});
```

```bash
curl -X POST http://localhost:7146/api/register \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com", "password": "securePass123"}'
```

```json
{
  "message": "Registration successful. Welcome email will arrive shortly.",
  "user_id": 42
}
```

Response returns immediately. The email job waits in the queue.

### The Queue::produce() Method

```php
Queue::produce($queueName, $payload, $options = []);
```

- **$queueName**: String identifying the queue. Consumers subscribe by name.
- **$payload**: Associative array. Must be JSON-serializable.
- **$options**: Delay, priority, max retries.

### Producing with Options

```php
// Delay 60 seconds
Queue::produce("send-reminder", [
    "user_id" => 42,
    "message" => "Do not forget to verify your email!"
], ["delay" => 60]);

// Max retries (default is 3)
Queue::produce("generate-invoice", [
    "order_id" => 101,
    "format" => "pdf"
], ["max_retries" => 5]);

// Priority (lower number = higher priority)
Queue::produce("resize-image", [
    "image_path" => "/uploads/photo.jpg",
    "sizes" => [100, 300, 600]
], ["priority" => 1]);
```

---

## 4. Consuming Jobs

A consumer listens for jobs on a named queue and processes them. Define consumers in `src/routes/` (or any auto-loaded file):

```php
<?php
use Tina4\Queue;

Queue::consume("send-welcome-email", function ($job) {
    $email = $job->payload["email"];
    $name = $job->payload["name"];

    error_log("Sending welcome email to " . $email . " for " . $name);

    // Return true to mark completed
    return true;
});
```

### Starting the Consumer

```bash
tina4 queue:work
```

```
Queue worker started
  Listening on: all queues
  Backend: sqlite:///data/queue.db
  Polling interval: 1s

[2026-03-22 14:30:01] Processing job #1 on "send-welcome-email"
[2026-03-22 14:30:01] Job #1 completed in 45ms
```

The worker polls every second. Picks up pending jobs. Calls your callback.

### Listening to Specific Queues

```bash
# One queue
tina4 queue:work --queue send-welcome-email

# Multiple queues
tina4 queue:work --queue send-welcome-email,generate-invoice
```

### Running Multiple Workers

```bash
# Terminal 1
tina4 queue:work --queue send-welcome-email

# Terminal 2
tina4 queue:work --queue generate-invoice

# Terminal 3
tina4 queue:work --queue resize-image
```

One worker per queue. Jobs processed in parallel.

---

## 5. Job Lifecycle

Every job moves through states:

```
pending -> reserved -> completed
                    -> failed -> pending (retry)
                              -> dead (max retries exceeded)
```

### Pending

Waiting in the queue. No worker has claimed it yet.

### Reserved

A worker claimed it. Processing. Other workers will not touch it. If the worker crashes, the job returns to `pending` after a timeout.

### Completed

Consumer returned `true`. Done. Removed from the active queue.

### Failed

Consumer returned `false` or threw an exception. Scheduled for retry.

### Dead Letter

Max retries exceeded. No more automatic retries. Needs human attention.

### Inspecting Job State

```php
<?php
use Tina4\Queue;

$stats = Queue::stats("send-welcome-email");
```

```php
[
    "queue" => "send-welcome-email",
    "pending" => 12,
    "reserved" => 2,
    "completed" => 1453,
    "failed" => 3,
    "dead" => 1
]
```

Also visible in the dev dashboard at `/tina4/console` under "Queue Manager".

---

## 6. Retry Logic and Max Retries

Failed jobs retry with exponential backoff:

- Retry 1: after 10 seconds
- Retry 2: after 30 seconds
- Retry 3: after 90 seconds

Default max: 3 retries. After the third failure, the job moves to dead letter.

### Handling Failures

```php
<?php
use Tina4\Queue;

Queue::consume("send-welcome-email", function ($job) {
    $email = $job->payload["email"];

    try {
        $success = sendEmail($email, "Welcome!", "Welcome to our platform.");

        if (!$success) {
            error_log("Failed to send email to " . $email . " (attempt " . $job->attempts . ")");
            return false; // Triggers retry
        }

        return true;

    } catch (\Exception $e) {
        error_log("Exception sending email to " . $email . ": " . $e->getMessage());
        return false;
    }
});
```

### Custom Max Retries

```php
// Critical: retry 10 times
Queue::produce("send-password-reset", [
    "email" => "alice@example.com",
    "token" => "abc123"
], ["max_retries" => 10]);

// Non-critical: retry once
Queue::produce("send-marketing-email", [
    "email" => "bob@example.com",
    "campaign" => "spring-sale"
], ["max_retries" => 1]);
```

### Accessing Attempt Count

```php
Queue::consume("generate-invoice", function ($job) {
    error_log("Processing invoice (attempt " . $job->attempts . " of " . $job->maxRetries . ")");

    if ($job->attempts >= 3) {
        error_log("Using fallback invoice generator");
    }

    return true;
});
```

---

## 7. Dead Letter Queue

Jobs that exhausted their retries. Something is wrong. Email server is down permanently. PDF template is broken. Input data is invalid.

### Viewing Dead Letter Jobs

```bash
tina4 queue:dead
```

```
Dead Letter Queue
-----------------
Job #42  Queue: send-welcome-email  Failed: 3 times  Last error: "Connection refused"
  Payload: {"user_id": 42, "email": "alice@example.com", "name": "Alice"}
  First attempt: 2026-03-22 14:30:00
  Last attempt:  2026-03-22 14:35:30

Job #67  Queue: generate-invoice  Failed: 3 times  Last error: "Template not found"
  Payload: {"order_id": 101, "format": "pdf"}
  First attempt: 2026-03-22 15:00:00
  Last attempt:  2026-03-22 15:05:00
```

### Re-Queuing

Fix the underlying issue. Then retry:

```bash
# Specific job
tina4 queue:retry 42

# All dead jobs for a queue
tina4 queue:retry --queue send-welcome-email

# All dead jobs
tina4 queue:retry --all
```

### Clearing

Job no longer relevant (user signed up again, order cancelled):

```bash
# Specific job
tina4 queue:clear 42

# Older than 7 days
tina4 queue:clear --older-than 7d
```

---

## 8. Switching to RabbitMQ

Higher throughput. Message durability across restarts. Distributed processing. One line in `.env`:

```env
TINA4_QUEUE_BACKEND=rabbitmq
TINA4_QUEUE_HOST=localhost
TINA4_QUEUE_PORT=5672
TINA4_QUEUE_USERNAME=guest
TINA4_QUEUE_PASSWORD=guest
TINA4_QUEUE_VHOST=/
```

Code unchanged. Same `Queue::produce()` and `Queue::consume()`. Tina4 handles the protocol.

### When to Switch

| Feature | SQLite Queue | RabbitMQ |
|---------|-------------|----------|
| Setup | Zero config | Requires RabbitMQ server |
| Throughput | Hundreds of jobs/sec | Tens of thousands |
| Multi-server | Single server only | Multiple servers, distributed |
| Persistence | File-based | Durable queues, survives restarts |
| Monitoring | Dev dashboard | RabbitMQ Management UI |
| Best for | Development, small apps | Production, high-volume |

---

## 9. Switching to Kafka

Event streaming at scale. Millions of events per second. Event replay. Multiple consumer groups.

```env
TINA4_QUEUE_BACKEND=kafka
TINA4_QUEUE_HOST=localhost
TINA4_QUEUE_PORT=9092
TINA4_QUEUE_GROUP_ID=my-app-workers
```

Same API. Same code.

### When to Use Kafka

- Millions of events per second
- Multiple independent consumers reading the same events
- Event replay (re-process historical events)
- Event-driven microservices

For most applications: SQLite for development, RabbitMQ for production. Kafka when you outgrow RabbitMQ.

---

## 9b. Switching to MongoDB

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
composer require ext-mongodb
```

Same API. Same code. Same `Queue::produce()` and `Queue::consume()` calls.

---

## 10. Monitoring via Dev Dashboard

`TINA4_DEBUG=true` activates the "Queue Manager" in `/tina4/console`:

- **Queue overview**: pending, reserved, completed, failed, dead counts per queue
- **Recent jobs**: last 50 processed with status, duration, payload
- **Failed jobs**: error messages, retry counts
- **Dead letter queue**: jobs that exhausted retries
- **Throughput graph**: jobs per minute over the last hour

Full visibility without command-line tools.

---

## 11. Producing Multiple Jobs

One action. Multiple background tasks:

```php
<?php
use Tina4Router;
use Tina4\Queue;

Router::post("/api/orders", function ($request, $response) {
    $body = $request->body;

    $orderId = 101;
    $userId = $body["user_id"];

    Queue::produce("send-order-confirmation", [
        "order_id" => $orderId,
        "email" => $body["email"]
    ]);

    Queue::produce("generate-invoice", [
        "order_id" => $orderId,
        "format" => "pdf"
    ]);

    Queue::produce("update-inventory", [
        "items" => $body["items"]
    ]);

    Queue::produce("notify-warehouse", [
        "order_id" => $orderId,
        "shipping_address" => $body["shipping_address"]
    ]);

    return $response->json([
        "message" => "Order placed successfully",
        "order_id" => $orderId
    ], 201);
});
```

Four jobs queued in under 5 milliseconds. Instant response. Email, invoice, inventory, warehouse notification -- all in the background.

---

## 12. Exercise: Build an Email Queue

Queue-based email for user signup. Queue the welcome email. Write a consumer.

### Requirements

1. `POST /api/signup` endpoint:
   - Accepts `name`, `email`, `password`
   - Queues a job on `welcome-emails`
   - Returns immediately

2. Consumer for `welcome-emails`:
   - Logs email details (simulating send)
   - Includes user name
   - Returns `true` on success

3. `GET /api/queue/stats` endpoint showing queue statistics

### Test with:

```bash
# Register
curl -X POST http://localhost:7146/api/signup \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com", "password": "securePass123"}'

# Register another
curl -X POST http://localhost:7146/api/signup \
  -H "Content-Type: application/json" \
  -d '{"name": "Bob", "email": "bob@example.com", "password": "anotherPass456"}'

# Check stats (2 pending)
curl http://localhost:7146/api/queue/stats

# Start worker in another terminal
tina4 queue:work --queue welcome-emails

# Check stats again (2 completed)
curl http://localhost:7146/api/queue/stats
```

---

## 13. Solution

Create `src/routes/email-queue.php`:

```php
<?php
use Tina4Router;
use Tina4\Queue;

/**
 * @noauth
 */
Router::post("/api/signup", function ($request, $response) {
    $body = $request->body;

    if (empty($body["name"]) || empty($body["email"]) || empty($body["password"])) {
        return $response->json(["error" => "Name, email, and password are required"], 400);
    }

    $userId = rand(1, 10000);

    Queue::produce("welcome-emails", [
        "user_id" => $userId,
        "name" => $body["name"],
        "email" => $body["email"],
        "signed_up_at" => date("c")
    ]);

    return $response->json([
        "message" => "Signup successful. A welcome email will be sent shortly.",
        "user_id" => $userId
    ], 201);
});

Queue::consume("welcome-emails", function ($job) {
    $name = $job->payload["name"];
    $email = $job->payload["email"];
    $userId = $job->payload["user_id"];

    error_log("=== Welcome Email ===");
    error_log("To: " . $email);
    error_log("Subject: Welcome to our platform, " . $name . "!");
    error_log("Body: Hi " . $name . ", your account (ID: " . $userId . ") has been created.");
    error_log("Signed up: " . $job->payload["signed_up_at"]);
    error_log("=====================");

    return true;
});

Router::get("/api/queue/stats", function ($request, $response) {
    $stats = Queue::stats("welcome-emails");

    return $response->json([
        "queue" => "welcome-emails",
        "stats" => $stats
    ]);
});
```

**Signup output:** `201 Created`

```json
{
  "message": "Signup successful. A welcome email will be sent shortly.",
  "user_id": 4829
}
```

**Stats before processing:**

```json
{
  "queue": "welcome-emails",
  "stats": {
    "queue": "welcome-emails",
    "pending": 2,
    "reserved": 0,
    "completed": 0,
    "failed": 0,
    "dead": 0
  }
}
```

**Worker output:**

```
[2026-03-22 14:30:01] Processing job #1 on "welcome-emails"
=== Welcome Email ===
To: alice@example.com
Subject: Welcome to our platform, Alice!
Body: Hi Alice, your account (ID: 4829) has been created.
Signed up: 2026-03-22T14:30:00+00:00
=====================
[2026-03-22 14:30:01] Job #1 completed in 2ms

[2026-03-22 14:30:02] Processing job #2 on "welcome-emails"
=== Welcome Email ===
To: bob@example.com
Subject: Welcome to our platform, Bob!
Body: Hi Bob, your account (ID: 7213) has been created.
Signed up: 2026-03-22T14:30:00+00:00
=====================
[2026-03-22 14:30:02] Job #2 completed in 1ms
```

**Stats after processing:**

```json
{
  "queue": "welcome-emails",
  "stats": {
    "queue": "welcome-emails",
    "pending": 0,
    "reserved": 0,
    "completed": 2,
    "failed": 0,
    "dead": 0
  }
}
```

---

## 14. Gotchas

### 1. Worker Must Be Running Separately

**Problem:** Jobs produced. Nothing happens. Queue fills up.

**Cause:** No worker process. Producing adds to the queue. A separate process must consume.

**Fix:** Run `tina4 queue:work` in another terminal. In production, use `supervisord` or `systemd` to keep the worker alive.

### 2. Consumer Not Registered

**Problem:** Worker starts. Reports "No consumer found for queue: my-queue".

**Cause:** `Queue::consume()` call is in a file the worker did not load.

**Fix:** Put the consumer in `src/routes/`. The `tina4 queue:work` command loads the same files as the web server.

### 3. Job Payload Is Not Serializable

**Problem:** `Queue::produce()` throws a serialization error.

**Cause:** You passed an object, database connection, file handle, or other non-serializable value.

**Fix:** Payload must contain only simple types: strings, numbers, booleans, arrays of these. Pass IDs, not objects. The consumer looks up records by ID.

### 4. Jobs Process in Wrong Order

**Problem:** Jobs arrive out of order.

**Cause:** Multiple workers process in parallel. No guaranteed ordering.

**Fix:** For ordering, use a single worker. Or include a sequence number in the payload. For most use cases (emails, PDFs), order does not matter.

### 5. SQLite Queue Lock Contention

**Problem:** Multiple workers on the same SQLite queue cause "database is locked" errors.

**Cause:** SQLite supports one writer at a time. Multiple workers compete for the same file.

**Fix:** Switch to RabbitMQ, Kafka, or MongoDB. SQLite queues are for single-worker setups and development.

### 6. Consumer Returns Nothing

**Problem:** Jobs process but immediately fail and retry.

**Cause:** No `return true`. PHP returns `null`. Tina4 interprets `null` as failure.

**Fix:** Always `return true` on success. `return false` on failure. Do not forget the `return`.

### 7. Dead Letter Jobs Accumulate

**Problem:** Dead letter queue grows. Nobody notices.

**Cause:** No monitoring or alerting.

**Fix:** Check `Queue::stats()` periodically. Set up alerts when the dead count exceeds a threshold. In production, integrate with monitoring (Prometheus, Datadog). Review dead letters regularly -- they reveal consumer bugs and external service failures.
