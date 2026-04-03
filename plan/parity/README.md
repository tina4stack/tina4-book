# Tina4 v3 — API Parity Audit

> **Generated:** 2026-04-03 | **Version:** v3.10.67
> **Scope:** Every developer-facing method across Python, PHP, Ruby, Node.js

## Audit Files

| Class | File | Status | Critical Issues |
|-------|------|--------|----------------|
| [ORM](parity-orm.md) | parity-orm.md | 80% | PHP methods are instance not static; return types differ |
| [Router](parity-router.md) | parity-router.md | 99% | Minor naming; Ruby param order reversed in match |
| [Database](parity-database.md) | parity-database.md | 95% | execute() return types differ |
| [Auth](parity-auth.md) | parity-auth.md | 80% | Ruby bcrypt vs PBKDF2; Node hash delimiter; Python minutes vs seconds |
| [Session](parity-session.md) | parity-session.md | 85% | Node duplicate clear(); flash API split; regenerate return |
| [Template/Frond](parity-template.md) | parity-template.md | 75% | Ruby/Node missing render_string, add_filter, sandbox |
| [Request/Response](parity-request-response.md) | parity-request-response.md | 90% | Ruby body split; files format; xml() missing in PHP/Node |
| [Queue](parity-queue.md) | parity-queue.md | 75% | PHP naming; Node missing backends; consume pattern |
| [WebSocket](parity-websocket.md) | parity-websocket.md | 60% | PHP has NO WebSocket; event naming |
| [Remaining](parity-remaining.md) | parity-remaining.md | 90% | Ruby/Node missing Api Client; Node missing emit_async |

## Top Critical Issues (Fix First)

1. **PHP WebSocket server missing entirely**
2. **Ruby/Node.js outbound HTTP client (Api class) missing**
3. **Auth: Ruby uses bcrypt (not PBKDF2), Node.js hash delimiter is `:` not `$`**
4. **Auth: Python expires_in is minutes, others use seconds**
5. **ORM: PHP query methods are instance methods (should be static)**
6. **ORM: save/delete/all return types inconsistent across frameworks**
7. **Template: Ruby/Node missing render_string, add_filter, sandbox**
8. **Node.js Queue missing RabbitMQ/Kafka/MongoDB backends**
9. **Session: Node.js duplicate clear() method (bug)**
10. **Node.js Events missing emit_async()**

## Classes at Excellent Parity (No Action Needed)

- HtmlElement (99%)
- Seeder/FakeData (99%)
- i18n/Localization (95%)
- Events (95% — just Node missing emit_async)
