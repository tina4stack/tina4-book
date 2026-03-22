# Chapter 2: Architecture

## The Request Lifecycle

Every HTTP request that hits a Tina4 application follows the same path, regardless of which language is running on the backend. Understanding this path is the single most important thing you can learn about Tina4.

```
Client sends HTTP request
        │
        ▼
  ┌───────────┐
  │  Server   │  Accept connection, parse HTTP
  └─────┬─────┘
        │
        ▼
  ┌───────────┐
  │  Request  │  Build Request object (body, params, headers, files, session)
  └─────┬─────┘
        │
        ▼
  ┌───────────┐
  │  Router   │  Match URL pattern to a registered handler
  └─────┬─────┘
        │
        ▼
  ┌───────────┐
  │Middleware  │  Run before-handler functions (auth, logging, rate limit)
  └─────┬─────┘
        │
        ▼
  ┌───────────┐
  │  Handler  │  Your code runs here
  └─────┬─────┘
        │
        ▼
  ┌───────────┐
  │ Response  │  Build response (JSON, HTML, redirect, file)
  └─────┬─────┘
        │
        ▼
  ┌───────────┐
  │ Pipeline  │  Minify HTML, compact JSON, compress (gzip), set ETag
  └─────┬─────┘
        │
        ▼
  Client receives HTTP response
```

Let us walk through each stage.

### 1. Server

The server accepts TCP connections and parses raw HTTP into structured data. Each language uses its native server:

| Language | Server |
|----------|--------|
| Python | asyncio / ASGI |
| PHP | Built-in server / Swoole |
| Ruby | WEBrick / Puma |
| Node.js | `node:http` |

You never interact with the server directly. Tina4 handles this.

### 2. Request

The framework builds a `Request` object with everything you need:

```
request.body        # Parsed JSON or form data
request.params      # Path parameters ({id} from /users/{id})
request.query       # Query string (?page=2&sort=name)
request.headers     # HTTP headers (case-insensitive)
request.files       # Uploaded files
request.session     # Session data (read/write)
request.method      # GET, POST, PUT, DELETE, etc.
request.path        # URL path without query string
request.ip          # Client IP address
request.request_id  # Unique ID for this request (for log correlation)
request.cookies     # Parsed cookies
request.is_json     # True if Content-Type contains "json"
```

### 3. Router

The router matches the request's method and path against registered routes. Routes are registered in files under `src/routes/`:

```php
// PHP
Route::get("/api/products/{id:int}", function ($request, $response) {
    // Only matches if {id} is an integer
});
```

```python
# Python
@get("/api/products/{id:int}")
async def get_product(request, response):
    # Only matches if {id} is an integer
    pass
```

```ruby
# Ruby
get "/api/products/{id:int}" do |request, response|
  # Only matches if {id} is an integer
end
```

```typescript
// Node.js (file-based routing: src/routes/api/products/[id].ts)
export default function handler(request, response) {
    // id available via request.params.id
}
```

The router supports:

- **Basic parameters:** `/users/{id}` matches `/users/42`
- **Typed parameters:** `/users/{id:int}` only matches integers
- **Catch-all:** `/pages/{slug:.*}` matches `/pages/about/team/history`
- **Route groups:** Prefix multiple routes with a common path and middleware
- **Route caching:** Cache the response for a given TTL

If no route matches, Tina4 checks `src/public/` for a static file. If that also fails, it returns a 404.

### 4. Middleware

Middleware functions run before (and optionally after) your handler. They form a pipeline -- each middleware can modify the request, short-circuit the response, or pass control to the next function.

Tina4 includes built-in middleware for:

- **CORS** -- configured via environment variables, runs automatically
- **Rate limiting** -- 60 requests/minute per IP by default
- **Auth gating** -- attach `.secure()` to a route to require a valid JWT
- **Request ID tracking** -- generates or reads `X-Request-ID` header

You can write your own middleware:

```php
// PHP
function logRequests($request, $response, $next) {
    $start = microtime(true);
    $result = $next($request, $response);
    $duration = round((microtime(true) - $start) * 1000, 2);
    Log::info("Request completed", [
        "method" => $request->method,
        "path" => $request->path,
        "duration_ms" => $duration
    ]);
    return $result;
}

Route::get("/api/users", $handler)->middleware([logRequests]);
```

### 5. Handler

This is your code. The handler receives a `Request` and a `Response` and returns a response. What you do in between is your business. Tina4 does not dictate your application architecture.

### 6. Response

The `Response` object provides methods for every common response type:

