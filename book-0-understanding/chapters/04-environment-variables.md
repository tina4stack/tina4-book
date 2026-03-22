# Chapter 4: Environment Variables

Every piece of Tina4 configuration lives in a `.env` file at the root of your project. This chapter is the complete reference for every environment variable the framework recognizes.

## How .env Files Work

A `.env` file is a plain text file with key-value pairs:

```env
# This is a comment
DATABASE_URL=sqlite:///data/app.db
TINA4_DEBUG=true
TINA4_PORT=7145

# Blank lines are ignored

# Values with spaces need quotes
TINA4_MAIL_FROM="My App <noreply@example.com>"

# No quotes needed for simple values
JWT_SECRET=my-secret-key-change-in-production
```

### Rules

1. One variable per line.
2. Format is `KEY=VALUE` -- no spaces around the `=`.
3. Lines starting with `#` are comments.
4. Blank lines are ignored.
5. Values can optionally be wrapped in double quotes (`"value"`) or single quotes (`'value'`).
6. There is no variable interpolation -- `$OTHER_VAR` is treated as a literal string.

### The .env File Is Not Committed to Git

The `.env` file contains secrets (database passwords, JWT keys, API tokens). It must be in `.gitignore`. When you run `tina4 init`, the generated `.gitignore` already excludes it.

Instead, commit a `.env.example` file with placeholder values that document what the application expects:

```env
# .env.example -- copy to .env and fill in real values
DATABASE_URL=sqlite:///data/app.db
TINA4_DEBUG=false
JWT_SECRET=CHANGE_ME
TINA4_MAIL_HOST=smtp.example.com
TINA4_MAIL_USERNAME=
TINA4_MAIL_PASSWORD=
```

## The Priority Chain

Tina4 resolves every configurable value using a three-level priority chain:

```
Constructor argument  >  .env file  >  Hardcoded default
```

This means:

1. **Constructor argument wins.** If you pass a value directly in code, it overrides everything else.
2. **.env file is second.** If no code override exists, the value from `.env` is used.
3. **Default is last.** If neither code nor `.env` specifies a value, the framework's built-in default applies.

### Example

```env
# .env
TINA4_PORT=8080
```

```php
// Scenario 1: Constructor override
$app = new Tina4\App(["port" => 9000]);
// Result: server starts on port 9000 (constructor wins)

// Scenario 2: No constructor override
$app = new Tina4\App();
// Result: server starts on port 8080 (.env wins)

// Scenario 3: No .env value, no constructor
// (TINA4_PORT line removed from .env)
$app = new Tina4\App();
// Result: server starts on port 7145 (default wins)
```

This pattern is consistent across all 60+ variables. No exceptions.

## is_truthy() -- Boolean Values

Many environment variables are booleans (on/off toggles). Since `.env` files only contain strings, Tina4 uses `is_truthy()` to interpret them. The following values are treated as `true`:

| Value | Treated as |
|-------|-----------|
| `true` | `true` |
| `True` | `true` |
| `TRUE` | `true` |
| `1` | `true` |
| `yes` | `true` |
| `Yes` | `true` |
| `YES` | `true` |
| `on` | `true` |
| `On` | `true` |
| `ON` | `true` |

**Everything else is `false`**, including:

| Value | Treated as |
|-------|-----------|
| `false` | `false` |
| `0` | `false` |
| `no` | `false` |
| `off` | `false` |
| _(empty string)_ | `false` |
| _(variable not set)_ | `false` |

This means you can write whichever style you prefer:

```env
# All of these enable debug mode
TINA4_DEBUG=true
TINA4_DEBUG=1
TINA4_DEBUG=yes
TINA4_DEBUG=on
```

**Gotcha:** The string `"false"` is not truthy. But the string `"False"` is also not truthy. And the string `"FALSE"` is also not truthy. This works correctly because `is_truthy()` only returns `true` for the specific values listed above. Everything else -- including typos like `"tru"` or `"yess"` -- is `false`.

---

## Complete .env Reference

