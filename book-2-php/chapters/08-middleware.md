# Chapter 8: Middleware

## 1. The Gatekeepers

Your API needs CORS headers for the React frontend, rate limiting for the public endpoints, and auth checking for admin routes -- all without cluttering your route handlers. You could copy-paste the same ten lines of CORS code into every handler, but that breaks the moment you forget one. You could pile all the checks into a giant `if` tree at the top of each handler, but that buries the actual business logic under boilerplate.

Middleware solves this. It lets you wrap routes with reusable logic that runs before (or after) the handler. Each middleware does one job -- check a token, set CORS headers, log the request, enforce rate limits -- and passes control to the next layer. Your route handlers stay focused on their actual purpose.

In Chapter 2 you saw a brief introduction to middleware. This chapter goes deep: built-in middleware, custom middleware, execution order, short-circuiting, and real-world patterns.

---

## 2. What Middleware Is

A middleware function sits between the incoming HTTP request and your route handler. It receives the request, the response, and a `$next` function. It can:

1. Inspect or modify the request before passing it along
2. Decide not to pass it along (short-circuit)
3. Inspect or modify the response on the way back

Here is the simplest middleware that does nothing but pass through:

```php
<?php

function passthrough($request, $response, $next) {
    return $next($request, $response);
}
```

And here is one that blocks everything:

```php
<?php

function blockEverything($request, $response, $next) {
    return $response->json(["error" => "Service unavailable"], 503);
}
```

The `$next` function is what makes middleware composable. Call it to continue to the next middleware (or the route handler if there is no more middleware). Do not call it to stop the chain.

---

## 3. Built-in CorsMiddleware

Cross-Origin Resource Sharing (CORS) is the browser mechanism that controls which domains can call your API. When your React frontend at `http://localhost:3000` makes a fetch request to your Tina4 API at `http://localhost:7145`, the browser sends a preflight `OPTIONS` request first. If your API does not respond with the right headers, the browser blocks the request entirely.

Tina4 provides a built-in `CorsMiddleware` that handles this. Configure it in `.env`:

```env
CORS_ORIGINS=http://localhost:3000,https://myapp.com
CORS_METHODS=GET,POST,PUT,PATCH,DELETE,OPTIONS
CORS_HEADERS=Content-Type,Authorization,X-API-Key
CORS_MAX_AGE=86400
CORS_CREDENTIALS=true
```

Apply it to a group:

```php
<?php
use Tina4\Route;

Route::group("/api", function () {

    Route::get("/products", function ($request, $response) {
        return $response->json(["products" => []]);
    });

    Route::post("/products", function ($request, $response) {
        return $response->json(["created" => true], 201);
    });

}, "CorsMiddleware");
```

Test the preflight:

```bash
curl -X OPTIONS http://localhost:7145/api/products \
  -H "Origin: http://localhost:3000" \
  -H "Access-Control-Request-Method: POST" \
  -H "Access-Control-Request-Headers: Content-Type,Authorization" \
  -v
```

You should see these response headers:

```
Access-Control-Allow-Origin: http://localhost:3000
Access-Control-Allow-Methods: GET,POST,PUT,PATCH,DELETE,OPTIONS
Access-Control-Allow-Headers: Content-Type,Authorization,X-API-Key
Access-Control-Max-Age: 86400
Access-Control-Allow-Credentials: true
```

The `OPTIONS` request returns `204 No Content` with those headers. The browser caches the preflight result for 86400 seconds (24 hours), so subsequent requests skip the preflight entirely.

### Wildcard Origins

During development, you can allow all origins:

```env
CORS_ORIGINS=*
```

This is the default when you scaffold a project. Do not use `*` in production -- specify your actual domains.

### CORS Without Middleware

If you prefer, you can skip the middleware and handle CORS globally. Add `CORS_ORIGINS` to your `.env` and Tina4 applies CORS headers to all responses automatically. The middleware approach gives you finer control -- you can apply CORS to specific route groups and leave internal routes without CORS headers.

---

## 4. Built-in RateLimiter

Rate limiting prevents a single client from overwhelming your API. Tina4's built-in `RateLimiter` middleware tracks requests per IP address and returns `429 Too Many Requests` when the limit is exceeded.

Configure it in `.env`:

```env
TINA4_RATE_LIMIT=60
TINA4_RATE_LIMIT_WINDOW=60
```

This means 60 requests per 60 seconds per IP. Apply it:

```php
<?php
use Tina4\Route;

Route::group("/api/public", function () {

    Route::get("/search", function ($request, $response) {
        $q = $request->query["q"] ?? "";
        return $response->json(["query" => $q, "results" => []]);
    });

    Route::get("/catalog", function ($request, $response) {
        return $response->json(["items" => []]);
    });

}, "RateLimiter");
```

When a client exceeds the limit:

```bash
curl http://localhost:7145/api/public/search?q=test
```

```json
{"error":"Rate limit exceeded. Try again in 42 seconds.","retry_after":42}
```

The response includes a `Retry-After` header with the number of seconds until the limit resets.

### Custom Limits Per Group

You can override the global rate limit for specific groups by setting the limit in the middleware call:

```php
<?php
use Tina4\Route;

// Public endpoints: 30 requests per minute
Route::group("/api/public", function () {
    Route::get("/search", function ($request, $response) {
        return $response->json(["results" => []]);
    });
}, "RateLimiter:30");

// Authenticated endpoints: 120 requests per minute
Route::group("/api/v1", function () {
    Route::get("/data", function ($request, $response) {
        return $response->json(["data" => []]);
    });
}, ["authMiddleware", "RateLimiter:120"]);
```

The syntax `"RateLimiter:30"` passes `30` as a parameter to the rate limiter. This overrides the global `TINA4_RATE_LIMIT` for that group only.

---

## 5. Writing Custom Middleware

Custom middleware follows the same pattern: receive `$request`, `$response`, and `$next`. Define it as a named function.

### Request Logging Middleware

```php
<?php

function logRequest($request, $response, $next) {
    $start = microtime(true);
    $method = $request->method;
    $path = $request->path;
    $ip = $request->ip;

    // Log the incoming request
    error_log("[" . date("Y-m-d H:i:s") . "] " . $method . " " . $path . " from " . $ip);

    // Call the next middleware or route handler
    $result = $next($request, $response);

    // Log the completion
    $duration = round((microtime(true) - $start) * 1000, 2);
    error_log("  Completed in " . $duration . "ms");

    return $result;
}
```

Save this in `src/routes/middleware.php` (or any file in `src/routes/`). Apply it:

```php
Route::get("/api/products", function ($request, $response) {
    return $response->json(["products" => []]);
}, "logRequest");
```

```bash
curl http://localhost:7145/api/products
```

Your server log shows:

```
[2026-03-22 14:30:00] GET /api/products from 127.0.0.1
  Completed in 2.34ms
```

### Request Timing Middleware

```php
<?php

function addTiming($request, $response, $next) {
    $start = microtime(true);

    $result = $next($request, $response);

    $duration = round((microtime(true) - $start) * 1000, 2);

    // Add timing header to the response
    $response->addHeader("X-Response-Time", $duration . "ms");

    return $result;
}
```

```bash
curl http://localhost:7145/api/products -v
```

In the response headers:

```
X-Response-Time: 3.12ms
```

This is useful for performance monitoring. Your frontend or monitoring tools can read the `X-Response-Time` header to track endpoint performance.

### IP Whitelist Middleware

```php
<?php

function ipWhitelist($request, $response, $next) {
    $allowedIps = explode(",", $_ENV["ALLOWED_IPS"] ?? "127.0.0.1");

    if (!in_array($request->ip, $allowedIps)) {
        return $response->json([
            "error" => "Access denied",
            "your_ip" => $request->ip
        ], 403);
    }

    return $next($request, $response);
}
```

Configure in `.env`:

```env
ALLOWED_IPS=127.0.0.1,10.0.0.5,192.168.1.100
```

Apply it to admin routes:

```php
Route::group("/admin", function () {
    Route::get("/dashboard", function ($request, $response) {
        return $response->json(["page" => "admin dashboard"]);
    });
}, "ipWhitelist");
```

```bash
curl http://localhost:7145/admin/dashboard
```

If your IP is in the whitelist:

```json
{"page":"admin dashboard"}
```

If not:

```json
{"error":"Access denied","your_ip":"203.0.113.42"}
```

### Request Validation Middleware

