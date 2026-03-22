# Chapter 2: Routing

## 1. How Routing Works in Tina4

Every web application maps URLs to code. You type `/products` in your browser, the framework finds the function that handles `/products`, runs it, and sends back the result. That mapping is called routing.

In Tina4 Python, you define routes in Python files inside `src/routes/`. Every `.py` file in that directory (and its subdirectories) is auto-loaded when the server starts. You do not need to register files or update a central config -- just drop a file in and it works.

Here is the simplest possible route:

```python
from tina4_python.core.router import get

@get("/hello")
async def hello(request, response):
    return response.json({"message": "Hello, World!"})
```

Save that as `src/routes/hello.py`, start the server with `tina4 serve`, and visit `http://localhost:7145/hello`:

```json
{"message":"Hello, World!"}
```

That is it. One decorator registers the route, one function handles the request.

---

## 2. HTTP Methods

Tina4 supports all five standard HTTP methods. Each one has a corresponding decorator:

```python
from tina4_python.core.router import get, post, put, patch, delete

@get("/products")
async def list_products(request, response):
    return response.json({"action": "list all products"})

@post("/products")
async def create_product(request, response):
    return response.json({"action": "create a product"}, 201)

@put("/products/{id}")
async def replace_product(request, response):
    id = request.params["id"]
    return response.json({"action": f"replace product {id}"})

@patch("/products/{id}")
async def update_product(request, response):
    id = request.params["id"]
    return response.json({"action": f"update product {id}"})

@delete("/products/{id}")
async def delete_product(request, response):
    id = request.params["id"]
    return response.json({"action": f"delete product {id}"})
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

```python
from tina4_python.core.router import get

@get("/users/{id}/posts/{post_id}")
async def user_post(request, response):
    user_id = request.params["id"]
    post_id = request.params["post_id"]

    return response.json({
        "user_id": user_id,
        "post_id": post_id
    })
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

```python
from tina4_python.core.router import get

@get("/orders/{id:int}")
async def get_order(request, response):
    id = request.params["id"]  # This is now an integer
    return response.json({
        "order_id": id,
        "type": type(id).__name__
    })
```

```bash
curl http://localhost:7145/orders/42
```

```json
{"order_id":42,"type":"int"}
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

Query parameters are the key-value pairs after the `?` in a URL. Access them via `request.query`:

```python
from tina4_python.core.router import get

@get("/search")
async def search(request, response):
    q = request.query.get("q", "")
    page = int(request.query.get("page", 1))
    limit = int(request.query.get("limit", 10))

    return response.json({
        "query": q,
        "page": page,
        "limit": limit,
        "offset": (page - 1) * limit
    })
```

```bash
curl "http://localhost:7145/search?q=keyboard&page=2&limit=20"
```

```json
{"query":"keyboard","page":2,"limit":20,"offset":20}
```

If a query parameter is missing, `request.query.get("key")` returns `None`, so always use `.get()` with a default value.

---

## 5. Route Groups

When you have a set of routes that share a common prefix, use `group()` to avoid repeating yourself:

```python
from tina4_python.core.router import get, post, group

@group("/api/v1")
def api_v1():

    @get("/users")
    async def list_users(request, response):
        return response.json({"users": []})

    @get("/users/{id:int}")
    async def get_user(request, response):
        id = request.params["id"]
        return response.json({"user": {"id": id, "name": "Alice"}})

    @post("/users")
    async def create_user(request, response):
        return response.json({"created": True}, 201)

    @get("/products")
    async def list_products(request, response):
        return response.json({"products": []})
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

```python
from tina4_python.core.router import get, group

@group("/api")
def api():

    @group("/v1")
    def v1():
        @get("/status")
        async def v1_status(request, response):
            return response.json({"version": "1.0"})

    @group("/v2")
    def v2():
        @get("/status")
        async def v2_status(request, response):
            return response.json({"version": "2.0"})
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

## 6. Middleware on Routes

Middleware is code that runs before (or after) your route handler. Use it for authentication, logging, rate limiting, input validation, or anything that should happen on multiple routes. We will cover middleware in depth in Chapter 8, but here is how it works with routes.

### Middleware on a Single Route

Use the `@middleware` decorator to attach middleware to a route:

```python
from tina4_python.core.router import get, middleware
import time

async def log_request(request, response, next_handler):
    start = time.time()
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {request.method} {request.path}")

    result = await next_handler(request, response)

    duration = round((time.time() - start) * 1000, 2)
    print(f"  Completed in {duration}ms")

    return result

@get("/api/data")
@middleware(log_request)
async def get_data(request, response):
    return response.json({"data": [1, 2, 3]})
```

The middleware function receives `request`, `response`, and `next_handler`. Call `await next_handler(request, response)` to continue to the route handler. If you do not call `next_handler`, the route handler never runs -- useful for blocking unauthorized requests.

### Blocking Middleware

Here is middleware that checks for an API key:

```python
from tina4_python.core.router import get, middleware

