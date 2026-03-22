# Chapter 4: Templates

## 1. Why Templates

In Chapter 1, you saw `$response->render("products.html", $data)` and it produced a full HTML page. That rendering was done by **Frond**, Tina4's built-in template engine. Frond is a zero-dependency, Twig-compatible engine that ships with the framework. If you have used Twig, Jinja2, or Nunjucks, you already know 90% of Frond.

Templates live in `src/templates/`. When you call `$response->render("page.html", $data)`, Frond loads `src/templates/page.html`, processes the tags and expressions, and returns the final HTML.

This chapter covers every feature of the template engine so you can build real pages.

---

## 2. Variables and Expressions

Output a variable with double curly braces:

```html
<h1>Hello, {{ name }}!</h1>
```

Route handler:

```php
<?php
use Tina4\Route;

Route::get("/welcome", function ($request, $response) {
    return $response->render("welcome.html", [
        "name" => "Alice"
    ]);
});
```

Create `src/templates/welcome.html`:

```html
<!DOCTYPE html>
<html>
<head><title>Welcome</title></head>
<body>
    <h1>Hello, {{ name }}!</h1>
</body>
</html>
```

**Expected browser output:**

```
Hello, Alice!
```

### Accessing Nested Data

Use dot notation for nested arrays:

```php
$data = [
    "user" => [
        "name" => "Alice",
        "email" => "alice@example.com",
        "address" => [
            "city" => "Cape Town",
            "country" => "South Africa"
        ]
    ]
];

return $response->render("profile.html", $data);
```

```html
<p>{{ user.name }} lives in {{ user.address.city }}, {{ user.address.country }}.</p>
```

**Output:**

```
Alice lives in Cape Town, South Africa.
```

### Expressions

You can use basic expressions inside `{{ }}`:

```html
<p>Total: ${{ price * quantity }}</p>
<p>Discounted: ${{ price * 0.9 }}</p>
<p>Full name: {{ first_name ~ " " ~ last_name }}</p>
```

The `~` operator concatenates strings.

---

## 3. Template Inheritance

Template inheritance is the most powerful feature. Define a base layout once, then extend it in every page.

### Base Layout

Create `src/templates/base.twig`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}My App{% endblock %}</title>
    <link rel="stylesheet" href="/css/tina4.css">
    {% block head %}{% endblock %}
</head>
<body>
    <nav>
        <a href="/">Home</a>
        <a href="/about">About</a>
        <a href="/contact">Contact</a>
    </nav>

    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>&copy; 2026 My App. All rights reserved.</p>
    </footer>

    <script src="/js/frond.js"></script>
    {% block scripts %}{% endblock %}
</body>
</html>
```

This base defines four blocks: `title`, `head`, `content`, and `scripts`. Child templates override only the blocks they need.

### Child Template

Create `src/templates/about.twig`:

```html
{% extends "base.twig" %}

{% block title %}About Us{% endblock %}

{% block content %}
    <h1>About Us</h1>
    <p>We have been building things since {{ founded_year }}.</p>
    <p>Our team has {{ team_size }} members across {{ office_count }} offices.</p>
{% endblock %}
```

Route handler:

```php
<?php
use Tina4\Route;

Route::get("/about", function ($request, $response) {
    return $response->render("about.twig", [
        "founded_year" => 2020,
        "team_size" => 12,
        "office_count" => 3
    ]);
});
```

**Expected browser output:** A full HTML page with the nav, the "About Us" content, and the footer. The `<title>` tag says "About Us". The `head` and `scripts` blocks are empty because the child template did not override them.

### Using `{{ parent() }}`

Sometimes you want to add to a block rather than replace it entirely. Use `{{ parent() }}`:

```html
{% extends "base.twig" %}

{% block head %}
    {{ parent() }}
    <link rel="stylesheet" href="/css/contact-form.css">
{% endblock %}

{% block content %}
    <h1>Contact Us</h1>
    <form>...</form>
{% endblock %}
```

The `head` block now contains everything from the base template's `head` block plus the extra stylesheet.

---

## 4. Includes

Break your templates into reusable pieces with `{% include %}`:

Create `src/templates/partials/header.twig`:

```html
<header>
    <div class="logo">{{ site_name | default("My App") }}</div>
    <nav>
        <a href="/">Home</a>
        <a href="/products">Products</a>
        <a href="/contact">Contact</a>
    </nav>
