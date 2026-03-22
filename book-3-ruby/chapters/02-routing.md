# Chapter 2: Routing

## 1. How Routing Works in Tina4

Every web application maps URLs to code. You type `/products` in your browser, the framework finds the function that handles `/products`, runs it, and sends back the result. That mapping is called routing.

In Tina4, you define routes in Ruby files inside `src/routes/`. Every `.rb` file in that directory (and its subdirectories) is auto-loaded when the server starts. You do not need to register files or update a central config -- just drop a file in and it works.

Here is the simplest possible route:

```ruby
Tina4::Router.get("/hello") do |request, response|
  response.json({ message: "Hello, World!" })
end
```

Save that as `src/routes/hello.rb`, start the server with `tina4 serve`, and visit `http://localhost:7147/hello`:

```json
{"message":"Hello, World!"}
```

That is it. One line registers the route, one block handles the request.

---

## 2. HTTP Methods

Tina4 supports all five standard HTTP methods. Each one has a method on `Tina4::Router`:

```ruby
Tina4::Router.get("/products") do |request, response|
  response.json({ action: "list all products" })
end

Tina4::Router.post("/products") do |request, response|
  response.json({ action: "create a product" }, 201)
end

Tina4::Router.put("/products/{id}") do |request, response|
  id = request.params["id"]
  response.json({ action: "replace product #{id}" })
end

Tina4::Router.patch("/products/{id}") do |request, response|
  id = request.params["id"]
  response.json({ action: "update product #{id}" })
end

Tina4::Router.delete("/products/{id}") do |request, response|
  id = request.params["id"]
  response.json({ action: "delete product #{id}" })
end
```

Test each one:

```bash
curl http://localhost:7147/products
```

```json
{"action":"list all products"}
```

```bash
curl -X POST http://localhost:7147/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Widget"}'
```

```json
{"action":"create a product"}
```

```bash
curl -X PUT http://localhost:7147/products/42
```

```json
{"action":"replace product 42"}
```

```bash
curl -X PATCH http://localhost:7147/products/42
```

```json
{"action":"update product 42"}
```

```bash
curl -X DELETE http://localhost:7147/products/42
```

```json
{"action":"delete product 42"}
```

Use `GET` for reading, `POST` for creating, `PUT` for full replacement, `PATCH` for partial updates, and `DELETE` for removal. This follows the REST convention and makes your API predictable.

---

## 3. Path Parameters

Path parameters let you capture values from the URL. Wrap the parameter name in curly braces:

```ruby
Tina4::Router.get("/users/{id}/posts/{post_id}") do |request, response|
  user_id = request.params["id"]
  post_id = request.params["post_id"]

  response.json({
    user_id: user_id,
    post_id: post_id
  })
end
```

```bash
curl http://localhost:7147/users/5/posts/99
```

```json
{"user_id":"5","post_id":"99"}
```

Notice that `user_id` came back as the string `"5"`, not the integer `5`. Path parameters are always strings by default.

### Typed Parameters

You can enforce a type by adding a colon and the type after the parameter name:

```ruby
Tina4::Router.get("/orders/{id:int}") do |request, response|
  id = request.params["id"]
  response.json({
    order_id: id,
    type: id.class.name
  })
end
```

```bash
curl http://localhost:7147/orders/42
```

```json
{"order_id":42,"type":"Integer"}
```

If you pass a non-integer value, the route will not match and you will get a 404:

```bash
curl http://localhost:7147/orders/abc
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

```ruby
Tina4::Router.get("/search") do |request, response|
  q = request.query["q"] || ""
  page = (request.query["page"] || 1).to_i
  limit = (request.query["limit"] || 10).to_i

  response.json({
    query: q,
    page: page,
    limit: limit,
    offset: (page - 1) * limit
  })
end
```

```bash
curl "http://localhost:7147/search?q=keyboard&page=2&limit=20"
```

```json
{"query":"keyboard","page":2,"limit":20,"offset":20}
```

If a query parameter is missing, `request.query["key"]` will return `nil`, so always use `||` to provide defaults.

---

## 5. Route Groups

When you have a set of routes that share a common prefix, use `Tina4::Router.group` to avoid repeating yourself:

```ruby
Tina4::Router.group("/api/v1") do

  Tina4::Router.get("/users") do |request, response|
    response.json({ users: [] })
  end

  Tina4::Router.get("/users/{id:int}") do |request, response|
    id = request.params["id"]
    response.json({ user: { id: id, name: "Alice" } })
  end

  Tina4::Router.post("/users") do |request, response|
    response.json({ created: true }, 201)
  end

  Tina4::Router.get("/products") do |request, response|
    response.json({ products: [] })
  end

