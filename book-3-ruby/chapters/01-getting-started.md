# Chapter 1: Getting Started with Tina4 Ruby

## 1. What Is Tina4 Ruby

Tina4 Ruby is a zero-dependency web framework for Ruby 3.1+ that gives you routing, an ORM, a template engine, authentication, queues, WebSocket, and 70 other features in a single gem under 5,000 lines of code.

It is part of the Tina4 family -- four identical frameworks in Python, PHP, Ruby, and Node.js. Everything you learn here transfers directly to any of the other three languages. The project structure is the same. The template syntax is the same. The CLI commands are the same. The `.env` variables are the same.

Tina4 Ruby uses `snake_case` for method names (`fetch_one`, `soft_delete`, `has_many`) following Ruby community conventions. Class names are `PascalCase`. Constants are `UPPER_SNAKE_CASE`.

By the end of this chapter, you will have a working Tina4 Ruby project with an API endpoint and a rendered HTML page.

---

## 2. Prerequisites and Installation

### What You Need

Before installing Tina4, make sure you have:

1. **Ruby 3.1 or later** -- check with:

```bash
ruby -v
```

You should see output like:

```
ruby 3.3.0 (2023-12-25 revision 5124f9ac75) [arm64-darwin23]
```

If you see a version lower than 3.1, upgrade Ruby first.

2. **Bundler** -- Ruby's dependency manager. Check with:

```bash
bundle --version
```

You should see:

```
Bundler version 2.5.6
```

If Bundler is not installed, install it with `gem install bundler`.

3. **The Tina4 CLI** -- a Rust-based binary that manages all four Tina4 frameworks:

```bash
# macOS (Homebrew)
brew install tina4stack/tap/tina4

# Linux / macOS (install script)
curl -fsSL https://raw.githubusercontent.com/tina4stack/tina4/main/install.sh | bash

# Windows (PowerShell)
irm https://raw.githubusercontent.com/tina4stack/tina4/main/install.ps1 | iex
```

Verify the CLI is installed:

```bash
tina4 --version
```

```
tina4 0.1.0
```

4. **SQLite3 development libraries** -- these ship with most systems:

```bash
# macOS (already included)
# Ubuntu/Debian
sudo apt-get install libsqlite3-dev

# Fedora
sudo dnf install sqlite-devel
```

### Creating a New Project

Use the Tina4 CLI to scaffold a new project:

```bash
tina4 init my-store
```

You should see:

```
Creating Tina4 project in ./my-store ...
  Detected language: Ruby (Gemfile)
  Created .env
  Created .env.example
  Created .gitignore
  Created src/routes/
  Created src/orm/
  Created src/migrations/
  Created src/seeds/
  Created src/templates/
  Created src/templates/errors/
  Created src/public/
  Created src/public/js/
  Created src/public/css/
  Created src/public/scss/
  Created src/public/images/
  Created src/public/icons/
  Created src/locales/
  Created data/
  Created logs/
  Created secrets/
  Created tests/

Project created! Next steps:
  cd my-store
  bundle install
  tina4 serve
```

Now install the Ruby dependencies:

```bash
cd my-store
bundle install
```

```
Fetching gem metadata from https://rubygems.org/...
Resolving dependencies...
Installing tina4 (3.0.0)
Bundle complete! 1 Gemfile dependency, 1 gem installed.
```

That is right -- **one gem**. No dependency tree. No version conflicts. Just `tina4`.

### Starting the Dev Server

```bash
tina4 serve
```

