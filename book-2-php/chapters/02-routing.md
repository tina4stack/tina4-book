# Chapter 2: Routing

## 1. How Routing Works in Tina4

Every web application maps URLs to code. You type `/products` in your browser, the framework finds the function that handles `/products`, runs it, and sends back the result. That mapping is called routing.

In Tina4, you define routes in PHP files inside `src/routes/`. Every `.php` file in that directory (and its subdirectories) is auto-loaded when the server starts. You do not need to register files or update a central config -- just drop a file in and it works.

Here is the simplest possible route:

```php
<?php
use Tina4\Route;

Route::get("/hello", function ($request, $response) {
    return $response->json(["message" => "Hello, World!"]);
});
```

Save that as `src/routes/hello.php`, start the server with `tina4 serve`, and visit `http://localhost:7145/hello`:

```json
{"message":"Hello, World!"}
```

That is it. One line registers the route, one line handles the request.

---

## 2. HTTP Methods

Tina4 supports all five standard HTTP methods. Each one has a static method on the `Route` class:

```php
<?php
use Tina4\Route;

Route::get("/products", function ($request, $response) {
    return $response->json(["action" => "list all products"]);
});

Route::post("/products", function ($request, $response) {
    return $response->json(["action" => "create a product"], 201);
});

Route::put("/products/{id}", function ($request, $response) {
    $id = $request->params["id"];
    return $response->json(["action" => "replace product " . $id]);
});

Route::patch("/products/{id}", function ($request, $response) {
    $id = $request->params["id"];
    return $response->json(["action" => "update product " . $id]);
});

Route::delete("/products/{id}", function ($request, $response) {
    $id = $request->params["id"];
    return $response->json(["action" => "delete product " . $id]);
});
```

Test each one:

```bash
curl http://localhost:7145/products
```

```json
{"action":"list all products"}
```

```bash
curl -X POST http://localhost:7145/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Widget"}'
```

```json
{"action":"create a product"}
```

```bash
curl -X PUT http://localhost:7145/products/42
```

```json
{"action":"replace product 42"}
```

```bash
curl -X PATCH http://localhost:7145/products/42
```

```json
{"action":"update product 42"}
```

```bash
curl -X DELETE http://localhost:7145/products/42
```

```json
{"action":"delete product 42"}
```

Use `GET` for reading, `POST` for creating, `PUT` for full replacement, `PATCH` for partial updates, and `DELETE` for removal. This follows the REST convention and makes your API predictable.

---

## 3. Path Parameters

Path parameters let you capture values from the URL. Wrap the parameter name in curly braces:

```php
<?php
use Tina4\Route;

Route::get("/users/{id}/posts/{postId}", function ($request, $response) {
    $userId = $request->params["id"];
    $postId = $request->params["postId"];

    return $response->json([
        "user_id" => $userId,
        "post_id" => $postId
    ]);
});
```

```bash
curl http://localhost:7145/users/5/posts/99
```

```json
{"user_id":"5","post_id":"99"}
```

Notice that `user_id` came back as the string `"5"`, not the integer `5`. Path parameters are always strings by default.

### Typed Parameters

You can enforce a type by adding a colon and the type after the parameter name:

```php
<?php
use Tina4\Route;

Route::get("/orders/{id:int}", function ($request, $response) {
    $id = $request->params["id"]; // This is now an integer
    return $response->json([
        "order_id" => $id,
        "type" => gettype($id)
    ]);
});
```

```bash
curl http://localhost:7145/orders/42
```

```json
{"order_id":42,"type":"integer"}
```

If you pass a non-integer value, the route will not match and you will get a 404:

```bash
curl http://localhost:7145/orders/abc
```

```json
{"error":"Not found","path":"/orders/abc","status":404}
```

Supported types:

| Type | Matches | Example |
|------|---------|---------|
| `int` | Digits only | `{id:int}` matches `42` but not `abc` |
| `float` | Decimal numbers | `{price:float}` matches `19.99` |
| `alpha` | Letters only | `{slug:alpha}` matches `hello` but not `hello123` |
| `alphanumeric` | Letters and digits | `{code:alphanumeric}` matches `abc123` |

