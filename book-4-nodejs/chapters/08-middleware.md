# Chapter 8: Middleware

## 1. The Gatekeepers

Your API needs CORS headers for the React frontend, rate limiting for the public endpoints, and auth checking for admin routes -- all without cluttering your route handlers. Middleware solves this. It lets you wrap routes with reusable logic that runs before (or after) the handler. Each middleware does one job and passes control to the next layer.

In Chapter 2 you saw a brief introduction to middleware. This chapter goes deep: built-in middleware, custom middleware, execution order, short-circuiting, and real-world patterns.

---

## 2. What Middleware Is

A middleware function sits between the incoming HTTP request and your route handler. It receives the request, the response, and a `next` function:

```typescript
async function passthrough(req, res, next) {
    return next(req, res);
}
```

And one that blocks everything:

```typescript
async function blockEverything(req, res, next) {
    return res.status(503).json({ error: "Service unavailable" });
}
```

---

## 3. Built-in CorsMiddleware

```env
CORS_ORIGINS=http://localhost:3000,https://myapp.com
CORS_METHODS=GET,POST,PUT,PATCH,DELETE,OPTIONS
CORS_HEADERS=Content-Type,Authorization,X-API-Key
CORS_MAX_AGE=86400
CORS_CREDENTIALS=true
```

Apply it:

```typescript
import { Router } from "tina4-nodejs";

Router.group("/api", () => {
    Router.get("/products", async (req, res) => {
        return res.json({ products: [] });
    });
}, "CorsMiddleware");
```

---

## 4. Built-in RateLimiter

```env
TINA4_RATE_LIMIT=60
TINA4_RATE_LIMIT_WINDOW=60
```

```typescript
Router.group("/api/public", () => {
    Router.get("/search", async (req, res) => {
        return res.json({ results: [] });
    });
}, "RateLimiter");
```

Custom limits per group:

```typescript
Router.group("/api/public", () => {
    Router.get("/search", async (req, res) => {
        return res.json({ results: [] });
    });
}, "RateLimiter:30");
```

---

## 5. Writing Custom Middleware

### Request Logging

```typescript
async function logRequest(req, res, next) {
    const start = Date.now();
    console.log(`[${new Date().toISOString()}] ${req.method} ${req.path} from ${req.ip}`);

    const result = await next(req, res);

    const duration = Date.now() - start;
    console.log(`  Completed in ${duration}ms`);

    return result;
}
```

### Request Timing

```typescript
async function addTiming(req, res, next) {
    const start = Date.now();
    const result = await next(req, res);
    const duration = Date.now() - start;
    res.header("X-Response-Time", `${duration}ms`);
    return result;
}
```

### IP Whitelist

```typescript
async function ipWhitelist(req, res, next) {
    const allowedIps = (process.env.ALLOWED_IPS ?? "127.0.0.1").split(",");

    if (!allowedIps.includes(req.ip)) {
        return res.status(403).json({ error: "Access denied", your_ip: req.ip });
    }

    return next(req, res);
}
```

### Request Validation

```typescript
async function requireJson(req, res, next) {
    if (["POST", "PUT", "PATCH"].includes(req.method)) {
        const contentType = req.headers["content-type"] ?? "";

        if (!contentType.includes("application/json")) {
            return res.status(415).json({
                error: "Content-Type must be application/json",
                received: contentType
            });
        }
    }

    return next(req, res);
}
```

---

## 6. Applying Middleware

Single middleware:

```typescript
Router.get("/api/data", async (req, res) => {
    return res.json({ data: [1, 2, 3] });
}, "logRequest");
```

Multiple middleware:

```typescript
Router.post("/api/data", async (req, res) => {
    return res.status(201).json({ created: true });
}, ["logRequest", "requireJson"]);
```

---

## 7. Route Groups with Shared Middleware

```typescript
Router.group("/api/public", () => {
    Router.get("/products", async (req, res) => {
        return res.json({ products: [] });
    });
    Router.get("/categories", async (req, res) => {
        return res.json({ categories: [] });
    });
}, ["CorsMiddleware", "RateLimiter:30"]);

Router.group("/api/admin", () => {
    Router.get("/users", async (req, res) => {
        return res.json({ users: [] });
    });
}, ["logRequest", "ipWhitelist", "authMiddleware"]);
```

---

