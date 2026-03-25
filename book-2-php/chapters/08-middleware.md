# Chapter 8: Middleware

## 1. The Gatekeepers

Your API needs CORS headers for the React frontend, rate limiting for public endpoints, and auth checks for admin routes. You could paste the same 10 lines of CORS code into every handler. You will forget one. You could pile every check into a giant `if` tree. The business logic disappears under boilerplate.

Middleware solves this. Wrap routes with reusable logic. Each middleware does one job -- check a token, set CORS headers, log the request, enforce rate limits -- and passes control to the next layer. Route handlers stay focused on their purpose.

Chapter 2 introduced middleware briefly. This chapter goes deep: built-in middleware, custom middleware, execution order, short-circuiting, and real-world patterns.

---

## 2. What Middleware Is

Middleware is code that runs before or after your route handler. It sits in the HTTP pipeline between the incoming request and the response. Every request can pass through multiple middleware layers before reaching the handler.

Tina4 PHP supports two styles of middleware:

**Function-based middleware** receives `$request`, `$response`, and `$next`. Call `$next` to continue the chain. Skip it to short-circuit.

```php
<?php

function passthrough($request, $response, $next) {
    return $next($request, $response);
}
```

**Class-based middleware** uses naming conventions. Static methods prefixed with `before` run before the handler. Methods prefixed with `after` run after it. Each method receives `($request, $response)` and returns `[$request, $response]`.

```php
<?php
use Tina4\Request;
use Tina4\Response;

class MyMiddleware
{
    public static function beforeCheck(Request $request, Response $response): array
    {
        // Runs before the route handler
        return [$request, $response];
    }

    public static function afterCleanup(Request $request, Response $response): array
    {
        // Runs after the route handler
        return [$request, $response];
    }
}
```

If a `before*` method sets the response status to >= 400, the handler is skipped (short-circuit).

Register class-based middleware globally with `Middleware::use()`:

```php
<?php
use Tina4\Middleware;
use Tina4\Middleware\CorsMiddleware;
use Tina4\Middleware\RequestLogger;

Middleware::use(CorsMiddleware::class);
Middleware::use(RequestLogger::class);
```

Global middleware runs on every request, in the order registered.

---

## 3. Built-in CorsMiddleware

CORS controls which domains can call your API. When React at `http://localhost:3000` calls your Tina4 API at `http://localhost:7146`, the browser sends a preflight `OPTIONS` request first. Wrong headers: the browser blocks everything.

Tina4 provides `CorsMiddleware`. Configure in `.env`:

```env
TINA4_CORS_ORIGINS=http://localhost:3000,https://myapp.com
TINA4_CORS_METHODS=GET,POST,PUT,PATCH,DELETE,OPTIONS
TINA4_CORS_HEADERS=Content-Type,Authorization,X-API-Key
TINA4_CORS_MAX_AGE=86400
```

Apply it:

```php
<?php
use Tina4Router;

Router::group("/api", function () {

    Router::get("/products", function ($request, $response) {
        return $response->json(["products" => []]);
    });

    Router::post("/products", function ($request, $response) {
        return $response->json(["created" => true], 201);
    });

}, "CorsMiddleware");
```

Test the preflight:

```bash
curl -X OPTIONS http://localhost:7146/api/products \
  -H "Origin: http://localhost:3000" \
  -H "Access-Control-Request-Method: POST" \
  -H "Access-Control-Request-Headers: Content-Type,Authorization" \
  -v
```

Response headers:

```
Access-Control-Allow-Origin: http://localhost:3000
Access-Control-Allow-Methods: GET,POST,PUT,PATCH,DELETE,OPTIONS
Access-Control-Allow-Headers: Content-Type,Authorization,X-API-Key
Access-Control-Max-Age: 86400
```

The `OPTIONS` request returns `204 No Content` with those headers. The browser caches the preflight for 86400 seconds (24 hours). Subsequent requests skip the preflight.

### Wildcard Origins

During development:

```env
TINA4_CORS_ORIGINS=*
```

The default. Do not use `*` in production. Specify your domains.

### CORS Without Middleware

Set `TINA4_CORS_ORIGINS` in `.env` and Tina4 applies CORS headers globally. The middleware approach gives finer control -- CORS on specific groups, none on internal routes.

