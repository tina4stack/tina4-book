# Tina4 — Cross-Framework Parity Matrix

Last updated: 2026-04-01 | Version: 3.10.38

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
| CORS middleware | Yes | Yes | Yes | Yes |
| Health endpoint | Yes | Yes | Yes | Yes |
| **Auth & Security** | | | | |
| JWT auth (zero-dep) | Yes | Yes | Yes | Yes |
| Password hashing | Yes | Yes | Yes | Yes |
| Form token (CSRF) | Yes | Yes | Yes | Yes |
| CSRF middleware | Yes | Yes | Yes | Yes |
| Rate limiter | Yes | Yes | Yes | Yes |
| Validator | Yes | Yes | Yes | Yes |
| **Database** | | | | |
| URL-based multi-driver connection | Yes | Yes | Yes | Yes |
| SQLite driver | Yes | Yes | Yes | Yes |
| PostgreSQL driver | Yes | Yes | Yes | Yes |
| MySQL driver | Yes | Yes | Yes | Yes |
| MSSQL driver | Yes | Yes | Yes | Yes |
| Firebird driver | Yes | Yes | Yes | Yes |
| ODBC driver | Yes | No | No | No |
| DatabaseResult | Yes | Yes | Yes | Yes |
| SQL translation | Yes | Yes | Yes | Yes |
| Query caching | Yes | Yes | Yes | Yes |
| get_next_id (race-safe) | Yes | Yes | Yes | Yes |
| Transactions | Yes | Yes | Yes | Yes |
| **ORM** | | | | |
| Active Record (save/load/delete) | Yes | Yes | Yes | Yes |
| Field types | Yes | Yes | Yes | Yes |
| Relationships (has_many/has_one/belongs_to) | Yes | Yes | Yes | Yes |
| Soft delete | Yes | Yes | Yes | Yes |
| QueryBuilder | Yes | Yes | Yes | Yes |
| AutoCRUD | Yes | Yes | Yes | Yes |
| **Template Engine (Frond)** | | | | |
| Twig-compatible syntax | Yes | Yes | Yes | Yes |
| Block inheritance (extends/block) | Yes | Yes | Yes | Yes |
| parent()/super() in blocks | Yes | Yes | Yes | Yes |
| Include/import/macro | Yes | Yes | Yes | Yes |
| Filters | Yes | Yes | Yes | Yes |
| Custom filters/globals/tests | Yes | Yes | Yes | Yes |
| SafeString | Yes | Yes | Yes | Yes |
| Fragment caching | Yes | Yes | Yes | Yes |
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
| Redis session handler | Yes | No | Yes | Yes |
| Valkey session handler | Yes | Yes | Yes | Yes |
| MongoDB session handler | Yes | Yes | Yes | Yes |
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
| DevMailbox | Yes | Yes | Yes | Yes |
| DevReload (live-reload) | Yes | Yes | Yes | Yes |
| Gallery (interactive examples) | Yes | Yes | Yes | Yes |
| Metrics (code analysis + bubble chart) | Yes | Yes | Yes | Yes |
| Version check | Yes | Yes | Yes | Yes |
| **Testing & CLI** | | | | |
| TestClient | Yes | Yes | Yes | Yes |
| Inline testing | Yes | Yes | Yes | Yes |
| CLI (init, serve, migrate, generate) | Yes | Yes | Yes | Yes |
| AI context installer (menu-driven) | Yes | Yes | Yes | Yes |
| **Static Assets** | | | | |
| Minified CSS (tina4.min.css) | Yes | Yes | No | Yes |
| Minified JS (tina4.min.js, frond.min.js) | Yes | Yes | No | Yes |
| HtmlElement builder | Yes | Yes | Yes | Yes |

## Test Coverage

| Framework | Test Files | Test Methods | Runner |
|-----------|-----------|-------------|--------|
| Python | 52 | 2,018 | pytest |
| PHP | 54 | 1,551 | PHPUnit |
| Ruby | 63 | 1,784 | RSpec |
| Node.js | 57 | ~152 | node --test |

## Known Gaps

| Gap | Frameworks Missing | Priority |
|-----|-------------------|----------|
| ODBC driver | PHP, Ruby, Node.js | Low |
| Redis session handler | PHP | Medium |
| Minified CSS/JS bundles | Ruby | High |
| Node.js test depth | Node.js (most tests have 1 assertion) | High |

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.10.38 | 2026-04-01 | Metrics (bubble chart), AI installer (menu-driven), demo cleanup, dashboard full-width, sticky header/tabs, file analysis sort by worst first |
