# Parity Audit: Request & Response

> **Generated:** 2026-04-03 | **Version:** v3.10.67

## Status: HIGH PARITY (90%) — Minor property/naming gaps

---

## REQUEST Properties

| Property | Python | PHP | Ruby | Node.js | Parity |
|----------|--------|-----|------|---------|--------|
| `params` | dict | array | IndifferentHash | Record | OK |
| `body` | dict/str (parsed) | mixed (parsed) | `.body` (raw) + `.body_parsed` | unknown (parsed) | INCONSISTENT |
| `headers` | dict (lowercase-hyphen) | array (lowercase) | Hash (underscore) | Record (lowercase) | INCONSISTENT |
| `files` | dict (raw bytes) | array (raw bytes) | Hash (tempfile) | Array (Buffer) | INCONSISTENT |
| `ip` | str | str | str | str | OK |
| `method` | str (uppercase) | string (uppercase) | String (uppercase) | string (uppercase) | OK |
| `path` | str | string | String | string | OK |
| `query` | N/A (merged into params) | array | Hash | Record | MISSING in Python |
| `cookies` | dict | N/A (use $_COOKIE) | Hash | N/A (parse header) | INCONSISTENT |
| `content_type` | str (property) | string (property) | String (attr_reader) | via headers | INCONSISTENT |

## Issues — Request

| # | Issue | Severity | Frameworks |
|---|-------|----------|------------|
| 1 | **Ruby `body` vs `body_parsed`** — others have single parsed `body` | MEDIUM | Ruby |
| 2 | **Ruby header keys use underscores** — others use hyphens | MEDIUM | Ruby |
| 3 | **Ruby `files` uses tempfile** — others use raw bytes/Buffer in `content` | MEDIUM | Ruby |
| 4 | **Node.js `files` is array** — others are dict keyed by field name | MEDIUM | Node.js |
| 5 | **Python has no separate `query` property** — merged into params | LOW | Python |
| 6 | **PHP/Node don't expose `cookies` on request** | LOW | PHP, Node.js |
| 7 | **Node.js no `content_type` property** — must use `headers["content-type"]` | LOW | Node.js |

---

## RESPONSE Methods

| Method | Python | PHP | Ruby | Node.js | Parity |
|--------|--------|-----|------|---------|--------|
| `json(data, status?)` | YES | YES | YES | YES | OK |
| `html(content, status?)` | YES | YES | YES | YES | OK |
| `text(content, status?)` | YES | YES | YES | YES | OK |
| `xml(content, status?)` | YES | NO | YES | NO | MISSING |
| `redirect(url, status?)` | YES (302) | YES (302) | YES (302) | YES (302) | OK |
| `render(template, data)` | YES (sync) | YES (sync) | YES (sync) | YES (async) | OK |
| `file(path, options?)` | YES | YES | YES | YES | OK |
| `status(code)` | setter only | setter only | getter+setter | setter only | INCONSISTENT |
| `header(name, value)` | setter only | setter only | getter+setter | setter only | INCONSISTENT |
| `cookie(name, value, opts)` | YES | YES | YES | YES | OK (naming differs) |
| Callable `response(data)` | YES | YES | NO | YES | MISSING Ruby |

## Issues — Response

| # | Issue | Severity | Frameworks |
|---|-------|----------|------------|
| 1 | **`xml()` missing** in PHP and Node.js | MEDIUM | PHP, Node.js |
| 2 | **Ruby `status()` / `header()` are getter+setter** — others are setter only | LOW | Ruby |
| 3 | **Ruby missing callable `response(data, status, content_type)`** | LOW | Ruby |
| 4 | **Cookie option naming** — `http_only` (Py) vs `httponly` (PHP) vs `httpOnly` (Node) | LOW | All |
| 5 | **Node.js `render()` is async** — others are sync | MEDIUM | Node.js |

## Documentation Gaps

| # | Gap |
|---|-----|
| 1 | Request property differences not documented in any CLAUDE.md |
| 2 | `xml()` availability not flagged |
| 3 | Ruby getter+setter behavior on `status()`/`header()` not documented |
| 4 | Cookie option naming inconsistencies not documented |
