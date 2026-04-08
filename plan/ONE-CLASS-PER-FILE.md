# Plan: One Domain Object Per File — All 4 Frameworks

## Decision (2026-04-09)

Enforce **one domain object per file** across all 4 Tina4 frameworks (PHP, Python, Ruby, Node.js).

### Why

A duplicate `Job` class lived inside `Queue.php` alongside the canonical `Job.php`. When `getBasePath()` was made private on `Queue`, the copy in `Queue.php` still called it — a runtime fatal that tests missed entirely because the two class definitions masked each other.

### Rule

A **domain object** is any class that:
- Has a public API that users call directly
- Could reasonably have its own test file
- Could diverge from colocated classes without the compiler catching it

**Fine to colocate:** Internal metaclasses, simple response wrapper structs, data structs only used by the parent class (e.g. `Route`, `RouteRef`), abstract base classes with a single child in the same file.

---

## Work Required

### PHP (`tina4-php/Tina4/`)

| File | Classes to extract | Target |
|------|-------------------|--------|
| `DevAdmin.php` | `MessageLog`, `RequestInspector`, `ErrorTracker` | `DevAdmin/MessageLog.php`, `DevAdmin/RequestInspector.php`, `DevAdmin/ErrorTracker.php` |
| `WebSocketBackplane.php` | `RedisBackplane`, `NATSBackplane`, `WebSocketBackplaneFactory` | `WebSocket/RedisBackplane.php`, `WebSocket/NATSBackplane.php`, `WebSocket/BackplaneFactory.php` |
| `MCP.php` | `McpServer`, `McpTool`, `McpResource` | `MCP/McpServer.php`, `MCP/McpTool.php`, `MCP/McpResource.php` |

### Python (`tina4_python/`)

| File | Classes to extract | Target |
|------|-------------------|--------|
| `auth/__init__.py` | `AuthMiddleware` | `auth/middleware.py` |
| `core/middleware.py` | `CorsMiddleware`, `RateLimiter`, `SecurityHeadersMiddleware`, `CsrfMiddleware` | `core/middleware/cors.py`, `rate_limiter.py`, `security_headers.py`, `csrf.py` |
| `session/__init__.py` | `FileSessionHandler`, `DatabaseSessionHandler` | `session/file_handler.py`, `session/database_handler.py` |
| `websocket/__init__.py` | `WebSocketConnection`, `WebSocketManager` | `websocket/connection.py`, `websocket/manager.py` |

### Ruby (`lib/tina4/`)

| File | Classes to extract | Target |
|------|-------------------|--------|
| `middleware.rb` | `CorsClassMiddleware`, `RateLimiterMiddleware`, `CsrfMiddleware`, `SecurityHeadersMiddleware` | `middleware/cors.rb`, `rate_limiter.rb`, `csrf.rb`, `security_headers.rb` |
| `websocket.rb` | `WebSocketConnection` | `websocket_connection.rb` |

### Node.js (`packages/core/src/`)

| File | Classes to extract | Target |
|------|-------------------|--------|
| `middleware.ts` | `CorsMiddleware`, `RateLimiterMiddleware`, `SecurityHeadersMiddleware`, `CsrfMiddleware` | `middleware/cors.ts`, `rateLimiter.ts`, `securityHeaders.ts`, `csrf.ts` |
| `session.ts` | `FileSessionHandler`, `RedisSessionHandler` | `sessionHandlers/fileHandler.ts`, `redisHandler.ts` |
| `cache.ts` | `MemoryBackend`, `RedisBackend`, `FileBackend` | `cacheBackends/memoryBackend.ts`, `redisBackend.ts`, `fileBackend.ts` |

---

## Execution Notes

- Each split must maintain all existing imports/exports so nothing breaks
- Run full test suite after each framework's split
- Parity: split must happen in all 4 frameworks in the same session (per parity rule)
- Middleware splits are the highest value — `CsrfMiddleware` and auth bugs showed these diverge
- **Do not** split at once — do one framework at a time, run tests, commit, move on
