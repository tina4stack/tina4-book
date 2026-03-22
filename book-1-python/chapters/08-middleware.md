# Chapter 8: Middleware

## 1. The Pipeline Pattern

Every HTTP request passes through a series of gates before reaching your route handler. Rate limiter. Body parser. Auth check. Logger. These gates are middleware -- code that wraps your route handler and runs before, after, or both.

Picture a public API. Every request hits a rate limit check. Some endpoints require an API key. All responses need CORS headers. Errors need logging. Without middleware, that logic lives in every handler. Duplicated. Scattered. Fragile. With middleware, you write it once and attach it where it belongs.

Tina4 Python ships with built-in middleware (CORS, rate limiting) and lets you write your own. This chapter covers both.

---

## 2. Built-In Middleware

### CorsMiddleware

CORS (Cross-Origin Resource Sharing) controls which websites can call your API from a browser. Tina4 includes CORS middleware that is configured via `.env`:

```env
CORS_ORIGINS=https://app.example.com,https://admin.example.com
CORS_METHODS=GET,POST,PUT,DELETE
CORS_HEADERS=Content-Type,Authorization
CORS_CREDENTIALS=true
CORS_MAX_AGE=86400
```

With these settings, only `app.example.com` and `admin.example.com` can make cross-origin requests to your API. The browser automatically handles preflight `OPTIONS` requests.

For development, you can allow all origins:

```env
CORS_ORIGINS=*
```

The CORS middleware is active by default. You do not need to register it manually.

### RateLimiter

The rate limiter prevents abuse by limiting how many requests a single IP can make in a time window:

```env
TINA4_RATE_LIMIT=60
```

This allows 60 requests per minute per IP address. When a client exceeds the limit, they receive a `429 Too Many Requests` response with a `Retry-After` header.

Rate limit headers are included in every response:

```
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 57
X-RateLimit-Reset: 1711113000
```

Like CORS, the rate limiter is active by default based on your `.env` configuration.

---

## 3. Writing Custom Middleware

A middleware function takes three arguments: `request`, `response`, and `next_handler`. It must return a response.

```python
async def my_middleware(request, response, next_handler):
    # Code that runs BEFORE the route handler
    print("Before handler")

    # Call the next middleware or the route handler
    result = await next_handler(request, response)

    # Code that runs AFTER the route handler
    print("After handler")

    return result
```

### Example: Request Timer

```python
import time

async def timer_middleware(request, response, next_handler):
    start = time.time()

    result = await next_handler(request, response)

    duration_ms = round((time.time() - start) * 1000, 2)
    print(f"{request.method} {request.path} completed in {duration_ms}ms")

    return result
```

### Example: Request Logger

```python
from datetime import datetime

async def log_middleware(request, response, next_handler):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {request.method} {request.path}")
    print(f"  Headers: {dict(request.headers)}")

    if request.body:
        print(f"  Body: {request.body}")

    result = await next_handler(request, response)

    print(f"  Status: {result.status_code if hasattr(result, 'status_code') else 'unknown'}")

    return result
```

### Example: JSON Content-Type Enforcer

```python
async def require_json(request, response, next_handler):
    if request.method in ("POST", "PUT", "PATCH"):
        content_type = request.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            return response.json({
                "error": "Content-Type must be application/json"
            }, 415)

    return await next_handler(request, response)
```

---

## 4. The @middleware Decorator

Apply middleware to a single route with the `@middleware` decorator:

```python
from tina4_python.core.router import get, post, middleware

@get("/api/data")
@middleware(timer_middleware)
async def get_data(request, response):
    return response.json({"data": [1, 2, 3]})
```

Apply multiple middleware by passing them as separate arguments:

```python
@post("/api/items")
@middleware(log_middleware, require_json, timer_middleware)
async def create_item(request, response):
    return response.json({"item": request.body}, 201)
```

Middleware runs in the order you list them. In the example above: `log_middleware` runs first, then `require_json`, then `timer_middleware`, then the route handler.

---

## 5. Middleware on Route Groups

Apply middleware to all routes in a group:

```python
from tina4_python.core.router import get, post, group, middleware

@group("/api/v1")
@middleware(log_middleware, timer_middleware)
def api_v1():

    @get("/users")
    async def list_users(request, response):
        return response.json({"users": []})

    @post("/users")
    async def create_user(request, response):
        return response.json({"created": True}, 201)

    @get("/products")
    async def list_products(request, response):
        return response.json({"products": []})
```

