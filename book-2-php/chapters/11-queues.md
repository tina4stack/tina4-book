# Chapter 11: Queue System

## 1. Do Not Make the User Wait

Your app sends welcome emails on signup, generates PDF invoices, and resizes uploaded images. Each of these tasks takes between two and thirty seconds. If you do them inside the HTTP request, the user stares at a loading spinner while the server processes their email, renders their invoice, and resizes their photo. That is a terrible experience.

Queues solve this by moving slow work to a background process. The HTTP handler drops a job onto a queue and immediately responds to the user. A separate consumer process picks up the job and does the work at its own pace. The user sees "Welcome! Check your email." in under 100 milliseconds, and the email arrives 5 seconds later.

Tina4 has a built-in queue system that works out of the box with SQLite. No Redis, no RabbitMQ, no external services. Just add jobs and process them.

---

## 2. Why Queues Matter

Without queues:

```
User clicks "Sign Up"
  → Server validates input (10ms)
  → Server creates user in database (20ms)
  → Server sends welcome email (3000ms)
  → Server generates PDF welcome kit (2000ms)
  → Server resizes avatar (1500ms)
  → User sees response (6530ms later)
```

With queues:

```
User clicks "Sign Up"
  → Server validates input (10ms)
  → Server creates user in database (20ms)
  → Server queues: send welcome email (1ms)
  → Server queues: generate PDF (1ms)
  → Server queues: resize avatar (1ms)
  → User sees response (33ms later)

Meanwhile, in the background:
  → Consumer sends welcome email
  → Consumer generates PDF
  → Consumer resizes avatar
```

The user's experience goes from 6.5 seconds to 33 milliseconds. The work still gets done -- just not during the HTTP request.

Beyond speed, queues provide:

- **Retry logic**: If the email server is down, the job retries automatically
- **Rate limiting**: Process jobs at a controlled pace to avoid overwhelming external services
- **Fault isolation**: A failed PDF generation does not crash the signup request
- **Scaling**: Run more consumer processes to handle higher load

---

## 3. SQLite Queue (Default)

Tina4's queue system uses SQLite by default. No configuration needed. When you produce your first job, Tina4 creates a `data/queue.db` database automatically.

### Producing a Job

```php
<?php
use Tina4\Route;
use Tina4\Queue;

Route::post("/api/register", function ($request, $response) {
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
curl -X POST http://localhost:7145/api/register \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com", "password": "securePass123"}'
```

```json
{
  "message": "Registration successful. Welcome email will arrive shortly.",
  "user_id": 42
}
```

The response returns immediately. The email job is sitting in the queue, waiting to be processed.

### The Queue::produce() Method

```php
Queue::produce($queueName, $payload, $options = []);
```

- **$queueName**: A string that identifies which queue to put the job on. Consumers subscribe to specific queues by name.
- **$payload**: An associative array of data the consumer needs to process the job. Must be JSON-serializable.
- **$options**: Optional settings like delay, priority, and max retries.

### Producing with Options

```php
// Delay the job by 60 seconds (useful for "send reminder in 1 minute")
Queue::produce("send-reminder", [
    "user_id" => 42,
    "message" => "Do not forget to verify your email!"
], ["delay" => 60]);

// Set max retries (default is 3)
Queue::produce("generate-invoice", [
    "order_id" => 101,
    "format" => "pdf"
], ["max_retries" => 5]);

// Set priority (lower number = higher priority)
Queue::produce("resize-image", [
    "image_path" => "/uploads/photo.jpg",
    "sizes" => [100, 300, 600]
], ["priority" => 1]);
```

---

## 4. Consuming Jobs

A consumer listens for jobs on a specific queue and processes them. Define consumers in `src/routes/` (or any auto-loaded file):

```php
<?php
use Tina4\Queue;

Queue::consume("send-welcome-email", function ($job) {
    $email = $job->payload["email"];
    $name = $job->payload["name"];

    // Send the email (using Messenger, covered in Chapter 13)
    error_log("Sending welcome email to " . $email . " for " . $name);

    // Simulate email sending
    // In a real app, you would use Tina4\Messenger here

    // Return true to mark the job as completed
    return true;
});
```

### Starting the Consumer

Run the consumer process with the Tina4 CLI:

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

The worker polls the queue every second, picks up pending jobs, and calls your consumer callback.

### Listening to Specific Queues

```bash
# Process only email jobs
tina4 queue:work --queue send-welcome-email

# Process multiple specific queues
tina4 queue:work --queue send-welcome-email,generate-invoice
```