### Debug and Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `TINA4_DEBUG` | `false` | Master toggle for dev mode. Enables debug overlay, full stack traces, Swagger UI, live reload, query logging. **Never set to `true` in production.** |
| `TINA4_PORT` | `7145` | HTTP server port. Override with `--port` CLI flag. |
| `TINA4_HOST` | `0.0.0.0` | Bind address. `0.0.0.0` listens on all network interfaces. Use `127.0.0.1` to restrict to localhost only. |

### Database

| Variable | Default | Description |
|----------|---------|-------------|
| `DATABASE_URL` | `sqlite:///data/app.db` | Connection string. Format depends on the database driver (see below). |
| `DATABASE_USERNAME` | _(from URL)_ | Override the username embedded in `DATABASE_URL`. Useful when the password contains special characters that break URL parsing. |
| `DATABASE_PASSWORD` | _(from URL)_ | Override the password embedded in `DATABASE_URL`. |

**Connection string formats:**

```env
# SQLite (default -- no credentials needed)
DATABASE_URL=sqlite:///data/app.db

# PostgreSQL
DATABASE_URL=postgresql://user:password@hostname:5432/database_name

# MySQL / MariaDB
DATABASE_URL=mysql://user:password@hostname:3306/database_name

# Microsoft SQL Server
DATABASE_URL=mssql://user:password@hostname:1433/database_name

# Firebird
DATABASE_URL=firebird://user:password@hostname:3050/path/to/database.fdb

# ODBC (uses a configured DSN)
DATABASE_URL=odbc://MY_DSN_NAME

# MongoDB (SQL queries are auto-translated)
DATABASE_URL=mongodb://user:password@hostname:27017/database_name
```

**Gotcha:** If your database password contains special characters like `@`, `#`, `:`, or `/`, URL-encode them in the connection string (`@` becomes `%40`), or use `DATABASE_USERNAME` and `DATABASE_PASSWORD` to pass credentials separately:

```env
DATABASE_URL=postgresql://hostname:5432/mydb
DATABASE_USERNAME=admin
DATABASE_PASSWORD=p@ss#word/123
```

### DB Query Cache

| Variable | Default | Description |
|----------|---------|-------------|
| `TINA4_DB_CACHE` | `true` | Enable in-memory caching of database query results. Identical queries within the TTL return cached results instead of hitting the database. |
| `TINA4_DB_CACHE_TTL` | `60` | Cache time-to-live in seconds. After this period, cached results are discarded and the next query hits the database. |

Write operations (INSERT, UPDATE, DELETE) automatically invalidate relevant cache entries.

### Logging

| Variable | Default | Description |
|----------|---------|-------------|
| `TINA4_LOG_LEVEL` | `ALL` | Minimum log level to output to console. Options: `ALL`, `DEBUG`, `INFO`, `WARNING`, `ERROR`. File logs always write all levels regardless of this setting. |
| `TINA4_LOG_DIR` | `logs` | Directory for log files. Relative to the project root. |
| `TINA4_LOG_FILE` | `tina4.log` | Main log file name. |
| `TINA4_LOG_MAX_SIZE` | `10M` | Maximum log file size before rotation. Supports `K` (kilobytes), `M` (megabytes), `G` (gigabytes). |
| `TINA4_LOG_ROTATE` | `daily` | Rotation schedule. Options: `daily`, `hourly`, `size-only`. |
| `TINA4_LOG_RETAIN` | `30` | Number of days to keep rotated log files. Older files are deleted. |
| `TINA4_LOG_COMPRESS` | `true` | Gzip log files older than 2 days to save disk space. |
| `TINA4_LOG_SEPARATE_ERRORS` | `true` | Write errors and exceptions to a separate `error.log` file in addition to the main log. |
| `TINA4_LOG_QUERY` | `false` | Log all SQL queries to `query.log` with timing. Useful in development, costly in production. |
| `TINA4_LOG_ACCESS` | `false` | Write HTTP access logs in standard format to `access.log`. |