</header>
```

Create `src/templates/partials/product-card.twig`:

```html
<div class="product-card{{ product.featured ? ' featured' : '' }}">
    <h3>{{ product.name }}</h3>
    <p class="price">${{ product.price | number_format(2) }}</p>
    {% if product.in_stock %}
        <span class="badge-success">In Stock</span>
    {% else %}
        <span class="badge-danger">Out of Stock</span>
    {% endif %}
</div>
```

Use them in a page:

```html
{% extends "base.twig" %}

{% block content %}
    {% include "partials/header.twig" %}

    <h1>Products</h1>
    {% for product in products %}
        {% include "partials/product-card.twig" %}
    {% endfor %}
{% endblock %}
```

The `product` variable is automatically available inside the included template because it exists in the current scope (the for loop).

### Passing Variables to Includes

You can pass specific variables with `with`:

```html
{% include "partials/header.twig" with {"site_name": "Cool Store"} %}
```

Use `only` to isolate the included template from the parent scope:

```html
{% include "partials/header.twig" with {"site_name": "Cool Store"} only %}
```

With `only`, the included template can only access `site_name` -- it cannot see any other variables from the parent.

---

## 5. For Loops

Loop through arrays with `{% for %}`:

```html
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```

### The `loop` Variable

Inside a for loop, Frond provides a special `loop` variable:

| Property | Type | Description |
|----------|------|-------------|
| `loop.index` | int | Current iteration (1-based) |
| `loop.index0` | int | Current iteration (0-based) |
| `loop.first` | bool | True on the first iteration |
| `loop.last` | bool | True on the last iteration |
| `loop.length` | int | Total number of items |
| `loop.revindex` | int | Iterations remaining (1-based) |

```html
<table>
    <thead>
        <tr><th>#</th><th>Name</th><th>Price</th></tr>
    </thead>
    <tbody>
    {% for product in products %}
        <tr class="{{ loop.index is odd ? 'row-light' : 'row-dark' }}">
            <td>{{ loop.index }}</td>
            <td>{{ product.name }}</td>
            <td>${{ product.price | number_format(2) }}</td>
        </tr>
    {% endfor %}
    </tbody>
</table>
```

### Empty Lists

Handle empty lists with `{% else %}`:

```html
{% for product in products %}
    <div class="product-card">
        <h3>{{ product.name }}</h3>
    </div>
{% else %}
    <p>No products found.</p>
{% endfor %}
```

If `products` is empty (or not defined), the `else` block renders instead.

### Looping Over Key-Value Pairs

```html
{% for key, value in metadata %}
    <dt>{{ key }}</dt>
    <dd>{{ value }}</dd>
{% endfor %}
```

---

## 6. Conditionals

### if / elseif / else

```html
{% if user.role == "admin" %}
    <a href="/admin">Admin Panel</a>
{% elseif user.role == "editor" %}
    <a href="/editor">Editor Dashboard</a>
{% else %}
    <a href="/profile">My Profile</a>
{% endif %}
```

### Ternary Operator

For inline conditionals:

```html
<span class="{{ is_active ? 'text-green' : 'text-gray' }}">
    {{ is_active ? 'Active' : 'Inactive' }}