```php
<?php

function requireJson($request, $response, $next) {
    if (in_array($request->method, ["POST", "PUT", "PATCH"])) {
        $contentType = $request->headers["Content-Type"] ?? "";

        if (strpos($contentType, "application/json") === false) {
            return $response->json([
                "error" => "Content-Type must be application/json",
                "received" => $contentType
            ], 415);
        }
    }

    return $next($request, $response);
}
```

This middleware ensures all POST, PUT, and PATCH requests send JSON. Apply it to your entire API:

```php
Route::group("/api", function () {
    // All API routes here
}, "requireJson");
```

```bash
curl -X POST http://localhost:7145/api/products \
  -d "name=Widget"
```

```json
{"error":"Content-Type must be application/json","received":"application/x-www-form-urlencoded"}
```

(Status: `415 Unsupported Media Type`)

---

## 6. Applying Middleware to Individual Routes

Pass middleware as the third argument to any route method:

```php
<?php
use Tina4\Route;

Route::get("/api/data", function ($request, $response) {
    return $response->json(["data" => [1, 2, 3]]);
}, "logRequest");

Route::post("/api/data", function ($request, $response) {
    return $response->json(["created" => true], 201);
}, ["logRequest", "requireJson"]);
```

For a single middleware, pass a string. For multiple, pass an array. Each middleware runs in the order listed.

---

## 7. Route Groups with Shared Middleware

Groups apply middleware to every route inside them:

```php
<?php
use Tina4\Route;

// Public API -- rate limited, CORS enabled
Route::group("/api/public", function () {

    Route::get("/products", function ($request, $response) {
        return $response->json(["products" => []]);
    });

    Route::get("/categories", function ($request, $response) {
        return $response->json(["categories" => []]);
    });

}, ["CorsMiddleware", "RateLimiter:30"]);

// Admin API -- auth required, IP restricted, logged
Route::group("/api/admin", function () {

    Route::get("/users", function ($request, $response) {
        return $response->json(["users" => []]);
    });

    Route::delete("/users/{id:int}", function ($request, $response) {
        $id = $request->params["id"];
        return $response->json(["deleted" => $id]);
    });

}, ["logRequest", "ipWhitelist", "authMiddleware"]);
```

Individual routes inside a group can add their own middleware too. The group middleware runs first, then the route-specific middleware:

```php
Route::group("/api", function () {

    // This route gets: logRequest -> requireJson -> handler
    Route::post("/upload", function ($request, $response) {
        return $response->json(["uploaded" => true]);
    }, "requireJson");

}, "logRequest");
```

---

## 8. Middleware Execution Order

When you stack middleware, they execute from outer to inner -- like layers of an onion. The first middleware listed runs first on the way in and last on the way out.

Consider this setup:

```php
<?php

function middlewareA($request, $response, $next) {
    error_log("A: before");
    $result = $next($request, $response);
    error_log("A: after");
    return $result;
}

function middlewareB($request, $response, $next) {
    error_log("B: before");
    $result = $next($request, $response);
    error_log("B: after");
    return $result;
}

function middlewareC($request, $response, $next) {
    error_log("C: before");
    $result = $next($request, $response);
    error_log("C: after");
    return $result;
}
```

```php
Route::get("/api/test", function ($request, $response) {
    error_log("Handler");
    return $response->json(["ok" => true]);
}, ["middlewareA", "middlewareB", "middlewareC"]);
```

```bash
curl http://localhost:7145/api/test
```

Server log output:

```
A: before
B: before
C: before
Handler
C: after
B: after
A: after
```

The request flows inward: A, B, C, Handler. The response flows outward: C, B, A. This means:

- `middlewareA` sees the request first and the response last. Put CORS headers and request logging here.
- `middlewareC` sees the request last and the response first. Put response transformations here.
- Authentication should be early (catch unauthorized requests before doing expensive work).
- Timing should be outermost (measure the entire pipeline).

### Group + Route Middleware Order

```php
Route::group("/api", function () {

    Route::get("/data", function ($request, $response) {
        return $response->json(["data" => true]);
    }, "middlewareC");

}, ["middlewareA", "middlewareB"]);
```

Execution order: `middlewareA` -> `middlewareB` -> `middlewareC` -> handler. Group middleware always runs before route middleware.