**Log file structure:**

```
logs/
├── tina4.log                    # Current log file
├── tina4.2026-03-21.log         # Yesterday's log (rotated)
├── tina4.2026-03-20.log         # 2 days ago
├── tina4.2026-03-19.log.gz      # 3+ days ago (compressed)
├── error.log                    # Current errors only
├── error.2026-03-21.log         # Yesterday's errors
└── query.log                    # SQL queries (debug mode only)
```

### CORS (Cross-Origin Resource Sharing)

| Variable | Default | Description |
|----------|---------|-------------|
| `CORS_ORIGINS` | `*` | Comma-separated list of allowed origins. Use `*` to allow all origins (development only). In production, list your actual domains. |
| `CORS_METHODS` | `GET,POST,PUT,DELETE` | Comma-separated HTTP methods allowed in cross-origin requests. |
| `CORS_HEADERS` | `Content-Type,Authorization` | Comma-separated headers the client is allowed to send. |
| `CORS_CREDENTIALS` | `true` | Whether the browser should send cookies and auth headers in cross-origin requests. |
| `CORS_MAX_AGE` | `86400` | How long (in seconds) the browser caches preflight (OPTIONS) responses. `86400` = 24 hours. |

**Example for production:**

```env
CORS_ORIGINS=https://myapp.com,https://admin.myapp.com
CORS_METHODS=GET,POST,PUT,DELETE
CORS_HEADERS=Content-Type,Authorization,X-Request-ID
CORS_CREDENTIALS=true
CORS_MAX_AGE=86400
```

**Gotcha:** If you set `CORS_ORIGINS=*` (allow all origins) and `CORS_CREDENTIALS=true` simultaneously, browsers will reject the response. When credentials are enabled, you must list specific origins.

### Rate Limiter

| Variable | Default | Description |
|----------|---------|-------------|
| `TINA4_RATE_LIMIT` | `60` | Maximum requests per window per IP address. |
| `TINA4_RATE_WINDOW` | `60` | Window duration in seconds. Default: 60 requests per 60 seconds (1 per second average). |

The rate limiter adds these headers to every response:

```
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 45
X-RateLimit-Reset: 1679512800
```

When the limit is exceeded, the server returns `429 Too Many Requests` with a `Retry-After` header.

You can override the rate limit on individual routes in code:

```php
Route::get("/api/expensive-operation", $handler)->rateLimit(10, 60);
// This route: 10 requests per 60 seconds
// All other routes: default from .env
```

### Auth (JWT)

| Variable | Default | Description |
|----------|---------|-------------|
| `JWT_SECRET` | _(required if auth used)_ | Secret key for HMAC-SHA256 (HS256) signing. Must be a long, random string. **Never commit this to git.** |
| `JWT_ALGORITHM` | `HS256` | JWT signing algorithm. Options: `HS256` (symmetric, simpler), `RS256` (asymmetric, uses key files in `secrets/`). |
| `JWT_EXPIRY_DAYS` | `7` | Default token expiration period in days. Tokens issued without an explicit expiry use this value. |

**Gotcha:** If you use `.secure()` on any route without setting `JWT_SECRET`, the framework will reject all requests to that route with `500 Internal Server Error` because it cannot validate tokens.

### Sessions

| Variable | Default | Description |
|----------|---------|-------------|
| `TINA4_SESSION_HANDLER` | `file` | Session storage backend. Options: `file`, `redis`, `valkey`, `mongo`, `database`. |
| `SESSION_SECRET` | _(required)_ | Secret key for signing session cookies. Must be a long, random string. |
| `SESSION_TTL` | `3600` | Session expiry in seconds. Default: 1 hour. |
| `REDIS_URL` | `redis://localhost:6379` | Redis connection URL. Used when `TINA4_SESSION_HANDLER=redis`. Also used by the response cache backend. |
| `MONGODB_URL` | `mongodb://localhost:27017` | MongoDB connection URL. Used when `TINA4_SESSION_HANDLER=mongo`. |

### Queue

