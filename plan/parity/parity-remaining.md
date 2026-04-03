# Parity Audit: Remaining Classes

> **Generated:** 2026-04-03 | **Updated:** 2026-04-03 | **Version:** v3.10.67+

---

## GraphQL — FULL PARITY (100%)

| Feature | Python | PHP | Ruby | Node.js | Status |
|---------|--------|-----|------|---------|--------|
| `add_type()` | YES | YES | YES | YES | OK |
| `add_query()` | YES (config dict) | YES (separate params) | YES (kwargs+block) | YES (separate params) | BY DESIGN — language idioms |
| `add_mutation()` | YES | YES | YES | YES | OK |
| `execute(query, vars)` | YES | YES | YES | YES | OK |
| `from_orm(model)` | YES | YES | YES | YES | OK |
| `schema_sdl()` / `schemaSdl()` | YES | YES | YES | YES | FIXED this session |
| `introspect()` | YES | YES | YES | YES | FIXED this session |

- [x] ~~SDL output missing~~ — FIXED: `schema_sdl()` / `schemaSdl()` added to all 4
- [x] ~~introspect() Python only~~ — FIXED: added to PHP, Ruby, Node.js
- [x] Query/mutation param style — BY DESIGN (language idioms)

## WSDL/SOAP — FULL PARITY (100%)

All 4 frameworks auto-generate WSDL at `?wsdl` and handle SOAP requests.

| Feature | Python | PHP | Ruby | Node.js | Status |
|---------|--------|-----|------|---------|--------|
| Operation registration | `@wsdl_operation()` | `#[WSDLOperation()]` | `wsdl_operation` DSL | `@WSDLOp()` | BY DESIGN |
| WSDL generation | YES | YES | YES | YES | OK |
| SOAP handling | ElementTree DOM | SimpleXML DOM | REXML DOM | Stack-based DOM | FIXED — was regex |
| Lifecycle hooks | `on_request` / `on_result` | YES | YES | YES | OK |
| Route registration | Manual | Manual | Manual | Auto `.register()` | BY DESIGN |

- [x] ~~Node.js uses regex XML parsing~~ — FIXED: replaced with zero-dep stack-based DOM parser
- [x] Registration pattern — BY DESIGN (decorators vs attributes vs DSL)

## Events — EXCELLENT PARITY (95%)

| Method | Python | PHP | Ruby | Node.js | Status |
|--------|--------|-----|------|---------|--------|
| `on(event, handler, priority)` | YES | YES | YES | YES | OK |
| `once(event, handler)` | YES | YES | YES | YES | OK |
| `off(event, handler)` | YES | YES | YES | YES | OK |
| `emit(event, *args)` | YES | YES | YES | YES | OK |
| `emit_async(event, *args)` | YES | YES | YES (threads) | **NO** | TODO |
| `listeners(event)` | YES | YES | YES | YES | OK |
| `clear()` | YES | YES | YES | YES | OK |

- [x] ~~Node.js missing `emit_async()`~~ — FIXED: `emitAsync()` added

## Api Client (Outbound HTTP) — FULL PARITY (100%)

**AUDIT WAS WRONG.** All 4 frameworks have full outbound HTTP clients:

| Method | Python | PHP | Ruby | Node.js | Status |
|--------|--------|-----|------|---------|--------|
| `get(url)` | YES | YES | YES | YES | OK |
| `post(url, body)` | YES | YES | YES | YES | OK |
| `put(url, body)` | YES | YES | YES | YES | OK |
| `patch(url, body)` | YES | YES | YES | YES | OK |
| `delete(url)` | YES | YES | YES | YES | OK |
| `set_basic_auth()` | YES | YES | YES | YES | OK |
| `set_bearer_token()` | YES | YES | YES | YES | OK |
| `add_headers()` | YES | YES | YES | YES | OK |

All use zero dependencies (stdlib HTTP clients).

## Swagger — FULL PARITY (100%)

- [x] All 4 generate OpenAPI spec and serve Swagger UI at `/swagger`
- [x] Metadata style differs by language (decorators/attributes/hashes/types) — BY DESIGN
- [x] Output is equivalent across all 4

## i18n / Localization — EXCELLENT PARITY (95%)

| Method | Python | PHP | Ruby | Node.js | Status |
|--------|--------|-----|------|---------|--------|
| `t(key, vars)` | YES | YES | YES | YES | OK |
| `set_locale(locale)` | YES | YES | YES | YES | OK |
| `get_locale()` | YES | YES | YES | YES | OK |
| Auto-load from `src/locales/` | YES | YES | YES | YES | OK |
| Interpolation `{placeholder}` | YES | YES | YES | YES | OK |
| Nested keys (dot notation) | YES | YES | YES | YES | OK |

- [x] ~~Ruby uses YAML, others JSON~~ — FIXED: all 4 now support both JSON and YAML (zero-dep parser)

## HtmlElement — FULL PARITY (100%)

- [x] All 4 have identical API: constructor, builder pattern, tag helpers, void tags, attribute escaping
- [x] No issues

## Seeder / FakeData — FULL PARITY (100%)

- [x] All 4 have identical generators + `seed_table()` / `seed_orm()`
- [x] No issues

---

## SUMMARY

| Class | Status | Notes |
|-------|--------|-------|
| GraphQL | **100%** | schema_sdl + introspect added to all |
| WSDL/SOAP | **100%** | Node DOM parser fixed |
| Events | **100%** | emitAsync added |
| Api Client | **100%** | Audit was wrong — all 4 have it |
| Swagger | **100%** | BY DESIGN differences |
| i18n | **100%** | All support JSON + YAML |
| HtmlElement | **100%** | No issues |
| Seeder | **100%** | No issues |