```
response.json(data, statusCode)       # JSON with auto Content-Type
response.html(content, statusCode)    # HTML response
response.text(content, statusCode)    # Plain text
response.xml(content, statusCode)     # XML response
response.redirect(url, statusCode)    # HTTP redirect (302 or 301)
response.file(path)                   # File download with auto MIME type
response.render(template, data)       # Render a Frond template
response.status(code)                 # Set status code (chainable)
response.header(name, value)          # Set response header (chainable)
response.cookie(name, value, options) # Set a cookie
```

### 7. Response Pipeline

After your handler returns, the response passes through an automatic pipeline:

1. **Frond rendering** -- if you called `response.render()`, the template is compiled and executed
2. **HTML minification** -- in production (`TINA4_DEBUG=false`), whitespace is collapsed, comments stripped
3. **JSON compaction** -- JSON is always compact unless `?pretty=true` is in the query string
4. **gzip compression** -- if the client sends `Accept-Encoding: gzip` and the response is over 1KB
5. **ETag generation** -- a hash of the response body is set as an `ETag` header; subsequent requests with a matching `If-None-Match` get a `304 Not Modified` with zero body

This pipeline is automatic. You never need to configure it. It just works.

---

## Project Structure

Every Tina4 project follows the same directory layout, regardless of language:

```
my-project/
├── .env                    # All configuration lives here
├── src/
│   ├── routes/             # Route handlers (auto-discovered)
│   ├── orm/                # ORM models (auto-discovered)
│   ├── migrations/         # SQL migration files
│   ├── seeds/              # Database seed files
│   ├── templates/          # Frond templates
│   │   └── errors/         # Custom error pages
│   ├── public/             # Static files (served at /)
│   │   ├── js/
│   │   │   └── frond.js    # Auto-provided
│   │   ├── css/
│   │   ├── scss/           # SCSS source files (auto-compiled)
│   │   ├── images/
│   │   └── icons/
│   └── locales/            # Translation files (JSON)
│       └── en.json
├── data/                   # SQLite databases, .broken files
├── logs/                   # Log files with rotation
├── secrets/                # JWT keys
└── tests/                  # Test files
```

Let us look at each directory in detail.

### `src/routes/` -- Where Your API Lives

Drop any file in this directory and Tina4 auto-discovers the route definitions inside it. You can organize files however you want:

```
src/routes/
├── products.php        # All product routes
├── orders.php          # All order routes
└── admin/
    ├── users.php       # Admin user routes
    └── reports.php     # Admin report routes
```

Or use a single file. Or twenty files. Tina4 reads them all. The file name does not affect the route path -- only the route definition inside the file matters.

### `src/orm/` -- Where Your Models Live

ORM model classes go here. Again, auto-discovered:

```
src/orm/
├── Product.php
├── Order.php
├── OrderItem.php
└── User.php
```

### `src/migrations/` -- Database Schema Changes

Migrations are SQL files with timestamps:

```
src/migrations/
├── 20260319100000_create_users_table.sql
├── 20260319100000_create_users_table.down.sql
├── 20260320090000_create_products_table.sql
└── 20260320090000_create_products_table.down.sql
```

The `.sql` file runs on `tina4 migrate`. The `.down.sql` file runs on `tina4 migrate:rollback`. Tina4 tracks which migrations have run in a `tina4_migrations` table.

### `src/seeds/` -- Test Data

Seed files populate your database with test or default data. Run them with `tina4 seed`.

### `src/templates/` -- Frond Templates

Templates use the Frond engine (covered in the next section). They support inheritance, includes, filters, loops, and conditionals:

```
src/templates/
├── base.html           # Layout with blocks
├── index.html          # Extends base.html
├── products/
│   ├── list.html       # Product listing
│   └── detail.html     # Single product
├── partials/
│   ├── header.html
│   └── footer.html
└── errors/
    ├── 404.html         # Custom 404 page
    └── 500.html         # Custom 500 page
```

### `src/public/` -- Static Files

Files here are served directly at the root URL path. A file at `src/public/images/logo.png` is available at `/images/logo.png`. No route registration needed.

The framework auto-provides `frond.js` in `src/public/js/` and keeps it in sync with the installed framework version.

### `data/` -- Runtime Data

SQLite databases are stored here by default (`data/app.db`). The `.broken/` subdirectory holds error marker files used by the health check. This directory is in `.gitignore`.

### `logs/` -- Log Files

Structured log files with automatic rotation. In `.gitignore`.