### Running Multiple Workers

For higher throughput, run multiple worker processes:

```bash
# Terminal 1
tina4 queue:work --queue send-welcome-email

# Terminal 2
tina4 queue:work --queue generate-invoice

# Terminal 3
tina4 queue:work --queue resize-image
```

Each worker handles one queue. Jobs on different queues are processed in parallel.

---

## 5. Job Lifecycle

Every job moves through a series of states:

```
pending → reserved → completed
                  → failed → pending (retry)
                           → dead (max retries exceeded)
```

### Pending

The job is in the queue, waiting to be picked up. It stays here until a worker claims it.

### Reserved

A worker has claimed the job and is processing it. Other workers will not pick it up. If the worker crashes during processing, the job returns to `pending` after a timeout.

### Completed

The consumer returned `true`. The job is done and removed from the active queue.

### Failed

The consumer returned `false` or threw an exception. The job moves to `failed` state and is scheduled for retry.

### Dead Letter

A job that has exceeded its maximum retry count moves to the dead letter queue. It will not be retried automatically. You can inspect and re-queue dead letter jobs manually.

### Inspecting Job State

```php
<?php
use Tina4\Queue;

// Get queue statistics
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

You can also see these stats in the dev dashboard at `/tina4/console` under the "Queue Manager" section.

---

## 6. Retry Logic and Max Retries

When a job fails, Tina4 automatically retries it with exponential backoff:

- Retry 1: after 10 seconds
- Retry 2: after 30 seconds
- Retry 3: after 90 seconds

The default max retry count is 3. After the third failure, the job moves to the dead letter queue.

### Handling Failures in Consumers

```php
<?php
use Tina4\Queue;

Queue::consume("send-welcome-email", function ($job) {
    $email = $job->payload["email"];

    try {
        // Attempt to send the email
        $success = sendEmail($email, "Welcome!", "Welcome to our platform.");

        if (!$success) {
            error_log("Failed to send email to " . $email . " (attempt " . $job->attempts . ")");
            return false; // Triggers retry
        }

        return true; // Job completed

    } catch (\Exception $e) {
        error_log("Exception sending email to " . $email . ": " . $e->getMessage());
        return false; // Triggers retry
    }
});
```

### Custom Max Retries

Set max retries when producing the job:

```php
// Critical emails: retry up to 10 times
Queue::produce("send-password-reset", [
    "email" => "alice@example.com",
    "token" => "abc123"
], ["max_retries" => 10]);

// Non-critical: retry only once
Queue::produce("send-marketing-email", [
    "email" => "bob@example.com",
    "campaign" => "spring-sale"
], ["max_retries" => 1]);
```

### Accessing Attempt Count

The `$job` object tells you which attempt this is:

```php
Queue::consume("generate-invoice", function ($job) {
    error_log("Processing invoice (attempt " . $job->attempts . " of " . $job->maxRetries . ")");

    if ($job->attempts >= 3) {
        // On the last attempt, try a fallback approach
        error_log("Using fallback invoice generator");
    }

    return true;
});
```

---

## 7. Dead Letter Queue

Jobs that exceed their max retries land in the dead letter queue. These jobs need human attention -- maybe the email server is permanently down, the PDF template is broken, or the input data is invalid.

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

### Re-Queuing Dead Letter Jobs

Once you have fixed the underlying issue (started the email server, fixed the template), re-queue the dead letter jobs:

```bash
# Re-queue a specific job
tina4 queue:retry 42

# Re-queue all dead letter jobs for a specific queue
tina4 queue:retry --queue send-welcome-email

# Re-queue all dead letter jobs
tina4 queue:retry --all
```

### Clearing Dead Letter Jobs

If a dead letter job is no longer relevant (the user signed up again, the order was cancelled), remove it:

```bash
# Remove a specific dead letter job
tina4 queue:clear 42