---

## 4. Built-in RateLimiter

Prevents a single client from flooding your API. Tracks requests per IP. Returns `429 Too Many Requests` when exceeded.

Configure in `.env`:

```env
TINA4_RATE_LIMIT=60
TINA4_RATE_WINDOW=60
```

60 requests per 60 seconds per IP. Apply it:

```php
<?php
use Tina4Router;

Router::group("/api/public", function () {

    Router::get("/search", function ($request, $response) {
        $q = $request->query["q"] ?? "";
        return $response->json(["query" => $q, "results" => []]);
    });

    Router::get("/catalog", function ($request, $response) {
        return $response->json(["items" => []]);
    });

}, "RateLimiter");
```

When exceeded:

```json
{"error":"Rate limit exceeded. Try again in 42 seconds.","retry_after":42}
```

A `Retry-After` header accompanies the response.

### Custom Limits Per Group

Override the global limit with a parameter:

```php
<?php
use Tina4Router;

// Public endpoints: 30 requests per minute
Router::group("/api/public", function () {
    Router::get("/search", function ($request, $response) {
        return $response->json(["results" => []]);
    });
}, "RateLimiter:30");

// Authenticated endpoints: 120 requests per minute
Router::group("/api/v1", function () {
    Router::get("/data", function ($request, $response) {
        return $response->json(["data" => []]);
    });
}, ["authMiddleware", "RateLimiter:120"]);
```

`"RateLimiter:30"` passes `30` as a parameter. Overrides the global setting for that group.

### Built-in RequestLogger

The `RequestLogger` middleware logs every request with its timing. It uses two hooks:

- `beforeLog` stamps the start time before the handler runs
- `afterLog` calculates elapsed time and writes an info-level log entry

Register it globally:

```php
<?php
use Tina4\Middleware;
use Tina4\Middleware\RequestLogger;

Middleware::use(RequestLogger::class);
```

The log output looks like:

```
GET /api/users 12.34ms
POST /api/products 45.67ms
```

You can also apply it to specific route groups:

```php
Router::group("/api", function () {
    Router::get("/products", function ($request, $response) {
        return $response->json(["products" => []]);
    });
}, "RequestLogger");
```

### Combining All Three Built-In Middleware

A common production setup registers all three globally:

```php
<?php
use Tina4\Middleware;
use Tina4\Middleware\CorsMiddleware;
use Tina4\Middleware\RateLimiter;
use Tina4\Middleware\RequestLogger;

Middleware::use(CorsMiddleware::class);
Middleware::use(RateLimiter::class);
Middleware::use(RequestLogger::class);
```

Order matters. CORS handles `OPTIONS` preflight first. The rate limiter only counts real requests (not preflight). The logger measures total time including the other middleware.

---

## 5. Writing Custom Middleware

Same pattern every time. Receive `$request`, `$response`, `$next`. Define as a named function.

### Request Logging Middleware

```php
<?php

function logRequest($request, $response, $next) {
    $start = microtime(true);
    $method = $request->method;
    $path = $request->path;
    $ip = $request->ip;

    error_log("[" . date("Y-m-d H:i:s") . "] " . $method . " " . $path . " from " . $ip);

    $result = $next($request, $response);

    $duration = round((microtime(true) - $start) * 1000, 2);
    error_log("  Completed in " . $duration . "ms");

    return $result;
}
```

Save in `src/routes/middleware.php`. Apply it:

```php
Router::get("/api/products", function ($request, $response) {
    return $response->json(["products" => []]);
}, "logRequest");
```

Server log:

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

    $response->addHeader("X-Response-Time", $duration . "ms");

    return $result;
}
```

Response headers:

```
X-Response-Time: 3.12ms
```

Frontend tools and monitoring systems read this header.

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

Ensures all write requests send JSON. Status: `415 Unsupported Media Type`.

### Writing Class-Based Middleware

For more complex middleware, use the class-based pattern with `before*` and `after*` static methods:

```php
<?php
use Tina4\Request;
use Tina4\Response;

class InputSanitizer
{
    public static function beforeSanitize(Request $request, Response $response): array
    {
        if (is_array($request->body)) {
            $request->body = self::sanitize($request->body);
        }
        return [$request, $response];
    }