| Variable | Default | Description |
|----------|---------|-------------|
| `TINA4_QUEUE_BACKEND` | `database` | Queue storage backend. Options: `database` (uses the connected DB), `rabbitmq`, `kafka`. |
| `QUEUE_DRIVER` | `database` | Alias for `TINA4_QUEUE_BACKEND`. Either variable works. |
| `QUEUE_FALLBACK_DRIVER` | _(none)_ | Fallback backend if the primary is down. Same options as `QUEUE_DRIVER`. |
| `RABBITMQ_URL` | _(none)_ | AMQP connection URL when using RabbitMQ. |
| `KAFKA_BROKERS` | _(none)_ | Comma-separated Kafka broker addresses. |
| `KAFKA_GROUP_ID` | `tina4-workers` | Kafka consumer group ID. |
| `QUEUE_FAILOVER_TIMEOUT` | `300` | Seconds without a successful pop before switching to the fallback backend. |
| `QUEUE_FAILOVER_DEPTH` | `10000` | Maximum queue depth before triggering failover. |
| `QUEUE_FAILOVER_ERROR_RATE` | `50` | Error rate percentage (0-100) that triggers failover. |
| `QUEUE_CIRCUIT_BREAKER_THRESHOLD` | `5` | Number of consecutive failures before the circuit breaker trips (stops trying the primary backend). |
| `QUEUE_CIRCUIT_BREAKER_COOLDOWN` | `30` | Seconds to wait before retrying the primary backend after the circuit breaker trips. |

**Common setup for development:**

```env
# Database queue -- works out of the box, no additional services needed
TINA4_QUEUE_BACKEND=database
```

**Common setup for production:**

```env
TINA4_QUEUE_BACKEND=rabbitmq
RABBITMQ_URL=amqp://user:password@rabbitmq-host:5672/vhost
QUEUE_FALLBACK_DRIVER=database
```

### Response Cache

| Variable | Default | Description |
|----------|---------|-------------|
| `TINA4_CACHE_BACKEND` | `memory` | Cache storage for route-level response caching. Options: `memory` (in-process, cleared on restart), `redis` (shared, persistent), `file` (disk-based). |
| `TINA4_CACHE_TTL` | `300` | Default cache TTL in seconds for routes with `.cache()`. Override per-route with `.cache(ttl)`. |
| `TINA4_CACHE_MAX_ENTRIES` | `1000` | Maximum number of cached responses (memory backend only). Oldest entries are evicted when the limit is reached. |

### Response Compression

| Variable | Default | Description |
|----------|---------|-------------|
| `TINA4_COMPRESS` | `true` | Enable gzip response compression. |
| `TINA4_COMPRESS_THRESHOLD` | `1024` | Minimum response body size (in bytes) before compression kicks in. Responses smaller than this are sent uncompressed. |
| `TINA4_COMPRESS_LEVEL` | `6` | gzip compression level (1-9). Lower = faster, larger output. Higher = slower, smaller output. `6` is a good balance. |
| `TINA4_MINIFY_HTML` | `true` | Strip HTML comments and collapse whitespace in production mode. Only active when `TINA4_DEBUG=false`. |

### Messenger (Email / SMTP)

| Variable | Default | Description |
|----------|---------|-------------|
| `TINA4_MAIL_HOST` | _(none)_ | SMTP server hostname (e.g., `smtp.gmail.com`, `smtp.sendgrid.net`). |
| `TINA4_MAIL_PORT` | `587` | SMTP port. Common values: `587` (TLS), `465` (SSL), `25` (unencrypted). |
| `TINA4_MAIL_USERNAME` | _(none)_ | SMTP authentication username. |
| `TINA4_MAIL_PASSWORD` | _(none)_ | SMTP authentication password. |
| `TINA4_MAIL_FROM` | _(none)_ | Default sender address for outgoing emails. Can include a display name: `"My App <noreply@example.com>"`. |
| `TINA4_MAIL_ENCRYPTION` | `tls` | Connection encryption. Options: `tls`, `ssl`, `none`. Use `none` only for local development mail servers (like MailHog). |