# Remove all dead letter jobs older than 7 days
tina4 queue:clear --older-than 7d
```

---

## 8. Switching to RabbitMQ

For production deployments that need higher throughput, message durability across server restarts, and distributed processing, switch to RabbitMQ. Change one line in `.env`:

```env
TINA4_QUEUE_BACKEND=rabbitmq
TINA4_QUEUE_HOST=localhost
TINA4_QUEUE_PORT=5672
TINA4_QUEUE_USERNAME=guest
TINA4_QUEUE_PASSWORD=guest
TINA4_QUEUE_VHOST=/
```

Your code does not change. The same `Queue::produce()` and `Queue::consume()` calls work with RabbitMQ as the backend. Tina4 handles the protocol differences internally.

### Why Switch?

| Feature | SQLite Queue | RabbitMQ |
|---------|-------------|----------|
| Setup | Zero config | Requires RabbitMQ server |
| Throughput | Hundreds of jobs/sec | Tens of thousands of jobs/sec |
| Multi-server | Single server only | Multiple servers, distributed |
| Persistence | File-based | Durable queues, survives restarts |
| Monitoring | Dev dashboard | RabbitMQ Management UI |
| Best for | Development, small apps | Production, high-volume apps |

---

## 9. Switching to Kafka

For event streaming at scale (millions of events per second, event replay, multiple consumer groups), switch to Kafka:

```env
TINA4_QUEUE_BACKEND=kafka
TINA4_QUEUE_HOST=localhost
TINA4_QUEUE_PORT=9092
TINA4_QUEUE_GROUP_ID=my-app-workers
```

Again, your code stays the same. The `Queue::produce()` and `Queue::consume()` API is identical across all backends.

### When to Use Kafka

- You need to process millions of events per second
- Multiple independent consumers need to read the same events
- You need event replay (re-process historical events)
- You are building event-driven microservices

For most applications, SQLite (development) and RabbitMQ (production) are the right choices. Kafka is for when you outgrow RabbitMQ.

---

## 10. Monitoring via Dev Dashboard

When `TINA4_DEBUG=true`, the dev dashboard at `/tina4/console` shows a "Queue Manager" section with:

- **Queue overview**: pending, reserved, completed, failed, and dead counts for each queue
- **Recent jobs**: the last 50 processed jobs with their status, duration, and payload
- **Failed jobs**: jobs that failed with their error messages and retry count
- **Dead letter queue**: jobs that exceeded max retries
- **Throughput graph**: jobs processed per minute over the last hour

This gives you visibility into your queue system without command-line tools.

---

## 11. Producing Multiple Jobs

Sometimes a single action triggers multiple background tasks:

```php
<?php
use Tina4\Route;
use Tina4\Queue;

