# Chapter 1: What Is Tina4?

## The "Not a Framework" Philosophy

Most web frameworks start with a bold claim: "We make web development easier." Then they hand you a 200MB install, a dependency tree that looks like a family reunion gone wrong, and a learning curve shaped like a cliff face.

Tina4 takes a different approach. It is a **toolkit**, not a cathedral. There is no grand architecture you must worship. There is no dependency graph you must appease. There is no "the Tina4 way" that forces you to restructure your brain before you can print "Hello, World."

Here is a Tina4 project that serves a JSON API:

```php
<?php
// src/routes/greeting.php
use Tina4\Route;

Route::get("/api/greeting/{name}", function ($request, $response) {
    return $response->json([
        "message" => "Hello, " . $request->params["name"]
    ]);
});
```

That is it. No base controller. No service provider. No bootstrapping ritual. You drop that file into `src/routes/`, start the server, and it works. Tina4 discovers it automatically.

The philosophy is simple: **you write code, Tina4 gets out of the way.** Convention over configuration means files go in predictable places, and the framework figures out the rest. If you know where `src/routes/` is, you know how to add a route. If you know where `src/templates/` is, you know how to add a page. If you know where `src/orm/` is, you know how to add a model.

This is not laziness. This is a design decision rooted in a decade of watching developers waste hours on configuration files, dependency conflicts, and framework upgrades that break everything.

## Why Zero Dependencies Matters

Tina4 v3 has **zero third-party dependencies** for its core features. Every component -- the template engine, the JWT library, the SCSS compiler, the queue system, the GraphQL parser, the logger, the rate limiter -- is built from scratch using only the language's standard library.

This is not a flex. It is a survival strategy. Here is why:

### Security

Every dependency is an attack surface. When a package in your dependency tree gets compromised (and it will -- look up `event-stream`, `colors.js`, `ua-parser-js`, or any of the dozens of npm/PyPI/Packagist supply chain attacks), your application is exposed. With Tina4, the attack surface is the language runtime and your code. That is it.

### Size

A typical Laravel installation pulls in over 70 packages. A typical Rails app starts with 40+ gems. A Next.js project's `node_modules` folder is famously measured in hundreds of megabytes.

A Tina4 project installs **one package**. The entire framework is roughly **5,000 lines of code** per language. The Docker image targets **40-80MB**. Your production container ships with exactly what it needs and nothing else.

### Portability

Zero dependencies means zero compatibility conflicts. You will never see this with Tina4:

```
Your requirements could not be resolved to an installable set of packages.
  Problem 1
    - package-a v2.1 requires other-package ^3.0
    - package-b v1.4 requires other-package ^2.0
    - You can only install one version of other-package
```

There is no diamond dependency problem when there are no dependencies.

### Upgrades

Upgrading Tina4 means upgrading one package. There is no cascade of breaking changes through a dependency tree. The framework team controls every line of code, so when something breaks, the fix is in one place.

### The One Exception

Database drivers are the single exception. You cannot talk to PostgreSQL without a PostgreSQL driver, and you cannot talk to MySQL without a MySQL driver. These are native connectors to external systems. They are optional -- install only what you need. SQLite works out of the box with every language's standard library.

## 38 Features in ~5,000 Lines

Tina4 ships with everything you need to build a production web application. Here is what is included in every installation, across all four languages:

**Core Web (12 features)**
- HTTP router with path parameters, typed params, middleware, caching, and auth gating
- Request and Response objects with full HTTP access
- Static file serving from `src/public/`
- CORS handling from environment variables
- Rate limiting (sliding window, per-IP)
- Health check endpoint (`GET /health`)
- Graceful shutdown on SIGTERM/SIGINT
- Request ID tracking (generated or passed via `X-Request-ID`)
- Structured logging (JSON in production, human-readable in dev)
- Response compression (gzip, automatic)
- ETag support for zero-bandwidth cache hits
- HTML minification in production