### Localization (i18n)

| Variable | Default | Description |
|----------|---------|-------------|
| `TINA4_LANGUAGE` | `en` | Default locale. Determines which translation file (`src/locales/{locale}.json`) is loaded. |

The fallback chain for translations: requested locale > `TINA4_LANGUAGE` > `en` > raw key.

### WebSocket

| Variable | Default | Description |
|----------|---------|-------------|
| `TINA4_WS_MAX_FRAME_SIZE` | `1048576` | Maximum WebSocket frame size in bytes (default: 1MB). |
| `TINA4_WS_MAX_CONNECTIONS` | `10000` | Maximum concurrent WebSocket connections. |
| `TINA4_WS_PING_INTERVAL` | `30` | Server sends a ping frame every N seconds to keep connections alive. |
| `TINA4_WS_PING_TIMEOUT` | `10` | If the client does not respond to a ping within N seconds, the connection is closed. |

### Dev Admin Console

| Variable | Default | Description |
|----------|---------|-------------|
| `TINA4_CONSOLE` | `false` | Enable the admin console at `/tina4/console`. |
| `TINA4_CONSOLE_TOKEN` | _(required)_ | Authentication token for console access. There is no default -- if you enable the console without setting a token, it is inaccessible. |
| `TINA4_CONSOLE_PATH` | `/tina4/console` | URL path for the admin console. Change this if the default conflicts with your routes. |

### Error Handling (.broken Files)

| Variable | Default | Description |
|----------|---------|-------------|
| `TINA4_BROKEN_DIR` | `data/.broken` | Directory where `.broken` marker files are created when unhandled exceptions occur in production. |
| `TINA4_BROKEN_THRESHOLD` | `1` | Number of `.broken` files that causes the health check (`GET /health`) to return `503 Service Unavailable`. Container orchestrators (Kubernetes, Docker Swarm) use this to restart unhealthy containers. |
| `TINA4_BROKEN_AUTO_RESOLVE` | `0` | Automatically delete `.broken` files after N seconds. `0` means never auto-delete (requires manual resolution via the admin console or by deleting the files). |
| `TINA4_BROKEN_MAX_FILES` | `100` | Maximum number of `.broken` files to keep. Oldest are deleted when the limit is reached. |

---

## Minimal .env for Development

If you are just getting started, this is all you need:

```env
TINA4_DEBUG=true
```

Everything else uses sensible defaults:

- Port `7145`
- SQLite database at `data/app.db`
- File-based sessions
- Database-backed queue
- In-memory response cache
- gzip compression enabled
- All CORS origins allowed
- 60 requests/minute rate limit

## Minimal .env for Production

```env
TINA4_DEBUG=false
DATABASE_URL=postgresql://app_user:strong_password@db-host:5432/myapp
JWT_SECRET=a-very-long-random-string-at-least-32-characters
SESSION_SECRET=another-very-long-random-string
CORS_ORIGINS=https://myapp.com
TINA4_MAIL_HOST=smtp.sendgrid.net
TINA4_MAIL_PORT=587
TINA4_MAIL_USERNAME=apikey
TINA4_MAIL_PASSWORD=SG.xxxxx
TINA4_MAIL_FROM="My App <noreply@myapp.com>"
```

## Full .env Template

Copy this to your `.env.example` file as a starting point:

```env
# =============================================================================
# Tina4 Environment Configuration
# Copy this file to .env and fill in your values
# =============================================================================

# --- Debug & Server ---
TINA4_DEBUG=false
TINA4_PORT=7145
TINA4_HOST=0.0.0.0

# --- Database ---
DATABASE_URL=sqlite:///data/app.db
# DATABASE_USERNAME=
# DATABASE_PASSWORD=

# --- Logging ---
TINA4_LOG_LEVEL=ALL
TINA4_LOG_DIR=logs
TINA4_LOG_FILE=tina4.log
TINA4_LOG_MAX_SIZE=10M
TINA4_LOG_ROTATE=daily
TINA4_LOG_RETAIN=30
TINA4_LOG_COMPRESS=true
TINA4_LOG_SEPARATE_ERRORS=true
TINA4_LOG_QUERY=false
TINA4_LOG_ACCESS=false

# --- CORS ---
CORS_ORIGINS=*
CORS_METHODS=GET,POST,PUT,DELETE
CORS_HEADERS=Content-Type,Authorization
CORS_CREDENTIALS=true
CORS_MAX_AGE=86400

# --- Rate Limiting ---
TINA4_RATE_LIMIT=60
TINA4_RATE_WINDOW=60

# --- Auth (JWT) ---
JWT_SECRET=CHANGE_ME
JWT_ALGORITHM=HS256
JWT_EXPIRY_DAYS=7

# --- Sessions ---
TINA4_SESSION_HANDLER=file
SESSION_SECRET=CHANGE_ME
SESSION_TTL=3600
# REDIS_URL=redis://localhost:6379
# MONGODB_URL=mongodb://localhost:27017

# --- Queue ---
TINA4_QUEUE_BACKEND=database
# QUEUE_FALLBACK_DRIVER=
# RABBITMQ_URL=
# KAFKA_BROKERS=
# KAFKA_GROUP_ID=tina4-workers
# QUEUE_FAILOVER_TIMEOUT=300
# QUEUE_FAILOVER_DEPTH=10000
# QUEUE_FAILOVER_ERROR_RATE=50
# QUEUE_CIRCUIT_BREAKER_THRESHOLD=5
# QUEUE_CIRCUIT_BREAKER_COOLDOWN=30

# --- Response Cache ---
TINA4_CACHE_BACKEND=memory
TINA4_CACHE_TTL=300
TINA4_CACHE_MAX_ENTRIES=1000

# --- DB Query Cache ---
TINA4_DB_CACHE=true
TINA4_DB_CACHE_TTL=60

# --- Compression ---
TINA4_COMPRESS=true
TINA4_COMPRESS_THRESHOLD=1024
TINA4_COMPRESS_LEVEL=6
TINA4_MINIFY_HTML=true

# --- Email (SMTP) ---
# TINA4_MAIL_HOST=smtp.example.com
# TINA4_MAIL_PORT=587
# TINA4_MAIL_USERNAME=
# TINA4_MAIL_PASSWORD=
# TINA4_MAIL_FROM="App Name <noreply@example.com>"
# TINA4_MAIL_ENCRYPTION=tls

# --- Localization ---
TINA4_LANGUAGE=en

# --- WebSocket ---
TINA4_WS_MAX_FRAME_SIZE=1048576
TINA4_WS_MAX_CONNECTIONS=10000
TINA4_WS_PING_INTERVAL=30
TINA4_WS_PING_TIMEOUT=10

# --- Dev Admin Console ---
TINA4_CONSOLE=false
# TINA4_CONSOLE_TOKEN=
# TINA4_CONSOLE_PATH=/tina4/console

# --- Error Handling ---
TINA4_BROKEN_DIR=data/.broken
TINA4_BROKEN_THRESHOLD=1
TINA4_BROKEN_AUTO_RESOLVE=0
TINA4_BROKEN_MAX_FILES=100
```

## Summary

| Count | Category |
|-------|----------|
| 3 | Debug and server configuration |
| 3 | Database |
| 2 | DB query cache |
| 10 | Logging |
| 5 | CORS |
| 2 | Rate limiter |
| 3 | Auth (JWT) |
| 5 | Sessions |
| 10 | Queue |
| 3 | Response cache |
| 4 | Compression |
| 6 | Messenger (email) |
| 1 | Localization |
| 4 | WebSocket |
| 3 | Dev admin console |
| 4 | Error handling |
| **68** | **Total** |

Every variable follows the same priority chain: constructor > `.env` > default. Every boolean variable is interpreted by `is_truthy()`. Every variable has a sensible default that works for development without any configuration.