end
```

The routes above register as `/api/v1/users`, `/api/v1/users/{id}`, and `/api/v1/products`. You write short paths inside the group, and Tina4 prepends the prefix automatically.

```bash
curl http://localhost:7147/api/v1/users
```

```json
{"users":[]}
```

```bash
curl http://localhost:7147/api/v1/products
```

```json
{"products":[]}
```

Groups can be nested:

```ruby
Tina4::Router.group("/api") do
  Tina4::Router.group("/v1") do
    Tina4::Router.get("/status") do |request, response|
      response.json({ version: "1.0" })
    end
  end

  Tina4::Router.group("/v2") do
    Tina4::Router.get("/status") do |request, response|
      response.json({ version: "2.0" })
    end
  end
end
```

```bash
curl http://localhost:7147/api/v1/status
```

```json
{"version":"1.0"}
```

```bash
curl http://localhost:7147/api/v2/status
```

```json
{"version":"2.0"}
```

---

## 6. Middleware

Middleware is code that runs before (or after) your route handler. Use it for authentication, logging, rate limiting, input validation, or anything that should happen on multiple routes.

### Middleware on a Single Route

Pass middleware as the third argument to any route method:

```ruby
log_request = lambda do |request, response, next_handler|
  start = Process.clock_gettime(Process::CLOCK_MONOTONIC)
  $stderr.puts "[#{Time.now.strftime('%Y-%m-%d %H:%M:%S')}] #{request.method} #{request.path}"

  result = next_handler.call(request, response)

  duration = ((Process.clock_gettime(Process::CLOCK_MONOTONIC) - start) * 1000).round(2)
  $stderr.puts "  Completed in #{duration}ms"

  result
end

Tina4::Router.get("/api/data", middleware: "log_request") do |request, response|
  response.json({ data: [1, 2, 3] })
end
```

The middleware receives `request`, `response`, and `next_handler`. Call `next_handler.call(request, response)` to continue to the route handler. If you do not call `next_handler`, the route handler never runs -- useful for blocking unauthorized requests.

### Blocking Middleware

Here is middleware that checks for an API key:

```ruby
require_api_key = lambda do |request, response, next_handler|
  api_key = request.headers["X-API-Key"] || ""

  if api_key != "my-secret-key"
    return response.json({ error: "Invalid API key" }, 401)
  end

  next_handler.call(request, response)
end

Tina4::Router.get("/api/secret", middleware: "require_api_key") do |request, response|
  response.json({ secret: "The answer is 42" })
end
```

```bash
curl http://localhost:7147/api/secret
```

```json
{"error":"Invalid API key"}
```

The response status is `401 Unauthorized`.

```bash
curl http://localhost:7147/api/secret -H "X-API-Key: my-secret-key"
```

```json
{"secret":"The answer is 42"}
```

### Middleware on a Group

Apply middleware to an entire group by passing it as an option to `Tina4::Router.group`:

```ruby
Tina4::Router.group("/api/admin", middleware: "require_auth") do

  Tina4::Router.get("/dashboard") do |request, response|
    response.json({ page: "admin dashboard" })
  end

  Tina4::Router.get("/users") do |request, response|
    response.json({ page: "user management" })
  end

end
```

Every route inside the group now requires the `Authorization` header. You do not need to add the middleware to each route individually.

### Multiple Middleware

Chain multiple middleware by passing an array:

```ruby
Tina4::Router.get("/api/important", middleware: ["log_request", "require_api_key", "require_auth"]) do |request, response|
  response.json({ data: "important stuff" })
end
```

Middleware runs in order: `log_request` first, then `require_api_key`, then `require_auth`, then the route handler. If any middleware does not call `next_handler`, the chain stops there.

---

## 7. Route Decorators: @noauth and @secured

Tina4 provides two special decorators for controlling authentication on routes.

### @noauth -- Public Routes

When your application has global authentication middleware, use the `@noauth` annotation to mark specific routes as public:

```ruby
# @noauth
Tina4::Router.get("/api/public/info") do |request, response|
  response.json({
    app: "My Store",
    version: "1.0.0"
  })
end
```

The `@noauth` comment tells Tina4 to skip authentication checks for this route, even if global auth middleware is configured in `.env` or applied to the parent group.

### @secured -- Protected GET Routes

The `@secured` annotation explicitly marks a GET route as requiring authentication:

```ruby
# @secured
Tina4::Router.get("/api/profile") do |request, response|
  # request.user is populated by the auth middleware
  response.json({ user: request.user })