---

## 9. Short-Circuiting

When middleware does not call `$next`, the chain stops. No subsequent middleware runs and the route handler is never called. This is called short-circuiting.

### Authentication Short-Circuit

```php
<?php

function requireAuth($request, $response, $next) {
    $token = $request->headers["Authorization"] ?? "";

    if (empty($token)) {
        // Short-circuit: return 401, do not call $next
        return $response->json(["error" => "Authentication required"], 401);
    }

    return $next($request, $response);
}
```

If the `Authorization` header is missing, the middleware returns a `401` immediately. The route handler never executes. This saves server resources -- you do not query the database or run business logic for unauthenticated requests.

### Maintenance Mode

```php
<?php

function maintenanceMode($request, $response, $next) {
    $isMaintenanceMode = ($_ENV["MAINTENANCE_MODE"] ?? "false") === "true";

    if ($isMaintenanceMode) {
        // Allow health checks even in maintenance mode
        if ($request->path === "/health") {
            return $next($request, $response);
        }

        return $response->json([
            "error" => "Service is undergoing maintenance",
            "retry_after" => 300
        ], 503);
    }

    return $next($request, $response);
}
```

Add to `.env` when you need to take the site down:

```env
MAINTENANCE_MODE=true
```

Apply it globally:

```php
Route::group("/", function () {
    // All your routes
}, "maintenanceMode");
```

Every request except `/health` gets a `503 Service Unavailable` response.

### Conditional Short-Circuiting

Sometimes you want to short-circuit only certain methods:

```php
<?php

function readOnly($request, $response, $next) {
    if (in_array($request->method, ["POST", "PUT", "PATCH", "DELETE"])) {
        return $response->json([
            "error" => "API is in read-only mode"
        ], 405);
    }

    return $next($request, $response);
}
```

GET requests pass through. Write operations are blocked. This is useful for standby replicas or demo environments.

---

## 10. Modifying Requests in Middleware

Middleware can add data to the request before passing it to the handler. This is how authentication middleware attaches user information:

```php
<?php
use Tina4\Auth;

function attachUser($request, $response, $next) {
    $authHeader = $request->headers["Authorization"] ?? "";

    if (!empty($authHeader) && str_starts_with($authHeader, "Bearer ")) {
        $token = substr($authHeader, 7);
        if (Auth::validToken($token)) {
            $request->user = Auth::getPayload($token);
        }
    }

    // Always call $next -- this middleware does not block requests
    // Routes that need auth should check $request->user themselves
    return $next($request, $response);
}
```

This pattern is different from a blocking auth middleware. It attaches user data if a token is present but does not block unauthenticated requests. Some routes need the user data (show personalized content) but are still accessible without it.

### Adding Request Metadata

```php
<?php

function addRequestId($request, $response, $next) {
    $requestId = bin2hex(random_bytes(8));
    $request->requestId = $requestId;

    $result = $next($request, $response);

    // Add request ID to response headers for debugging
    $response->addHeader("X-Request-Id", $requestId);

    return $result;
}
```

Your route handler can now access `$request->requestId` for logging, error tracking, or correlation:

```php
Route::get("/api/data", function ($request, $response) {
    error_log("[" . $request->requestId . "] Processing data request");
    return $response->json(["request_id" => $request->requestId, "data" => []]);
}, "addRequestId");
```

```bash
curl http://localhost:7145/api/data -v
```

```json
{"request_id":"a1b2c3d4e5f6a7b8","data":[]}
```

Response headers include:

```
X-Request-Id: a1b2c3d4e5f6a7b8
```

---

## 11. Real-World Middleware Stack

Here is a realistic middleware setup for a production API:

```php
<?php
use Tina4\Route;

// src/routes/middleware.php

function addRequestId($request, $response, $next) {
    $request->requestId = bin2hex(random_bytes(8));
    $result = $next($request, $response);
    $response->addHeader("X-Request-Id", $request->requestId);
    return $result;
}

function logRequest($request, $response, $next) {
    $start = microtime(true);
    error_log("[" . $request->requestId . "] " . $request->method . " " . $request->path);

    $result = $next($request, $response);

    $duration = round((microtime(true) - $start) * 1000, 2);
    error_log("[" . $request->requestId . "] Completed in " . $duration . "ms");

    return $result;
}

function requireApiKey($request, $response, $next) {
    $apiKey = $request->headers["X-API-Key"] ?? "";
    $validKeys = explode(",", $_ENV["API_KEYS"] ?? "");

    if (!in_array($apiKey, $validKeys)) {
        return $response->json([
            "error" => "Invalid or missing API key",
            "request_id" => $request->requestId ?? null
        ], 401);
    }

    return $next($request, $response);
}
```

