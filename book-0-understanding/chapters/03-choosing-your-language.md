# Chapter 3: Choosing Your Language

Tina4 runs on four languages. The framework API, project structure, template syntax, and CLI commands are identical across all of them. So the question is not "which Tina4 is best?" -- the question is "which language fits your team, your hosting, and your problem?"

This chapter gives you the information to make that decision.

---

## Python

**Best for:** Data science teams, ML/AI integration, async-heavy applications, rapid prototyping.

```python
# src/routes/products.py
from tina4_python import get, post

@get("/api/products")
async def list_products(request, response):
    products = Product.select(page=request.query.get("page", 1))
    return response.json(products)

@post("/api/products")
async def create_product(request, response):
    product = Product.create(request.body)
    return response.json(product, 201)
```

### Why Choose Python

**Async-native.** Tina4 Python runs on asyncio. Every route handler is an async function by default. If your application calls external APIs, runs database queries, or processes files, async means your server handles thousands of concurrent connections without threads.

**Data science integration.** If your web application sits next to a machine learning pipeline, a data processing job, or a Jupyter notebook, Python is the natural choice. Your API endpoint can import pandas, numpy, or scikit-learn directly. No inter-process communication, no REST calls to a separate service.

**Fastest growing community.** Python is the most-taught programming language in universities worldwide. Finding Python developers is easier than finding PHP or Ruby developers, especially among recent graduates.

**Reference implementation.** Tina4 Python was the first v3 framework to reach 100% completion. It is the reference implementation -- when there is ambiguity in the spec, the Python behavior is canonical.

### Watch Out For

**GIL limitations.** CPU-bound work in Python is single-threaded due to the Global Interpreter Lock. If your application does heavy computation (image processing, PDF generation), use background tasks or a queue worker process.

**Deployment complexity.** Python deployment is more involved than PHP. You need to manage virtual environments, pip dependencies (even though Tina4 has zero deps, your app might use others), and a process manager like systemd or Docker.

**Package naming.** Install with `pip install tina4-python`. The CLI command is `tina4` (auto-detects language). The import is `from tina4_python import ...`.

### Quick Start

```bash
pip install tina4-python
tina4 init my-project
cd my-project
tina4 serve
```

---

## PHP

**Best for:** Existing PHP teams, shared hosting, CMS-adjacent projects, the largest hosting support.

```php
<?php
// src/routes/products.php
use Tina4\Route;

Route::get("/api/products", function ($request, $response) {
    $products = Product::select(page: $request->query["page"] ?? 1);
    return $response->json($products);
});

Route::post("/api/products", function ($request, $response) {
    $product = Product::create($request->body);
    return $response->json($product, 201);
});
```

### Why Choose PHP

**Hosting is everywhere.** PHP runs on virtually every web host on the planet. Shared hosting, VPS, dedicated servers, cloud platforms -- if it has a web server, it probably runs PHP. This matters when your client's infrastructure is not negotiable.

**Fastest Tina4.** PHP 8.1+ with JIT compilation makes Tina4 PHP the fastest of the four implementations in raw request throughput. Combined with OPcache (which caches compiled bytecode), PHP serves requests with minimal overhead.

**Mature ecosystem.** PHP has 30 years of web development behind it. The ecosystem for database drivers, payment processing, PDF generation, and image manipulation is enormous. While Tina4 itself has zero dependencies, your application can still use Composer packages alongside it.

**Familiar to most web developers.** PHP was the first server-side language for a generation of developers. If your team already knows PHP, there is no reason to switch.

