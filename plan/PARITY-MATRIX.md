# Tina4 — Cross-Framework Parity Matrix

Last updated: 2026-04-02 | Version: 3.10.55 (pending release)

## Feature Parity

| Feature | Python | PHP | Ruby | Node.js |
|---------|--------|-----|------|---------|
| **Core HTTP** | | | | |
| Router (GET/POST/PUT/PATCH/DELETE/ANY) | Yes | Yes | Yes | Yes |
| Path params ({id:int}, {price:float}) | Yes | Yes | Yes | Yes |
| Wildcard routes (*) | Yes | Yes | Yes | Yes |
| Route grouping | Yes | Yes | Yes | Yes |
| Route discovery (auto-load src/) | Yes | Yes | Yes | Yes |
| Server (built-in) | Yes | Yes | Yes | Yes |
| Request object | Yes | Yes | Yes | Yes |
| Response object | Yes | Yes | Yes | Yes |
| Static file serving | Yes | Yes | Yes | Yes |
| CORS middleware (proper origin matching) | Yes | Yes | Yes | Yes |
| Health endpoint | Yes | Yes | Yes | Yes |
| TINA4_DEBUG env var | Yes | Yes | Yes | Yes |
| TINA4_NO_BROWSER + --no-browser | Yes | Yes | Yes | Yes |
| TINA4_NO_RELOAD + --no-reload | Yes | Yes | Yes | Yes |
| Auto AI dual-port (port+1) | Yes | Yes | Yes | Yes |
| TINA4_NO_AI_PORT | Yes | Yes | Yes | Yes |
| --production flag | Yes | Yes | Yes | Yes |
| Star wiggle animation | Yes | Yes | Yes | Yes |
| **Auth & Security** | | | | |
| JWT auth (zero-dep) | Yes | Yes | Yes | Yes |
| Password hashing | Yes | Yes | Yes | Yes |
| Form token (CSRF) | Yes | Yes | Yes | Yes |
| CSRF middleware | Yes | Yes | Yes | Yes |
| Rate limiter | Yes | Yes | Yes | Yes |
| Security headers middleware | Yes | Yes | Yes | Yes |
| Validator | Yes | Yes | Yes | Yes |
| noauth / secured decorators | Yes | Yes | Yes | Yes |
| **Database** | | | | |
| URL-based multi-driver connection | Yes | Yes | Yes | Yes |
| SQLite driver | Yes | Yes | Yes | Yes |
| PostgreSQL driver | Yes | Yes | Yes | Yes |
| MySQL driver | Yes | Yes | Yes | Yes |
| MSSQL driver | Yes | Yes | Yes | Yes |
| Firebird driver | Yes | Yes | Yes | Yes |
| MongoDB driver | Yes | Yes | Yes | Yes |
| ODBC driver | Yes | Yes | Yes | Yes |
| DatabaseResult | Yes | Yes | Yes | Yes |
| SQL translation | Yes | Yes | Yes | Yes |
| Query caching (TINA4_DB_CACHE) | Yes | Yes | Yes | Yes |
| get_next_id (race-safe) | Yes | Yes | Yes | Yes |
| Transactions (commit safe without txn) | Yes | Yes | Yes | Yes |
| Connection pooling | Yes | Yes | Yes | Yes |
| fetch() default limit = 100 | Yes | Yes | Yes | Yes |
| DATABASE_URL auto-discovery (ORM) | Yes | Yes | Yes | Yes |
| Firebird path parsing (absolute safe) | Yes | Yes | Yes | Yes |
| **ORM** | | | | |
| Active Record (save/load/delete) | Yes | Yes | Yes | Yes |
| Field types | Yes | Yes | Yes | Yes |
| query() → QueryBuilder | Yes | Yes | Yes | Yes |
| select() with filter/order/limit | Yes | Yes | Yes | Yes |
| autoMap / snakeToCamel (lowercase-safe) | Yes | Yes | Yes | Yes |
| Relationships (has_many/has_one/belongs_to) | Yes | Yes | Yes | Yes |
| Soft delete | Yes | Yes | Yes | Yes |
| AutoCRUD | Yes | Yes | Yes | Yes |
| **Template Engine (Frond)** | | | | |
| Twig-compatible syntax | Yes | Yes | Yes | Yes |
| Block inheritance (extends/block) | Yes | Yes | Yes | Yes |
| parent()/super() in blocks | Yes | Yes | Yes | Yes |
| Include/import/macro | Yes | Yes | Yes | Yes |
| {% import "file" as alias %} | Yes | Yes | Yes | Yes |
| Filters | Yes | Yes | Yes | Yes |
| Custom filters/globals/tests | Yes | Yes | Yes | Yes |
| SafeString | Yes | Yes | Yes | Yes |
| Fragment caching | Yes | Yes | Yes | Yes |
| Sandbox mode | Yes | Yes | Yes | Yes |
| form_token / formTokenValue | Yes | Yes | Yes | Yes |
| Arithmetic in {% set %} | Yes | Yes | Yes | Yes |
| Filter-aware conditions | Yes | Yes | Yes | Yes |
| Dev mode cache bypass | Yes | Yes | Yes | Yes |
| **API & Protocols** | | | | |
| API client (zero-dep) | Yes | Yes | Yes | Yes |
| Swagger/OpenAPI generator | Yes | Yes | Yes | Yes |
| GraphQL engine (zero-dep) | Yes | Yes | Yes | Yes |
| WSDL/SOAP server | Yes | Yes | Yes | Yes |
| MCP server (JSON-RPC 2.0) | Yes | Yes | Yes | Yes |
| **Real-time & Messaging** | | | | |
| WebSocket server | Yes | Yes | Yes | Yes |
| WebSocket backplane | Yes | Yes | Yes | Yes |
| Messenger (SMTP/IMAP) | Yes | Yes | Yes | Yes |
| **Queue** | | | | |
| Database-backed job queue | Yes | Yes | Yes | Yes |
| Kafka backend | Yes | Yes | Yes | Yes |
| RabbitMQ backend | Yes | Yes | Yes | Yes |
| MongoDB backend | Yes | Yes | Yes | Yes |
| **Sessions** | | | | |
| File session handler | Yes | Yes | Yes | Yes |
| Database session handler | Yes | Yes | Yes | Yes |
| Redis session handler | Yes | Yes | Yes | Yes |
| Valkey session handler | Yes | Yes | Yes | Yes |
| MongoDB session handler | Yes | Yes | Yes | Yes |
| Session TTL / GC | Yes | Yes | Yes | Yes |
| **Infrastructure** | | | | |
| Migrations | Yes | Yes | Yes | Yes |
| Seeder / FakeData | Yes | Yes | Yes | Yes |
| i18n / Localization | Yes | Yes | Yes | Yes |
| SCSS compiler (zero-dep) | Yes | Yes | Yes | Yes |
| Events (observer pattern) | Yes | Yes | Yes | Yes |
| DotEnv loader | Yes | Yes | Yes | Yes |
| Structured logging | Yes | Yes | Yes | Yes |
| Error overlay (dev mode) | Yes | Yes | Yes | Yes |
| DI Container | Yes | Yes | Yes | Yes |
| Response cache | Yes | Yes | Yes | Yes |
| Service runner | Yes | Yes | Yes | Yes |
| **Dev Tools** | | | | |
| DevAdmin dashboard | Yes | Yes | Yes | Yes |
| Database tab (split-screen) | Yes | Yes | Yes | Yes |
| Metrics (bubble chart) | Yes | Yes | Yes | Yes |
| Metrics dependency lines | Yes | Yes | Yes | Yes |
| DevMailbox | Yes | Yes | Yes | Yes |
| DevReload (live-reload) | Yes | Yes | Yes | Yes |
| Gallery (interactive examples) | Yes | Yes | Yes | Yes |
| Dev toolbar injection | Yes | Yes | Yes | Yes |
| Version check | Yes | Yes | Yes | Yes |
| **Testing & CLI** | | | | |
| TestClient | Yes | Yes | Yes | Yes |
| Inline testing | Yes | Yes | Yes | Yes |
| CLI (init, serve, migrate, generate) | Yes | Yes | Yes | Yes |
| AI context installer (menu-driven) | Yes | Yes | Yes | Yes |
| Scaffold copies CSS/JS on init | Yes | Yes | Yes | Yes |
| **Static Assets** | | | | |
| Minified CSS (tina4.min.css) | Yes | Yes | Yes | Yes |
| Minified JS (tina4.min.js, frond.min.js) | Yes | Yes | Yes | Yes |
| HtmlElement builder | Yes | Yes | Yes | Yes |

