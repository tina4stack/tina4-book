# Chapter 11: Queue System

## 1. Do Not Make the User Wait

Your app sends welcome emails on signup. Generates PDF invoices. Resizes uploaded images. Each task takes 2 to 30 seconds. Run them inside the HTTP request and the user stares at a spinner while the server grinds through email delivery, invoice rendering, and image resizing.

Queues move slow work to a background process. The HTTP handler drops a job onto a queue and responds to the user in under 100 milliseconds. A separate consumer picks up the job and does the work at its own pace. The user sees "Welcome! Check your email." The email arrives 5 seconds later.

Tina4's queue system works out of the box with SQLite. No Redis. No RabbitMQ. No external services. Add jobs and process them.

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

6.5 seconds becomes 33 milliseconds. The user feels the difference.

---

## 3. SQLite Queue (Default)

Tina4's queue system uses SQLite by default. No configuration needed. When you produce your first job, Tina4 creates a `data/queue.db` database automatically.

### Producing a Job

```ruby
Tina4::Router.post("/api/register") do |request, response|
  body = request.body

  # Create the user (database logic)
  user_id = 42 # Simulated

  # Queue a welcome email
  Tina4::Queue.produce("send-welcome-email", {
    user_id: user_id,
    email: body["email"],
    name: body["name"]
  })

  response.json({
    message: "Registration successful. Welcome email will arrive shortly.",
    user_id: user_id
  }, 201)
end
```

```bash
curl -X POST http://localhost:7147/api/register \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com", "password": "securePass123"}'
```

```json
{
  "message": "Registration successful. Welcome email will arrive shortly.",
  "user_id": 42
}
```

### The Queue.produce Method

```ruby
Tina4::Queue.produce(queue_name, payload, options = {})
```

- **queue_name**: A string that identifies which queue to put the job on.
- **payload**: A hash of data the consumer needs to process the job.
- **options**: Optional settings like delay, priority, and max retries.

### Producing with Options

```ruby
# Delay the job by 60 seconds
Tina4::Queue.produce("send-reminder", {
  user_id: 42,
  message: "Do not forget to verify your email!"
}, { delay: 60 })

# Set max retries (default is 3)
Tina4::Queue.produce("generate-invoice", {
  order_id: 101,
  format: "pdf"
}, { max_retries: 5 })

# Set priority (lower number = higher priority)
Tina4::Queue.produce("resize-image", {
  image_path: "/uploads/photo.jpg",
  sizes: [100, 300, 600]
}, { priority: 1 })
```

---

## 4. Consuming Jobs

A consumer listens for jobs on a specific queue and processes them:

```ruby
Tina4::Queue.consume("send-welcome-email") do |job|
  email = job.payload["email"]
  name = job.payload["name"]

  $stderr.puts "Sending welcome email to #{email} for #{name}"

  # In a real app, you would use Tina4::Messenger here

  true  # Return true to mark the job as completed
end
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

### Listening to Specific Queues

```bash
tina4 queue:work --queue send-welcome-email

tina4 queue:work --queue send-welcome-email,generate-invoice
```

---

## 5. Job Lifecycle

Every job moves through a series of states:

```
pending -> reserved -> completed
                    -> failed -> pending (retry)
                              -> dead (max retries exceeded)
```

### Inspecting Job State

```ruby
stats = Tina4::Queue.stats("send-welcome-email")
```

```ruby
{
  "queue" => "send-welcome-email",
  "pending" => 12,
  "reserved" => 2,
  "completed" => 1453,
  "failed" => 3,
  "dead" => 1
}
```

---

## 6. Retry Logic and Max Retries

When a job fails, Tina4 automatically retries it with exponential backoff:

- Retry 1: after 10 seconds
- Retry 2: after 30 seconds
- Retry 3: after 90 seconds

### Handling Failures in Consumers

```ruby
Tina4::Queue.consume("send-welcome-email") do |job|
  email = job.payload["email"]

  begin
    success = send_email(email, "Welcome!", "Welcome to our platform.")

    unless success
      $stderr.puts "Failed to send email to #{email} (attempt #{job.attempts})"
      next false  # Triggers retry
    end

    true  # Job completed

  rescue => e
    $stderr.puts "Exception sending email to #{email}: #{e.message}"
    false  # Triggers retry
  end