**Monorepo simplicity.** Tina4 PHP v3 is a single Composer package under the `Tina4\` namespace. No split packages, no sub-repositories. One `composer require`, and you have everything.

### Watch Out For

**No native async.** Standard PHP is synchronous. For WebSocket support and true async behavior, you need the Swoole or OpenSwoole extension. This is not a problem for most web applications, but if you need to hold thousands of persistent connections, make sure Swoole is available.

**Extension management.** PHP database drivers are PHP extensions (ext-pgsql, ext-mysqli, ext-sqlite3). On some hosting platforms, enabling these requires contacting support or recompiling PHP. Check that your target platform has the extensions you need.

**Case sensitivity.** PHP uses `camelCase` for methods (`fetchOne()`, `softDelete()`, `hasMany()`). If you are coming from a Python or Ruby background, this is a style adjustment.

### Quick Start

```bash
composer require tina4/tina4-php
tina4 init my-project
cd my-project
tina4 serve
```

---

## Ruby

**Best for:** Startups, elegant code, Rails refugees who want less framework.

```ruby
# src/routes/products.rb
get "/api/products" do |request, response|
  products = Product.select(page: request.query["page"] || 1)
  response.json(products)
end

post "/api/products" do |request, response|
  product = Product.create(request.body)
  response.json(product, 201)
end
```

### Why Choose Ruby

**Elegant syntax.** Ruby was designed to make programmers happy. The Tina4 Ruby API reflects this -- route definitions read like English, blocks feel natural, and the DSL is clean.

**Rails refugees.** If you have built Rails applications and found yourself fighting the framework more than using it, Tina4 Ruby gives you the parts you liked (convention over configuration, migrations, ORM, template engine) without the parts you did not (massive dependency tree, complex configuration, opaque internals).

**Startup velocity.** Ruby's expressiveness means less code for the same functionality. For startups that need to ship fast and iterate, Ruby reduces the time between "I have an idea" and "it is in production."

**Strong testing culture.** The Ruby community takes testing seriously. Tina4 Ruby integrates with Ruby's testing ecosystem naturally, and the framework itself has 1,334 tests -- the most of any Tina4 implementation.

### Watch Out For

**Smaller hosting pool.** Ruby hosting is less ubiquitous than PHP. You will generally need a VPS, container platform, or PaaS (Heroku, Render, Fly.io). Shared hosting with Ruby support is rare.

**Performance.** Ruby is not the fastest language. For raw throughput, PHP and Node.js outperform it. For most web applications, Ruby is fast enough -- but if you are building a high-traffic API that serves thousands of requests per second, benchmark first.

**Smaller talent pool.** Ruby developers are harder to find than Python or JavaScript developers. If you are hiring a team, factor this in.

### Quick Start

```bash
gem install tina4
tina4 init my-project
cd my-project
tina4 serve
```

---

## Node.js

**Best for:** JavaScript/TypeScript teams, file-based routing, real-time applications, highest raw speed.

```typescript
// src/routes/api/products/index.ts
export default function handler(request, response) {
    const products = Product.select({ page: request.query.page || 1 });
    return response.json(products);
}