**Data Layer (15 features)**
- SQL-first ORM with Active Record pattern
- Seven database drivers: SQLite, PostgreSQL, MySQL, MSSQL, Firebird, ODBC, MongoDB
- Soft delete with restore and force delete
- Relationships: hasOne, hasMany, belongsTo with eager loading
- Scopes for reusable query filters
- Field mapping (property names to column names)
- Paginated results in a standardized JSON format
- Query result caching with TTL
- Input validation from field definitions
- Migrations with rollback support
- Database seeders with 50+ fake data generators

**Template and Frontend (5 features)**
- Frond: a zero-dependency, Twig-compatible template engine with 55+ filters
- Template inheritance, includes, macros
- SCSS compiler (zero-dependency)
- tina4css: built-in CSS utility framework
- frond.js: lightweight JS helper for AJAX, WebSocket, CRUD tables, modals, forms

**Auth and Sessions (4 features)**
- JWT (HS256/RS256) built from scratch
- Five session backends: file, Redis, Valkey, MongoDB, database
- Swagger/OpenAPI auto-generation from route definitions
- Auto-CRUD endpoint generation from models

**Extended Features (7 features)**
- Database-backed queue with retry, dead-letter, failover, and circuit breaker
- GraphQL parser and executor (zero-dependency)
- WebSocket server (zero-dependency)
- WSDL/SOAP support
- HTTP API client (stdlib-based)
- Email/SMTP messenger
- Localization/i18n with JSON translation files

**Developer Experience (7 features)**
- Rust-based unified CLI (`tina4 init`, `tina4 serve`, `tina4 migrate`, etc.)
- Dev admin dashboard with 11 panels (queue manager, WebSocket monitor, request inspector, error log, and more)
- Debug overlay injected into HTML pages in dev mode
- Configurable error pages (404, 500, etc.)
- Live reload in development
- Event/listener system with priority and async support
- AI tool integration

All of this fits in roughly 5,000 lines of code per language. No feature requires more than 500 lines. The biggest component -- the Frond template engine -- is about 1,500-2,000 lines. Most features are under 200 lines.

## Convention Over Configuration

Tina4 projects follow a predictable structure. When you run `tina4 init`, you get:

```
my-project/
├── .env                    # Environment configuration
├── src/
│   ├── routes/             # Route handlers (auto-discovered)
│   ├── orm/                # ORM models (auto-discovered)
│   ├── migrations/         # SQL migration files
│   ├── seeds/              # Database seed files
│   ├── templates/          # Frond templates
│   │   └── errors/         # Custom error pages (404.html, 500.html)
│   ├── public/             # Static files (served directly)
│   │   ├── js/
│   │   │   └── frond.js    # Auto-provided by the framework
│   │   ├── css/
│   │   ├── scss/
│   │   ├── images/
│   │   └── icons/
│   └── locales/            # Translation files (JSON)
│       └── en.json
├── data/                   # SQLite databases (gitignored)
├── logs/                   # Log files with rotation (gitignored)
├── secrets/                # JWT keys (gitignored)
└── tests/                  # Test files
```

The rules are simple:

1. **Routes go in `src/routes/`.** Any `.php`, `.py`, `.rb`, or `.js`/`.ts` file in this directory is auto-discovered at startup. Name the files however you want. Organize them into subdirectories if you like. Tina4 does not care about the file names -- it reads the route definitions inside them.

2. **Models go in `src/orm/`.** Same auto-discovery. Define your ORM classes here and Tina4 finds them.

3. **Templates go in `src/templates/`.** When you call `response.render("products/list.html", data)`, Tina4 looks for `src/templates/products/list.html`.

4. **Static files go in `src/public/`.** A file at `src/public/css/style.css` is served at `/css/style.css`. No route needed.

5. **Configuration goes in `.env`.** One file. Key-value pairs. No YAML, no TOML, no JSON config files.