    private static function sanitize(array $data): array
    {
        $clean = [];
        foreach ($data as $key => $value) {
            if (is_string($value)) {
                $clean[$key] = htmlspecialchars($value, ENT_QUOTES, 'UTF-8');
            } elseif (is_array($value)) {
                $clean[$key] = self::sanitize($value);
            } else {
                $clean[$key] = $value;
            }
        }
        return $clean;
    }
}
```

Register it globally or apply to specific groups:

```php
// Global registration
Middleware::use(InputSanitizer::class);

// Or on a specific group
Router::group("/api", function () {
    // routes here
}, "InputSanitizer");
```

### JWT Authentication Middleware (Class-Based)

A real-world authentication middleware that verifies JWT tokens:

```php
<?php
use Tina4\Auth;
use Tina4\Request;
use Tina4\Response;

class JwtAuthMiddleware
{
    public static function beforeVerifyToken(Request $request, Response $response): array
    {
        $authHeader = $request->headers["Authorization"] ?? "";

        if (empty($authHeader) || !str_starts_with($authHeader, "Bearer ")) {
            $response->status(401);
            return [$request, $response->json(["error" => "Authorization header required"])];
        }

        $token = substr($authHeader, 7);

        if (!Auth::validToken($token)) {
            $response->status(401);
            return [$request, $response->json(["error" => "Invalid or expired token"])];
        }

        $request->user = Auth::getPayload($token);
        return [$request, $response];
    }
}
```

Apply it to a group of protected routes:

```php
Router::group("/api/protected", function () {

    Router::get("/profile", function ($request, $response) {
        return $response->json(["user" => $request->user]);
    });

    Router::post("/settings", function ($request, $response) {
        $userId = $request->user["sub"];
        return $response->json(["updated" => true, "user_id" => $userId]);
    });

}, "JwtAuthMiddleware");
```

The middleware short-circuits with 401 if the token is missing or invalid. The decoded payload is available as `$request->user` in the handler.

---

## 6. Applying Middleware to Individual Routes

Third argument to any route method:

```php
<?php
use Tina4Router;

Router::get("/api/data", function ($request, $response) {
    return $response->json(["data" => [1, 2, 3]]);
}, "logRequest");

Router::post("/api/data", function ($request, $response) {
    return $response->json(["created" => true], 201);
}, ["logRequest", "requireJson"]);
```

String for one. Array for multiple. Each runs in listed order.

---

## 7. Route Groups with Shared Middleware

Groups apply middleware to every route inside:

```php
<?php
use Tina4Router;

// Public API -- rate limited, CORS enabled
Router::group("/api/public", function () {

    Router::get("/products", function ($request, $response) {
        return $response->json(["products" => []]);
    });

    Router::get("/categories", function ($request, $response) {
        return $response->json(["categories" => []]);
    });

}, ["CorsMiddleware", "RateLimiter:30"]);

// Admin API -- auth required, IP restricted, logged
Router::group("/api/admin", function () {

    Router::get("/users", function ($request, $response) {
        return $response->json(["users" => []]);
    });

    Router::delete("/users/{id:int}", function ($request, $response) {
        $id = $request->params["id"];
        return $response->json(["deleted" => $id]);
    });

}, ["logRequest", "ipWhitelist", "authMiddleware"]);
```

Routes inside a group can add their own middleware. Group middleware runs first, then route-specific:

```php
Router::group("/api", function () {

    // Execution: logRequest -> requireJson -> handler
    Router::post("/upload", function ($request, $response) {
        return $response->json(["uploaded" => true]);
    }, "requireJson");

}, "logRequest");
```

---

## 8. Middleware Execution Order

Middleware stacks like layers of an onion. First listed runs first on the way in, last on the way out.

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
Router::get("/api/test", function ($request, $response) {
    error_log("Handler");
    return $response->json(["ok" => true]);
}, ["middlewareA", "middlewareB", "middlewareC"]);
```

Server log:

```
A: before
B: before
C: before
Handler
C: after
B: after
A: after
```

The request flows inward: A, B, C, Handler. The response flows outward: C, B, A.

Placement matters:

- `middlewareA` sees the request first, the response last. CORS headers and logging go here.
- `middlewareC` sees the request last, the response first. Response transformations go here.
- Authentication goes early. Catch unauthorized requests before doing work.
- Timing goes outermost. Measure the entire pipeline.