</span>
```

### Testing for Existence

Use `is defined` to check if a variable exists:

```html
{% if error_message is defined %}
    <div class="alert alert-danger">{{ error_message }}</div>
{% endif %}
```

### Truthiness

These values are considered false: `false`, `null`, `0`, `""` (empty string), `[]` (empty array). Everything else is true.

```html
{% if items %}
    <p>{{ items | length }} items found.</p>
{% else %}
    <p>No items.</p>
{% endif %}
```

---

## 7. Filters

Filters transform values. Apply them with the `|` (pipe) character:

```html
{{ name | upper }}
```

Here are the most commonly used filters:

### Text Filters

| Filter | Input | Output | Description |
|--------|-------|--------|-------------|
| `upper` | `"hello"` | `"HELLO"` | Uppercase |
| `lower` | `"HELLO"` | `"hello"` | Lowercase |
| `capitalize` | `"hello world"` | `"Hello world"` | Capitalize first letter |
| `title` | `"hello world"` | `"Hello World"` | Capitalize each word |
| `trim` | `"  hello  "` | `"hello"` | Remove whitespace |
| `striptags` | `"<b>bold</b>"` | `"bold"` | Remove HTML tags |

### Number Filters

| Filter | Input | Output | Description |
|--------|-------|--------|-------------|
| `number_format(2)` | `1234.5` | `"1,234.50"` | Format number |
| `round` | `3.7` | `4` | Round to nearest integer |
| `round(2)` | `3.14159` | `3.14` | Round to N decimal places |
| `abs` | `-5` | `5` | Absolute value |

### Array Filters

| Filter | Input | Output | Description |
|--------|-------|--------|-------------|
| `length` | `[1,2,3]` | `3` | Count items |
| `join(", ")` | `["a","b","c"]` | `"a, b, c"` | Join with separator |
| `first` | `[1,2,3]` | `1` | First item |
| `last` | `[1,2,3]` | `3` | Last item |
| `reverse` | `[1,2,3]` | `[3,2,1]` | Reverse order |
| `sort` | `[3,1,2]` | `[1,2,3]` | Sort ascending |
| `slice(1, 2)` | `[1,2,3,4]` | `[2,3]` | Slice from offset, length |

### Date Filter

```html
<p>Published: {{ created_at | date("F j, Y") }}</p>
<p>Time: {{ created_at | date("H:i") }}</p>
```

With a PHP timestamp or date string as input:

- `date("F j, Y")` outputs `"March 22, 2026"`
- `date("H:i")` outputs `"14:30"`
- `date("Y-m-d")` outputs `"2026-03-22"`

### The `default` Filter

Provide a fallback value when a variable is null or undefined:

```html
<p>{{ subtitle | default("No subtitle") }}</p>
<p>{{ user.nickname | default(user.name) | default("Anonymous") }}</p>
```

### The `escape` and `raw` Filters

By default, all `{{ }}` output is auto-escaped for HTML safety. This prevents XSS attacks.

```html
{{ user_input }}
{# If user_input is "<script>alert('xss')</script>", outputs:
   &lt;script&gt;alert('xss')&lt;/script&gt; #}
```

If you trust the content and need raw HTML:

```html
{{ trusted_html | raw }}
```

Use `raw` sparingly. Only apply it to content you fully control, never to user input.

### Chaining Filters

Filters chain left to right:

```html
{{ name | trim | lower | capitalize }}
{# "  ALICE SMITH  " -> "Alice smith" #}
```

---

## 8. Macros

Macros are reusable template functions. Think of them as components you define once and call many times.

### Defining a Macro

Create `src/templates/macros.twig`:

```html
{% macro button(text, url, style) %}
    <a href="{{ url | default('#') }}" class="btn btn-{{ style | default('primary') }}">
        {{ text }}
    </a>
{% endmacro %}

{% macro alert(message, type) %}
    <div class="alert alert-{{ type | default('info') }}">
        {{ message }}
    </div>
{% endmacro %}

{% macro input(name, label, type, value) %}
    <div class="form-group">
        <label for="{{ name }}">{{ label | default(name | capitalize) }}</label>
        <input type="{{ type | default('text') }}" id="{{ name }}" name="{{ name }}" value="{{ value | default('') }}">
    </div>
{% endmacro %}
```

### Using Macros

Import macros in your template:

```html
{% from "macros.twig" import button, alert, input %}

{% extends "base.twig" %}

{% block content %}
    {{ alert("Your profile has been updated.", "success") }}

    <form method="POST" action="/profile">
        {{ input("name", "Full Name", "text", user.name) }}
        {{ input("email", "Email Address", "email", user.email) }}
        {{ input("phone", "Phone Number", "tel", user.phone) }}

        {{ button("Save Changes", "", "primary") }}
        {{ button("Cancel", "/dashboard", "secondary") }}
    </form>
{% endblock %}
```

**Expected output** (simplified):

```html
<div class="alert alert-success">
    Your profile has been updated.
</div>

<form method="POST" action="/profile">
    <div class="form-group">
        <label for="name">Full Name</label>
        <input type="text" id="name" name="name" value="Alice">
    </div>
    <div class="form-group">
        <label for="email">Email Address</label>
        <input type="email" id="email" name="email" value="alice@example.com">
    </div>
    <div class="form-group">
        <label for="phone">Phone Number</label>
        <input type="tel" id="phone" name="phone" value="">
    </div>

    <a href="#" class="btn btn-primary">Save Changes</a>
    <a href="/dashboard" class="btn btn-secondary">Cancel</a>
</form>
```

---

## 9. Special Tags

### {% raw %} -- Literal Output

When you need to output literal `{{ }}` or `{% %}` (for example, in a Vue.js or Angular template):

```html
{% raw %}
    <div id="app">
        {{ message }}
    </div>
{% endraw %}
```

This outputs the literal text `{{ message }}` without trying to process it as a Frond expression.

### {% spaceless %} -- Remove Whitespace

Remove whitespace between HTML tags:

```html
{% spaceless %}
    <div>
        <span>Hello</span>
    </div>
{% endspaceless %}
```

**Output:**

```html
<div><span>Hello</span></div>
```

Useful for inline elements where whitespace creates unwanted gaps.

### {% autoescape %} -- Control Escaping

Override the auto-escaping behavior for a block:

```html
{% autoescape false %}
    {{ trusted_html }}
{% endautoescape %}
```

Everything inside the block outputs without HTML escaping. Equivalent to using `| raw` on every variable, but more convenient for large blocks of trusted content.

### Comments

Template comments are invisible in the output:

```html
{# This comment will not appear in the HTML output #}

{#
    Multi-line comments work too.
    Use them to document template logic.
#}
```

---

## 10. tina4css Integration

Every Tina4 project includes `tina4.css`, a built-in CSS utility framework. It is available at `/css/tina4.css` and provides layout, typography, and common UI patterns without external dependencies.

Include it in your base template:

```html
<link rel="stylesheet" href="/css/tina4.css">
```

### Layout Classes

```html
<div class="container">
    <div class="row">
        <div class="col-6">Left half</div>
        <div class="col-6">Right half</div>
    </div>
</div>
```

### Common Components

```html
<!-- Buttons -->
<button class="btn btn-primary">Primary</button>
<button class="btn btn-secondary">Secondary</button>
<button class="btn btn-danger">Danger</button>

<!-- Cards -->
<div class="card">
    <div class="card-header">Title</div>
    <div class="card-body">Content here</div>
    <div class="card-footer">Footer</div>
</div>

<!-- Alerts -->
<div class="alert alert-success">Operation completed.</div>
<div class="alert alert-danger">Something went wrong.</div>
<div class="alert alert-warning">Please review your input.</div>

<!-- Forms -->
<div class="form-group">
    <label for="name">Name</label>
    <input type="text" id="name" class="form-control">
</div>
```

### Utility Classes

```html
<p class="text-center">Centered text</p>
<p class="text-right">Right-aligned text</p>
<div class="mt-4">Margin top</div>
<div class="p-3">Padding all around</div>
<span class="text-muted">Gray text</span>
<span class="text-primary">Primary color text</span>
```

You do not need Bootstrap or Tailwind. If you prefer those, you can replace `tina4.css` with your preferred framework -- just change the `<link>` tag.

---

## 11. Exercise: Build a Product Catalog Page

Build a product catalog page with a base layout, product cards, category filters, and a reusable card macro.

### Requirements

1. Create a base layout at `src/templates/catalog-base.twig` with blocks for `title`, `content`, and `scripts`
2. Create a macro file at `src/templates/catalog-macros.twig` with:
   - A `productCard(product)` macro that renders a styled card with name, category, price, stock status, and optional featured badge
   - A `categoryFilter(categories, active)` macro that renders filter buttons
3. Create a page template at `src/templates/catalog.twig` that:
   - Extends the base layout
   - Uses the macros
   - Shows a heading with the total product count
   - Shows category filter buttons (All, and one per unique category)
   - Shows product cards in a grid
   - Shows featured products with a distinct style
   - Handles the case when no products match the filter
4. Create a route at `GET /catalog` that accepts an optional `?category=` filter

### Data

Use this product list in your route handler:

```php
$products = [
    ["name" => "Espresso Machine", "category" => "Kitchen", "price" => 299.99, "in_stock" => true, "featured" => true],
    ["name" => "Yoga Mat", "category" => "Fitness", "price" => 29.99, "in_stock" => true, "featured" => false],
    ["name" => "Standing Desk", "category" => "Office", "price" => 549.99, "in_stock" => true, "featured" => true],
    ["name" => "Blender", "category" => "Kitchen", "price" => 89.99, "in_stock" => false, "featured" => false],
    ["name" => "Running Shoes", "category" => "Fitness", "price" => 119.99, "in_stock" => true, "featured" => false],
    ["name" => "Desk Lamp", "category" => "Office", "price" => 39.99, "in_stock" => true, "featured" => true],
    ["name" => "Cast Iron Skillet", "category" => "Kitchen", "price" => 44.99, "in_stock" => true, "featured" => false]
];
```

### Test with:

```
http://localhost:7145/catalog
http://localhost:7145/catalog?category=Kitchen
http://localhost:7145/catalog?category=Fitness
```

---

## 12. Solution

Create `src/templates/catalog-base.twig`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Product Catalog{% endblock %}</title>
    <link rel="stylesheet" href="/css/tina4.css">
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; margin: 0; padding: 0; background: #f8f9fa; }
        .container { max-width: 1000px; margin: 0 auto; padding: 20px; }
        .header { background: #2c3e50; color: white; padding: 20px; margin-bottom: 24px; }
        .header h1 { margin: 0; }
        .header p { margin: 4px 0 0; opacity: 0.8; }
        .filters { margin-bottom: 20px; }
        .filter-btn { display: inline-block; padding: 6px 14px; margin: 0 6px 6px 0; border-radius: 20px; text-decoration: none; font-size: 0.9em; border: 1px solid #dee2e6; color: #495057; background: white; }
        .filter-btn.active { background: #2c3e50; color: white; border-color: #2c3e50; }
        .product-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; }
        .product-card { background: white; border: 2px solid #e9ecef; border-radius: 8px; padding: 16px; transition: border-color 0.2s; }
        .product-card:hover { border-color: #adb5bd; }
        .product-card.featured { border-color: #f39c12; background: #fef9e7; }
        .product-name { font-size: 1.1em; font-weight: 600; margin: 0 0 4px; }
        .product-category { font-size: 0.85em; color: #6c757d; margin: 0 0 8px; }
        .product-price { font-size: 1.2em; font-weight: bold; color: #27ae60; }
        .badge { display: inline-block; padding: 2px 8px; border-radius: 4px; font-size: 0.75em; font-weight: 600; margin-left: 8px; }
        .badge-featured { background: #f39c12; color: white; }
        .badge-stock { background: #d4edda; color: #155724; }
        .badge-nostock { background: #f8d7da; color: #721c24; }
        .empty-state { text-align: center; padding: 40px; color: #6c757d; }
    </style>
</head>
<body>
    {% block content %}{% endblock %}

    <script src="/js/frond.js"></script>
    {% block scripts %}{% endblock %}
</body>
</html>
```

Create `src/templates/catalog-macros.twig`:

```html
{% macro productCard(product) %}
    <div class="product-card{{ product.featured ? ' featured' : '' }}">
        <p class="product-name">
            {{ product.name }}
            {% if product.featured %}
                <span class="badge badge-featured">Featured</span>
            {% endif %}
        </p>
        <p class="product-category">{{ product.category }}</p>
        <p class="product-price">
            ${{ product.price | number_format(2) }}
            {% if product.in_stock %}
                <span class="badge badge-stock">In Stock</span>
            {% else %}
                <span class="badge badge-nostock">Out of Stock</span>
            {% endif %}
        </p>
    </div>
{% endmacro %}

{% macro categoryFilter(categories, active) %}
    <div class="filters">
        <a href="/catalog" class="filter-btn{{ active is not defined or active == '' ? ' active' : '' }}">All</a>
        {% for cat in categories %}
            <a href="/catalog?category={{ cat }}" class="filter-btn{{ active == cat ? ' active' : '' }}">{{ cat }}</a>
        {% endfor %}
    </div>
{% endmacro %}
```

Create `src/templates/catalog.twig`:

```html
{% extends "catalog-base.twig" %}

{% from "catalog-macros.twig" import productCard, categoryFilter %}

{% block title %}{{ active_category | default("All") }} Products - Catalog{% endblock %}

{% block content %}
    <div class="header">
        <h1>Product Catalog</h1>
        <p>{{ products | length }} product{{ products | length != 1 ? 's' : '' }}{% if active_category %} in {{ active_category }}{% endif %}</p>
    </div>

    <div class="container">
        {{ categoryFilter(categories, active_category) }}

        {% if products | length > 0 %}
            <div class="product-grid">
                {% for product in products %}
                    {{ productCard(product) }}
                {% endfor %}
            </div>
        {% else %}
            <div class="empty-state">
                <h2>No products found</h2>
                <p>Try a different category or <a href="/catalog">view all products</a>.</p>
            </div>
        {% endif %}
    </div>
{% endblock %}
```

Create `src/routes/catalog.php`:

```php
<?php
use Tina4\Route;

Route::get("/catalog", function ($request, $response) {
    $allProducts = [
        ["name" => "Espresso Machine", "category" => "Kitchen", "price" => 299.99, "in_stock" => true, "featured" => true],
        ["name" => "Yoga Mat", "category" => "Fitness", "price" => 29.99, "in_stock" => true, "featured" => false],
        ["name" => "Standing Desk", "category" => "Office", "price" => 549.99, "in_stock" => true, "featured" => true],
        ["name" => "Blender", "category" => "Kitchen", "price" => 89.99, "in_stock" => false, "featured" => false],
        ["name" => "Running Shoes", "category" => "Fitness", "price" => 119.99, "in_stock" => true, "featured" => false],
        ["name" => "Desk Lamp", "category" => "Office", "price" => 39.99, "in_stock" => true, "featured" => true],
        ["name" => "Cast Iron Skillet", "category" => "Kitchen", "price" => 44.99, "in_stock" => true, "featured" => false]
    ];

    // Get unique categories
    $categories = array_unique(array_column($allProducts, "category"));
    sort($categories);

    // Filter by category if specified
    $activeCategory = $request->query["category"] ?? "";
    if (!empty($activeCategory)) {
        $products = array_values(array_filter(
            $allProducts,
            fn($p) => strtolower($p["category"]) === strtolower($activeCategory)
        ));
    } else {
        $products = $allProducts;
    }

    return $response->render("catalog.twig", [
        "products" => $products,
        "categories" => $categories,
        "active_category" => $activeCategory
    ]);
});
```

**Expected browser output for `/catalog`:**

- A dark header with "Product Catalog" and "7 products"
- Filter buttons: All (active), Fitness, Kitchen, Office
- A grid of 7 product cards
- Three cards (Espresso Machine, Standing Desk, Desk Lamp) have a gold border and "Featured" badge
- The Blender card shows an "Out of Stock" badge in red

**Expected browser output for `/catalog?category=Kitchen`:**

- Header shows "3 products in Kitchen"
- The Kitchen filter button is active
- Only three cards: Espresso Machine, Blender, Cast Iron Skillet

---

## 13. Gotchas

### 1. `{% extends %}` Must Be the First Tag

**Problem:** Template inheritance does not work. The page renders without the base layout.

**Cause:** `{% extends "base.twig" %}` must be the very first tag in the template. If there is any text, whitespace, or even a comment before it, inheritance breaks.

**Fix:** Make `{% extends %}` the absolute first thing in the file. Move any `{% from %}` imports to after the extends tag.

### 2. Undefined Variables Show Nothing

**Problem:** `{{ username }}` renders as empty instead of showing an error.

**Cause:** Frond silently outputs nothing for undefined variables. This is by design (like Twig), but it can hide bugs.

**Fix:** Use the `default` filter: `{{ username | default("Guest") }}`. Or check first with `{% if username is defined %}`.

### 3. Auto-Escaping Prevents HTML Output

**Problem:** You pass HTML content like `"<strong>bold</strong>"` but it appears as literal text in the page.

**Cause:** Auto-escaping converts `<` to `&lt;` and `>` to `&gt;` for security.

**Fix:** If the content is trusted, use `{{ content | raw }}`. Never use `raw` on user-supplied input.

### 4. Variable Scope in Includes

**Problem:** A variable defined inside a `{% for %}` loop is not accessible after the loop ends.

**Cause:** Loop variables are scoped to the loop. They do not leak into the outer scope.

**Fix:** If you need to accumulate values, use `{% set %}` before the loop and update it inside. Or restructure your template to keep all logic within the loop.

### 5. Macro Arguments Are Positional

**Problem:** Calling `{{ button("Click", style="danger") }}` does not work as expected.

**Cause:** Frond macros use positional arguments, not keyword arguments. The order matters.

**Fix:** Pass arguments in the order they are defined: `{{ button("Click", "/url", "danger") }}`. If you have many optional arguments, consider passing a single object.

### 6. Template File Extension Does Not Matter

**Problem:** You are not sure whether to use `.html`, `.twig`, or `.tpl`.

**Cause:** Frond does not care about the file extension. It processes any file in `src/templates/`.

**Fix:** Pick one extension and be consistent. This book uses `.twig` for templates with Twig syntax and `.html` for simple HTML files. Both work identically.

### 7. Filters Are Not PHP Functions

**Problem:** You try `{{ items | count }}` or `{{ name | strtoupper }}` and get an error.

**Cause:** Frond filters are not PHP functions. The filter names follow Twig conventions, not PHP conventions.

**Fix:** Use `{{ items | length }}` instead of `count`, `{{ name | upper }}` instead of `strtoupper`, `{{ text | lower }}` instead of `strtolower`. See the filter table in section 7 for the full list.