There is nothing to configure beyond this. No routing table to maintain. No service container to wire up. No middleware stack to arrange in the right order. Drop files in the right directories and they work.

**Auto-repair on startup:** Every time Tina4 starts, it verifies the folder structure and silently creates any missing directories. If you clone a project and `data/` is missing (because it is in `.gitignore`), Tina4 creates it. If you manually scaffold a project and forget `src/templates/errors/`, Tina4 creates it. The framework never fails because of a missing directory.

## The 4-Language Paradigm

Tina4 is not one framework. It is four:

- **tina4-python** -- Python 3.10+
- **tina4-php** -- PHP 8.1+
- **tina4-ruby** -- Ruby 3.0+
- **tina4-nodejs** -- Node.js 18+ (TypeScript)

All four share the same:

- **Project structure** -- `src/routes/`, `src/orm/`, `src/templates/`, `src/public/`
- **Environment variables** -- the same `.env` file works across all four (language-specific entries are prefixed)
- **Template syntax** -- Frond templates are identical regardless of backend language
- **Frontend library** -- `frond.js` is the same JavaScript, served by all four backends
- **CLI commands** -- `tina4 init`, `tina4 serve`, `tina4 migrate`, `tina4 test`
- **API contracts** -- the same endpoints, the same JSON responses, the same HTTP behavior
- **Test specifications** -- test cases are defined language-agnostically; each framework implements them

The only differences are the language-idiomatic naming conventions:

| Concept | Python / Ruby | PHP / Node.js |
|---------|--------------|---------------|
| Method names | `snake_case` | `camelCase` |
| Model field | `created_at` | `createdAt` |
| Fetch one row | `fetch_one()` | `fetchOne()` |
| Soft delete | `soft_delete()` | `softDelete()` |

This means:

- A team can prototype in Python and deploy in PHP without relearning the framework.
- Frontend developers using `frond.js` do not need to know or care which backend language is running.
- DevOps deploys the same Docker structure, the same `.env`, the same health checks, regardless of language.
- Documentation covers all four languages simultaneously -- learn one, understand all.

A single Rust-based CLI binary (`tina4`) auto-detects the project language and dispatches to the correct runtime:

```bash
# These all work the same way, regardless of language
tina4 init my-project         # Scaffold a new project
tina4 serve                   # Start dev server on port 7145
tina4 migrate                 # Run pending migrations
tina4 migrate:create "add users table"
tina4 migrate:rollback        # Rollback last migration
tina4 seed                    # Run database seeders
tina4 test                    # Run the test suite
tina4 routes                  # List all registered routes
```

## What Tina4 Is Not

Tina4 is not trying to replace Laravel, Django, Rails, or Next.js. Those are excellent frameworks for teams that want a full-stack opinion on everything from authentication workflows to payment processing.

Tina4 is for developers who want:

- **Control** -- you see every line of code that runs your application
- **Simplicity** -- one package, one import, predictable behavior
- **Speed** -- sub-millisecond framework overhead, 40MB Docker images
- **Portability** -- switch languages without switching paradigms
- **Security** -- no supply chain risk from transitive dependencies

If you want a batteries-included platform with an ecosystem of plugins and a marketplace of themes, Tina4 is not the right tool. If you want a sharp, minimal toolkit that does exactly what you tell it to and nothing else, keep reading.

## Summary

| Aspect | Tina4 |
|--------|-------|
| Philosophy | Toolkit, not a cathedral |
| Dependencies | Zero (core features) |
| Framework size | ~5,000 lines per language |
| Docker image | 40-80MB |
| Languages | Python, PHP, Ruby, Node.js |
| Configuration | `.env` file only |
| Discovery | Automatic (routes, models, templates) |
| CLI | Unified Rust binary across all languages |
| Tests | 4,912 tests across all four frameworks |
| Features | 78 features at 100% parity |