end
```

---

## 7. Dead Letter Queue

Jobs that exceed their max retries land in the dead letter queue.

### Viewing Dead Letter Jobs

```bash
tina4 queue:dead
```

### Re-Queuing Dead Letter Jobs

```bash
tina4 queue:retry 42
tina4 queue:retry --queue send-welcome-email
tina4 queue:retry --all
```

### Clearing Dead Letter Jobs

```bash
tina4 queue:clear 42
tina4 queue:clear --older-than 7d
```

---

## 8. Switching to RabbitMQ

For production deployments:

```env
TINA4_QUEUE_BACKEND=rabbitmq
TINA4_QUEUE_HOST=localhost
TINA4_QUEUE_PORT=5672
TINA4_QUEUE_USERNAME=guest
TINA4_QUEUE_PASSWORD=guest
TINA4_QUEUE_VHOST=/
```

Your code does not change. The same `Tina4::Queue.produce` and `Tina4::Queue.consume` calls work with RabbitMQ as the backend.

---

## 9. Switching to Kafka

For event streaming at scale:

```env
TINA4_QUEUE_BACKEND=kafka
TINA4_QUEUE_HOST=localhost
TINA4_QUEUE_PORT=9092
TINA4_QUEUE_GROUP_ID=my-app-workers
```

---

## 10. Monitoring via Dev Dashboard

When `TINA4_DEBUG=true`, the dev dashboard at `/tina4/console` shows a "Queue Manager" section with:

- Queue overview: pending, reserved, completed, failed, and dead counts
- Recent jobs: the last 50 processed jobs
- Failed jobs with error messages and retry counts
- Dead letter queue
- Throughput graph: jobs processed per minute

---

## 11. Producing Multiple Jobs

Sometimes a single action triggers multiple background tasks:

```ruby
Tina4::Router.post("/api/orders") do |request, response|
  body = request.body
  order_id = 101

  Tina4::Queue.produce("send-order-confirmation", {
    order_id: order_id,
    email: body["email"]
  })

  Tina4::Queue.produce("generate-invoice", {
    order_id: order_id,
    format: "pdf"
  })

  Tina4::Queue.produce("update-inventory", {
    items: body["items"]
  })

  Tina4::Queue.produce("notify-warehouse", {
    order_id: order_id,
    shipping_address: body["shipping_address"]
  })

  response.json({
    message: "Order placed successfully",
    order_id: order_id
  }, 201)
end
```

Four jobs are queued in under 5 milliseconds. The user gets an instant response.

---

## 12. Exercise: Build an Email Queue

Build a queue-based email system for user signup.

### Requirements

1. Create a `POST /api/signup` endpoint that queues a job on the `welcome-emails` queue
2. Create a consumer for the `welcome-emails` queue that logs the email details
3. Create a `GET /api/queue/stats` endpoint that shows the queue statistics

### Test with:

```bash
curl -X POST http://localhost:7147/api/signup \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com", "password": "securePass123"}'

curl http://localhost:7147/api/queue/stats

tina4 queue:work --queue welcome-emails

curl http://localhost:7147/api/queue/stats
```

---

## 13. Solution

Create `src/routes/email_queue.rb`:

```ruby
# @noauth
Tina4::Router.post("/api/signup") do |request, response|
  body = request.body

  if body["name"].nil? || body["email"].nil? || body["password"].nil?
    return response.json({ error: "Name, email, and password are required" }, 400)
  end

  user_id = rand(1..10000)

  Tina4::Queue.produce("welcome-emails", {
    user_id: user_id,
    name: body["name"],
    email: body["email"],
    signed_up_at: Time.now.iso8601
  })

  response.json({
    message: "Signup successful! A welcome email will be sent shortly.",
    user_id: user_id
  }, 201)
end

Tina4::Queue.consume("welcome-emails") do |job|
  name = job.payload["name"]
  email = job.payload["email"]
  user_id = job.payload["user_id"]

  $stderr.puts "=== Welcome Email ==="
  $stderr.puts "To: #{email}"
  $stderr.puts "Subject: Welcome to our platform, #{name}!"
  $stderr.puts "Body: Hi #{name}, your account (ID: #{user_id}) has been created."
  $stderr.puts "Signed up: #{job.payload['signed_up_at']}"
  $stderr.puts "====================="

  true
end

Tina4::Router.get("/api/queue/stats") do |request, response|
  stats = Tina4::Queue.stats("welcome-emails")

  response.json({
    queue: "welcome-emails",
    stats: stats
  })
end
```

---

## 14. Gotchas

### 1. Worker Must Be Running Separately

**Problem:** You produce jobs but nothing happens.

**Fix:** Run `tina4 queue:work` in a separate terminal.

### 2. Consumer Not Registered

**Problem:** The worker reports "No consumer found for queue: my-queue".

**Fix:** Make sure your consumer is in a file inside `src/routes/`.

### 3. Job Payload Is Not Serializable

**Problem:** `Queue.produce` throws an error about serialization.

**Fix:** Only pass simple data types in the payload. If you need to reference a database record, pass the ID.

### 4. Jobs Process in Wrong Order

**Problem:** Jobs are processed in a different order than they were produced.

**Fix:** With multiple workers, jobs are processed in parallel. Use a single worker if order matters.

### 5. SQLite Queue Lock Contention

**Problem:** Multiple workers on the same SQLite queue cause "database is locked" errors.

**Fix:** For multiple workers, switch to RabbitMQ or Kafka.

### 6. Consumer Returns Nothing

**Problem:** Jobs are processed but immediately marked as failed.

**Cause:** Your consumer block does not return `true`. Without an explicit `true`, Ruby returns the result of the last expression, which might be `nil`.

**Fix:** Always return `true` when the job succeeds and `false` when it fails.

### 7. Dead Letter Jobs Accumulate

**Problem:** The dead letter queue grows over time.

**Fix:** Check `Tina4::Queue.stats` periodically. Review dead letter jobs regularly.