async def require_api_key(request, response, next_handler):
    api_key = request.headers.get("X-API-Key", "")

    if api_key != "my-secret-key":
        return response.json({"error": "Invalid API key"}, 401)

    return await next_handler(request, response)

@get("/api/secret")
@middleware(require_api_key)
async def secret_data(request, response):
    return response.json({"secret": "The answer is 42"})
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

### Multiple Middleware

Chain multiple middleware by passing them as arguments:

```python
@get("/api/important")
@middleware(log_request, require_api_key)
async def important_data(request, response):
    return response.json({"data": "important stuff"})
```

Middleware runs in order: `log_request` first, then `require_api_key`, then the route handler. If any middleware does not call `next_handler`, the chain stops there.

---

## 7. Route Decorators: @noauth and @secured

Tina4 provides two special decorators for controlling authentication on routes.

### @noauth -- Public Routes

When your application has global authentication middleware, use `@noauth` to mark specific routes as public:

```python
from tina4_python.core.router import get, noauth

@get("/api/public/info")
@noauth
async def public_info(request, response):
    return response.json({
        "app": "My Store",
        "version": "1.0.0"
    })
```

The `@noauth` decorator tells Tina4 to skip authentication checks for this route, even if global auth middleware is configured in `.env` or applied to the parent group.

### @secured -- Protected GET Routes

The `@secured` decorator explicitly marks a GET route as requiring authentication:

```python
from tina4_python.core.router import get, secured

@get("/api/profile")
@secured
async def profile(request, response):
    # request.user is populated by the auth middleware
    return response.json({
        "user": request.user
    })
```

By default, `POST`, `PUT`, `PATCH`, and `DELETE` routes are considered secured. `GET` routes are not -- they are public unless you add `@secured`. This matches the common pattern where reading data is public but modifying data requires authentication.

---

## 8. Wildcard and Catch-All Routes

### Wildcard Routes

Use `*` at the end of a path to match anything after it:

```python
from tina4_python.core.router import get

@get("/docs/*")
async def docs_handler(request, response):
    path = request.params.get("*", "")
    return response.json({
        "section": "docs",
        "path": path
    })
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

```python
from tina4_python.core.router import get

@get("/*")
async def not_found(request, response):
    return response.json({
        "error": "Page not found",
        "path": request.path
    }, 404)
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
```

---

## 10. Organizing Route Files

You are free to organize route files any way you like. Tina4 loads every `.py` file in `src/routes/` recursively. Here are two common patterns:

### Pattern 1: One File Per Resource

```
src/routes/
├── products.py     # All product routes
├── users.py        # All user routes
├── orders.py       # All order routes
└── pages.py        # HTML page routes
```

### Pattern 2: Subdirectories by Feature

```
src/routes/
├── api/
│   ├── products.py
│   ├── users.py
│   └── orders.py
├── admin/
│   ├── dashboard.py
│   └── settings.py
└── pages/
    ├── home.py
    └── about.py
```

Both patterns work identically. The directory structure has no effect on the URL paths -- only the route definitions inside the files matter. Choose whichever pattern keeps your project navigable.

---

## 11. Exercise: Build a Full CRUD API for Products

Build a complete REST API for managing products. All data is stored in a Python list (no database yet -- we will add that in Chapter 5).

### Requirements

Create a file `src/routes/product_api.py` with the following routes:

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/products` | List all products. Support `?category=` filter. |
| `GET` | `/api/products/{id:int}` | Get a single product by ID. Return 404 if not found. |
| `POST` | `/api/products` | Create a new product. Return 201. |
| `PUT` | `/api/products/{id:int}` | Replace a product. Return 404 if not found. |
| `DELETE` | `/api/products/{id:int}` | Delete a product. Return 204 with no body. |

Each product has: `id` (int), `name` (string), `category` (string), `price` (float), `in_stock` (bool).

Start with this seed data:

```python
products = [
    {"id": 1, "name": "Wireless Keyboard", "category": "Electronics", "price": 79.99, "in_stock": True},
    {"id": 2, "name": "Yoga Mat", "category": "Fitness", "price": 29.99, "in_stock": True},
    {"id": 3, "name": "Coffee Grinder", "category": "Kitchen", "price": 49.99, "in_stock": False},
    {"id": 4, "name": "Standing Desk", "category": "Office", "price": 549.99, "in_stock": True},
    {"id": 5, "name": "Running Shoes", "category": "Fitness", "price": 119.99, "in_stock": True}
]
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

Create `src/routes/product_api.py`:

```python
from tina4_python.core.router import get, post, put, delete

# In-memory product store (resets on server restart)
products = [
    {"id": 1, "name": "Wireless Keyboard", "category": "Electronics", "price": 79.99, "in_stock": True},
    {"id": 2, "name": "Yoga Mat", "category": "Fitness", "price": 29.99, "in_stock": True},
    {"id": 3, "name": "Coffee Grinder", "category": "Kitchen", "price": 49.99, "in_stock": False},
    {"id": 4, "name": "Standing Desk", "category": "Office", "price": 549.99, "in_stock": True},
    {"id": 5, "name": "Running Shoes", "category": "Fitness", "price": 119.99, "in_stock": True}
]