---

## 4. Query Parameters

Query parameters are the key-value pairs after the `?` in a URL. Access them via `$request->query`:

```php
<?php
use Tina4\Route;

Route::get("/search", function ($request, $response) {
    $q = $request->query["q"] ?? "";
    $page = (int) ($request->query["page"] ?? 1);
    $limit = (int) ($request->query["limit"] ?? 10);

    return $response->json([
        "query" => $q,
        "page" => $page,
        "limit" => $limit,
        "offset" => ($page - 1) * $limit
    ]);
});
```

```bash
curl "http://localhost:7145/search?q=keyboard&page=2&limit=20"
```

```json
{"query":"keyboard","page":2,"limit":20,"offset":20}
```

If a query parameter is missing, `$request->query["key"]` will not exist, so always use the null coalescing operator (`??`) to provide defaults.

---

## 5. Route Groups

When you have a set of routes that share a common prefix, use `Route::group()` to avoid repeating yourself:

```php
<?php
use Tina4\Route;

Route::group("/api/v1", function () {

    Route::get("/users", function ($request, $response) {
        return $response->json(["users" => []]);
    });

    Route::get("/users/{id:int}", function ($request, $response) {
        $id = $request->params["id"];
        return $response->json(["user" => ["id" => $id, "name" => "Alice"]]);
    });

    Route::post("/users", function ($request, $response) {
        return $response->json(["created" => true], 201);
    });

    Route::get("/products", function ($request, $response) {
        return $response->json(["products" => []]);
    });
});
```

The routes above register as `/api/v1/users`, `/api/v1/users/{id}`, and `/api/v1/products`. You write short paths inside the group, and Tina4 prepends the prefix automatically.

```bash
curl http://localhost:7145/api/v1/users
```

```json
{"users":[]}
```

```bash
curl http://localhost:7145/api/v1/products
```

```json
{"products":[]}
```

Groups can be nested:

```php
<?php
use Tina4\Route;

Route::group("/api", function () {
    Route::group("/v1", function () {
        Route::get("/status", function ($request, $response) {
            return $response->json(["version" => "1.0"]);
        });
    });

    Route::group("/v2", function () {
        Route::get("/status", function ($request, $response) {
            return $response->json(["version" => "2.0"]);
        });
    });
});
```

```bash
curl http://localhost:7145/api/v1/status
```

```json
{"version":"1.0"}
```

```bash
curl http://localhost:7145/api/v2/status
```

```json
{"version":"2.0"}
```

---

## 6. Middleware

Middleware is code that runs before (or after) your route handler. Use it for authentication, logging, rate limiting, input validation, or anything that should happen on multiple routes.

### Middleware on a Single Route

Pass middleware as the third argument to any route method:

```php
<?php
use Tina4\Route;

function logRequest($request, $response, $next) {
    $start = microtime(true);
    error_log("[" . date("Y-m-d H:i:s") . "] " . $request->method . " " . $request->path);

    $result = $next($request, $response);

    $duration = round((microtime(true) - $start) * 1000, 2);
    error_log("  Completed in " . $duration . "ms");

    return $result;
}

Route::get("/api/data", function ($request, $response) {
    return $response->json(["data" => [1, 2, 3]]);
}, "logRequest");
```

The middleware function receives `$request`, `$response`, and `$next`. Call `$next($request, $response)` to continue to the route handler. If you do not call `$next`, the route handler never runs -- useful for blocking unauthorized requests.

### Blocking Middleware

Here is middleware that checks for an API key:

```php
<?php
use Tina4\Route;

function requireApiKey($request, $response, $next) {
    $apiKey = $request->headers["X-API-Key"] ?? "";

    if ($apiKey !== "my-secret-key") {
        return $response->json(["error" => "Invalid API key"], 401);
    }

    return $next($request, $response);
}

Route::get("/api/secret", function ($request, $response) {
    return $response->json(["secret" => "The answer is 42"]);
}, "requireApiKey");
```