### Group + Route Middleware Order

```php
Router::group("/api", function () {

    Router::get("/data", function ($request, $response) {
        return $response->json(["data" => true]);
    }, "middlewareC");

}, ["middlewareA", "middlewareB"]);
```

Execution: `middlewareA` -> `middlewareB` -> `middlewareC` -> handler. Group middleware always runs before route middleware.

---

## 9. Short-Circuiting

When middleware does not call `$next`, the chain stops. No subsequent middleware runs. The handler never executes.

### Authentication Short-Circuit

```php
<?php

function requireAuth($request, $response, $next) {
    $token = $request->headers["Authorization"] ?? "";

    if (empty($token)) {
        return $response->json(["error" => "Authentication required"], 401);
    }

    return $next($request, $response);
}
```

Missing header: `401` returned. Handler never runs. No database query. No business logic. Resources saved.

### Maintenance Mode

```php
<?php

function maintenanceMode($request, $response, $next) {
    $isMaintenanceMode = ($_ENV["MAINTENANCE_MODE"] ?? "false") === "true";

    if ($isMaintenanceMode) {
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

Add to `.env`:

```env
MAINTENANCE_MODE=true
```

Every request except `/health` gets `503 Service Unavailable`.

### Read-Only Mode

```php
<?php

function readOnly($request, $response, $next) {
    if (in_array($request->method, ["POST", "PUT", "PATCH", "DELETE"])) {
        return $response->json(["error" => "API is in read-only mode"], 405);
    }

    return $next($request, $response);
}
```

GET requests pass. Write operations blocked. Useful for standby replicas or demo environments.

---

## 10. Modifying Requests in Middleware

Middleware can attach data to the request before the handler sees it:

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

    // Always call $next -- this middleware does not block
    return $next($request, $response);
}
```

Different from blocking auth middleware. This attaches user data if present but does not reject unauthenticated requests. Some routes need user data for personalization but remain accessible without it.

### Adding Request Metadata

```php
<?php

function addRequestId($request, $response, $next) {
    $requestId = bin2hex(random_bytes(8));
    $request->requestId = $requestId;

    $result = $next($request, $response);

    $response->addHeader("X-Request-Id", $requestId);

    return $result;
}
```

The handler accesses `$request->requestId` for logging and correlation:

```php
Router::get("/api/data", function ($request, $response) {
    error_log("[" . $request->requestId . "] Processing data request");
    return $response->json(["request_id" => $request->requestId, "data" => []]);
}, "addRequestId");
```

---

## 11. Real-World Middleware Stack

A realistic production setup:

```php
<?php
use Tina4Router;

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
use Tina4Router;

// src/routes/api.php

Router::group("/api/v1", function () {

    Router::get("/products", function ($request, $response) {
        return $response->json(["products" => [
            ["id" => 1, "name" => "Widget", "price" => 9.99],
            ["id" => 2, "name" => "Gadget", "price" => 19.99]
        ]]);
    });

    Router::get("/products/{id:int}", function ($request, $response) {
        $id = $request->params["id"];
        return $response->json(["id" => $id, "name" => "Widget", "price" => 9.99]);
    });

    Router::post("/products", function ($request, $response) {
        $body = $request->body;
        return $response->json([
            "id" => 3,
            "name" => $body["name"] ?? "Unknown",
            "price" => (float) ($body["price"] ?? 0)
        ], 201);
    });

}, ["addRequestId", "logRequest", "CorsMiddleware", "requireApiKey"]);
```

Without API key:

```json
{"error":"Invalid or missing API key","request_id":"a1b2c3d4e5f6a7b8"}
```

With valid key:

```json
{"products":[{"id":1,"name":"Widget","price":9.99},{"id":2,"name":"Gadget","price":19.99}]}
```

---

## 12. Exercise: Build an API Key Middleware

Build `validateApiKey` middleware:

1. Check for `X-API-Key` header
2. Validate against a comma-separated list in `API_KEYS` env variable
3. Missing key: `401` with `{"error": "API key required"}`
4. Invalid key: `403` with `{"error": "Invalid API key"}`
5. Valid key: attach to `$request->apiKey` and continue
6. Apply to a group with at least two endpoints

### Setup