Every route inside the group now has `log_middleware` and `timer_middleware` applied. You can still add route-specific middleware on top:

```python
@group("/api/v1")
@middleware(log_middleware)
def api_v1():

    @get("/public")
    async def public_endpoint(request, response):
        # Only log_middleware runs
        return response.json({"public": True})

    @post("/admin")
    @middleware(auth_middleware)
    async def admin_endpoint(request, response):
        # log_middleware + auth_middleware both run
        return response.json({"admin": True})
```

---

## 6. Execution Order

Stacked middleware forms a nested pipeline. Requests travel inward. Responses travel outward:

```
Request arrives
  → log_middleware (before)
    → auth_middleware (before)
      → timer_middleware (before)
        → route handler
      → timer_middleware (after)
    → auth_middleware (after)
  → log_middleware (after)
Response sent
```

Each middleware wraps around the next one. The outermost middleware runs first on the way in and last on the way out.

Here is a concrete example showing the order:

```python
async def middleware_a(request, response, next_handler):
    print("A: before")
    result = await next_handler(request, response)
    print("A: after")
    return result

async def middleware_b(request, response, next_handler):
    print("B: before")
    result = await next_handler(request, response)
    print("B: after")
    return result

@get("/test")
@middleware(middleware_a, middleware_b)
async def test(request, response):
    print("Handler")
    return response.json({"ok": True})
```

When you request `/test`, the console shows:

```
A: before
B: before
Handler
B: after
A: after
```

---

## 7. Short-Circuiting

Skip `next_handler` and the chain stops cold. The route handler never runs. This is how blocking middleware works:

```python
async def maintenance_mode(request, response, next_handler):
    import os
    if os.getenv("MAINTENANCE_MODE") == "true":
        return response.json({
            "error": "Service is under maintenance. Please try again later."
        }, 503)

    return await next_handler(request, response)
```

When `MAINTENANCE_MODE=true`, every request gets a 503 response without reaching any route handler.

### Conditional Short-Circuit

```python
async def require_api_key(request, response, next_handler):
    api_key = request.headers.get("X-API-Key", "")

    if not api_key:
        return response.json({"error": "API key required"}, 401)

    # Validate the key against a database or config
    valid_keys = ["key-abc-123", "key-def-456", "key-ghi-789"]
    if api_key not in valid_keys:
        return response.json({"error": "Invalid API key"}, 403)

    # Attach the key info to the request for the handler to use
    request.api_key = api_key

    return await next_handler(request, response)
```

```bash
# No key -- 401
curl http://localhost:7145/api/data
```

```json
{"error":"API key required"}
```

```bash
# Invalid key -- 403
curl http://localhost:7145/api/data -H "X-API-Key: wrong-key"
```

```json
{"error":"Invalid API key"}
```

```bash
# Valid key -- 200
curl http://localhost:7145/api/data -H "X-API-Key: key-abc-123"
```

```json
{"data":[1,2,3]}
```

---

## 8. Modifying Request and Response

Middleware can modify the request before it reaches the handler, and the response before it reaches the client.

### Adding Data to the Request

```python
async def inject_user_agent(request, response, next_handler):
    ua = request.headers.get("User-Agent", "")

    request.is_mobile = "Mobile" in ua or "Android" in ua or "iPhone" in ua
    request.is_bot = "bot" in ua.lower() or "spider" in ua.lower()

    return await next_handler(request, response)
```

Now the route handler can access `request.is_mobile` and `request.is_bot`.

### Modifying the Response

```python
async def add_security_headers(request, response, next_handler):
    result = await next_handler(request, response)

    # Add security headers to every response
    return response.header("X-Content-Type-Options", "nosniff") \
                   .header("X-Frame-Options", "DENY") \
                   .header("X-XSS-Protection", "1; mode=block") \
                   .header("Strict-Transport-Security", "max-age=31536000; includeSubDomains")
```

---

## 9. Real-World Example: API Key Middleware with Database Lookup

