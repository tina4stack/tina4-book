# Parity Audit: Remaining Classes

> **Generated:** 2026-04-03 | **Version:** v3.10.67

---

## GraphQL — GOOD PARITY (90%)

| Feature | Python | PHP | Ruby | Node.js | Status |
|---------|--------|-----|------|---------|--------|
| `add_type()` | YES | YES | YES | YES | OK |
| `add_query()` | YES (config dict) | YES (separate params) | YES (config hash) | YES (separate params) | PARAM STYLE DIFFERS |
| `add_mutation()` | YES | YES | YES | YES | OK |
| `execute(query, vars)` | YES | YES | YES | YES | OK |
| `from_orm(model)` | YES | YES | YES | YES | OK |
| `schema()` SDL output | NO | YES | NO | YES | MISSING Py/Ru |
| `introspect()` | YES | NO | NO | NO | PYTHON ONLY |

- [ ] **Issue:** Query/mutation config format differs (dict vs separate params)
- [ ] **Issue:** SDL output missing in Python/Ruby
- [ ] **Documented?** All CLAUDE.md: yes

## WSDL/SOAP — GOOD PARITY (85%)

All 4 frameworks auto-generate WSDL at `?wsdl` and handle SOAP requests. Registration patterns differ:
- Python: `@wsdl_operation()` decorator
- PHP: Subclass `WSDL`
- Ruby: Inline on route
- Node.js: Plain class with types

- [ ] **Issue:** Registration pattern inconsistent
- [ ] **Documented?** All CLAUDE.md: yes

## Events — EXCELLENT PARITY (95%)

| Method | Python | PHP | Ruby | Node.js | Status |
|--------|--------|-----|------|---------|--------|
| `on(event, handler, priority)` | YES | YES | YES | YES | OK |
| `once(event, handler)` | YES | YES | YES | YES | OK |
| `off(event, handler)` | YES | YES | YES | YES | OK |
| `emit(event, *args)` | YES | YES | YES | YES | OK |
| `emit_async(event, *args)` | YES | YES (not real async) | YES (threads) | **NO** | MISSING Node |
| `listeners(event)` | YES | YES | YES | YES | OK |
| `clear()` | YES | YES | YES | YES | OK |

- [ ] **Issue:** Node.js missing `emit_async()`
- [ ] **Documented?** All CLAUDE.md: yes

## Api Client (Outbound HTTP) — CRITICAL GAP

| Method | Python | PHP | Ruby | Node.js | Status |
|--------|--------|-----|------|---------|--------|
| `get(url)` | YES | via `send_request` | **NO** | **NO** | MISSING |
| `post(url, body)` | YES | via `send_request` | **NO** | **NO** | MISSING |
| `put(url, body)` | YES | via `send_request` | **NO** | **NO** | MISSING |
| `delete(url)` | YES | via `send_request` | **NO** | **NO** | MISSING |
| `set_basic_auth(user, pass)` | YES | YES | **NO** | **NO** | MISSING |
| `set_bearer_token(token)` | YES | NO | **NO** | **NO** | MISSING |

- [ ] **CRITICAL:** Ruby and Node.js have NO built-in outbound HTTP client
- [ ] **Documented?** Python CLAUDE.md: yes. Others: N/A

## Swagger — GOOD PARITY (90%)

- [ ] All 4 generate OpenAPI spec and serve Swagger UI at `/swagger`
- [ ] Python uses decorators (`@description`, `@tags`, `@example`)
- [ ] PHP/Ruby use metadata dicts/hashes on routes
- [ ] Node.js generates from TypeScript types
- [ ] **Issue:** Decorator/metadata style differs but output is equivalent
- [ ] **Documented?** All CLAUDE.md: yes

## i18n / Localization — EXCELLENT PARITY (95%)

| Method | Python | PHP | Ruby | Node.js | Status |
|--------|--------|-----|------|---------|--------|
| `t(key, vars)` | YES | YES | YES | YES | OK |
| `set_locale(locale)` | YES | YES | YES | YES | OK |
| `get_locale()` | YES | YES | YES | YES | OK |
| Auto-load from `src/locales/` | YES | YES | YES | YES | OK |
| Interpolation `{placeholder}` | YES | YES | YES | YES | OK |
| Nested keys (dot notation) | YES | YES | YES | YES | OK |

- [ ] **Minor:** Ruby uses YAML files, others use JSON
- [ ] **Documented?** All CLAUDE.md: yes

## HtmlElement — EXCELLENT PARITY (99%)

- [ ] All 4 have identical API: constructor, builder pattern, tag helpers, void tags, attribute escaping
- [ ] **No issues found**
- [ ] **Documented?** All CLAUDE.md: yes

## Seeder / FakeData — EXCELLENT PARITY (99%)

- [ ] All 4 have identical generators: name, email, phone, integer, float, datetime, boolean, uuid, sentence, paragraph, address, url
- [ ] All support `seed_table()` and `seed_orm()` for database seeding
- [ ] **No issues found**
- [ ] **Documented?** All CLAUDE.md: yes

---

## CROSS-FRAMEWORK PRIORITY SUMMARY

| Priority | Issue | Affected |
|----------|-------|----------|
| **CRITICAL** | Ruby/Node missing outbound HTTP client (Api class) | Ruby, Node.js |
| **CRITICAL** | PHP missing WebSocket server | PHP |
| **HIGH** | Node.js missing `emit_async()` | Node.js |
| **HIGH** | Node.js Queue missing RabbitMQ/Kafka/MongoDB backends | Node.js |
| **MEDIUM** | GraphQL config format inconsistency | All |
| **MEDIUM** | WSDL registration pattern inconsistency | All |
| **LOW** | Ruby i18n uses YAML not JSON | Ruby |
| **NONE** | HtmlElement, Seeder/FakeData — excellent parity | None |