## 8. Middleware Execution Order

Middleware executes from outer to inner:

```typescript
Router.get("/api/test", async (req, res) => {
    console.log("Handler");
    return res.json({ ok: true });
}, ["middlewareA", "middlewareB", "middlewareC"]);
```

Output:

```
A: before
B: before
C: before
Handler
C: after
B: after
A: after
```

Group middleware always runs before route middleware.

---

## 9. Short-Circuiting

When middleware does not call `next`, the chain stops:

```typescript
async function requireAuth(req, res, next) {
    const token = req.headers["authorization"] ?? "";

    if (!token) {
        return res.status(401).json({ error: "Authentication required" });
    }

    return next(req, res);
}
```

### Maintenance Mode

```typescript
async function maintenanceMode(req, res, next) {
    const isMaintenanceMode = process.env.MAINTENANCE_MODE === "true";

    if (isMaintenanceMode) {
        if (req.path === "/health") {
            return next(req, res);
        }
        return res.status(503).json({ error: "Service is undergoing maintenance", retry_after: 300 });
    }

    return next(req, res);
}
```

---

## 10. Modifying Requests in Middleware

```typescript
async function addRequestId(req, res, next) {
    const { randomUUID } = await import("crypto");
    req.requestId = randomUUID();
    const result = await next(req, res);
    res.header("X-Request-Id", req.requestId);
    return result;
}
```

---

## 11. Real-World Middleware Stack

```typescript
import { Router } from "tina4-nodejs";

Router.group("/api/v1", () => {
    Router.get("/products", async (req, res) => {
        return res.json({ products: [
            { id: 1, name: "Widget", price: 9.99 },
            { id: 2, name: "Gadget", price: 19.99 }
        ]});
    });

    Router.post("/products", async (req, res) => {
        return res.status(201).json({
            id: 3,
            name: req.body.name ?? "Unknown",
            price: parseFloat(req.body.price ?? 0)
        });
    });
}, ["addRequestId", "logRequest", "CorsMiddleware", "requireApiKey"]);
```

---

## 12. Exercise: Build an API Key Middleware

Build `validateApiKey` middleware that checks `X-API-Key` header against `API_KEYS` env variable.

### Requirements

1. Missing key: return 401 with `{"error": "API key required"}`
2. Invalid key: return 403 with `{"error": "Invalid API key"}`
3. Valid key: attach to `req.apiKey` and continue
4. Apply to a route group with at least two endpoints

---

## 13. Solution

```typescript
import { Router } from "tina4-nodejs";

async function validateApiKey(req, res, next) {
    const apiKey = req.headers["x-api-key"] ?? "";

    if (!apiKey) {
        return res.status(401).json({ error: "API key required" });
    }

    const validKeys = (process.env.API_KEYS ?? "").split(",").map(k => k.trim());

    if (!validKeys.includes(apiKey)) {
        return res.status(403).json({ error: "Invalid API key" });
    }

    req.apiKey = apiKey;
    return next(req, res);
}

Router.group("/api/partner", () => {
    Router.get("/data", async (req, res) => {
        return res.json({
            authenticated_with: req.apiKey,
            data: [{ id: 1, value: "alpha" }, { id: 2, value: "beta" }]
        });
    });

    Router.get("/stats", async (req, res) => {
        return res.json({
            authenticated_with: req.apiKey,
            stats: { total_requests: 1423, avg_response_ms: 42 }
        });
    });
}, "validateApiKey");
```

---

## 14. Gotchas

### 1. Middleware Must Be a Named Function

**Fix:** Define as a named function and pass the name as a string.

### 2. Forgetting to Return next()

**Fix:** Always `return await next(req, res)`.

### 3. Middleware Order Matters

**Fix:** Put `addRequestId` before `logRequest`: `["addRequestId", "logRequest"]`.

### 4. CORS Preflight Returns 404

**Fix:** Apply `CorsMiddleware` to the group. It handles `OPTIONS` automatically.

### 5. Rate Limiter Counts Preflight Requests

**Fix:** Put `CorsMiddleware` before `RateLimiter`.

### 6. Middleware File Not Auto-Loaded

**Fix:** Put middleware functions in a file inside `src/routes/`.

### 7. Short-Circuiting Skips Cleanup

**Fix:** Put timing/logging middleware at the outermost layer.