```python
from tina4_python.database.connection import Database
from datetime import datetime

async def api_key_middleware(request, response, next_handler):
    api_key = request.headers.get("X-API-Key", "")

    if not api_key:
        return response.json({
            "error": "API key required. Send it in the X-API-Key header."
        }, 401)

    db = Database()
    key_record = db.fetch_one(
        "SELECT id, name, rate_limit, is_active FROM api_keys WHERE key_value = :key",
        {"key": api_key}
    )

    if key_record is None:
        return response.json({"error": "Invalid API key"}, 403)

    if not key_record["is_active"]:
        return response.json({"error": "API key has been deactivated"}, 403)

    # Update last used timestamp
    db.execute(
        "UPDATE api_keys SET last_used_at = :now, request_count = request_count + 1 WHERE id = :id",
        {"now": datetime.now().isoformat(), "id": key_record["id"]}
    )

    # Attach key info to request
    request.api_key_id = key_record["id"]
    request.api_key_name = key_record["name"]

    return await next_handler(request, response)
```

---

## 10. Exercise: Build an API Key Middleware System

Build a complete API key system with key management and usage tracking.

### Requirements

1. Create a migration for an `api_keys` table: `id`, `name`, `key_value` (unique), `is_active` (default true), `rate_limit` (default 100), `request_count` (default 0), `last_used_at`, `created_at`

2. Build these endpoints:

| Method | Path | Middleware | Description |
|--------|------|-----------|-------------|
| `POST` | `/admin/api-keys` | Auth | Create a new API key (generate random key) |
| `GET` | `/admin/api-keys` | Auth | List all API keys with usage stats |
| `DELETE` | `/admin/api-keys/{id:int}` | Auth | Deactivate an API key |
| `GET` | `/api/data` | API Key | Protected endpoint -- requires valid API key |
| `GET` | `/api/status` | API Key | Another protected endpoint |

3. The API key middleware should:
   - Check `X-API-Key` header
   - Validate against the database
   - Reject deactivated keys
   - Track usage (increment count, update last_used_at)
   - Attach key info to the request

### Test with:

```bash
# Create an API key (requires auth token from Chapter 7)
curl -X POST http://localhost:7145/admin/api-keys \
  -H "Authorization: Bearer YOUR_AUTH_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "Mobile App"}'

# Use the API key
curl http://localhost:7145/api/data \
  -H "X-API-Key: THE_GENERATED_KEY"

# List keys with stats
curl http://localhost:7145/admin/api-keys \
  -H "Authorization: Bearer YOUR_AUTH_TOKEN"
```

---

## 11. Solution

### Migration

Create `src/migrations/20260322170000_create_api_keys_table.sql`:

```sql
-- UP
CREATE TABLE api_keys (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    key_value TEXT NOT NULL UNIQUE,
    is_active INTEGER NOT NULL DEFAULT 1,
    rate_limit INTEGER NOT NULL DEFAULT 100,
    request_count INTEGER NOT NULL DEFAULT 0,
    last_used_at TEXT,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

CREATE UNIQUE INDEX idx_api_keys_key ON api_keys (key_value);

-- DOWN
DROP INDEX IF EXISTS idx_api_keys_key;
DROP TABLE IF EXISTS api_keys;
```

### Routes

Create `src/routes/api_keys.py`:

```python
from tina4_python.core.router import get, post, delete as delete_route, middleware
from tina4_python.auth import Auth
from tina4_python.database.connection import Database
from datetime import datetime
import secrets


async def auth_middleware(request, response, next_handler):
    auth_header = request.headers.get("Authorization", "")
    if not auth_header or not auth_header.startswith("Bearer "):
        return response.json({"error": "Authorization required"}, 401)

    token = auth_header[7:]
    if not Auth.valid_token(token):
        return response.json({"error": "Invalid or expired token"}, 401)

    request.user = Auth.get_payload(token)
    return await next_handler(request, response)


async def api_key_middleware(request, response, next_handler):
    api_key = request.headers.get("X-API-Key", "")

    if not api_key:
        return response.json({"error": "API key required. Send in X-API-Key header."}, 401)

    db = Database()
    key_record = db.fetch_one(
        "SELECT id, name, is_active FROM api_keys WHERE key_value = :key",
        {"key": api_key}
    )

    if key_record is None:
        return response.json({"error": "Invalid API key"}, 403)

    if not key_record["is_active"]:
        return response.json({"error": "API key has been deactivated"}, 403)

    db.execute(
        "UPDATE api_keys SET last_used_at = :now, request_count = request_count + 1 WHERE id = :id",
        {"now": datetime.now().isoformat(), "id": key_record["id"]}
    )

    request.api_key_id = key_record["id"]
    request.api_key_name = key_record["name"]

    return await next_handler(request, response)


@post("/admin/api-keys")
@middleware(auth_middleware)
async def create_api_key(request, response):
    db = Database()
    name = request.body.get("name", "Unnamed Key")
    key_value = f"tk_{secrets.token_hex(24)}"

    db.execute(
        "INSERT INTO api_keys (name, key_value) VALUES (:name, :key)",
        {"name": name, "key": key_value}
    )

    key = db.fetch_one("SELECT * FROM api_keys WHERE id = last_insert_rowid()")

    return response.json({"message": "API key created", "key": key}, 201)


@get("/admin/api-keys")
@middleware(auth_middleware)
async def list_api_keys(request, response):
    db = Database()
    keys = db.fetch("SELECT id, name, key_value, is_active, rate_limit, request_count, last_used_at, created_at FROM api_keys ORDER BY created_at DESC")
    return response.json({"keys": keys, "count": len(keys)})


@delete_route("/admin/api-keys/{id:int}")
@middleware(auth_middleware)
async def deactivate_api_key(request, response):
    db = Database()
    key_id = request.params["id"]

    existing = db.fetch_one("SELECT id FROM api_keys WHERE id = :id", {"id": key_id})
    if existing is None:
        return response.json({"error": "API key not found"}, 404)

    db.execute("UPDATE api_keys SET is_active = 0 WHERE id = :id", {"id": key_id})
    return response.json({"message": "API key deactivated"})


@get("/api/data")
@middleware(api_key_middleware)
async def api_data(request, response):
    return response.json({
        "data": [1, 2, 3, 4, 5],
        "api_key": request.api_key_name
    })


@get("/api/status")
@middleware(api_key_middleware)
async def api_status(request, response):
    return response.json({
        "status": "operational",
        "api_key": request.api_key_name
    })
```

---

## 12. Gotchas

### 1. Forgetting to await next_handler

**Problem:** The route handler never runs, or you get an error about a coroutine object.

**Cause:** You called `next_handler(request, response)` without `await`.

**Fix:** Always use `await next_handler(request, response)`. Since Tina4 Python is async, every middleware and handler must be awaited.

### 2. Middleware modifies response after it is sent

**Problem:** Headers or cookies you add in the "after" phase of middleware do not appear in the response.

**Cause:** The response was already finalized by the route handler.

**Fix:** In the "after" phase, modify the result returned by `next_handler`, not the original `response` object. Some modifications may need to happen in the "before" phase instead.

### 3. Middleware applied to wrong routes

**Problem:** Your API key middleware runs on public routes that should not require a key.

**Cause:** The middleware is applied to the group, and the public route is inside that group.

**Fix:** Move public routes outside the group, or use `@noauth` on specific routes to bypass authentication middleware. For custom middleware like API key checks, you need to handle exemptions manually by checking the path in the middleware.

### 4. Middleware execution order surprises

**Problem:** Your auth check runs after your logging middleware, but you wanted it to run first.

**Cause:** Middleware in `@middleware(a, b, c)` runs in left-to-right order: `a` wraps `b` wraps `c` wraps handler.

**Fix:** Put the middleware you want to run first at the leftmost position: `@middleware(auth_middleware, log_middleware)`.

### 5. Error in middleware breaks the chain

**Problem:** An unhandled exception in middleware causes a 500 error without reaching the route handler.

**Cause:** If middleware throws an exception before calling `next_handler`, no subsequent middleware or the handler runs.

**Fix:** Wrap risky middleware code in try/except and return an appropriate error response instead of letting the exception propagate.

### 6. Database connections in middleware

**Problem:** Opening a database connection in middleware that runs on every request causes connection pool exhaustion.

**Cause:** Each middleware call creates a new `Database()` instance.

**Fix:** Tina4's `Database()` uses connection pooling internally, so this is usually safe. But if you are seeing issues, cache your database lookups (like API keys) in memory with a TTL instead of querying on every request.

### 7. Modifying request in middleware does not persist

**Problem:** You set `request.custom_field = "value"` in middleware, but the route handler does not see it.

**Cause:** In some edge cases, the request object may be copied between middleware stages.

**Fix:** Use `request.custom_field` consistently. If it is not persisting, check that you are modifying the same request object that is passed to `next_handler`. Do not create a new request object.