```bash
curl http://localhost:7145/api/secret
```

```json
{"error":"Invalid API key"}
```

The response status is `401 Unauthorized`.

```bash
curl http://localhost:7145/api/secret -H "X-API-Key: my-secret-key"
```

```json
{"secret":"The answer is 42"}
```

### Middleware on a Group

Apply middleware to an entire group by passing it as the third argument to `Route::group()`:

```php
<?php
use Tina4\Route;

function requireAuth($request, $response, $next) {
    $token = $request->headers["Authorization"] ?? "";

    if (empty($token)) {
        return $response->json(["error" => "Authentication required"], 401);
    }

    return $next($request, $response);
}

Route::group("/api/admin", function () {

    Route::get("/dashboard", function ($request, $response) {
        return $response->json(["page" => "admin dashboard"]);
    });

    Route::get("/users", function ($request, $response) {
        return $response->json(["page" => "user management"]);
    });

}, "requireAuth");
```

Every route inside the group now requires the `Authorization` header. You do not need to add the middleware to each route individually.

### Multiple Middleware

Chain multiple middleware by passing an array:

```php
Route::get("/api/important", function ($request, $response) {
    return $response->json(["data" => "important stuff"]);
}, ["logRequest", "requireApiKey", "requireAuth"]);
```

Middleware runs in order: `logRequest` first, then `requireApiKey`, then `requireAuth`, then the route handler. If any middleware does not call `$next`, the chain stops there.

---

## 7. Route Decorators: @noauth and @secured

Tina4 provides two special decorators for controlling authentication on routes.

### @noauth -- Public Routes

When your application has global authentication middleware, use the `@noauth` annotation to mark specific routes as public:

```php
<?php
use Tina4\Route;

/**
 * @noauth
 */
Route::get("/api/public/info", function ($request, $response) {
    return $response->json([
        "app" => "My Store",
        "version" => "1.0.0"
    ]);
});
```

The `@noauth` decorator tells Tina4 to skip authentication checks for this route, even if global auth middleware is configured in `.env` or applied to the parent group.

### @secured -- Protected GET Routes

The `@secured` annotation explicitly marks a GET route as requiring authentication:

```php
<?php
use Tina4\Route;

/**
 * @secured
 */
Route::get("/api/profile", function ($request, $response) {
    // $request->user is populated by the auth middleware
    return $response->json([
        "user" => $request->user
    ]);
});
```

By default, `POST`, `PUT`, `PATCH`, and `DELETE` routes are considered secured. `GET` routes are not -- they are public unless you add `@secured`. This matches the common pattern where reading data is public but modifying data requires authentication.

---

## 8. Wildcard and Catch-All Routes

### Wildcard Routes

Use `*` at the end of a path to match anything after it:

```php
<?php
use Tina4\Route;

Route::get("/docs/*", function ($request, $response) {
    $path = $request->params["*"] ?? "";
    return $response->json([
        "section" => "docs",
        "path" => $path
    ]);
});
```

```bash
curl http://localhost:7145/docs/getting-started
```

```json
{"section":"docs","path":"getting-started"}
```

```bash
curl http://localhost:7145/docs/api/authentication/jwt
```

```json
{"section":"docs","path":"api/authentication/jwt"}
```

### Catch-All Route (Custom 404)

Register a catch-all to handle any unmatched URL:

```php
<?php
use Tina4\Route;

Route::get("/*", function ($request, $response) {
    return $response->json([
        "error" => "Page not found",
        "path" => $request->path
    ], 404);
});
```

This route should be defined last (or in a file that sorts alphabetically after your other route files) so it does not shadow your real routes. Tina4 matches routes in the order they are registered -- the first match wins.

Alternatively, you can create a custom 404 page by placing a template at `src/templates/errors/404.html`:

```html
{% extends "base.html" %}

{% block title %}Not Found{% endblock %}

{% block content %}
    <h1>404 - Page Not Found</h1>
    <p>The page you are looking for does not exist.</p>
    <a href="/">Go back home</a>
{% endblock %}
```

Tina4 automatically uses this template for any unmatched route when the template file exists.

---

## 9. Route Listing via CLI

As your application grows, you will want to see all registered routes at a glance. Use the Tina4 CLI:

```bash
tina4 routes
```

```
Method   Path                          Middleware          Auth
------   ----                          ----------          ----
GET      /hello                        -                   public
GET      /products                     -                   public
POST     /products                     -                   secured
PUT      /products/{id}                -                   secured
PATCH    /products/{id}                -                   secured
DELETE   /products/{id}                -                   secured
GET      /api/v1/users                 -                   public
GET      /api/v1/users/{id:int}        -                   public
POST     /api/v1/users                 -                   secured
GET      /api/admin/dashboard          requireAuth         public
GET      /api/admin/users              requireAuth         public
GET      /api/public/info              -                   @noauth
GET      /api/profile                  -                   @secured
GET      /search                       -                   public
GET      /docs/*                       -                   public
```

The `Auth` column shows whether a route is public, secured (default for non-GET methods), explicitly `@noauth`, or explicitly `@secured`.

You can also filter by method:

```bash
tina4 routes --method POST
```

```
Method   Path                          Middleware          Auth
------   ----                          ----------          ----
POST     /products                     -                   secured
POST     /api/v1/users                 -                   secured
```

Or search for a specific path pattern:

```bash
tina4 routes --filter users
```

```
Method   Path                          Middleware          Auth
------   ----                          ----------          ----
GET      /api/v1/users                 -                   public
GET      /api/v1/users/{id:int}        -                   public
POST     /api/v1/users                 -                   secured
GET      /api/admin/users              requireAuth         public
```

---

## 10. Organizing Route Files

You are free to organize route files any way you like. Tina4 loads every `.php` file in `src/routes/` recursively. Here are two common patterns:

### Pattern 1: One File Per Resource

```
src/routes/
├── products.php     # All product routes
├── users.php        # All user routes
├── orders.php       # All order routes
└── pages.php        # HTML page routes
```

### Pattern 2: Subdirectories by Feature

```
src/routes/
├── api/
│   ├── products.php
│   ├── users.php
│   └── orders.php
├── admin/
│   ├── dashboard.php
│   └── settings.php
└── pages/
    ├── home.php
    └── about.php
```

Both patterns work identically. The directory structure has no effect on the URL paths -- only the route definitions inside the files matter. Choose whichever pattern keeps your project navigable.

---

## 11. Exercise: Build a Full CRUD API for Products

Build a complete REST API for managing products. All data is stored in a PHP array (no database yet -- we will add that in Chapter 5).

### Requirements

Create a file `src/routes/product-api.php` with the following routes:

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/products` | List all products. Support `?category=` filter. |
| `GET` | `/api/products/{id:int}` | Get a single product by ID. Return 404 if not found. |
| `POST` | `/api/products` | Create a new product. Return 201. |
| `PUT` | `/api/products/{id:int}` | Replace a product. Return 404 if not found. |
| `DELETE` | `/api/products/{id:int}` | Delete a product. Return 204 with no body. |

Each product has: `id` (int), `name` (string), `category` (string), `price` (float), `in_stock` (bool).

Start with this seed data:

```php
$products = [
    ["id" => 1, "name" => "Wireless Keyboard", "category" => "Electronics", "price" => 79.99, "in_stock" => true],
    ["id" => 2, "name" => "Yoga Mat", "category" => "Fitness", "price" => 29.99, "in_stock" => true],
    ["id" => 3, "name" => "Coffee Grinder", "category" => "Kitchen", "price" => 49.99, "in_stock" => false],
    ["id" => 4, "name" => "Standing Desk", "category" => "Office", "price" => 549.99, "in_stock" => true],
    ["id" => 5, "name" => "Running Shoes", "category" => "Fitness", "price" => 119.99, "in_stock" => true]
];
```

Test with:

```bash
# List all
curl http://localhost:7145/api/products