```php
<?php
use Tina4\Route;

// src/routes/api.php

Route::group("/api/v1", function () {

    Route::get("/products", function ($request, $response) {
        return $response->json(["products" => [
            ["id" => 1, "name" => "Widget", "price" => 9.99],
            ["id" => 2, "name" => "Gadget", "price" => 19.99]
        ]]);
    });

    Route::get("/products/{id:int}", function ($request, $response) {
        $id = $request->params["id"];
        return $response->json(["id" => $id, "name" => "Widget", "price" => 9.99]);
    });

    Route::post("/products", function ($request, $response) {
        $body = $request->body;
        return $response->json([
            "id" => 3,
            "name" => $body["name"] ?? "Unknown",
            "price" => (float) ($body["price"] ?? 0)
        ], 201);
    });

}, ["addRequestId", "logRequest", "CorsMiddleware", "requireApiKey"]);
```

Test without an API key:

```bash
curl http://localhost:7145/api/v1/products
```

```json
{"error":"Invalid or missing API key","request_id":"a1b2c3d4e5f6a7b8"}
```

(Status: `401 Unauthorized`)

Test with a valid API key:

```bash
curl http://localhost:7145/api/v1/products \
  -H "X-API-Key: my-secret-key"
```

```json
{"products":[{"id":1,"name":"Widget","price":9.99},{"id":2,"name":"Gadget","price":19.99}]}
```

---

## 12. Exercise: Build an API Key Middleware

Build a middleware called `validateApiKey` that:

1. Checks for an `X-API-Key` header on every request
2. Validates the key against a comma-separated list stored in the `API_KEYS` environment variable
3. If the key is missing, returns `401` with `{"error": "API key required"}`
4. If the key is invalid, returns `403` with `{"error": "Invalid API key"}`
5. If the key is valid, attaches the key to `$request->apiKey` and continues
6. Apply this middleware to a route group with at least two endpoints

### Setup

Add this to your `.env`:

```env
API_KEYS=key-alpha-001,key-beta-002,key-gamma-003
```

### Test with:

```bash
# No API key -- should get 401
curl http://localhost:7145/api/partner/data

# Invalid API key -- should get 403
curl http://localhost:7145/api/partner/data \
  -H "X-API-Key: wrong-key"

# Valid API key -- should get 200
curl http://localhost:7145/api/partner/data \
  -H "X-API-Key: key-alpha-001"

# Valid key on another endpoint
curl http://localhost:7145/api/partner/stats \
  -H "X-API-Key: key-beta-002"
```

---

## 13. Solution

Create `src/routes/api-key-middleware.php`:

```php
<?php
use Tina4\Route;

function validateApiKey($request, $response, $next) {
    $apiKey = $request->headers["X-API-Key"] ?? "";

    // Check if header is present
    if (empty($apiKey)) {
        return $response->json(["error" => "API key required"], 401);
    }

    // Validate against allowed keys
    $validKeys = array_map("trim", explode(",", $_ENV["API_KEYS"] ?? ""));

    if (!in_array($apiKey, $validKeys)) {
        return $response->json(["error" => "Invalid API key"], 403);
    }

    // Attach key to request for downstream use
    $request->apiKey = $apiKey;

    return $next($request, $response);
}

Route::group("/api/partner", function () {

    Route::get("/data", function ($request, $response) {
        return $response->json([
            "authenticated_with" => $request->apiKey,
            "data" => [
                ["id" => 1, "value" => "alpha"],
                ["id" => 2, "value" => "beta"]
            ]
        ]);
    });

    Route::get("/stats", function ($request, $response) {
        return $response->json([
            "authenticated_with" => $request->apiKey,
            "stats" => [
                "total_requests" => 1423,
                "avg_response_ms" => 42
            ]
        ]);
    });

}, "validateApiKey");
```

