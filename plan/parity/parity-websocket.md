# Parity Audit: WebSocket

> **Generated:** 2026-04-03 | **Version:** v3.10.67

## Status: HIGH PARITY (95%) — audit corrected, PHP has full WebSocket

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

| # | Issue | Severity | Status |
|---|-------|----------|--------|
| 1 | ~~PHP has NO WebSocket server~~ | CRITICAL | **AUDIT ERROR** — PHP has full WS: WebSocket.php, WebSocketConnection.php, WebSocketBackplane.php |
| 2 | ~~Event naming inconsistent~~ | MEDIUM | FIXED — all use `open/message/close/error`. Python added `on("open", handler)` alongside decorators. Node changed `connection` → `open`. |
| 3 | ~~Connection missing ip/headers/params~~ | MEDIUM | FIXED — PHP: added ip, headers, params to WebSocketConnection. Node: added ip, headers to interface. |
| 4 | Node.js missing NATS backplane | LOW | PARKED |
| 5 | Backplane config style differs | LOW | BY DESIGN — env vars vs classes |