end
```

By default, `POST`, `PUT`, `PATCH`, and `DELETE` routes are considered secured. `GET` routes are not -- they are public unless you add `@secured`. This matches the common pattern where reading data is public but modifying data requires authentication.

---

## 8. Wildcard and Catch-All Routes

### Wildcard Routes

Use `*` at the end of a path to match anything after it:

```ruby
Tina4::Router.get("/docs/*") do |request, response|
  path = request.params["*"] || ""
  response.json({
    section: "docs",
    path: path
  })
end
```

```bash
curl http://localhost:7147/docs/getting-started
```

```json
{"section":"docs","path":"getting-started"}
```

```bash
curl http://localhost:7147/docs/api/authentication/jwt
```

```json
{"section":"docs","path":"api/authentication/jwt"}
```

### Catch-All Route (Custom 404)

Register a catch-all to handle any unmatched URL:

```ruby
Tina4::Router.get("/*") do |request, response|
  response.json({
    error: "Page not found",
    path: request.path
  }, 404)
end
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
GET      /api/admin/dashboard          require_auth        public
GET      /api/admin/users              require_auth        public
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
GET      /api/admin/users              require_auth        public
```

---

## 10. Organizing Route Files

You are free to organize route files any way you like. Tina4 loads every `.rb` file in `src/routes/` recursively. Here are two common patterns:

### Pattern 1: One File Per Resource

```
src/routes/
├── products.rb     # All product routes
├── users.rb        # All user routes
├── orders.rb       # All order routes
└── pages.rb        # HTML page routes
```

### Pattern 2: Subdirectories by Feature

```
src/routes/
├── api/
│   ├── products.rb
│   ├── users.rb
│   └── orders.rb
├── admin/
│   ├── dashboard.rb
│   └── settings.rb
└── pages/
    ├── home.rb
    └── about.rb
```

Both patterns work identically. The directory structure has no effect on the URL paths -- only the route definitions inside the files matter. Choose whichever pattern keeps your project navigable.

---

## 11. Exercise: Build a Full CRUD API for Products

Build a complete REST API for managing products. All data is stored in a Ruby array (no database yet -- we will add that in Chapter 5).

### Requirements

Create a file `src/routes/product_api.rb` with the following routes:

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/products` | List all products. Support `?category=` filter. |
| `GET` | `/api/products/{id:int}` | Get a single product by ID. Return 404 if not found. |
| `POST` | `/api/products` | Create a new product. Return 201. |
| `PUT` | `/api/products/{id:int}` | Replace a product. Return 404 if not found. |
| `DELETE` | `/api/products/{id:int}` | Delete a product. Return 204 with no body. |

Each product has: `id` (int), `name` (string), `category` (string), `price` (float), `in_stock` (bool).

Start with this seed data:

```ruby
products = [
  { id: 1, name: "Wireless Keyboard", category: "Electronics", price: 79.99, in_stock: true },
  { id: 2, name: "Yoga Mat", category: "Fitness", price: 29.99, in_stock: true },
  { id: 3, name: "Coffee Grinder", category: "Kitchen", price: 49.99, in_stock: false },
  { id: 4, name: "Standing Desk", category: "Office", price: 549.99, in_stock: true },
  { id: 5, name: "Running Shoes", category: "Fitness", price: 119.99, in_stock: true }
]
```

Test with:

```bash
# List all
curl http://localhost:7147/api/products

# Filter by category
curl "http://localhost:7147/api/products?category=Fitness"

# Get one
curl http://localhost:7147/api/products/3

# Create
curl -X POST http://localhost:7147/api/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Desk Lamp", "category": "Office", "price": 39.99, "in_stock": true}'

# Update
curl -X PUT http://localhost:7147/api/products/3 \
  -H "Content-Type: application/json" \
  -d '{"name": "Burr Coffee Grinder", "category": "Kitchen", "price": 59.99, "in_stock": true}'

# Delete
curl -X DELETE http://localhost:7147/api/products/3

# Not found
curl http://localhost:7147/api/products/999
```

---

## 12. Solution

Create `src/routes/product_api.rb`:

```ruby
# In-memory product store (resets on server restart)
$products = [
  { id: 1, name: "Wireless Keyboard", category: "Electronics", price: 79.99, in_stock: true },
  { id: 2, name: "Yoga Mat", category: "Fitness", price: 29.99, in_stock: true },
  { id: 3, name: "Coffee Grinder", category: "Kitchen", price: 49.99, in_stock: false },
  { id: 4, name: "Standing Desk", category: "Office", price: 549.99, in_stock: true },
  { id: 5, name: "Running Shoes", category: "Fitness", price: 119.99, in_stock: true }
]

$next_id = 6

# List all products, optionally filter by category
Tina4::Router.get("/api/products") do |request, response|
  category = request.query["category"]

  if category
    filtered = $products.select { |p| p[:category].downcase == category.downcase }
    response.json({ products: filtered, count: filtered.length })
  else
    response.json({ products: $products, count: $products.length })
  end
end

# Get a single product by ID
Tina4::Router.get("/api/products/{id:int}") do |request, response|
  id = request.params["id"]

  product = $products.find { |p| p[:id] == id }

  if product
    response.json(product)
  else
    response.json({ error: "Product not found", id: id }, 404)
  end
end

# Create a new product
Tina4::Router.post("/api/products") do |request, response|
  body = request.body

  if body["name"].nil? || body["name"].empty?
    return response.json({ error: "Name is required" }, 400)
  end

  product = {
    id: $next_id,
    name: body["name"],
    category: body["category"] || "Uncategorized",
    price: (body["price"] || 0).to_f,
    in_stock: body["in_stock"] != false
  }

  $next_id += 1
  $products << product

  response.json(product, 201)
end

# Replace a product
Tina4::Router.put("/api/products/{id:int}") do |request, response|
  id = request.params["id"]
  body = request.body

  index = $products.index { |p| p[:id] == id }

  if index.nil?
    response.json({ error: "Product not found", id: id }, 404)
  else
    $products[index] = {
      id: id,
      name: body["name"] || $products[index][:name],
      category: body["category"] || $products[index][:category],
      price: (body["price"] || $products[index][:price]).to_f,
      in_stock: body.key?("in_stock") ? body["in_stock"] : $products[index][:in_stock]
    }
    response.json($products[index])
  end
end

# Delete a product
Tina4::Router.delete("/api/products/{id:int}") do |request, response|
  id = request.params["id"]

  index = $products.index { |p| p[:id] == id }

  if index.nil?
    response.json({ error: "Product not found", id: id }, 404)
  else
    $products.delete_at(index)
    response.json(nil, 204)
  end
end
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

**Cause:** The second `{id}` overwrites the first in `request.params`.

**Fix:** Use distinct names: `/users/{user_id}/posts/{post_id}`.

### 3. Method Conflicts

**Problem:** You defined `Tina4::Router.get("/items/{id}", ...)` and `Tina4::Router.get("/items/{action}", ...)` and the wrong handler runs.

**Cause:** Both patterns match `/items/42`. The first one registered wins.

**Fix:** Use typed parameters to disambiguate: `Tina4::Router.get("/items/{id:int}", ...)` will only match integers, leaving `/items/export` free for the other route. Alternatively, restructure your paths: `/items/{id:int}` and `/items/actions/{action}`.

### 4. Route Handler Must Return a Response

**Problem:** Your route handler runs but the browser shows an empty page or a 500 error.

**Cause:** You forgot to use `response.json` or `response.render`. Without a return value from the response object, the handler returns `nil` and Tina4 does not know what to send back.

**Fix:** Always use `response.json(...)` or `response.html(...)` or `response.render(...)`. Every handler must produce a response.

### 5. Block Syntax Matters

**Problem:** Your route handler raises a syntax error about unexpected blocks.

**Cause:** Ruby blocks with `do...end` and `{...}` have different precedence. For multi-line route handlers, always use `do...end`.

**Fix:** Use `do |request, response| ... end` for route blocks. The curly brace form `{ |request, response| ... }` works for single-line handlers but can cause parsing issues with method arguments.

### 6. Middleware Must Be a Named Function or String

**Problem:** Passing an inline lambda as middleware causes unexpected behavior.

**Cause:** Tina4 expects middleware to be referenced by name (a string), not as an inline block. The string is resolved to a method or lambda at runtime.

**Fix:** Define your middleware as a named method or lambda and pass the name as a string: `"my_middleware"`, not `lambda { |req, res, next_h| ... }`.

### 7. Group Prefix Must Start with a Slash

**Problem:** `Tina4::Router.group("api/v1")` produces routes like `/api/v1/users` but they do not match.

**Cause:** The group prefix should start with `/` for consistency. While Tina4 may auto-correct this, it is better to be explicit.

**Fix:** Always start group prefixes with `/`: `Tina4::Router.group("/api/v1")`.