**Expected output -- no key:**

```bash
curl http://localhost:7145/api/partner/data
```

```json
{"error":"API key required"}
```

(Status: `401 Unauthorized`)

**Expected output -- invalid key:**

```bash
curl http://localhost:7145/api/partner/data -H "X-API-Key: wrong-key"
```

```json
{"error":"Invalid API key"}
```

(Status: `403 Forbidden`)

**Expected output -- valid key:**

```bash
curl http://localhost:7145/api/partner/data -H "X-API-Key: key-alpha-001"
```

```json
{
  "authenticated_with": "key-alpha-001",
  "data": [
    {"id": 1, "value": "alpha"},
    {"id": 2, "value": "beta"}
  ]
}
```

**Expected output -- different valid key on stats:**

```bash
curl http://localhost:7145/api/partner/stats -H "X-API-Key: key-beta-002"
```

```json
{
  "authenticated_with": "key-beta-002",
  "stats": {
    "total_requests": 1423,
    "avg_response_ms": 42
  }
}
```

---

## 14. Gotchas

### 1. Middleware Must Be a Named Function

**Problem:** You pass an anonymous closure as middleware and get an error.

**Cause:** Tina4 expects middleware to be referenced by a string name, not as an inline closure. The string is resolved to a function at runtime.

**Fix:** Define your middleware as a named function: `function myMiddleware($request, $response, $next) { ... }` and pass `"myMiddleware"` as a string.

### 2. Forgetting to Return $next()

**Problem:** Your middleware runs but the route handler never executes. The response is empty or a 500 error.

**Cause:** You called `$next($request, $response)` but did not `return` the result.

**Fix:** Always `return $next($request, $response)`. Without the `return`, the middleware discards the response from the handler and returns `null`.

### 3. Middleware Order Matters

**Problem:** Your logging middleware does not see the request ID, even though `addRequestId` is in the middleware list.

**Cause:** `logRequest` runs before `addRequestId`. Middleware executes in the order listed.

**Fix:** Put `addRequestId` before `logRequest` in the array: `["addRequestId", "logRequest"]`. Think of the order as "what needs to happen first."

### 4. CORS Preflight Returns 404

**Problem:** The browser's preflight `OPTIONS` request gets a 404, but `GET` and `POST` work fine when tested with curl.

**Cause:** You did not apply `CorsMiddleware` to the route, so the `OPTIONS` method is not handled.

**Fix:** Apply `CorsMiddleware` to the group. It automatically handles `OPTIONS` requests and returns the correct CORS headers. Alternatively, set `CORS_ORIGINS` in `.env` for global CORS handling.

### 5. Rate Limiter Counts Preflight Requests

**Problem:** Your frontend hits the rate limit faster than expected because every `POST` request actually counts as two requests (the `OPTIONS` preflight plus the `POST`).

**Cause:** The rate limiter counts all requests, including `OPTIONS`.

**Fix:** Put `CorsMiddleware` before `RateLimiter` in the middleware chain: `["CorsMiddleware", "RateLimiter"]`. The CORS middleware handles `OPTIONS` and returns immediately, so the rate limiter only sees actual requests. If CORS is configured globally via `.env`, the preflight is handled before middleware runs.

### 6. Middleware File Not Auto-Loaded

**Problem:** You defined middleware in a file but get "function not found" when referencing it.

**Cause:** The file is not in `src/routes/`. Tina4 auto-loads all `.php` files in `src/routes/`, but middleware defined outside that directory is not discovered.

**Fix:** Put your middleware functions in a file inside `src/routes/`, such as `src/routes/middleware.php`. The filename does not matter -- all `.php` files in the directory are loaded.

### 7. Short-Circuiting Skips Cleanup Middleware

**Problem:** Your timing middleware logs the start time but never logs the completion time for blocked requests.

**Cause:** When an inner middleware short-circuits, the outer middleware's code after `$next()` still runs. But if the short-circuiting middleware is listed before the timing middleware, the timing middleware never executes at all.

**Fix:** Put cleanup-dependent middleware (timing, logging) at the outermost layer. They wrap the entire chain, so they always see both the start and the end -- even when an inner middleware short-circuits. The code after `$next()` in outer middleware always runs, regardless of whether the chain was short-circuited.