### `secrets/` -- JWT Keys

Private and public keys for RS256 JWT signing. In `.gitignore`.

---

## .env Driven Configuration

Every piece of Tina4 configuration lives in a single `.env` file at the project root. No YAML. No TOML. No JSON config objects. One file, one format.

```env
# .env
TINA4_DEBUG=true
TINA4_PORT=7145
DATABASE_URL=sqlite:///data/app.db
JWT_SECRET=change-me-in-production
```

### The Priority Chain

Tina4 resolves configuration values using a three-level priority chain:

```
Constructor argument  >  .env file  >  Hardcoded default
```

For example, the database connection:

1. If you pass a connection string directly in code: `new Database("sqlite:///custom.db")` -- that wins.
2. If you do not, Tina4 reads `DATABASE_URL` from `.env`.
3. If `.env` does not have it either, the default is `sqlite:///data/app.db`.

This pattern applies to **every** configurable value in the framework. You always have three ways to set something, and they always resolve in the same order.

### Example: Priority Chain in Practice

```env
# .env
TINA4_PORT=8080
```

```php
// In code -- this overrides .env
$app = new Tina4\App(["port" => 9000]);
// Server starts on port 9000, not 8080
```

```php
// No code override, no .env value
$app = new Tina4\App();
// Server starts on port 7145 (the default)
```

### is_truthy() -- Boolean Environment Values

Tina4 needs to interpret string values from `.env` as booleans. The `is_truthy()` function accepts these values as `true`:

- `true` (any case: `True`, `TRUE`, `tRuE`)
- `1`
- `yes` (any case)
- `on` (any case)

Everything else is `false`, including empty strings and unset variables. This means all of these are equivalent:

```env
TINA4_DEBUG=true
TINA4_DEBUG=True
TINA4_DEBUG=1
TINA4_DEBUG=yes
TINA4_DEBUG=on
```

And all of these disable debug mode:

```env
TINA4_DEBUG=false
TINA4_DEBUG=0
TINA4_DEBUG=no
TINA4_DEBUG=off
TINA4_DEBUG=
# or simply omit the line
```

---

## Dev Mode vs. Production Mode

The entire behavior of a Tina4 application changes based on a single variable: `TINA4_DEBUG`.

### Dev Mode (`TINA4_DEBUG=true`)

When debug mode is on:

- **Debug overlay** is injected into every HTML response -- a toolbar at the bottom of the page showing request details, database queries, template render times, session data, and logs
- **Full stack traces** appear in the browser when errors occur, with source code context, the request that caused the error, and the database queries that ran
- **Swagger UI** is auto-registered at `/swagger`
- **Admin console** is available at `/tina4/console` (if `TINA4_CONSOLE_TOKEN` is set)
- **Live reload** watches for file changes and refreshes the browser
- **SQL query logging** writes every query to `logs/query.log`
- **Pretty JSON** is available via `?pretty=true` on any JSON endpoint
- **404 pages** show a helpful "route not found" message listing similar registered routes

### Production Mode (`TINA4_DEBUG=false`)

When debug mode is off:

- **No debug overlay** -- responses are clean
- **Generic error pages** -- no stack traces, no source code, no query details
- **HTML minification** -- comments stripped, whitespace collapsed (15-25% smaller)
- **.broken files** -- unhandled exceptions create marker files in `data/.broken/` that cause the health check to return `503 Service Unavailable`, triggering container restarts
- **No Swagger UI** -- unless explicitly enabled
- **No admin console** -- unless explicitly enabled with a token
- **No query logging** -- unless explicitly enabled
- **Compact JSON** only -- no `?pretty=true`

The default is `TINA4_DEBUG=false`. You must explicitly enable debug mode. This means forgetting to set it does the safe thing.

**Common mistake:** Deploying with `TINA4_DEBUG=true` in production. This exposes stack traces, database queries, and session data to anyone with a browser. Always set `TINA4_DEBUG=false` in production. Always.

---

## The Frond Template Engine

Frond is Tina4's built-in, zero-dependency template engine. It uses a syntax intentionally similar to Twig, so developers familiar with Twig, Jinja2, or Nunjucks will feel at home. But Frond is built from scratch in each language -- no third-party template library is involved.

### Basic Syntax

**Variables:**
```html
<h1>{{ title }}</h1>
<p>Welcome, {{ user.name }}</p>
<p>First item: {{ items[0] }}</p>
```

