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

| # | Issue | Severity | Status |
|---|-------|----------|--------|
| 1 | Ruby `body` vs `body_parsed` | MEDIUM | BY DESIGN — Rack idiom |
| 2 | Ruby header keys underscores | MEDIUM | BY DESIGN — Rack normalizes |
| 3 | Ruby `files` uses tempfile | MEDIUM | BY DESIGN — Rack manages temps |
| 4 | ~~Node.js `files` is array~~ | MEDIUM | FIXED — dict keyed by fieldName |
| 5 | ~~Python no `query` property~~ | LOW | FIXED — `query` added separate from `params` |
| 6 | ~~PHP/Node no `cookies`~~ | LOW | FIXED — parsed from Cookie header |
| 7 | ~~Node no `contentType`~~ | LOW | FIXED — contentType property added |

---

## RESPONSE Methods

| Method | Python | PHP | Ruby | Node.js | Parity |
|--------|--------|-----|------|---------|--------|
| `json(data, status?)` | YES | YES | YES | YES | OK |
| `html(content, status?)` | YES | YES | YES | YES | OK |
| `text(content, status?)` | YES | YES | YES | YES | OK |
| `xml(content, status?)` | YES | YES | YES | YES | OK |
| `redirect(url, status?)` | YES (302) | YES (302) | YES (302) | YES (302) | OK |
| `render(template, data)` | YES (sync) | YES (sync) | YES (sync) | YES (async) | OK |
| `file(path, options?)` | YES | YES | YES | YES | OK |
| `status(code)` | setter only | setter only | getter+setter | setter only | INCONSISTENT |
| `header(name, value)` | setter only | setter only | getter+setter | setter only | INCONSISTENT |
| `cookie(name, value, opts)` | YES | YES | YES | YES | OK (naming differs) |
| Callable `response(data)` | YES | YES | YES (call) | YES | OK |
| `stream(generator)` | YES | YES | YES | YES | OK |

## Issues — Response

| # | Issue | Severity | Status |
|---|-------|----------|--------|
| 1 | ~~`xml()` missing in PHP/Node~~ | MEDIUM | FIXED — added to both |
| 2 | Ruby `status()`/`header()` getter+setter | LOW | BY DESIGN — Ruby idiom |
| 3 | ~~Ruby missing callable response~~ | LOW | FIXED — `response.call(data, status, content_type)` |
| 4 | Cookie option naming differs | LOW | BY DESIGN — language conventions |
| 5 | Node.js `render()` async | MEDIUM | BY DESIGN — Node is async |

## Documentation Gaps

| # | Gap |
|---|-----|
| 1 | Request property differences not documented in any CLAUDE.md |
| 2 | `xml()` availability not flagged |
| 3 | Ruby getter+setter behavior on `status()`/`header()` not documented |
| 4 | Cookie option naming inconsistencies not documented |