next_id = 6


# List all products, optionally filter by category
@get("/api/products")
async def list_products(request, response):
    category = request.query.get("category")

    if category is not None:
        filtered = [p for p in products if p["category"].lower() == category.lower()]
        return response.json({"products": filtered, "count": len(filtered)})

    return response.json({"products": products, "count": len(products)})


# Get a single product by ID
@get("/api/products/{id:int}")
async def get_product(request, response):
    id = request.params["id"]

    for product in products:
        if product["id"] == id:
            return response.json(product)

    return response.json({"error": "Product not found", "id": id}, 404)


# Create a new product
@post("/api/products")
async def create_product(request, response):
    global next_id
    body = request.body

    if not body.get("name"):
        return response.json({"error": "Name is required"}, 400)

    product = {
        "id": next_id,
        "name": body["name"],
        "category": body.get("category", "Uncategorized"),
        "price": float(body.get("price", 0)),
        "in_stock": bool(body.get("in_stock", True))
    }
    next_id += 1

    products.append(product)

    return response.json(product, 201)


# Replace a product
@put("/api/products/{id:int}")
async def replace_product(request, response):
    id = request.params["id"]
    body = request.body

    for i, product in enumerate(products):
        if product["id"] == id:
            products[i] = {
                "id": id,
                "name": body.get("name", product["name"]),
                "category": body.get("category", product["category"]),
                "price": float(body.get("price", product["price"])),
                "in_stock": bool(body.get("in_stock", product["in_stock"]))
            }
            return response.json(products[i])

    return response.json({"error": "Product not found", "id": id}, 404)


# Delete a product
@delete("/api/products/{id:int}")
async def delete_product(request, response):
    id = request.params["id"]

    for i, product in enumerate(products):
        if product["id"] == id:
            products.pop(i)
            return response.json(None, 204)

    return response.json({"error": "Product not found", "id": id}, 404)
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

### 1. Trailing slashes matter

**Problem:** `/products` works but `/products/` returns a 404 (or vice versa).

**Cause:** Tina4 treats `/products` and `/products/` as different routes by default.

**Fix:** Pick one convention and stick with it. If you want both to work, register the route without a trailing slash -- Tina4 will redirect `/products/` to `/products` automatically when `TINA4_TRAILING_SLASH_REDIRECT=true` is set in `.env`.

### 2. Parameter names must be unique in a path

**Problem:** `/users/{id}/posts/{id}` does not work as expected -- both parameters have the same name.

**Cause:** The second `{id}` overwrites the first in `request.params`.

**Fix:** Use distinct names: `/users/{user_id}/posts/{post_id}`.

### 3. Method conflicts

**Problem:** You defined `@get("/items/{id}")` and `@get("/items/{action}")` and the wrong handler runs.

**Cause:** Both patterns match `/items/42`. The first one registered wins.

**Fix:** Use typed parameters to disambiguate: `@get("/items/{id:int}")` will only match integers, leaving `/items/export` free for the other route. Alternatively, restructure your paths: `/items/{id:int}` and `/items/actions/{action}`.

### 4. Route handler must return a response

**Problem:** Your route handler runs but the browser shows an empty page or a 500 error.

**Cause:** You forgot the `return` statement. Without `return`, the handler returns `None` and Tina4 does not know what to send back.

**Fix:** Always `return response.json(...)` or `return response.html(...)` or `return response.render(...)`. Every handler must return something.

### 5. Decorator order matters

**Problem:** Your `@middleware` decorator does not seem to work, or your `@noauth` has no effect.

**Cause:** Python decorators are applied bottom-up. If you stack decorators in the wrong order, the route may not register correctly.

**Fix:** Always put the route decorator (`@get`, `@post`, etc.) first (closest to the function), then additional decorators above it:

```python
@middleware(require_api_key)  # Applied second (wraps the route)
@get("/api/secret")           # Applied first (registers the route)
async def secret(request, response):
    ...
```

### 6. Forgetting async def

**Problem:** Your route handler raises a `TypeError` about a coroutine or the response is a coroutine object instead of JSON.

**Cause:** You used `def` instead of `async def` for your handler.

**Fix:** Every route handler in Tina4 Python must be `async def`. This is because Tina4 Python runs on an async server. Change `def my_handler(request, response):` to `async def my_handler(request, response):`.

### 7. Group prefix must start with a slash

**Problem:** `@group("api/v1")` produces routes like `/api/v1/users` but they do not match.

**Cause:** The group prefix should start with `/` for consistency. While Tina4 may auto-correct this, it is better to be explicit.

**Fix:** Always start group prefixes with `/`: `@group("/api/v1")`.