```env
API_KEYS=key-alpha-001,key-beta-002,key-gamma-003
```

### Test with:

```bash
# No key -- 401
curl http://localhost:7146/api/partner/data

# Invalid key -- 403
curl http://localhost:7146/api/partner/data \
  -H "X-API-Key: wrong-key"

# Valid key -- 200
curl http://localhost:7146/api/partner/data \
  -H "X-API-Key: key-alpha-001"

# Valid key on another endpoint
curl http://localhost:7146/api/partner/stats \
  -H "X-API-Key: key-beta-002"
```

---

## 13. Solution

Create `src/routes/api-key-middleware.php`:

```php
<?php
use Tina4Router;

function validateApiKey($request, $response, $next) {
    $apiKey = $request->headers["X-API-Key"] ?? "";

    if (empty($apiKey)) {
        return $response->json(["error" => "API key required"], 401);
    }

    $validKeys = array_map("trim", explode(",", $_ENV["API_KEYS"] ?? ""));

    if (!in_array($apiKey, $validKeys)) {
        return $response->json(["error" => "Invalid API key"], 403);
    }

    $request->apiKey = $apiKey;

    return $next($request, $response);
}

Router::group("/api/partner", function () {

    Router::get("/data", function ($request, $response) {
        return $response->json([
            "authenticated_with" => $request->apiKey,
            "data" => [
                ["id" => 1, "value" => "alpha"],
                ["id" => 2, "value" => "beta"]
            ]
        ]);
    });

    Router::get("/stats", function ($request, $response) {
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

**No key:** `401` -- `{"error":"API key required"}`

**Invalid key:** `403` -- `{"error":"Invalid API key"}`

**Valid key:**

```json
{
  "authenticated_with": "key-alpha-001",
  "data": [
    {"id": 1, "value": "alpha"},
    {"id": 2, "value": "beta"}
  ]
}
```

---

## 14. Gotchas

### 1. Middleware Must Be a Named Function

**Problem:** Anonymous closure as middleware causes an error.

**Cause:** Tina4 resolves middleware by string name at runtime.

**Fix:** Named function: `function myMiddleware($request, $response, $next) { ... }`. Pass as string: `"myMiddleware"`.

### 2. Forgetting to Return $next()

**Problem:** Middleware runs. Handler never executes. Empty response or 500.

**Cause:** Called `$next($request, $response)` but did not `return` the result.

**Fix:** `return $next($request, $response)`. Without `return`, the response from the handler is discarded.

### 3. Middleware Order Matters

**Problem:** Logging middleware does not see the request ID.

**Cause:** `logRequest` runs before `addRequestId`.

**Fix:** Put `addRequestId` first: `["addRequestId", "logRequest"]`. Think: what needs to happen first.

### 4. CORS Preflight Returns 404

**Problem:** Browser `OPTIONS` request gets 404. `GET` and `POST` work with curl.

**Cause:** No `CorsMiddleware` on the route group. `OPTIONS` is not handled.

**Fix:** Apply `CorsMiddleware`. It handles `OPTIONS` and returns correct CORS headers. Or set `CORS_ORIGINS` in `.env` for global handling.

### 5. Rate Limiter Counts Preflight Requests

**Problem:** Frontend hits rate limit faster than expected. Every `POST` counts as two (OPTIONS + POST).

**Fix:** Put `CorsMiddleware` before `RateLimiter`: `["CorsMiddleware", "RateLimiter"]`. CORS handles `OPTIONS` and returns. The rate limiter only sees real requests.

### 6. Middleware File Not Auto-Loaded

**Problem:** "Function not found" when referencing middleware.

**Cause:** File is not in `src/routes/`. Tina4 auto-loads `.php` files from that directory only.

**Fix:** Put middleware in `src/routes/middleware.php`. Filename does not matter. Location does.

### 7. Short-Circuiting Skips Cleanup Middleware

**Problem:** Timing middleware logs start but never logs completion for blocked requests.

**Cause:** When an inner middleware short-circuits, outer middleware code after `$next()` still runs. But if the short-circuiting middleware is listed before the timing middleware, timing never executes.

**Fix:** Put cleanup-dependent middleware (timing, logging) outermost. They wrap the entire chain. Code after `$next()` in outer middleware always runs, even when inner middleware short-circuits.