## Test Coverage

| Framework | Test Files | Tests | Runner |
|-----------|-----------|-------|--------|
| Python | 52 | ~2,400 | pytest |
| PHP | 54 | ~1,800 | PHPUnit |
| Ruby | 63 | ~2,400 | RSpec |
| Node.js | 57 | ~2,580 | tsx |

## Known Gaps

**None.** All 108 features are at 100% parity across Python, PHP, Ruby, and Node.js.

### Resolved (this session)

| Gap | Resolution |
|-----|-----------|
| MongoDB driver | Implemented — pymongo, ext-mongodb, mongo gem, mongodb npm |
| ODBC driver | Implemented — pyodbc, pdo_odbc, ruby-odbc, odbc npm |
| Route groups (Python) | RouteGroup class added — matches PHP/Ruby/Node |
| ORM relationships | All 4 have declarative + imperative styles |
| Frond sandbox mode | Already implemented in all 4 (was false positive) |
| Frond fragment caching | Already implemented in all 4 (was false positive) |
| AutoCRUD (Node) | Already at parity (was false positive) |
| Redis session handler (PHP) | Already existed (was false positive) |
| Minified CSS/JS (Ruby) | Already existed (was false positive) |
| Pagination inconsistency | Standardized: limit/offset primary, merged dual-key response |

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.10.55 | 2026-04-02 | MongoDB adapter (all 4), ODBC adapter (PHP/Ruby/Node), pagination standardized, Python RouteGroup class, Ruby imperative relationships, metrics dep lines fix |
| 3.10.54 | 2026-04-02 | Auto AI dual-port, TINA4_NO_RELOAD, bug fixes (#101-#105), CORS fix, DATABASE_URL discovery, ORM query() docs, metrics dep lines fix |
| 3.10.50 | 2026-04-02 | Issue #106 fixes, session TTL/GC, dev admin auth bypass, test expansion to ~9,100 |
| 3.10.48 | 2026-04-02 | TINA4_NO_BROWSER, --production flag, gallery fixes |
| 3.10.42 | 2026-04-01 | Database tab redesign, star wiggle, copy/paste, fetch limit=100 |
| 3.10.38 | 2026-04-01 | Metrics (bubble chart), AI installer, dashboard cleanup |
