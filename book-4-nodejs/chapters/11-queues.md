# Chapter 11: Queue System

## 1. Do Not Make the User Wait

Your app sends welcome emails on signup. Generates PDF invoices. Resizes uploaded images. Each task takes 2 to 30 seconds. Run them inside the HTTP request and the user stares at a spinner.

Queues move slow work to a background process. The user gets a response in milliseconds. The work still happens -- just not during the request.

Tina4 has a built-in queue system. Works out of the box with SQLite. No Redis. No RabbitMQ. No external services.

---

## 2. Why Queues Matter

Without queues: 6530ms response time. With queues: 33ms. Same work done. Different timing.

Queues also deliver retry logic, rate limiting, fault isolation, and horizontal scaling.

---

## 3. SQLite Queue (Default)

### Producing a Job

```typescript
import { Router, Queue } from "tina4-nodejs";

Router.post("/api/register", async (req, res) => {
    const body = req.body;
    const userId = 42;

    await Queue.produce("send-welcome-email", {
        user_id: userId,
        email: body.email,
        name: body.name
    });

    return res.status(201).json({
        message: "Registration successful. Welcome email will arrive shortly.",
        user_id: userId
    });
});
```

### Producing with Options

```typescript
// Delay by 60 seconds
await Queue.produce("send-reminder", { user_id: 42, message: "Verify your email!" }, { delay: 60 });

// Set max retries
await Queue.produce("generate-invoice", { order_id: 101 }, { maxRetries: 5 });

// Set priority (lower = higher priority)
await Queue.produce("resize-image", { image_path: "/uploads/photo.jpg" }, { priority: 1 });
```

---

## 4. Consuming Jobs

```typescript
import { Queue } from "tina4-nodejs";

Queue.consume("send-welcome-email", async (job) => {
    const { email, name } = job.payload;

    console.log(`Sending welcome email to ${email} for ${name}`);

    return true; // Mark as completed
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

### Running Multiple Workers

```bash
tina4 queue:work --queue send-welcome-email
tina4 queue:work --queue generate-invoice
```

---

## 5. Job Lifecycle

```
pending → reserved → completed
                  → failed → pending (retry)
                           → dead (max retries exceeded)
```

### Queue Statistics

```typescript
const stats = await Queue.stats("send-welcome-email");
// { queue: "send-welcome-email", pending: 12, reserved: 2, completed: 1453, failed: 3, dead: 1 }
```

---

## 6. Retry Logic

Retries use exponential backoff: 10s, 30s, 90s. Default max retries: 3.

```typescript
Queue.consume("send-welcome-email", async (job) => {
    try {
        const success = await sendEmail(job.payload.email, "Welcome!", "Welcome to our platform.");
        if (!success) {
            console.log(`Failed to send email (attempt ${job.attempts})`);
            return false; // Triggers retry
        }
        return true;
    } catch (e) {
        console.log(`Exception: ${e.message}`);
        return false;
    }
});
```

---

## 7. Dead Letter Queue

```bash
tina4 queue:dead
tina4 queue:retry 42
tina4 queue:retry --queue send-welcome-email
tina4 queue:clear --older-than 7d
```

---

## 8. Switching to RabbitMQ

```env
TINA4_QUEUE_BACKEND=rabbitmq
TINA4_QUEUE_HOST=localhost
TINA4_QUEUE_PORT=5672
TINA4_QUEUE_USERNAME=guest
TINA4_QUEUE_PASSWORD=guest
```

Your code stays identical. Same `Queue.produce()` and `Queue.consume()` calls. The backend is an implementation detail.

---

## 9. Switching to Kafka

```env
TINA4_QUEUE_BACKEND=kafka
TINA4_QUEUE_HOST=localhost
TINA4_QUEUE_PORT=9092
TINA4_QUEUE_GROUP_ID=my-app-workers
```

---

## 10. Multiple Jobs from One Action

```typescript
Router.post("/api/orders", async (req, res) => {
    const orderId = 101;

    await Queue.produce("send-order-confirmation", { order_id: orderId, email: req.body.email });
    await Queue.produce("generate-invoice", { order_id: orderId, format: "pdf" });
    await Queue.produce("update-inventory", { items: req.body.items });
    await Queue.produce("notify-warehouse", { order_id: orderId, shipping_address: req.body.shipping_address });

    return res.status(201).json({ message: "Order placed successfully", order_id: orderId });
});
```

---

## 11. Exercise: Build an Email Queue

Create `POST /api/signup` that queues a welcome email, a consumer that logs it, and `GET /api/queue/stats`.

---

## 12. Solution

```typescript
import { Router, Queue } from "tina4-nodejs";

/**
 * @noauth
 */
Router.post("/api/signup", async (req, res) => {
    const body = req.body;
    if (!body.name || !body.email || !body.password) {
        return res.status(400).json({ error: "Name, email, and password are required" });
    }

    const userId = Math.floor(Math.random() * 10000);

    await Queue.produce("welcome-emails", {
        user_id: userId,
        name: body.name,
        email: body.email,
        signed_up_at: new Date().toISOString()
    });

    return res.status(201).json({
        message: "Signup successful! A welcome email will be sent shortly.",
        user_id: userId
    });
});

Queue.consume("welcome-emails", async (job) => {
    const { name, email, user_id } = job.payload;
    console.log(`=== Welcome Email ===`);
    console.log(`To: ${email}`);
    console.log(`Subject: Welcome to our platform, ${name}!`);
    console.log(`Body: Hi ${name}, your account (ID: ${user_id}) has been created.`);
    console.log(`=====================`);
    return true;
});

Router.get("/api/queue/stats", async (req, res) => {
    const stats = await Queue.stats("welcome-emails");
    return res.json({ queue: "welcome-emails", stats });
});
```

---

## 13. Gotchas

### 1. Worker Must Be Running Separately

**Fix:** Run `tina4 queue:work` in a separate terminal.

### 2. Consumer Not Registered

**Fix:** Put `Queue.consume()` in a file inside `src/routes/`.

### 3. Job Payload Must Be JSON-Serializable

**Fix:** Only pass simple data types. Pass IDs, not full objects.

### 4. Jobs Process in Wrong Order

**Fix:** Use a single worker for ordered processing. Most use cases do not need ordering.

### 5. SQLite Queue Lock Contention

**Fix:** For multiple workers, switch to RabbitMQ or Kafka.

### 6. Consumer Returns Nothing

**Fix:** Always `return true` on success, `return false` on failure.

### 7. Dead Letter Jobs Accumulate

**Fix:** Monitor `Queue.stats()` and set up alerts.