// src/routes/api/products/index.post.ts
export default function handler(request, response) {
    const product = Product.create(request.body);
    return response.json(product, 201);
}
```

### Why Choose Node.js

**One language everywhere.** If your team writes JavaScript or TypeScript, Node.js means no context switching between frontend and backend. The same developers, the same language, the same tooling.

**File-based routing.** Tina4 Node.js supports file-based routing -- the file path determines the URL path. A file at `src/routes/api/products/[id].ts` automatically handles `/api/products/42`. If you like the Next.js routing pattern, this will feel familiar.

**Highest raw speed.** Node.js on V8 has the highest raw request throughput of the four implementations. For APIs that serve simple JSON responses, Node.js handles the most requests per second.

**TypeScript support.** Tina4 Node.js is written in TypeScript. You get full type safety, autocompletion, and compile-time error checking.

**WebSocket native.** Node.js has native WebSocket support without additional extensions. Real-time features (chat, live dashboards, notifications) work out of the box.

### Watch Out For

**Callback/Promise complexity.** While modern async/await syntax is clean, the underlying Node.js ecosystem still has gotchas with unhandled promise rejections, callback-style APIs, and the event loop. If your team is new to async JavaScript, there is a learning curve.

**Single-threaded by nature.** Like Python, Node.js is single-threaded for user code. CPU-heavy operations block the event loop. Use worker threads or queue background tasks for heavy computation.

**Dependency culture.** The Node.js ecosystem is famous for micro-dependencies. While Tina4 itself has zero core dependencies, your application's other packages might pull in hundreds of transitive dependencies. Be deliberate about what you `npm install`.

### Quick Start

```bash
npm install tina4
tina4 init my-project
cd my-project
tina4 serve
```

---

## Comparison Table

| Factor | Python | PHP | Ruby | Node.js |
|--------|--------|-----|------|---------|
| **Install** | `pip install tina4-python` | `composer require tina4/tina4-php` | `gem install tina4` | `npm install tina4` |
| **CLI** | `tina4` | `tina4` | `tina4` | `tina4` |
| **Naming** | `snake_case` | `camelCase` | `snake_case` | `camelCase` |
| **Async** | Native (asyncio) | Swoole extension | Rack-based | Native (event loop) |
| **Hosting** | VPS, containers, PaaS | Everywhere | VPS, containers, PaaS | VPS, containers, PaaS |
| **Raw speed** | Good | Very good (JIT) | Adequate | Best |
| **Test count** | 1,165 | 1,166 | 1,334 | 1,247 |
| **Best for** | Data/ML teams | Web agencies, existing PHP | Startups, clean code | JS/TS full-stack teams |
| **WebSocket** | Native async | Swoole required | Rack hijack / Puma | Native |
| **Routing style** | Decorator-based | Static method calls | DSL blocks | File-based + decorators |
| **Learning curve** | Low (if you know Python) | Low (if you know PHP) | Low (if you know Ruby) | Low (if you know JS/TS) |
| **Framework LOC** | ~5,000 | ~5,000 | ~5,000 | ~5,000 |
| **Docker image** | ~60MB | ~50MB | ~70MB | ~40MB |
| **Community size** | Largest (general) | Largest (web-specific) | Smallest | Large |
| **Shared hosting** | Rare | Universal | Rare | Rare |
| **Package manager** | pip | Composer | RubyGems | npm |

---

## Switching Languages

Because all four Tina4 implementations share the same project structure, template syntax, and CLI commands, switching languages is straightforward:

1. Your `src/templates/` directory works without changes -- Frond syntax is identical.
2. Your `.env` file works without changes -- same variables, same defaults.
3. Your `src/migrations/` directory works without changes -- same SQL.
4. Your `src/public/` directory works without changes -- same static files.
5. Your `frond.js` frontend code works without changes -- same API.

What you need to rewrite:

1. `src/routes/` -- route handlers, translated to the new language's syntax.
2. `src/orm/` -- model definitions, translated to the new language's class syntax.
3. `tests/` -- test files, translated to the new language's test framework.

This is not "rewrite your application." It is "translate your business logic." The framework knowledge transfers completely.

---

## How to Decide

Answer these questions:

1. **What does your team already know?** Use that language. The learning curve for Tina4 is the same regardless. The learning curve for a new programming language is not.

2. **Where are you deploying?** If it is shared hosting, use PHP. If it is containers, use anything. If it is a serverless platform, check which runtimes are supported.

3. **What are you building alongside the web app?** If you have ML models, use Python. If you have a React/Vue frontend team, use Node.js. If you have an existing PHP codebase, use PHP.

4. **How many concurrent connections do you need?** For high-concurrency scenarios (chat, live dashboards, thousands of WebSocket connections), use Python or Node.js for native async. PHP requires Swoole for this. Ruby can handle moderate concurrency with Puma.

5. **Does raw performance matter?** For most applications, all four are fast enough. If you are serving 10,000+ requests per second on a single instance, benchmark with your actual workload. The framework overhead is sub-millisecond in all four -- the bottleneck is usually your database queries.

If none of these questions produce a clear answer, use Python. It is the reference implementation, has the largest general-purpose community, and is the most taught language in the world.