**Filters (pipe syntax):**
```html
<p>{{ name | upper }}</p>           <!-- JOHN DOE -->
<p>{{ name | lower }}</p>           <!-- john doe -->
<p>{{ price | number_format(2) }}</p> <!-- 29.99 -->
<p>{{ text | truncate(100) }}</p>    <!-- First 100 chars... -->
<p>{{ description | raw }}</p>       <!-- No auto-escaping -->
<p>{{ items | length }}</p>          <!-- 5 -->
<p>{{ items | join(", ") }}</p>      <!-- apple, banana, cherry -->
```

There are over 55 filters available, covering strings, numbers, dates, arrays, encoding, and formatting.

**Control structures:**
```html
{% if products | length > 0 %}
    {% for product in products %}
        <div class="product">
            <h2>{{ product.name }}</h2>
            <p>{{ product.price | number_format(2) }}</p>
            {% if loop.last %}
                <hr>
            {% endif %}
        </div>
    {% else %}
        <p>No products found.</p>
    {% endfor %}
{% endif %}
```

**Template inheritance:**
```html
{# base.html #}
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}My App{% endblock %}</title>
</head>
<body>
    {% block content %}{% endblock %}
</body>
</html>

{# products/list.html #}
{% extends "base.html" %}

{% block title %}Products{% endblock %}

{% block content %}
    <h1>Our Products</h1>
    {% for product in products %}
        <p>{{ product.name }} - ${{ product.price | number_format(2) }}</p>
    {% endfor %}
{% endblock %}
```

**Includes:**
```html
{% include "partials/header.html" %}
<main>
    {{ content }}
</main>
{% include "partials/footer.html" %}
```

**Fragment caching:**
```html
{% cache "product-list" 300 %}
    {# This block is cached for 300 seconds #}
    {% for product in products %}
        <div>{{ product.name }}</div>
    {% endfor %}
{% endcache %}
```

Frond is covered in depth in each language-specific book. The key point for now: the template syntax is identical across all four languages. A template written for a Python backend works without changes on PHP, Ruby, or Node.js.

---

## How Auto-Discovery Works

Tina4 uses auto-discovery to find routes, models, and templates without explicit registration. Here is how it works:

### Routes

On startup, Tina4 scans every file in `src/routes/` (recursively). In each file, it looks for route registration calls -- `get()`, `post()`, `put()`, `delete()`, `any()`. Each call registers a route with the router.

```
Startup
  │
  ├── Scan src/routes/
  │   ├── products.php → registers GET /api/products, POST /api/products, ...
  │   ├── orders.php → registers GET /api/orders, ...
  │   └── admin/users.php → registers GET /api/admin/users, ...
  │
  └── Router now has all routes in memory
```

The scan happens once at startup. In dev mode with live reload, the scan re-runs when files change.

**Important:** The file name and path within `src/routes/` do not determine the URL path. Only the route definition inside the file matters. You could put all your routes in one file called `everything.php` and it would work fine. The directory structure is for your organization, not the framework's.

### Models

ORM model classes in `src/orm/` are auto-discovered the same way. The framework scans for classes that extend the ORM base class and registers them. This enables features like auto-CRUD (generating REST endpoints from models) and route model binding (resolving URL parameters to model instances).

### Templates

Templates are not "discovered" in the same sense -- they are loaded on demand when `response.render()` is called. But the framework knows to look in `src/templates/` without being told. If you reference `"products/list.html"`, it resolves to `src/templates/products/list.html`.

### Static Files

When the router cannot match a request to a registered route, it falls back to `src/public/`. If a file exists at the matching path, it is served with the correct MIME type. If not, the framework checks its own built-in assets (frond.js, tina4css, Swagger UI). If nothing matches, a 404 is returned.

The lookup order:

```
1. Registered route?          → Run handler
2. File in src/public/?       → Serve static file
3. Framework built-in asset?  → Serve framework file
4. Nothing matches            → 404 response
```

---

## Summary

| Concept | How It Works in Tina4 |
|---------|----------------------|
| Request lifecycle | Request > Router > Middleware > Handler > Response > Pipeline |
| Project structure | Fixed conventions: routes, orm, templates, public, migrations |
| Configuration | `.env` only, priority: constructor > .env > default |
| Dev vs. production | Single toggle: `TINA4_DEBUG` |
| Template engine | Frond: Twig-like syntax, zero dependencies, identical across languages |
| Auto-discovery | Files in `src/routes/` and `src/orm/` are found at startup |
| Static files | Files in `src/public/` are served at `/` |
| Response pipeline | Minification > compression > ETag, all automatic |
