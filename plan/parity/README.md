# Tina4 v3 — API Parity Audit

> **Generated:** 2026-04-03 | **Updated:** 2026-04-03 | **Version:** v3.10.67+
> **Scope:** Every developer-facing method across Python, PHP, Ruby, Node.js

## Final Status

| Class | File | Status | Notes |
|-------|------|--------|-------|
| [ORM](parity-orm.md) | parity-orm.md | **100%** | All 12 issues fixed |
| [Router](parity-router.md) | parity-router.md | **99%** | 2 minor by-design |
| [Database](parity-database.md) | parity-database.md | **100%** | All 4 issues fixed |
| [Auth](parity-auth.md) | parity-auth.md | **100%** | 7 fixed, RS256 parked |
| [Session](parity-session.md) | parity-session.md | **100%** | 6 fixed, 2 by-design |
| [Template/Frond](parity-template.md) | parity-template.md | **100%** | Audit was wrong — all methods exist |
| [Request/Response](parity-request-response.md) | parity-request-response.md | **100%** | 6 fixed, 5 by-design |
| [Queue](parity-queue.md) | parity-queue.md | **100%** | Audit was wrong — consume poll_interval only real fix |
| [WebSocket](parity-websocket.md) | parity-websocket.md | **100%** | Audit was wrong — PHP has full WS. Events + props fixed |
| [Remaining](parity-remaining.md) | parity-remaining.md | **98%** | GraphQL/WSDL/Api/Swagger/i18n/Html/Seeder all 100%. Node emit_async TODO |

## Issues Fixed This Session

1. ~~ORM: return types (save, all, select, where)~~ — self/false, arrays
2. ~~ORM: PHP count() no params~~ — added
3. ~~ORM: Node findAll/where missing~~ — renamed to all(), where() added
4. ~~ORM: scope() semantics~~ — all register reusable method
5. ~~ORM: toArray/toDict/toAssoc~~ — standardized
6. ~~Auth: Ruby bcrypt~~ — PBKDF2
7. ~~Auth: Node hash delimiter~~ — $ with backward compat
8. ~~Auth: expires_in units~~ — all minutes
9. ~~Auth: API key fallback~~ — all frameworks
10. ~~Auth: env SECRET fallback~~ — all frameworks
11. ~~Session: Node duplicate clear~~ — removed
12. ~~Session: flash dual-mode~~ — all frameworks
13. ~~Session: cookieHeader~~ — all frameworks
14. ~~Database: execute() return type~~ — bool/DatabaseResult
15. ~~Database: get_last_id/get_error~~ — all frameworks
16. ~~WebSocket: event naming~~ — all use open/message/close/error
17. ~~WebSocket: connection properties~~ — ip/headers/params added
18. ~~Request: Node files dict~~ — keyed by fieldName
19. ~~Request: Python query property~~ — added
20. ~~Request: cookies~~ — PHP/Node added
21. ~~Response: xml()~~ — PHP/Node added
22. ~~Response: Ruby callable~~ — response.call() added
23. ~~Queue: consume poll_interval~~ — all frameworks
24. ~~GraphQL: schema_sdl()~~ — all frameworks
25. ~~GraphQL: introspect()~~ — all frameworks
26. ~~WSDL: Node DOM parser~~ — replaced regex
27. ~~File upload: Python base64~~ — removed, raw bytes
28. ~~File upload: api.upload()~~ — tina4-js
29. ~~load() API~~ — instance method, selectOne params, returns bool
30. ~~CLAUDE.md~~ — all 4 updated with correct stubs

## Remaining TODO

1. **Node.js Events missing `emit_async()`** — low priority
2. **Ruby i18n uses YAML** — by design
3. **Python RS256** — parked (install cryptography module)

## Audit Errors Discovered

The initial automated audit had significant false negatives:
- PHP WebSocket was flagged as missing — it exists (full RFC 6455)
- Ruby/Node Api Client flagged as missing — both exist (full HTTP client)
- Node Queue backends flagged as missing — all 4 backends exist
- Template methods flagged as missing in Ruby/Node — Frond class has them all
- Queue method naming flagged — all use push/pop/consume
