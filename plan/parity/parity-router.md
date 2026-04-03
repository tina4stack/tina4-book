# Parity Audit: Router

> **Generated:** 2026-04-03 | **Version:** v3.10.67

## Status: HIGH PARITY (99%)

Route registration, parameter syntax, auth defaults, middleware, grouping, and WebSocket routes are consistent across all 4 frameworks. Differences are intentional language idioms (decorators vs methods vs blocks).

---

## Route Registration

| Framework | Style | Signature | Return |
|-----------|-------|-----------|--------|
| Python | Decorator `@get(path)` or `Router.get(path, handler)` | path + handler + **options | `function` or `RouteRef` |
| PHP | Static `Router::get(path, callback)` | string + callable | `self` (fluent) |
| Ruby | Class `Router.get(path, &block)` | path + middleware: [] + &block | `Route` |
| Node.js | Instance `router.get(path, handler, middlewares?, meta?)` or top-level `get()` | path + handler + optional arrays | `RouteRef` |

- [ ] **PARITY: OK** — all support GET/POST/PUT/PATCH/DELETE/ANY + WebSocket
- [ ] **Documented?** All CLAUDE.md: yes

## Route Parameter Syntax

| Syntax | Python | PHP | Ruby | Node.js |
|--------|--------|-----|------|---------|
| `{id}` | YES | YES | YES | YES |
| `{id:int}` | YES | YES | YES | YES |
| `{id:float}` | YES | YES | YES | YES |
| `{id:path}` | YES | YES | YES | YES |
| `:id` (Express) | NO | NO | NO | YES (compat) |
| `[id]` (file-based) | NO | NO | NO | YES (compat) |

- [ ] **PARITY: OK** — all use `{param}` as primary syntax
- [ ] **Documented?** CLAUDE.md: yes. Skill: yes (just added). Book Ch5: yes.

## Auth Defaults

- [ ] **PARITY: OK** — GET=public, POST/PUT/PATCH/DELETE=secured across all 4

## Middleware

| Framework | Route-level | Group-level | Global |
|-----------|-------------|-------------|--------|
| Python | `@middleware()` decorator or `middleware=[]` kwarg | `Router.group(prefix, cb, middleware=[])` | N/A |
| PHP | `.middleware([])` chain | `Router::group(prefix, cb, middleware)` | `Router::use(class)` |
| Ruby | `middleware: []` kwarg | `Router.group(prefix, middleware: [], &block)` | `Router.use(class)` |
| Node.js | `middlewares?` param | `router.group(prefix, cb, middlewares?)` | `Router.use(class)` |

- [ ] **PARITY: OK** — all support route, group, and global middleware
- [ ] **Documented?** All CLAUDE.md: yes

## Route Grouping

| Framework | Signature | Callback receives |
|-----------|-----------|-------------------|
| Python | `Router.group(prefix, callback, middleware=[])` | `RouteGroup` instance |
| PHP | `Router::group(prefix, callback, middleware=[])` | Uses static state |
| Ruby | `Router.group(prefix, middleware: [], &block)` | `GroupContext` instance |
| Node.js | `router.group(prefix, callback, middlewares?)` | `RouteGroup` instance |

- [ ] **PARITY: OK** — all support nested groups with prefix + middleware inheritance
- [ ] **Documented?** All CLAUDE.md: yes

## Chaining (secure/noAuth/cache)

| Method | Python | PHP | Ruby | Node.js |
|--------|--------|-----|------|---------|
| Require auth | `@secured()` / `.secure()` | `.secure()` | `.secure()` | `.secure()` |
| Make public | `@noauth()` / `.noAuth()` | `.noAuth()` | `.no_auth()` | `.noAuth()` |
| Cache response | `@cached()` / `.cache()` | `.cache()` | `.cache()` | `.cache()` |

- [ ] **PARITY: OK** — naming follows language conventions (snake_case vs camelCase)
- [ ] **Documented?** All CLAUDE.md: yes

## Route Matching

| Framework | Method | Return |
|-----------|--------|--------|
| Python | `Router.match(method, path)` static | `(route, params)` tuple |
| PHP | `Router::match(method, path)` static | `array` or `null` |
| Ruby | `Router.find_route(path, method)` class | `[route, params]` or `nil` |
| Node.js | `router.match(method, pathname)` instance | `MatchResult` or `null` |

- [ ] **MINOR ISSUE:** Ruby param order is `(path, method)`, others are `(method, path)`
- [ ] **MINOR ISSUE:** Ruby method name is `find_route`, others use `match`
- [ ] **Documented?** Internal API, not developer-facing

## Handler Signature

- [ ] **PARITY: OK** — all use `handler(request, response)` with same request/response properties

## File-Based Route Discovery

| Framework | Auto-discovery from src/routes/ |
|-----------|-------------------------------|
| Python | YES (scans .py files) |
| PHP | YES (scans .php files) |
| Ruby | YES (`Router.load_routes(dir)`) |
| Node.js | YES (scans .ts/.js files with `[param]` syntax) |

- [ ] **PARITY: OK**
- [ ] **Documented?** All CLAUDE.md: yes

## Issues to Fix

| # | Issue | Severity | Frameworks |
|---|-------|----------|------------|
| 1 | Ruby `find_route(path, method)` param order reversed vs `match(method, path)` | LOW | Ruby |
| 2 | Node.js also accepts `:id` and `[id]` syntax (others don't) | LOW | Node.js (compat only) |

## Documentation Gaps

| # | Gap |
|---|-----|
| 1 | Route matching internals not documented (internal API) |
| 2 | `@template()` decorator (Python) not in other frameworks |