# Filter by category
curl "http://localhost:7145/api/products?category=Fitness"

# Get one
curl http://localhost:7145/api/products/3

# Create
curl -X POST http://localhost:7145/api/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Desk Lamp", "category": "Office", "price": 39.99, "in_stock": true}'

# Update
curl -X PUT http://localhost:7145/api/products/3 \
  -H "Content-Type: application/json" \
  -d '{"name": "Burr Coffee Grinder", "category": "Kitchen", "price": 59.99, "in_stock": true}'

# Delete
curl -X DELETE http://localhost:7145/api/products/3

# Not found
curl http://localhost:7145/api/products/999
```

---

## 12. Solution

Create `src/routes/product-api.php`:

```php
<?php
use Tina4\Route;

// In-memory product store (resets on server restart)
$products = [
    ["id" => 1, "name" => "Wireless Keyboard", "category" => "Electronics", "price" => 79.99, "in_stock" => true],
    ["id" => 2, "name" => "Yoga Mat", "category" => "Fitness", "price" => 29.99, "in_stock" => true],
    ["id" => 3, "name" => "Coffee Grinder", "category" => "Kitchen", "price" => 49.99, "in_stock" => false],
    ["id" => 4, "name" => "Standing Desk", "category" => "Office", "price" => 549.99, "in_stock" => true],
    ["id" => 5, "name" => "Running Shoes", "category" => "Fitness", "price" => 119.99, "in_stock" => true]
];

$nextId = 6;

// List all products, optionally filter by category
Route::get("/api/products", function ($request, $response) use (&$products) {
    $category = $request->query["category"] ?? null;

    if ($category !== null) {
        $filtered = array_values(array_filter(
            $products,
            fn($p) => strtolower($p["category"]) === strtolower($category)
        ));
        return $response->json(["products" => $filtered, "count" => count($filtered)]);
    }

    return $response->json(["products" => $products, "count" => count($products)]);
});

// Get a single product by ID
Route::get("/api/products/{id:int}", function ($request, $response) use (&$products) {
    $id = $request->params["id"];

    foreach ($products as $product) {
        if ($product["id"] === $id) {
            return $response->json($product);
        }
    }

    return $response->json(["error" => "Product not found", "id" => $id], 404);
});

// Create a new product
Route::post("/api/products", function ($request, $response) use (&$products, &$nextId) {
    $body = $request->body;

    if (empty($body["name"])) {
        return $response->json(["error" => "Name is required"], 400);
    }

    $product = [
        "id" => $nextId++,
        "name" => $body["name"],
        "category" => $body["category"] ?? "Uncategorized",
        "price" => (float) ($body["price"] ?? 0),
        "in_stock" => (bool) ($body["in_stock"] ?? true)
    ];

    $products[] = $product;

    return $response->json($product, 201);
});

// Replace a product
Route::put("/api/products/{id:int}", function ($request, $response) use (&$products) {
    $id = $request->params["id"];
    $body = $request->body;

    foreach ($products as $index => $product) {
        if ($product["id"] === $id) {
            $products[$index] = [
                "id" => $id,
                "name" => $body["name"] ?? $product["name"],
                "category" => $body["category"] ?? $product["category"],
                "price" => (float) ($body["price"] ?? $product["price"]),
                "in_stock" => (bool) ($body["in_stock"] ?? $product["in_stock"])
            ];
            return $response->json($products[$index]);
        }
    }

    return $response->json(["error" => "Product not found", "id" => $id], 404);
});