```
 _____ _             _  _
|_   _(_)_ __   __ _| || |
  | | | | '_ \ / _` | || |_
  | | | | | | | (_| |__   _|
  |_| |_|_| |_|\__,_|  |_|

  Tina4 Ruby v3.0.0
  Server running at http://0.0.0.0:7147
  Debug mode: ON
  Database: sqlite:///data/app.db
  Press Ctrl+C to stop
```

Open your browser to `http://localhost:7147`. You should see the Tina4 welcome page.

Open `http://localhost:7147/health` in your browser or curl it:

```bash
curl http://localhost:7147/health
```

```json
{
  "status": "ok",
  "database": "connected",
  "uptime_seconds": 12,
  "version": "3.0.0",
  "framework": "tina4-ruby"
}
```

Your Tina4 Ruby project is running.

---

## 3. Project Structure Walkthrough

Let us look at what `tina4 init` created:

```
my-store/
├── .env                    # Your configuration (gitignored)
├── .env.example            # Template for other developers
├── .gitignore              # Pre-configured
├── Gemfile                 # Gem dependencies
├── Gemfile.lock            # Locked dependency versions
├── app.rb                  # Application entry point
├── src/
│   ├── routes/             # Your route handlers go here
│   ├── orm/                # Your ORM model classes go here
│   ├── migrations/         # SQL migration files
│   ├── seeds/              # Database seed files
│   ├── templates/          # Frond/Twig templates
│   │   └── errors/         # Custom 404.html, 500.html
│   ├── public/             # Static files (CSS, JS, images)
│   │   ├── js/
│   │   │   └── frond.js    # Auto-provided JS helper library
│   │   ├── css/
│   │   │   └── tina4.css   # Built-in CSS utility framework
│   │   ├── scss/
│   │   ├── images/
│   │   └── icons/
│   └── locales/            # Translation files
│       └── en.json
├── data/                   # SQLite databases (gitignored)
├── logs/                   # Log files (gitignored)
├── secrets/                # JWT keys (gitignored)
└── tests/                  # Your test files
```

**Key directories:**

- **`src/routes/`** -- Every `.rb` file here is auto-loaded at startup. Put your route definitions here. Organize into subdirectories if you want.
- **`src/orm/`** -- Every `.rb` file here is auto-loaded. Put your ORM model classes here.
- **`src/templates/`** -- Frond looks here when you call `response.render("my-page.html", data)`.
- **`src/public/`** -- Files served directly. `src/public/images/logo.png` is available at `/images/logo.png`.
- **`data/`** -- The default SQLite database (`app.db`) lives here. Gitignored because databases should not be in version control.

---

## 4. Your First Route

Let us create an API endpoint that returns a JSON greeting.

Create the file `src/routes/greeting.rb`:

```ruby
Tina4::Router.get("/api/greeting/{name}") do |request, response|
  name = request.params["name"]
  response.json({
    message: "Hello, #{name}!",
    timestamp: Time.now.iso8601
  })
end
```

Save the file. If the dev server is running with live reload, it picks up the change automatically. If not, restart the server with `tina4 serve`.

### Test It

Open your browser to:

```
http://localhost:7147/api/greeting/Alice
```

You should see:

```json
{
  "message": "Hello, Alice!",
  "timestamp": "2026-03-22T14:30:00+00:00"
}
```

Or use curl:

```bash
curl http://localhost:7147/api/greeting/Alice
```

```json
{"message":"Hello, Alice!","timestamp":"2026-03-22T14:30:00+00:00"}
```

Notice the difference: the browser shows pretty-printed JSON (because of browser extensions or dev mode), while curl shows compact JSON. You can force pretty output by adding `?pretty=true`:

```bash
curl "http://localhost:7147/api/greeting/Alice?pretty=true"
```

```json
{
  "message": "Hello, Alice!",
  "timestamp": "2026-03-22T14:30:00+00:00"
}
```

### Understanding What Happened

1. You created a file in `src/routes/`. Tina4 auto-discovered it at startup.
2. `Tina4::Router.get("/api/greeting/{name}")` registered a GET route with a path parameter `{name}`.
3. When you requested `/api/greeting/Alice`, the router matched the pattern and called your handler block.
4. `request.params["name"]` gave you the value `"Alice"` from the URL.
5. `response.json(...)` serialized the hash to JSON, set `Content-Type: application/json`, and returned a `200 OK` response.

### Adding More HTTP Methods

Let us add a POST endpoint. Update `src/routes/greeting.rb`:

```ruby
Tina4::Router.get("/api/greeting/{name}") do |request, response|
  name = request.params["name"]
  response.json({
    message: "Hello, #{name}!",
    timestamp: Time.now.iso8601
  })
end

Tina4::Router.post("/api/greeting") do |request, response|
  name = request.body["name"] || "World"
  language = request.body["language"] || "en"

  greetings = {
    "en" => "Hello",
    "es" => "Hola",
    "fr" => "Bonjour",
    "de" => "Hallo",
    "ja" => "Konnichiwa"
  }

  greeting = greetings[language] || greetings["en"]

  response.json({
    message: "#{greeting}, #{name}!",
    language: language
  }, 201)
end
```

Test the POST endpoint:

```bash
curl -X POST http://localhost:7147/api/greeting \
  -H "Content-Type: application/json" \
  -d '{"name": "Carlos", "language": "es"}'
```

```json
{"message":"Hola, Carlos!","language":"es"}
```

The HTTP status code is `201 Created` (the second argument to `response.json`).

---

## 5. Your First Template

Tina4 uses the **Frond** template engine -- a zero-dependency, Twig-compatible engine built from scratch. If you have used Twig, Jinja2, or Nunjucks, this will feel familiar.

### Create a Base Layout

Create `src/templates/base.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My Store{% endblock %}</title>
    <link rel="stylesheet" href="/css/tina4.css">
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 0; }
        .container { max-width: 960px; margin: 0 auto; padding: 20px; }
        .product-card { border: 1px solid #ddd; border-radius: 8px; padding: 16px; margin: 8px 0; }
        .product-card h3 { margin-top: 0; }
        .price { color: #2d8f2d; font-weight: bold; font-size: 1.2em; }
        .badge { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 0.8em; }
        .badge-success { background: #d4edda; color: #155724; }
        .badge-danger { background: #f8d7da; color: #721c24; }
        nav { background: #333; color: white; padding: 12px 20px; }
        nav a { color: white; text-decoration: none; margin-right: 16px; }
    </style>
</head>
<body>
    <nav>
        <a href="/">Home</a>
        <a href="/products">Products</a>
    </nav>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
    <script src="/js/frond.js"></script>
</body>
</html>
```

This base layout defines two blocks (`title` and `content`) that child templates can override. It includes `tina4.css` (the built-in CSS framework) and `frond.js` (the built-in JS helper library).

### Create a Product Listing Page

Create `src/templates/products.html`:

```html
{% extends "base.html" %}

{% block title %}Products - My Store{% endblock %}

{% block content %}
    <h1>Our Products</h1>
    <p>Showing {{ products | length }} product{{ products | length != 1 ? "s" : "" }}</p>

    {% if products | length > 0 %}
        {% for product in products %}
            <div class="product-card">
                <h3>{{ product.name }}</h3>
                <p>{{ product.description }}</p>
                <p class="price">${{ product.price | number_format(2) }}</p>
                {% if product.in_stock %}
                    <span class="badge badge-success">In Stock</span>
                {% else %}
                    <span class="badge badge-danger">Out of Stock</span>
                {% endif %}
                {% if not loop.last %}
                    {# Don't add separator after the last item #}
                {% endif %}
            </div>
        {% endfor %}
    {% else %}
        <p>No products available at the moment.</p>
    {% endif %}
{% endblock %}
```

### Create the Route That Renders the Template

Create `src/routes/pages.rb`:

```ruby
Tina4::Router.get("/products") do |request, response|
  products = [
    {
      name: "Wireless Keyboard",
      description: "Ergonomic wireless keyboard with backlit keys.",
      price: 79.99,
      in_stock: true
    },
    {
      name: "USB-C Hub",
      description: "7-port USB-C hub with HDMI, SD card reader, and Ethernet.",
      price: 49.99,
      in_stock: true
    },
    {
      name: "Monitor Stand",
      description: "Adjustable aluminum monitor stand with cable management.",
      price: 129.99,
      in_stock: false
    },
    {
      name: "Mechanical Mouse",
      description: "High-precision wireless mouse with 16,000 DPI sensor.",
      price: 59.99,
      in_stock: true
    }
  ]

  response.render("products.html", { products: products })
end
```

### See It in the Browser

Open `http://localhost:7147/products` in your browser. You should see:

- A dark navigation bar at the top with "Home" and "Products" links
- The heading "Our Products"
- A subheading showing "Showing 4 products"
- Four product cards, each with a name, description, price, and stock badge
- The "Monitor Stand" card shows a red "Out of Stock" badge
- The other three show green "In Stock" badges

### How Template Rendering Works

1. `response.render("products.html", { products: products })` tells Frond to render `src/templates/products.html` with the given data.
2. Frond sees `{% extends "base.html" %}` and loads the base template.
3. The `{% block content %}` in `products.html` replaces the same block in `base.html`.
4. `{{ product.name }}` outputs the value, auto-escaped for HTML safety.
5. `{{ product.price | number_format(2) }}` formats the number with 2 decimal places.
6. `{% for product in products %}` loops through the array.
7. `{% if product.in_stock %}` conditionally renders the stock badge.
8. `{{ products | length }}` returns the count of items in the array.

### About tina4css

The `tina4.css` file included in the base template is Tina4's built-in CSS utility framework. It provides layout utilities, typography, and common UI patterns without needing Bootstrap or Tailwind. It is auto-provided when you scaffold a project -- you do not need to download it separately.

---

## 6. Understanding .env

Open the `.env` file at the root of your project:

```env
TINA4_DEBUG=true
```

That is likely all you see. The scaffold creates a minimal `.env` with debug mode enabled. Everything else uses defaults.

The important defaults for development:

| Variable | Default Value | What It Means |
|----------|---------------|---------------|
| `TINA4_PORT` | `7147` | Server runs on port 7147 |
| `DATABASE_URL` | `sqlite:///data/app.db` | SQLite database in the `data/` directory |
| `TINA4_LOG_LEVEL` | `ALL` | All log messages are output |
| `CORS_ORIGINS` | `*` | All origins allowed (fine for development) |
| `TINA4_RATE_LIMIT` | `60` | 60 requests per minute per IP |

To change the port, add it to `.env`:

```env
TINA4_DEBUG=true
TINA4_PORT=8080
```

Restart the server (`Ctrl+C`, then `tina4 serve`). It now runs on port 8080.

For the complete `.env` reference with all 68 variables, see Book 0, Chapter 4.

---

## 7. The Dev Dashboard

With `TINA4_DEBUG=true`, Tina4 provides a built-in development dashboard. First, enable it by adding a console token to your `.env`:

```env
TINA4_DEBUG=true
TINA4_CONSOLE=true
TINA4_CONSOLE_TOKEN=my-dev-token
```

Restart the server and navigate to:

```
http://localhost:7147/tina4/console
```

Enter your token (`my-dev-token`) when prompted. You will see:

- **System Overview** -- framework version, Ruby version, uptime, memory usage, database status
- **Request Inspector** -- recent HTTP requests with method, path, status, duration, and request ID. Click any request to see full headers, body, database queries, and template renders.
- **Error Log** -- unhandled exceptions with stack traces and occurrence counts
- **Queue Manager** -- queue status (pending, reserved, failed, dead-letter messages)
- **WebSocket Monitor** -- active WebSocket connections with metadata
- **Routes** -- all registered routes with their methods, paths, and middleware

The console is a powerful debugging tool. It shows you exactly what your application is doing without adding print statements or log calls to your code.

Additionally, when you visit any HTML page (like `/products`), you will see a **debug overlay** -- a toolbar at the bottom of the page showing:

- Request details (method, URL, duration)
- Database queries executed (with timing)
- Template renders (with timing)
- Session data
- Recent log entries

This overlay is only visible when `TINA4_DEBUG=true`. It is never shown in production.

---

## 8. Exercise: Greeting API + Product List Template

Build the following two features from scratch, without looking at the examples above.

### Exercise Part A: Greeting API

Create an API endpoint at `GET /api/greet` that:

1. Accepts a query parameter `name` (e.g., `/api/greet?name=Sarah`)
2. If `name` is missing, defaults to `"Stranger"`
3. Returns JSON like:

```json
{
  "greeting": "Welcome, Sarah!",
  "time_of_day": "afternoon"
}
```

4. The `time_of_day` should be calculated from the server's current hour:
   - 5:00 - 11:59 = "morning"
   - 12:00 - 16:59 = "afternoon"
   - 17:00 - 20:59 = "evening"
   - 21:00 - 4:59 = "night"

**Test your endpoint with:**

```bash
curl "http://localhost:7147/api/greet?name=Sarah"
curl "http://localhost:7147/api/greet"
```

### Exercise Part B: Product List Page

Create a page at `GET /store` that:

1. Displays a list of at least 5 products (hardcoded for now)
2. Each product has: name, category, price, and a boolean `featured` flag
3. Featured products should be visually highlighted (different background color, border, or badge)
4. The page should show the total number of products and the number of featured products
5. Use template inheritance -- create a layout template and a page template that extends it
6. Include `tina4.css` and `frond.js`

**Your products data should look like this in your route handler:**

```ruby
products = [
  { name: "Espresso Machine", category: "Kitchen", price: 299.99, featured: true },
  { name: "Yoga Mat", category: "Fitness", price: 29.99, featured: false },
  { name: "Standing Desk", category: "Office", price: 549.99, featured: true },
  { name: "Noise-Canceling Headphones", category: "Electronics", price: 199.99, featured: true },
  { name: "Water Bottle", category: "Fitness", price: 24.99, featured: false }
]
```

**Expected browser output:**

- A page titled "Our Store"
- Text showing "5 products, 3 featured"
- A list of product cards with name, category, price, and a "Featured" badge on the highlighted items
- Featured products have a distinct visual style (your choice -- different border color, background, star icon, etc.)

---

## 9. Solutions

### Solution A: Greeting API

Create `src/routes/greet.rb`:

```ruby
Tina4::Router.get("/api/greet") do |request, response|
  name = request.query["name"] || "Stranger"
  hour = Time.now.hour

  time_of_day = if hour >= 5 && hour < 12
                  "morning"
                elsif hour >= 12 && hour < 17
                  "afternoon"
                elsif hour >= 17 && hour < 21
                  "evening"
                else
                  "night"
                end

  response.json({
    greeting: "Welcome, #{name}!",
    time_of_day: time_of_day
  })
end
```

**Test:**

```bash
curl "http://localhost:7147/api/greet?name=Sarah"
```

```json
{"greeting":"Welcome, Sarah!","time_of_day":"afternoon"}
```

```bash
curl "http://localhost:7147/api/greet"
```

```json
{"greeting":"Welcome, Stranger!","time_of_day":"afternoon"}
```

### Solution B: Product List Page

Create `src/templates/store-layout.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Store{% endblock %}</title>
    <link rel="stylesheet" href="/css/tina4.css">
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 0; background: #f5f5f5; }
        .container { max-width: 960px; margin: 0 auto; padding: 20px; }
        header { background: #1a1a2e; color: white; padding: 16px 20px; }
        header h1 { margin: 0; }
        .stats { color: #888; margin: 8px 0 20px; }
        .product-grid { display: grid; gap: 16px; }
        .product-card { background: white; border: 2px solid #e0e0e0; border-radius: 8px; padding: 16px; }
        .product-card.featured { border-color: #ffc107; background: #fffdf0; }
        .product-name { font-size: 1.2em; font-weight: bold; margin: 0 0 4px; }
        .product-category { color: #666; font-size: 0.9em; }
        .product-price { color: #2d8f2d; font-weight: bold; font-size: 1.1em; margin-top: 8px; }
        .featured-badge { background: #ffc107; color: #333; padding: 2px 8px; border-radius: 4px; font-size: 0.8em; font-weight: bold; }
    </style>
</head>
<body>
    <header>
        <h1>{% block header %}Store{% endblock %}</h1>
    </header>
    <div class="container">
        {% block content %}{% endblock %}
    </div>
    <script src="/js/frond.js"></script>
</body>
</html>
```

Create `src/templates/store.html`:

```html
{% extends "store-layout.html" %}

{% block title %}Our Store{% endblock %}
{% block header %}Our Store{% endblock %}

{% block content %}
    <p class="stats">{{ products | length }} products, {{ featured_count }} featured</p>

    <div class="product-grid">
        {% for product in products %}
            <div class="product-card{{ product.featured ? ' featured' : '' }}">
                <p class="product-name">
                    {{ product.name }}
                    {% if product.featured %}
                        <span class="featured-badge">Featured</span>
                    {% endif %}
                </p>
                <p class="product-category">{{ product.category }}</p>
                <p class="product-price">${{ product.price | number_format(2) }}</p>
            </div>
        {% endfor %}
    </div>
{% endblock %}
```

Create `src/routes/store.rb`:

```ruby
Tina4::Router.get("/store") do |request, response|
  products = [
    { name: "Espresso Machine", category: "Kitchen", price: 299.99, featured: true },
    { name: "Yoga Mat", category: "Fitness", price: 29.99, featured: false },
    { name: "Standing Desk", category: "Office", price: 549.99, featured: true },
    { name: "Noise-Canceling Headphones", category: "Electronics", price: 199.99, featured: true },
    { name: "Water Bottle", category: "Fitness", price: 24.99, featured: false }
  ]

  featured_count = products.count { |p| p[:featured] }

  response.render("store.html", {
    products: products,
    featured_count: featured_count
  })
end
```

**Open `http://localhost:7147/store` in your browser.** You should see:

- A dark header reading "Our Store"
- Text showing "5 products, 3 featured"
- Five product cards in a grid
- Three cards (Espresso Machine, Standing Desk, Noise-Canceling Headphones) have a yellow border, light yellow background, and a "Featured" badge
- Two cards (Yoga Mat, Water Bottle) have a standard white background with gray border
- Each card shows the product name, category, and price formatted with two decimal places

---

## 10. Gotchas

### 1. File not auto-discovered

**Problem:** You created a route file but nothing happens when you visit the URL.

**Cause:** The file is not in `src/routes/`. Double-check the path. It must be inside `src/routes/` (or a subdirectory of it), and the file must end with `.rb`.

**Fix:** Move the file to `src/routes/your-file.rb` and restart the server.

### 2. "Uninitialized constant" errors

**Problem:** `NameError: uninitialized constant Tina4::Router` or similar.

**Cause:** The Tina4 gem is not loaded, or the file is not being required by the framework.

**Fix:** Make sure your `Gemfile` includes `gem "tina4"` and you have run `bundle install`. Route files in `src/routes/` are auto-loaded -- you do not need `require` statements.

### 3. JSON response shows HTML

**Problem:** Your JSON endpoint returns HTML instead of JSON.

**Cause:** You returned a string instead of using `response.json`. If you return a plain string, Tina4 treats it as HTML.

**Fix:** Always use `response.json(data)` for JSON endpoints, not `puts data.to_json`.

### 4. Template not found

**Problem:** `Template "my-page.html" not found` error.

**Cause:** The template file is not in `src/templates/`, or there is a typo in the filename.

**Fix:** Check that the file exists at `src/templates/my-page.html`. The name in `response.render` is relative to `src/templates/`.

### 5. Port already in use

**Problem:** `Error: Address already in use (port 7147)`

**Cause:** Another process (or another Tina4 instance) is using port 7147.

**Fix:** Either stop the other process, or change the port:

```env
TINA4_PORT=8080
```

Or use the CLI flag: `tina4 serve --port 8080`.

### 6. Changes not reflected

**Problem:** You edited a file but the browser shows the old version.

**Cause:** In some setups, live reload may not be active. Also, browser caching can serve stale versions.

**Fix:** Hard-refresh the browser (`Ctrl+Shift+R` or `Cmd+Shift+R`). If that does not help, restart the dev server with `Ctrl+C` and `tina4 serve`.

### 7. .env not loaded

**Problem:** Environment variables seem to have no effect.

**Cause:** The `.env` file must be at the project root (same directory as `Gemfile`). If it is in a subdirectory, Tina4 will not find it.

**Fix:** Move `.env` to the project root.

### 8. Debug mode in production

**Problem:** Your production site shows stack traces and query details.

**Cause:** `TINA4_DEBUG=true` in production.

**Fix:** Set `TINA4_DEBUG=false` in your production `.env`. This hides all debug information, enables HTML minification, and activates `.broken` file health checks.