Route::post("/api/orders", function ($request, $response) {
    $body = $request->body;

    // Create the order (database logic)
    $orderId = 101;
    $userId = $body["user_id"];

    // Queue multiple background tasks
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

```bash
curl -X POST http://localhost:7145/api/orders \
  -H "Content-Type: application/json" \
  -d '{"user_id": 42, "email": "alice@example.com", "items": [{"product_id": 1, "quantity": 2}], "shipping_address": "123 Main St"}'
```

```json
{"message":"Order placed successfully","order_id":101}
```

Four jobs are queued in under 5 milliseconds. The user gets an instant response. The email, invoice, inventory update, and warehouse notification happen in the background.

---

## 12. Exercise: Build an Email Queue

Build a queue-based email system for user signup. When a user registers, queue a welcome email. Write a consumer that processes the email jobs.

### Requirements

1. Create a `POST /api/signup` endpoint that:
   - Accepts `name`, `email`, and `password`
   - Queues a job on the `welcome-emails` queue
   - Returns immediately with a success message

2. Create a consumer for the `welcome-emails` queue that:
   - Logs the email details (simulating sending)
   - Includes the user's name in the log message
   - Returns `true` on success

3. Create a `GET /api/queue/stats` endpoint that shows the queue statistics

### Test with:

```bash
# Register a user
curl -X POST http://localhost:7145/api/signup \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com", "password": "securePass123"}'

# Register another user
curl -X POST http://localhost:7145/api/signup \
  -H "Content-Type: application/json" \
  -d '{"name": "Bob", "email": "bob@example.com", "password": "anotherPass456"}'

# Check queue stats (should show 2 pending)
curl http://localhost:7145/api/queue/stats

# Start the worker in another terminal
tina4 queue:work --queue welcome-emails

# Check stats again (should show 2 completed)
curl http://localhost:7145/api/queue/stats
```

---

## 13. Solution

Create `src/routes/email-queue.php`:

```php
<?php
use Tina4\Route;
use Tina4\Queue;

/**
 * @noauth
 */
Route::post("/api/signup", function ($request, $response) {
    $body = $request->body;

    // Validate input
    if (empty($body["name"]) || empty($body["email"]) || empty($body["password"])) {
        return $response->json(["error" => "Name, email, and password are required"], 400);
    }

    // Simulate user creation (in a real app, save to database)
    $userId = rand(1, 10000);

    // Queue the welcome email
    Queue::produce("welcome-emails", [
        "user_id" => $userId,
        "name" => $body["name"],
        "email" => $body["email"],
        "signed_up_at" => date("c")
    ]);

    return $response->json([
        "message" => "Signup successful! A welcome email will be sent shortly.",
        "user_id" => $userId
    ], 201);
});

// Consumer for welcome emails
Queue::consume("welcome-emails", function ($job) {
    $name = $job->payload["name"];
    $email = $job->payload["email"];
    $userId = $job->payload["user_id"];

    // In a real app, use Tina4\Messenger to send the email
    // For now, we log it
    error_log("=== Welcome Email ===");
    error_log("To: " . $email);
    error_log("Subject: Welcome to our platform, " . $name . "!");
    error_log("Body: Hi " . $name . ", your account (ID: " . $userId . ") has been created.");
    error_log("Signed up: " . $job->payload["signed_up_at"]);
    error_log("=====================");

    return true;
});

// Queue statistics endpoint
Route::get("/api/queue/stats", function ($request, $response) {
    $stats = Queue::stats("welcome-emails");

    return $response->json([
        "queue" => "welcome-emails",
        "stats" => $stats
    ]);
});
```

**Expected output -- signup:**

```bash
curl -X POST http://localhost:7145/api/signup \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com", "password": "securePass123"}'
```

```json
{
  "message": "Signup successful! A welcome email will be sent shortly.",
  "user_id": 4829
}
```

(Status: `201 Created`)

**Expected output -- stats before processing:**

```bash
curl http://localhost:7145/api/queue/stats
```

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

**Expected worker output:**

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

**Expected output -- stats after processing:**

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

**Problem:** You produce jobs but nothing happens. The queue fills up but jobs are never processed.

**Cause:** The queue worker is not running. Producing a job only adds it to the queue -- you need a separate process to consume it.

**Fix:** Run `tina4 queue:work` in a separate terminal. In production, use a process manager like `supervisord` or `systemd` to keep the worker running.

### 2. Consumer Not Registered

**Problem:** The worker starts but reports "No consumer found for queue: my-queue".

**Cause:** The `Queue::consume()` call is in a file that the worker did not load. The worker must discover the consumer registration.

**Fix:** Make sure your consumer is registered in a file inside `src/routes/` so it is auto-loaded. The `tina4 queue:work` command loads the same files as the web server.

### 3. Job Payload Is Not Serializable

**Problem:** `Queue::produce()` throws an error about serialization.

**Cause:** You passed an object, a database connection, a file handle, or another non-serializable value in the payload.

**Fix:** Only pass simple data types in the payload: strings, numbers, booleans, and arrays of these types. If you need to reference a database record, pass the ID, not the record itself. The consumer can look up the record by ID.

### 4. Jobs Process in Wrong Order

**Problem:** Jobs are processed in a different order than they were produced.

**Cause:** With multiple workers, jobs are distributed across workers and processed in parallel. There is no guaranteed ordering.

**Fix:** If order matters, use a single worker for that queue. Or include a sequence number in the payload and handle ordering in the consumer logic. For most use cases (sending emails, generating PDFs), order does not matter.

### 5. SQLite Queue Lock Contention

**Problem:** Multiple workers on the same SQLite queue cause "database is locked" errors.

**Cause:** SQLite supports only one writer at a time. Multiple workers competing for the same SQLite database create contention.

**Fix:** For multiple workers, switch to RabbitMQ or Kafka. SQLite queues are designed for single-worker setups and development environments.

### 6. Consumer Returns Nothing

**Problem:** Jobs are processed but immediately marked as failed and retried.

**Cause:** Your consumer function does not return `true`. Without an explicit `return true`, PHP returns `null`, which Tina4 interprets as failure.

**Fix:** Always `return true` when the job succeeds and `return false` when it fails. Do not forget the `return` statement.

### 7. Dead Letter Jobs Accumulate

**Problem:** The dead letter queue grows over time and nobody notices.

**Cause:** No monitoring or alerting is set up for dead letter jobs.

**Fix:** Check `Queue::stats()` periodically or set up an alert when the dead count exceeds a threshold. In production, integrate with your monitoring system (Prometheus, Datadog, etc.) to track dead letter counts. Review dead letter jobs regularly -- they often reveal bugs in your consumer logic or issues with external services.