// Delete a product
Route::delete("/api/products/{id:int}", function ($request, $response) use (&$products) {
    $id = $request->params["id"];

    foreach ($products as $index => $product) {
        if ($product["id"] === $id) {
            array_splice($products, $index, 1);
            return $response->json(null, 204);
        }
    }

    return $response->json(["error" => "Product not found", "id" => $id], 404);
});
```

**Expected output for the test commands:**

List all:

```json
{"products":[{"id":1,"name":"Wireless Keyboard","category":"Electronics","price":79.99,"in_stock":true},{"id":2,"name":"Yoga Mat","category":"Fitness","price":29.99,"in_stock":true},{"id":3,"name":"Coffee Grinder","category":"Kitchen","price":49.99,"in_stock":false},{"id":4,"name":"Standing Desk","category":"Office","price":549.99,"in_stock":true},{"id":5,"name":"Running Shoes","category":"Fitness","price":119.99,"in_stock":true}],"count":5}
```

Filter by category:

```json
{"products":[{"id":2,"name":"Yoga Mat","category":"Fitness","price":29.99,"in_stock":true},{"id":5,"name":"Running Shoes","category":"Fitness","price":119.99,"in_stock":true}],"count":2}
```

Get one:

```json
{"id":3,"name":"Coffee Grinder","category":"Kitchen","price":49.99,"in_stock":false}
```

Create:

```json
{"id":6,"name":"Desk Lamp","category":"Office","price":39.99,"in_stock":true}
```

(Status: `201 Created`)

Update:

```json
{"id":3,"name":"Burr Coffee Grinder","category":"Kitchen","price":59.99,"in_stock":true}
```

Delete: empty response with status `204 No Content`.

Not found:

```json
{"error":"Product not found","id":999}
```

(Status: `404 Not Found`)

---

## 13. Gotchas

### 1. Trailing Slashes Matter

**Problem:** `/products` works but `/products/` returns a 404 (or vice versa).

**Cause:** Tina4 treats `/products` and `/products/` as different routes by default.

**Fix:** Pick one convention and stick with it. If you want both to work, register the route without a trailing slash -- Tina4 will redirect `/products/` to `/products` automatically when `TINA4_TRAILING_SLASH_REDIRECT=true` is set in `.env`.

### 2. Parameter Names Must Be Unique in a Path

**Problem:** `/users/{id}/posts/{id}` does not work as expected -- both parameters have the same name.

**Cause:** The second `{id}` overwrites the first in `$request->params`.

**Fix:** Use distinct names: `/users/{userId}/posts/{postId}`.

### 3. Method Conflicts

**Problem:** You defined `Route::get("/items/{id}", ...)` and `Route::get("/items/{action}", ...)` and the wrong handler runs.

**Cause:** Both patterns match `/items/42`. The first one registered wins.

**Fix:** Use typed parameters to disambiguate: `Route::get("/items/{id:int}", ...)` will only match integers, leaving `/items/export` free for the other route. Alternatively, restructure your paths: `/items/{id:int}` and `/items/actions/{action}`.

### 4. Route Handler Must Return a Response

**Problem:** Your route handler runs but the browser shows an empty page or a 500 error.

**Cause:** You forgot the `return` statement. Without `return`, the handler returns `null` and Tina4 does not know what to send back.

**Fix:** Always `return $response->json(...)` or `return $response->html(...)` or `return $response->render(...)`. Every handler must return something.

### 5. Route Files Must Start with `<?php`

**Problem:** Your route file is ignored. No errors, just no routes registered.

**Cause:** The file does not start with `<?php`. Without the PHP opening tag, the file is not parsed as PHP code.

**Fix:** Make sure every route file starts with `<?php` on the very first line.

### 6. Middleware Function Must Be a String Name

**Problem:** Passing a closure directly as middleware causes an error.

**Cause:** Tina4 expects middleware to be referenced by function name (a string), not as an inline closure.

**Fix:** Define your middleware as a named function and pass the name as a string: `"myMiddleware"`, not `function ($request, $response, $next) { ... }`.

### 7. Group Prefix Must Start with a Slash

**Problem:** `Route::group("api/v1", ...)` produces routes like `/api/v1/users` but they do not match.

**Cause:** The group prefix should start with `/` for consistency. While Tina4 may auto-correct this, it is better to be explicit.

**Fix:** Always start group prefixes with `/`: `Route::group("/api/v1", ...)`.
