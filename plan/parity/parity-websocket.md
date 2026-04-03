# Parity Audit: WebSocket

> **Generated:** 2026-04-03 | **Version:** v3.10.67

## Status: LOW PARITY (60%) — PHP missing entirely

---

## Server Implementation

| Feature | Python | PHP | Ruby | Node.js |
|---------|--------|-----|------|---------|
| WebSocket server | YES | **NO** | YES | YES |
| Route registration | `@websocket(path)` | N/A | `Router.websocket(path)` | `websocket(path, handler)` |
| Broadcast | YES | N/A | YES | YES |
| Rooms/channels | YES | N/A | YES | YES |
| Backplane (Redis) | YES | N/A | YES | YES (env-based) |
| Backplane (NATS) | YES | N/A | YES | NO |

## Event Handler Naming

| Event | Python | PHP | Ruby | Node.js |
|-------|--------|-----|------|---------|
| Message received | `on_message` | N/A | `on(:message)` | `on("message")` |
| Client connected | `on_connect` | N/A | `on(:open)` | `on("connection")` |
| Client disconnected | `on_close` | N/A | `on(:close)` | `on("close")` |
| Error | `on_error` | N/A | `on(:error)` | `on("error")` |

- [ ] **PARITY ISSUE:** Event names differ — `on_connect` vs `on(:open)` vs `on("connection")`

## Connection Properties

| Property | Python | PHP | Ruby | Node.js |
|----------|--------|-----|------|---------|
| `id` | YES | N/A | YES | YES |
| `path` | YES | N/A | YES | YES |
| `ip` | YES | N/A | NO | YES |
| `headers` | YES | N/A | NO | NO |
| `params` | YES | N/A | NO | NO |

## Issues to Fix

| # | Issue | Severity | Frameworks |
|---|-------|----------|------------|
| 1 | **PHP has NO WebSocket server** | CRITICAL | PHP |
| 2 | **Event handler naming inconsistent** — connect/open/connection | MEDIUM | All |
| 3 | **Ruby/Node missing connection headers and params** | MEDIUM | Ruby, Node.js |
| 4 | **Node.js missing NATS backplane** | LOW | Node.js |
| 5 | **Backplane config style** — Python/Ruby use classes, Node uses env vars | LOW | Node.js |

## Documentation Gaps

| # | Gap |
|---|-----|
| 1 | PHP WebSocket gap not documented as known limitation |
| 2 | Event name differences not flagged anywhere |
| 3 | Connection property availability not compared |
