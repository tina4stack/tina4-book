# Tina4 Signature Parity Report

> Auto-generated on 2026-04-15

Compares public method signatures (params + return types) across Python, PHP, Ruby, and Node.js.
Methods are matched by normalised snake_case name. ✅ = full parity, ⚠️ = mismatch or missing.

## Summary

| Feature | Methods | ✅ Match | ⚠️ Mismatch | ⚠️ Missing |
|---------|--------:|--------:|------------:|----------:|
| ORM | 37 | 37 | 0 | 0 |
| Queue | 15 | 15 | 0 | 0 |
| Job | 7 | 7 | 0 | 0 |
| Auth | 8 | 8 | 0 | 0 |
| Database | 28 | 28 | 0 | 0 |
| Router | 19 | 19 | 0 | 0 |
| Session | 17 | 17 | 0 | 0 |
| Migration | 13 | 13 | 0 | 0 |
| MCP | 13 | 13 | 0 | 0 |
| Frond | 10 | 10 | 0 | 0 |
| GraphQL | 13 | 13 | 0 | 0 |
| Api | 9 | 9 | 0 | 0 |
| Cache | 7 | 7 | 0 | 0 |
| Container | 5 | 5 | 0 | 0 |
| Events | 8 | 8 | 0 | 0 |
| WebSocket | 20 | 20 | 0 | 0 |
| WSDL | 5 | 5 | 0 | 0 |
| Swagger | 1 | 1 | 0 | 0 |
| I18n | 7 | 7 | 0 | 0 |
| Seeder | 33 | 33 | 0 | 0 |
| QueryBuilder | 16 | 16 | 0 | 0 |
| Validator | 11 | 11 | 0 | 0 |
| HtmlElement | 1 | 1 | 0 | 0 |
| Testing | 7 | 7 | 0 | 0 |
| Messenger | 16 | 16 | 0 | 0 |
| Logger | 7 | 7 | 0 | 0 |
| AI | 5 | 5 | 0 | 0 |
| Request | 4 | 4 | 0 | 0 |
| Response | 18 | 18 | 0 | 0 |
| Middleware | 13 | 13 | 0 | 0 |
| AutoCrud | 5 | 5 | 0 | 0 |
| SqlTranslation | 17 | 17 | 0 | 0 |
| Metrics | 3 | 3 | 0 | 0 |
| ErrorOverlay | 3 | 3 | 0 | 0 |
| DotEnv | 7 | 7 | 0 | 0 |
| DevAdmin | 13 | 13 | 0 | 0 |
| Service | 8 | 8 | 0 | 0 |
| ScssCompiler | 5 | 5 | 0 | 0 |
| RateLimiter | 4 | 4 | 0 | 0 |
| Server | 3 | 3 | 0 | 0 |
| TestClient | 7 | 7 | 0 | 0 |
| WebSocketBackplane | 5 | 5 | 0 | 0 |
| DatabaseResult | 6 | 6 | 0 | 0 |
| DevReload | 0 | 0 | 0 | 0 |

## ORM

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `all` | `limit, offset, include, order_by` | `limit, offset, include, orderBy` | `limit, offset` | `where?, params?, include?, orderBy?` | ✅ |
| `belongs_to` | `related_class, foreign_key` | `relatedClass, foreignKey` | `related_class, foreign_key` | `relatedClass, foreignKey` | ✅ |
| `cached` | `sql, params, ttl, limit, offset, include` | `sql, params, ttl, limit, offset, include` | `sql, params, limit, offset` | `sql, params?, ttl, limit, offset, include?` | ✅ |
| `camel_to_snake` | `name` | `name` | `name` | `name` | ✅ |
| `clear_cache` | `()` | `()` | `()` | `()` | ✅ |
| `clear_rel_cache` | `()` | `()` | `()` | `()` | ✅ |
| `count` | `conditions, params` | `conditions, params` | `conditions, params` | `conditions?, params?` | ✅ |
| `create` | `data` | `data` | `attributes` | `data` | ✅ |
| `create_table` | `()` | `()` | `()` | `()` | ✅ |
| `delete` | `()` | `()` | `()` | `()` | ✅ |
| `eager_load` | `instances, include_list` | `instances, include, db` | `instances, include_list` | `instances, includeList` | ✅ |
| `exists` | `pk_value` | `pkValue` | `pk_value` | `pkValue` | ✅ |
| `find` | `filter, limit, offset, order_by, include` | `filter, limit, offset, orderBy, include` | `filter, limit, offset` | `filter?, limit, offset, orderBy?, include?` | ✅ |
| `find_by_id` | `pk_value, include` | `id, include` | `id` | `id, include?` | ✅ |
| `find_or_fail` | `pk_value` | `id` | `id` | `id` | ✅ |
| `force_delete` | `()` | `()` | `()` | `()` | ✅ |
| `get_db` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `get_db_column` | `prop` | `property` | `property` | `prop` | ℹ️ return type differs |
| `has_many` | `related_class, foreign_key, limit, offset` | `relatedClass, foreignKey, limit, offset` | `related_class, foreign_key, limit, offset` | `relatedClass, foreignKey, limit, offset` | ✅ |
| `has_one` | `related_class, foreign_key` | `relatedClass, foreignKey` | `related_class, foreign_key` | `relatedClass, foreignKey` | ✅ |
| `load` | `filter, params, include` | `filter, params, include` | `filter, params` | `filter?, params?, include?` | ✅ |
| `query` | `()` | `()` | `()` | `()` | ✅ |
| `restore` | `()` | `()` | `()` | `()` | ✅ |
| `save` | `()` | `()` | `()` | `()` | ✅ |
| `scope` | `name, filter_sql, params` | `name, filterSql, params` | `name, filter_sql, params` | `name, filterSql, params?` | ✅ |
| `select` | `sql, params, limit, offset, include` | `sql, params, limit, offset, include` | `*fields` | `sql, params?` | ✅ |
| `select_one` | `sql, params, include` | `sql, params, include` | `sql, params` | `sql, params?, include?` | ✅ |
| `snake_to_camel` | `name` | `name` | `name` | `name` | ✅ |
| `to_array` | `()` | `()` | `()` | `()` | ✅ |
| `to_assoc` | `include, case` | `include` | `()` | `include?` | ✅ |
| `to_dict` | `include, case` | `include, case` | `()` | `include?` | ✅ |
| `to_json` | `include` | `include` | `()` | `include?` | ✅ |
| `to_list` | `()` | `()` | `()` | `()` | ✅ |
| `to_object` | `case` | `()` | `()` | `()` | ✅ |
| `validate` | `()` | `()` | `()` | `()` | ✅ |
| `where` | `filter_sql, params, limit, offset, include` | `filterSql, params, limit, offset, include` | `conditions, params, limit, offset` | `conditions, params?, limit, offset, include?` | ✅ |
| `with_trashed` | `filter_sql, params, limit, offset` | `filterSql, params, limit, offset` | `conditions, params, limit, offset` | `conditions?, params?, limit?, offset?` | ✅ |

### Mismatch Details

#### `get_db`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `DatabaseAdapter|None` |
| Ruby | `` | `Database` |
| Node | `` | `DatabaseAdapter` |

#### `get_db_column`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `prop: str` | `str` |
| PHP | `property: string` | `str` |
| Ruby | `property` | `Symbol` |
| Node | `prop: string` | `str` |

## Queue

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `clear` | `()` | `()` | `()` | `()` | ✅ |
| `consume` | `topic, id, poll_interval, iterations, batch_size` | `topic, id, pollInterval, iterations, batchSize` | `topic, id, poll_interval, iterations, batch_size, handler` | `topicOrOptions?, id?, pollInterval, iterations, batchSize` | ℹ️ return type differs |
| `dead_letters` | `max_retries` | `maxRetries` | `max_retries` | `maxRetries?` | ✅ |
| `failed` | `()` | `()` | `()` | `()` | ✅ |
| `get_topic` | `()` | `()` | `()` | `()` | ✅ |
| `pop` | `()` | `()` | `()` | `()` | ✅ |
| `pop_batch` | `count` | `count` | `count` | `count` | ✅ |
| `pop_by_id` | `id` | `id` | `id` | `id` | ✅ |
| `process` | `handler, topic, max_jobs, batch_size` | `handlerOrQueue, queueOrHandlerOrOptions, options` | `topic, max_jobs, batch_size, handler` | `handler, options?` | ✅ |
| `produce` | `topic, data, priority, delay_seconds` | `topic, payload, priority, delaySeconds` | `topic, payload, priority, delay_seconds` | `topic, payload, priority, delay` | ✅ |
| `purge` | `status, max_retries` | `status, maxRetries` | `status, max_retries` | `status, maxRetries?` | ✅ |
| `push` | `data, priority, delay_seconds` | `payload, priority, delay` | `payload, priority, delay_seconds` | `payload, delay?, priority` | ✅ |
| `retry` | `job_id, delay_seconds` | `jobId, delaySeconds` | `job_id, delay_seconds` | `jobId?, delaySeconds?` | ✅ |
| `retry_failed` | `max_retries` | `maxRetries` | `max_retries` | `maxRetries?` | ✅ |
| `size` | `status` | `status` | `()` | `status` | ✅ |

### Mismatch Details

#### `consume`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `topic: str = None, id: str = None, poll_interval: float = 1.0, iterations: int = 0, batch_size: int = 1` | `untyped` |
| PHP | `topic: string '' = '', id: ?string null = null, pollInterval: float 1.0 = 1.0, iterations: int 0 = 0, batchSize: int 1 = 1` | `\Generator` |
| Ruby | `topic = nil, id: nil, poll_interval: 1.0, iterations: 0, batch_size: 1, &block` | `untyped` |
| Node | `topicOrOptions?: string | ConsumeOptions, id?: string, pollInterval: number = 1000, iterations: number = 0, batchSize: number = 1` | `AsyncGenerator<dict|list>` |

## Job

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `complete` | `()` | `()` | `()` | `()` | ✅ |
| `fail` | `error` | `reason` | `reason` | `reason?` | ✅ |
| `reject` | `reason` | `reason` | `reason` | `reason?` | ✅ |
| `retry` | `delay_seconds` | `delaySeconds` | `delay_seconds` | `delaySeconds?` | ✅ |
| `to_array` | `()` | `()` | `()` | `()` | ✅ |
| `to_hash` | `()` | `()` | `()` | `()` | ✅ |
| `to_json` | `()` | `()` | `()` | `()` | ✅ |

## Auth

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `authenticate_request` | `headers, secret, algorithm` | `headers, secret, algorithm` | `headers, secret, algorithm` | `headers, string | string[] | undefined>, secret?, algorithm` | ✅ |
| `check_password` | `password, hashed` | `password, hash` | `password, hash` | `"secret123", hash` | ✅ |
| `get_payload` | `token` | `token` | `token` | `token` | ✅ |
| `get_token` | `payload, expires_in, secret` | `payload, secret, expiresIn` | `payload, expires_in, secret` | `payload, unknown>, secretOrExpiresIn?, expiresIn, algorithm?` | ✅ |
| `hash_password` | `password, salt, iterations` | `password, salt, iterations` | `password, salt, iterations` | `password, salt?, iterations` | ✅ |
| `refresh_token` | `token, expires_in` | `token, expiresIn` | `token, expires_in` | `token, expiresIn` | ✅ |
| `valid_token` | `token` | `token, secret` | `token` | `token, secret?, algorithm?` | ✅ |
| `validate_api_key` | `provided, expected` | `provided, expected` | `provided` | `provided, expected?` | ✅ |

## Database

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `active_count` | `()` | `()` | `()` | `()` | ✅ |
| `cache_clear` | `()` | `()` | `()` | `()` | ✅ |
| `cache_stats` | `()` | `()` | `()` | `()` | ✅ |
| `checkin` | `adapter` | `adapter` | `_driver` | `_adapter` | ✅ |
| `checkout` | `()` | `()` | `()` | `()` | ✅ |
| `close` | `()` | `()` | `()` | `()` | ✅ |
| `close_all` | `()` | `()` | `()` | `()` | ✅ |
| `commit` | `()` | `()` | `()` | `()` | ✅ |
| `create` | `url, username, password, pool` | `url, autoCommit, username, password, pool` | `url, pool` | `url, username?, password?, pool` | ℹ️ return type differs |
| `delete` | `table, filter_sql, params` | `table, filter, whereParams` | `table, filter, params` | `table, filter?, params?` | ℹ️ return type differs |
| `execute` | `sql, params` | `sql, params` | `sql, params` | `sql, params?` | ℹ️ return type differs |
| `execute_many` | `sql, params_list` | `sql, paramsList` | `sql, params_list` | `sql, paramSets` | ℹ️ return type differs |
| `fetch` | `sql, params, limit, offset` | `sql, params, limit, offset` | `sql, params, limit, offset` | `sql, params?, limit?, offset?` | ✅ |
| `fetch_one` | `sql, params` | `sql, params` | `sql, params` | `sql, params?` | ℹ️ return type differs |
| `from_env` | `env_key, pool` | `envKey, autoCommit, pool` | `pool` | `envKey, pool` | ℹ️ return type differs |
| `get_adapter` | `()` | `()` | `()` | `()` | ✅ |
| `get_columns` | `table` | `tableName` | `table_name` | `tableName` | ✅ |
| `get_error` | `()` | `()` | `()` | `()` | ✅ |
| `get_last_id` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `get_next_id` | `table, pk_column, generator_name` | `table, pkColumn, generatorName` | `table, pk_column, generator_name` | `table, pkColumn, generatorName?` | ✅ |
| `get_tables` | `()` | `()` | `()` | `()` | ✅ |
| `insert` | `table, data` | `table, data` | `table, data` | `table, data` | ℹ️ return type differs |
| `pool_size` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `rollback` | `()` | `()` | `()` | `()` | ✅ |
| `size` | `()` | `()` | `()` | `()` | ✅ |
| `start_transaction` | `()` | `()` | `()` | `()` | ✅ |
| `table_exists` | `name` | `tableName` | `table_name` | `name` | ✅ |
| `update` | `table, data, filter_sql, params` | `table, data, filterSql, params` | `table, data, filter, params` | `table, data, filter?, params?` | ℹ️ return type differs |

### Mismatch Details

#### `create`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `url: str, username: str = '', password: str = '', pool: int = 0` | `Database` |
| PHP | `url: string, autoCommit: ?bool null = null, username: string '' = '', password: string '' = '', pool: int 0 = 0` | `Self` |
| Ruby | `url, username: "", password: "", pool: 0` | `untyped` |
| Node | `url: string, username?: string, password?: string, pool: number = 0` | `Database` |

#### `delete`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `table: str, filter_sql: str | dict | list = '', params: list = None` | `DatabaseResult` |
| PHP | `table: string, filter: string|array '' = '', whereParams: array [] = []` | `bool` |
| Ruby | `table, filter = {}, params = nil` | `untyped` |
| Node | `table: string, filter?: Record<string, unknown>, params?: unknown[]` | `DatabaseWriteResult` |

#### `execute`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `sql: str, params: list = None` | `untyped` |
| PHP | `sql: string, params: array [] = []` | `bool|DatabaseResult` |
| Ruby | `sql, params = []` | `untyped` |
| Node | `sql: string, params?: unknown[]` | `bool|unknown` |

#### `execute_many`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `sql: str, params_list: list[list] = None` | `DatabaseResult` |
| PHP | `sql: string, paramsList: array [] = []` | `list` |
| Ruby | `sql, params_list = []` | `untyped` |
| Node | `sql: string, paramSets: unknown[][] = []` | `list` |

#### `fetch_one`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `sql: str, params: list = None` | `dict|None` |
| PHP | `sql: string, params: array [] = []` | `dict|None` |
| Ruby | `sql, params = []` | `untyped` |
| Node | `sql: string, params?: unknown[]` | `Self|None` |

#### `from_env`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `env_key: str = 'DATABASE_URL', pool: int = 0` | `Database|None` |
| PHP | `envKey: string 'DATABASE_URL' = 'DATABASE_URL', autoCommit: ?bool null = null, pool: int 0 = 0` | `Self|None` |
| Ruby | `env_key: "DATABASE_URL", pool: 0` | `untyped` |
| Node | `envKey = "DATABASE_URL", pool: number = 0` | `Database` |

#### `get_last_id`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `int|str` |
| Ruby | `` | `untyped` |
| Node | `` | `str|int` |

#### `insert`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `table: str, data: dict | list` | `DatabaseResult` |
| PHP | `table: string, data: array` | `bool` |
| Ruby | `table, data` | `untyped` |
| Node | `table: string, data: Record<string, unknown>` | `DatabaseWriteResult` |

#### `pool_size`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `int` |
| PHP | `` | `DatabaseAdapter` |
| Ruby | `` | `untyped` |
| Node | `` | `int` |

#### `update`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `table: str, data: dict, filter_sql: str = '', params: list = None` | `DatabaseResult` |
| PHP | `table: string, data: array, filterSql: string '' = '', params: array [] = []` | `bool` |
| Ruby | `table, data, filter = {}, params = nil` | `untyped` |
| Node | `table: string, data: Record<string, unknown>, filter?: Record<string, unknown>, params?: unknown[]` | `DatabaseWriteResult` |

## Router

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `add` | `method, path, handler, middleware, swagger_meta, template` | `method, path, handler, middleware, swaggerMeta, template` | `method, path, handler` | `method, path, handler, middleware?, swaggerMeta?, template?` | ℹ️ return type differs |
| `any` | `path, handler, middleware, swagger_meta, template` | `path, handler, middleware, swaggerMeta, template` | `path, handler` | `path, handler, middleware?, swaggerMeta?, template?` | ℹ️ return type differs |
| `cache` | `()` | `()` | `()` | `()` | ✅ |
| `clear` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `delete` | `path, handler, middleware, swagger_meta, template` | `path, handler, middleware, swaggerMeta, template` | `path, handler` | `path, handler, middleware?, swaggerMeta?, template?` | ℹ️ return type differs |
| `get` | `path, handler, middleware, swagger_meta, template` | `path, handler, middleware, swaggerMeta, template` | `path, handler` | `path, handler, middleware?, swaggerMeta?, template?` | ℹ️ return type differs |
| `get_routes` | `()` | `()` | `()` | `()` | ✅ |
| `get_web_socket_routes` | `()` | `()` | `()` | `()` | ✅ |
| `group` | `prefix, callback, middleware` | `prefix, callback, middleware` | `prefix, handler` | `prefix, callback, middlewares?` | ✅ |
| `list_routes` | `()` | `()` | `()` | `()` | ✅ |
| `match` | `method, path` | `method, path` | `method, path` | `method, path` | ℹ️ return type differs |
| `middleware` | `*middleware_classes` | `middleware` | `*middleware_classes` | `...middlewareClasses` | ✅ |
| `no_auth` | `()` | `()` | `()` | `()` | ✅ |
| `patch` | `path, handler, middleware, swagger_meta, template` | `path, handler, middleware, swaggerMeta, template` | `path, handler` | `path, handler, middleware?, swaggerMeta?, template?` | ℹ️ return type differs |
| `post` | `path, handler, middleware, swagger_meta, template` | `path, handler, middleware, swaggerMeta, template` | `path, handler` | `path, handler, middleware?, swaggerMeta?, template?` | ℹ️ return type differs |
| `put` | `path, handler, middleware, swagger_meta, template` | `path, handler, middleware, swaggerMeta, template` | `path, handler` | `path, handler, middleware?, swaggerMeta?, template?` | ℹ️ return type differs |
| `secure` | `()` | `()` | `()` | `()` | ✅ |
| `use` | `middleware_class` | `class` | `klass` | `middlewareClass` | ✅ |
| `websocket` | `path, handler` | `path, handler` | `path, handler` | `path, handler` | ✅ |

### Mismatch Details

#### `add`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `method: str, path: str, handler, middleware: list = None, swagger_meta: dict = None, template: str = None, **options` | `RouteRef` |
| PHP | `method: string, path: string, handler: callable, middleware: array [] = [], swaggerMeta: array [] = [], template: ?string null = null` | `Self` |
| Ruby | `method, path, handler, auth_handler: nil, swagger_meta: {}, middleware: [], template: nil` | `untyped` |
| Node | `method: string, path: string, handler: RouteHandler, middleware?: Middleware[], swaggerMeta?: RouteMeta, template?: string` | `RouteRef` |

#### `any`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str, handler, middleware: list = None, swagger_meta: dict = None, template: str = None, **options` | `RouteRef` |
| PHP | `path: string, handler: callable, middleware: array [] = [], swaggerMeta: array [] = [], template: ?string null = null` | `Self` |
| Ruby | `path, middleware: [], swagger_meta: {}, template: nil, &block` | `untyped` |
| Node | `path: string, handler: RouteHandler, middleware?: Middleware[], swaggerMeta?: RouteMeta, template?: string` | `RouteRef` |

#### `clear`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `None` |

#### `delete`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str, handler, middleware: list = None, swagger_meta: dict = None, template: str = None, **options` | `RouteRef` |
| PHP | `path: string, handler: callable, middleware: array [] = [], swaggerMeta: array [] = [], template: ?string null = null` | `Self` |
| Ruby | `path, middleware: [], swagger_meta: {}, template: nil, &block` | `untyped` |
| Node | `path: string, handler: RouteHandler, middleware?: Middleware[], swaggerMeta?: RouteMeta, template?: string` | `RouteRef` |

#### `get`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str, handler, middleware: list = None, swagger_meta: dict = None, template: str = None, **options` | `RouteRef` |
| PHP | `path: string, handler: callable, middleware: array [] = [], swaggerMeta: array [] = [], template: ?string null = null` | `Self` |
| Ruby | `path, middleware: [], swagger_meta: {}, template: nil, &block` | `untyped` |
| Node | `path: string, handler: RouteHandler, middleware?: Middleware[], swaggerMeta?: RouteMeta, template?: string` | `RouteRef` |

#### `match`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `method: str, path: str` | `tuple[dict|None, dict]` |
| PHP | `method: string, path: string` | `list` |
| Ruby | `method, path` | `untyped` |
| Node | `method: string, path: string` | `MatchResult|None` |

#### `patch`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str, handler, middleware: list = None, swagger_meta: dict = None, template: str = None, **options` | `RouteRef` |
| PHP | `path: string, handler: callable, middleware: array [] = [], swaggerMeta: array [] = [], template: ?string null = null` | `Self` |
| Ruby | `path, middleware: [], swagger_meta: {}, template: nil, &block` | `untyped` |
| Node | `path: string, handler: RouteHandler, middleware?: Middleware[], swaggerMeta?: RouteMeta, template?: string` | `RouteRef` |

#### `post`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str, handler, middleware: list = None, swagger_meta: dict = None, template: str = None, **options` | `RouteRef` |
| PHP | `path: string, handler: callable, middleware: array [] = [], swaggerMeta: array [] = [], template: ?string null = null` | `Self` |
| Ruby | `path, middleware: [], swagger_meta: {}, template: nil, &block` | `untyped` |
| Node | `path: string, handler: RouteHandler, middleware?: Middleware[], swaggerMeta?: RouteMeta, template?: string` | `RouteRef` |

#### `put`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str, handler, middleware: list = None, swagger_meta: dict = None, template: str = None, **options` | `RouteRef` |
| PHP | `path: string, handler: callable, middleware: array [] = [], swaggerMeta: array [] = [], template: ?string null = null` | `Self` |
| Ruby | `path, middleware: [], swagger_meta: {}, template: nil, &block` | `untyped` |
| Node | `path: string, handler: RouteHandler, middleware?: Middleware[], swaggerMeta?: RouteMeta, template?: string` | `RouteRef` |

## Session

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `all` | `()` | `()` | `()` | `()` | ✅ |
| `clear` | `()` | `()` | `()` | `()` | ✅ |
| `cookie_header` | `cookie_name` | `cookieName` | `cookie_name` | `cookieName` | ✅ |
| `delete` | `key` | `key` | `key` | `key` | ✅ |
| `destroy` | `()` | `()` | `()` | `()` | ✅ |
| `flash` | `key, value` | `key, value` | `key, value` | `key, value?` | ✅ |
| `gc` | `()` | `maxLifetime` | `max_lifetime` | `()` | ✅ |
| `get` | `key, default` | `key, default` | `key, default` | `key, defaultValue?` | ✅ |
| `get_flash` | `key, default` | `key, default` | `key, default` | `key, defaultValue?` | ✅ |
| `get_session_id` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `has` | `key` | `key` | `key` | `key` | ✅ |
| `read` | `session_id` | `sessionId` | `session_id` | `sessionId` | ℹ️ return type differs |
| `regenerate` | `()` | `()` | `()` | `()` | ✅ |
| `save` | `()` | `()` | `()` | `()` | ✅ |
| `set` | `key, value` | `key, value` | `key, value` | `key, value` | ✅ |
| `start` | `session_id` | `sessionId` | `session_id` | `sessionId?` | ✅ |
| `write` | `session_id, data, ttl` | `sessionId, data, ttl` | `session_id, data, ttl` | `sessionId, data, ttl?` | ✅ |

### Mismatch Details

#### `get_session_id`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `str|None` |
| PHP | `` | `str` |
| Ruby | `` | `untyped` |
| Node | `` | `str|None` |

#### `read`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `session_id: str` | `dict` |
| PHP | `sessionId: string` | `list|None` |
| Ruby | `session_id` | `untyped` |
| Node | `sessionId: string` | `SessionData|None` |

## Migration

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `create` | `description, kind` | `description, kind` | `description, kind` | `description` | ℹ️ return type differs |
| `create_migration` | `description, migration_folder, kind` | `description, migrationsDir, kind` | `description` | `description, options?` | ℹ️ return type differs |
| `down` | `db` | `()` | `db` | `()` | ✅ |
| `get_applied` | `()` | `()` | `()` | `()` | ✅ |
| `get_applied_migrations` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `get_files` | `()` | `()` | `()` | `()` | ✅ |
| `get_pending` | `()` | `()` | `()` | `()` | ✅ |
| `migrate` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `record_migration` | `name, batch, passed` | `name, batch, passed` | `name, batch` | `name, batch` | ✅ |
| `remove_migration_record` | `name` | `name` | `name` | `migration.name` | ✅ |
| `rollback` | `steps` | `steps` | `steps` | `steps` | ✅ |
| `status` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `up` | `db` | `()` | `db` | `()` | ✅ |

### Mismatch Details

#### `create`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `description: str, kind: str = 'sql'` | `str` |
| PHP | `description: string, kind: string 'sql' = 'sql'` | `str` |
| Ruby | `description, kind = "sql"` | `untyped` |
| Node | `description: string, kind: "sql" | "class" = "sql"` | `Promise<str|` |

#### `create_migration`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `description: str, migration_folder: str = 'migrations', kind: str = 'sql'` | `str` |
| PHP | `description: string, migrationsDir: string 'migrations' = 'migrations', kind: string 'sql' = 'sql'` | `str` |
| Ruby | `description, migrations_dir: "migrations", kind: "sql"` | `untyped` |
| Node | `description: string, options?: { migrationsDir?: string; kind?: "sql" | "class" }` | `Promise<str|` |

#### `get_applied_migrations`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `list<` |

#### `migrate`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `MigrationResult` |

#### `status`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `MigrationStatus` |

## MCP

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `decode_request` | `data` | `data` | `data` | `data` | ℹ️ return type differs |
| `encode_error` | `request_id, code, message, data` | `requestId, code, message, data` | `request_id, code, message, data` | `requestId, code, message, data?` | ✅ |
| `encode_notification` | `method, params` | `method, params` | `method, params` | `method, params?` | ✅ |
| `encode_response` | `request_id, result` | `requestId, result` | `request_id, result` | `requestId, result` | ✅ |
| `handle_message` | `raw_data` | `rawData` | `raw_data` | `rawData` | ✅ |
| `is_localhost` | `()` | `()` | `()` | `()` | ✅ |
| `mcp_resource` | `uri, description, mime_type, server` | `uri, description, mimeType, server` | `uri, handler` | `uri, description, mimeType, server?` | ✅ |
| `mcp_tool` | `name, description, server` | `name, description, server` | `name, handler` | `name, description, server?, params?` | ✅ |
| `register` | `server` | `server` | `server` | `server` | ✅ |
| `register_resource` | `uri, handler, description, mime_type` | `uri, handler, description, mimeType` | `uri, handler, description, mime_type` | `uri, handler, description, mimeType` | ✅ |
| `register_routes` | `router_module` | `router` | `router` | `router` | ✅ |
| `register_tool` | `name, handler, description, schema` | `name, handler, description, schema` | `name, handler, description, schema` | `name, handler, description, schema?` | ✅ |
| `write_claude_config` | `port` | `port` | `port` | `port` | ✅ |

### Mismatch Details

#### `decode_request`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `data: str | bytes | dict` | `tuple` |
| PHP | `data: string|array` | `list` |
| Ruby | `data` | `untyped` |
| Node | `data: string | Record<string, unknown>` | `untyped` |

## Frond

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `add_filter` | `name, fn` | `name, fn` | `name, handler` | `name, fn` | ✅ |
| `add_global` | `name, value` | `name, value` | `name, value` | `name, value` | ✅ |
| `add_test` | `name, fn` | `name, fn` | `name, handler` | `name, fn` | ℹ️ return type differs |
| `clear_cache` | `()` | `()` | `()` | `()` | ✅ |
| `render` | `template, data` | `template, data` | `template, data` | `template, data?` | ✅ |
| `render_dump` | `v` | `v` | `value` | `value` | ✅ |
| `render_string` | `source, data` | `source, data, templateName` | `source, data` | `source, data?` | ✅ |
| `sandbox` | `allowed_filters, allowed_tags, allowed_vars` | `filters, tags, vars` | `()` | `filters?, tags?, vars?` | ℹ️ return type differs |
| `set_form_token_session_id` | `session_id` | `sessionId` | `session_id` | `sessionId` | ✅ |
| `unsandbox` | `()` | `()` | `()` | `()` | ℹ️ return type differs |

### Mismatch Details

#### `add_test`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `name: str, fn` | `untyped` |
| PHP | `name: string, fn: callable` | `dict` |
| Ruby | `name, &blk` | `untyped` |
| Node | `name: string, fn: TestFn` | `None` |

#### `sandbox`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `allowed_filters: list[str] = None, allowed_tags: list[str] = None, allowed_vars: list[str] = None` | `untyped` |
| PHP | `filters: ?array null = null, tags: ?array null = null, vars: ?array null = null` | `Self` |
| Ruby | `filters: nil, tags: nil, vars: nil` | `untyped` |
| Node | `filters?: string[], tags?: string[], vars?: string[]` | `Frond` |

#### `unsandbox`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `Self` |
| Ruby | `` | `untyped` |
| Node | `` | `Frond` |

## GraphQL

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `add_mutation` | `name, args, return_type, resolver` | `name, args, returnType, resolver` | `name, args, return_type, resolver, handler` | `name, args, returnType, resolver` | ℹ️ return type differs |
| `add_query` | `name, args, return_type, resolver` | `name, args, returnType, resolver` | `name, args, return_type, resolver, handler` | `name, args, returnType, resolver` | ℹ️ return type differs |
| `add_type` | `name, fields` | `name, fields` | `name_or_type, fields` | `name, fields` | ℹ️ return type differs |
| `advance` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `execute` | `query, variables, context` | `query, variables, context` | `query` | `query, variables?, context?` | ℹ️ return type differs |
| `expect` | `type, value` | `type, value` | `type, value` | `type, value?` | ℹ️ return type differs |
| `from_orm` | `orm_class` | `ormInstance` | `klass` | `modelClass, adapter?` | ℹ️ return type differs |
| `introspect` | `()` | `()` | `()` | `()` | ✅ |
| `match` | `type, value` | `type, value` | `type, value` | `type, value?` | ℹ️ return type differs |
| `parse` | `type_str` | `typeStr` | `type_str` | `typeStr` | ℹ️ return type differs |
| `peek` | `()` | `offset` | `offset` | `()` | ℹ️ return type differs |
| `schema_sdl` | `()` | `()` | `()` | `()` | ✅ |
| `tokenize` | `source` | `source` | `src` | `source` | ✅ |

### Mismatch Details

#### `add_mutation`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `name: str, args: dict, return_type: str, resolver: callable` | `untyped` |
| PHP | `name: string, args: array, returnType: string, resolver: callable` | `Self` |
| Ruby | `name, args = {}, return_type = nil, resolver = nil, &block` | `untyped` |
| Node | `name: string, args: Record<string, string>, returnType: string, resolver: ResolverFn` | `GraphQL` |

#### `add_query`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `name: str, args: dict, return_type: str, resolver: callable` | `untyped` |
| PHP | `name: string, args: array, returnType: string, resolver: callable` | `Self` |
| Ruby | `name, args = {}, return_type = nil, resolver = nil, &block` | `untyped` |
| Node | `name: string, args: Record<string, string>, returnType: string, resolver: ResolverFn` | `GraphQL` |

#### `add_type`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `name: str, fields: dict[str, str]` | `untyped` |
| PHP | `name: string, fields: array` | `Self` |
| Ruby | `name_or_type, fields = nil` | `untyped` |
| Node | `name: string, fields: Record<string, GraphQLField>` | `GraphQL` |

#### `advance`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `Token` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `Token` |

#### `execute`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `query: str, variables: dict = None, context: dict = None` | `dict` |
| PHP | `query: string, variables: ?array null = null, context: array [] = []` | `list` |
| Ruby | `query, variables: {}, context: {}, operation_name: nil` | `untyped` |
| Node | `query: string, variables?: Record<string, unknown>, context?: Record<string, unknown>` | `GraphQLResult` |

#### `expect`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `type: str, value: str = None` | `Token` |
| PHP | `type: string, value: ?string null = null` | `list` |
| Ruby | `type, value = nil` | `untyped` |
| Node | `type: string, value?: string` | `Token` |

#### `from_orm`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `orm_class` | `untyped` |
| PHP | `ormInstance: ORM` | `Self` |
| Ruby | `klass` | `untyped` |
| Node | `modelClass: {       tableName: string;       fields: Record<string, { type: string; primaryKey?: boolean }>;       name?: string;     }, adapter?: {       query: <T = Record<string, unknown>>(sql: string, params?: unknown[]) => T[];       execute: (sql: string, params?: unknown[]) => unknown;     }` | `GraphQL` |

#### `match`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `type: str, value: str = None` | `Token|None` |
| PHP | `type: string, value: ?string null = null` | `list|None` |
| Ruby | `type, value = nil` | `untyped` |
| Node | `type: string, value?: string` | `Token|None` |

#### `parse`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `type_str: str` | `GraphQLType` |
| PHP | `typeStr: string` | `Self` |
| Ruby | `type_str` | `untyped` |
| Node | `typeStr: string` | `GraphQLType` |

#### `peek`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `Token|None` |
| PHP | `offset: int 0 = 0` | `list|None` |
| Ruby | `offset = 0` | `untyped` |
| Node | `` | `Token|None` |

## Api

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `add_headers` | `headers` | `headers` | `headers` | `headers` | ✅ |
| `delete` | `path, body` | `path, body` | `path, body` | `path, body?` | ℹ️ return type differs |
| `get` | `path, params` | `path, params` | `path, params` | `path, params?` | ℹ️ return type differs |
| `patch` | `path, body, content_type` | `path, body, contentType` | `path, body, content_type` | `path, body?, contentType` | ℹ️ return type differs |
| `post` | `path, body, content_type` | `path, body, contentType` | `path, body, content_type` | `path, body?, contentType` | ℹ️ return type differs |
| `put` | `path, body, content_type` | `path, body, contentType` | `path, body, content_type` | `path, body?, contentType` | ℹ️ return type differs |
| `send_request` | `method, path, body, content_type` | `method, path, body, contentType` | `method, path, body, content_type` | `method, path, body?, contentType` | ℹ️ return type differs |
| `set_basic_auth` | `username, password` | `username, password` | `username, password` | `username, password` | ✅ |
| `set_bearer_token` | `token` | `token` | `token` | `token` | ✅ |

### Mismatch Details

#### `delete`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str = '', body = None` | `dict` |
| PHP | `path: string '' = '', body: mixed null = null` | `list` |
| Ruby | `path, body: nil` | `untyped` |
| Node | `path: string, body?: unknown` | `ApiResult` |

#### `get`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str = '', params: dict = None` | `dict` |
| PHP | `path: string '' = '', params: array [] = []` | `list` |
| Ruby | `path, params: {}` | `untyped` |
| Node | `path: string, params?: Record<string, string>` | `ApiResult` |

#### `patch`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str = '', body = None, content_type: str = 'application/json'` | `dict` |
| PHP | `path: string '' = '', body: mixed null = null, contentType: string 'application/json' = 'application/json'` | `list` |
| Ruby | `path, body: nil, content_type: "application/json"` | `untyped` |
| Node | `path: string, body?: unknown, contentType: string = "application/json"` | `ApiResult` |

#### `post`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str = '', body = None, content_type: str = 'application/json'` | `dict` |
| PHP | `path: string '' = '', body: mixed null = null, contentType: string 'application/json' = 'application/json'` | `list` |
| Ruby | `path, body: nil, content_type: "application/json"` | `untyped` |
| Node | `path: string, body?: unknown, contentType: string = "application/json"` | `ApiResult` |

#### `put`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str = '', body = None, content_type: str = 'application/json'` | `dict` |
| PHP | `path: string '' = '', body: mixed null = null, contentType: string 'application/json' = 'application/json'` | `list` |
| Ruby | `path, body: nil, content_type: "application/json"` | `untyped` |
| Node | `path: string, body?: unknown, contentType: string = "application/json"` | `ApiResult` |

#### `send_request`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `method: str, path: str = '', body = None, content_type: str = 'application/json'` | `dict` |
| PHP | `method: string 'GET' = 'GET', path: string '' = '', body: mixed null = null, contentType: string 'application/json' = 'application/json'` | `list` |
| Ruby | `method = "GET", path = "", body: nil, content_type: "application/json"` | `untyped` |
| Node | `method: string, path: string, body?: unknown, contentType: string = "application/json"` | `ApiResult` |

## Cache

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `cache_clear` | `()` | `()` | `()` | `()` | ✅ |
| `cache_delete` | `key` | `key` | `key` | `key` | ✅ |
| `cache_get` | `key` | `key` | `key` | `key` | ✅ |
| `cache_set` | `key, value, ttl` | `key, value, ttl` | `key, value` | `key, value, ttl?` | ✅ |
| `cache_stats` | `()` | `()` | `()` | `()` | ✅ |
| `clear_cache` | `()` | `()` | `()` | `()` | ✅ |
| `sweep` | `()` | `()` | `()` | `()` | ✅ |

## Container

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `get` | `name` | `name` | `name` | `name` | ✅ |
| `has` | `name` | `name` | `name` | `name` | ✅ |
| `register` | `name, factory` | `name, factory` | `name, instance, handler` | `name, factory` | ✅ |
| `reset` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `singleton` | `name, factory` | `name, factory` | `name, handler` | `name, factory` | ✅ |

### Mismatch Details

#### `reset`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `None` |
| PHP | `` | `bool` |
| Ruby | `` | `untyped` |
| Node | `` | `None` |

## Events

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `clear` | `()` | `()` | `()` | `()` | ✅ |
| `emit` | `event` | `event` | `event` | `event` | ✅ |
| `emit_async` | `event` | `event` | `event` | `event` | ✅ |
| `events` | `()` | `()` | `()` | `()` | ✅ |
| `listeners` | `event` | `event` | `event` | `event` | ℹ️ return type differs |
| `off` | `event, listener` | `event, callback` | `event, callback` | `event, callback?` | ✅ |
| `on` | `event, listener, priority` | `event, callback, priority` | `event, priority, handler` | `event, callback, priority` | ✅ |
| `once` | `event, listener, priority` | `event, callback, priority` | `event, priority, handler` | `event, callback, priority` | ✅ |

### Mismatch Details

#### `listeners`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `event: str` | `list` |
| PHP | `event: string` | `list` |
| Ruby | `event` | `untyped` |
| Node | `event: string` | `list None>` |

## WebSocket

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `broadcast` | `message, exclude_self` | `message, includeSelf` | `message` | `message` | ✅ |
| `broadcast_to_room` | `room_name, message, exclude_self` | `roomName, message, excludeSelf` | `room_name, message` | `roomName, message, excludeIds?` | ✅ |
| `build_frame` | `opcode, payload, fin` | `message, opcode` | `opcode, data` | `opcode, payload, fin` | ℹ️ return type differs |
| `close` | `code, reason` | `code, reason` | `()` | `()` | ✅ |
| `compute_accept_key` | `key` | `key` | `key` | `key` | ✅ |
| `get_client_rooms` | `client_id` | `clientId` | `client_id` | `clientId` | ✅ |
| `get_clients` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `get_room_connections` | `room_name` | `roomName` | `room_name` | `roomName` | ✅ |
| `join_room` | `room_name` | `roomName` | `room_name` | `roomName` | ✅ |
| `leave_room` | `room_name` | `roomName` | `room_name` | `roomName` | ✅ |
| `on` | `event, handler` | `event, handler` | `event, handler` | `event, handler` | ℹ️ return type differs |
| `on_close` | `handler` | `handler` | `handler` | `handler` | ✅ |
| `on_message` | `handler` | `handler` | `handler` | `handler` | ✅ |
| `room_count` | `room_name` | `roomName` | `room_name` | `roomName` | ✅ |
| `route` | `path, handler` | `path, handler` | `path, handler` | `path, handler` | ℹ️ return type differs |
| `send` | `message` | `message` | `message` | `message` | ✅ |
| `send_json` | `data` | `data` | `data` | `data` | ✅ |
| `send_to` | `client_id, message` | `clientId, message` | `conn_id, message` | `clientId, message` | ✅ |
| `start` | `()` | `()` | `()` | `()` | ✅ |
| `stop` | `()` | `()` | `()` | `()` | ✅ |

### Mismatch Details

#### `build_frame`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `opcode: int, payload: bytes, fin: bool = True` | `bytes` |
| PHP | `message: string, opcode: int self::OP_TEXT = self::OP_TEXT` | `str` |
| Ruby | `opcode, data, fin: true` | `untyped` |
| Node | `opcode: number, payload: Buffer, fin: boolean = true` | `Buffer` |

#### `get_clients`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `Map<str, WebSocketClient>` |

#### `on`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `event: str, handler: Callable` | `untyped` |
| PHP | `event: string, handler: callable` | `Self` |
| Ruby | `event, &block` | `untyped` |
| Node | `event: string, handler: Function` | `WebSocketServer` |

#### `route`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str, handler: Callable | None = None` | `untyped` |
| PHP | `path: string, handler: ?callable null = null` | `callable|Self` |
| Ruby | `path, &block` | `untyped` |
| Node | `path: string, handler: (conn: WebSocketConnection) => void | Promise<void>` | `None` |

## WSDL

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `generate_wsdl` | `endpoint_url` | `endpointUrl` | `endpoint_url` | `endpointUrl?` | ✅ |
| `handle` | `()` | `()` | `()` | `soapXml` | ℹ️ return type differs |
| `on_request` | `request` | `request` | `request` | `_request` | ✅ |
| `on_result` | `result` | `result` | `result` | `result` | ✅ |
| `wsdl_operation` | `response_schema` | `returnTypes` | `()` | `config?` | ✅ |

### Mismatch Details

#### `handle`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `str` |
| PHP | `` | `Response` |
| Ruby | `` | `untyped` |
| Node | `soapXml: string = ""` | `str` |

## Swagger

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `generate` | `routes` | `routes` | `routes` | `routes, models` | ℹ️ return type differs |

### Mismatch Details

#### `generate`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `routes: list[dict]` | `dict` |
| PHP | `routes: array [] = []` | `dict` |
| Ruby | `routes = []` | `untyped` |
| Node | `routes: RouteDefinition[], models: ModelDefinition[] = []` | `OpenAPISpec` |

## I18n

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `add_translation` | `locale, key, value` | `locale, key, value` | `locale, key, value` | `locale, key, value` | ✅ |
| `available_locales` | `()` | `()` | `()` | `()` | ✅ |
| `get_locale` | `()` | `()` | `()` | `()` | ✅ |
| `load_translations` | `locale` | `locale` | `locale` | `locale` | ✅ |
| `set_locale` | `locale` | `locale` | `locale` | `locale` | ✅ |
| `t` | `key` | `key, params, locale` | `key` | `key, params?, locale?` | ✅ |
| `translate` | `key, params, locale` | `key, params, locale` | `key, params` | `key, params?, locale?` | ✅ |

## Seeder

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `address` | `()` | `()` | `()` | `()` | ✅ |
| `boolean` | `()` | `()` | `()` | `()` | ✅ |
| `choice` | `items` | `items` | `items` | `items` | ✅ |
| `city` | `()` | `()` | `()` | `()` | ✅ |
| `color_hex` | `()` | `()` | `()` | `()` | ✅ |
| `company` | `()` | `()` | `()` | `()` | ✅ |
| `country` | `()` | `()` | `()` | `()` | ✅ |
| `credit_card` | `()` | `()` | `()` | `()` | ✅ |
| `currency` | `()` | `()` | `()` | `()` | ✅ |
| `date` | `start_year, end_year` | `start, end` | `()` | `start?, end?` | ✅ |
| `datetime` | `start_year, end_year` | `startYear, endYear` | `()` | `startYear, endYear` | ℹ️ return type differs |
| `email` | `()` | `()` | `()` | `()` | ✅ |
| `first_name` | `()` | `()` | `()` | `()` | ✅ |
| `for_field` | `field_def, column_name` | `fieldDef, columnName` | `field_def, column_name` | `fieldDef, columnName?` | ✅ |
| `integer` | `min_val, max_val` | `min, max` | `()` | `min, max` | ✅ |
| `ip_address` | `()` | `()` | `()` | `()` | ✅ |
| `job_title` | `()` | `()` | `()` | `()` | ✅ |
| `last_name` | `()` | `()` | `()` | `()` | ✅ |
| `name` | `()` | `()` | `()` | `()` | ✅ |
| `numeric` | `min_val, max_val, decimals` | `min, max, decimals` | `()` | `min, max, decimals` | ℹ️ return type differs |
| `paragraph` | `sentences` | `sentences` | `()` | `sentences` | ✅ |
| `phone` | `()` | `()` | `()` | `()` | ✅ |
| `run` | `fn, count` | `seeder, count` | `count, handler` | `fn, count` | ✅ |
| `seed` | `seed` | `seed` | `seed` | `seed` | ℹ️ return type differs |
| `seed_dir` | `seed_folder` | `seedDir` | `()` | `seedDir?` | ✅ |
| `seed_orm` | `orm_class, count, overrides, clear, seed` | `ormClass, count, overrides, clear, seed` | `orm_class` | `ormClass, count, overrides?, seed?` | ✅ |
| `seed_table` | `db, table, count, field_map, overrides` | `db, tableName, count, fieldMap, overrides` | `table_name, columns` | `db, tableName, count, fieldMap?, overrides?` | ✅ |
| `sentence` | `words` | `words` | `()` | `words` | ✅ |
| `text` | `paragraphs` | `paragraphs` | `()` | `paragraphs` | ✅ |
| `url` | `()` | `()` | `()` | `()` | ✅ |
| `uuid` | `()` | `()` | `()` | `()` | ✅ |
| `word` | `()` | `()` | `()` | `()` | ✅ |
| `zip_code` | `()` | `()` | `()` | `()` | ✅ |

### Mismatch Details

#### `datetime`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `start_year: int = 2020, end_year: int = 2025` | `str` |
| PHP | `startYear: int 2020 = 2020, endYear: int 2025 = 2025` | `str` |
| Ruby | `start_year: 2020, end_year: 2026` | `untyped` |
| Node | `startYear = 2020, endYear = 2025` | `Date` |

#### `numeric`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `min_val: float = 0.0, max_val: float = 1000.0, decimals: int = 2` | `float` |
| PHP | `min: float 0.0 = 0.0, max: float 1000.0 = 1000.0, decimals: int 2 = 2` | `float` |
| Ruby | `min: 0.0, max: 1000.0, decimals: 2` | `untyped` |
| Node | `min = 0, max = 1000, decimals = 2` | `int` |

#### `seed`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `seed: int` | `FakeData` |
| PHP | `seed: int` | `Self` |
| Ruby | `seed` | `untyped` |
| Node | `seed: number` | `FakeData` |

## QueryBuilder

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `count` | `()` | `()` | `()` | `()` | ✅ |
| `exists` | `()` | `()` | `()` | `()` | ✅ |
| `first` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `from_table` | `table_name, db` | `table, db` | `table_name` | `tableName, db?` | ℹ️ return type differs |
| `get` | `()` | `()` | `()` | `()` | ✅ |
| `group_by` | `column` | `column` | `column` | `column` | ℹ️ return type differs |
| `having` | `expression, params` | `expression, params` | `expression, params` | `expression, params` | ℹ️ return type differs |
| `join` | `table, on_clause` | `table, on` | `table, on_clause` | `table, onClause` | ℹ️ return type differs |
| `left_join` | `table, on_clause` | `table, on` | `table, on_clause` | `table, onClause` | ℹ️ return type differs |
| `limit` | `count, offset` | `count, offset` | `count, offset` | `count, offset?` | ℹ️ return type differs |
| `or_where` | `condition, params` | `condition, params` | `condition, params` | `condition, params` | ℹ️ return type differs |
| `order_by` | `expression` | `expression` | `expression` | `expression` | ℹ️ return type differs |
| `select` | `*columns` | `*columns` | `*columns` | `...cols` | ℹ️ return type differs |
| `to_mongo` | `()` | `()` | `()` | `()` | ✅ |
| `to_sql` | `()` | `()` | `()` | `()` | ✅ |
| `where` | `condition, params` | `condition, params` | `condition, params` | `condition, params` | ℹ️ return type differs |

### Mismatch Details

#### `first`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict|None` |
| PHP | `` | `list|None` |
| Ruby | `` | `untyped` |
| Node | `` | `Self|None` |

#### `from_table`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `table_name: str, db = None` | `QueryBuilder` |
| PHP | `table: string, db: ?DatabaseAdapter null = null` | `Self` |
| Ruby | `table_name, db: nil` | `untyped` |
| Node | `tableName: string, db?: DatabaseAdapter` | `QueryBuilder` |

#### `group_by`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `column: str` | `QueryBuilder` |
| PHP | `column: string` | `Self` |
| Ruby | `column` | `untyped` |
| Node | `column: string` | `QueryBuilder` |

#### `having`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `expression: str, params: list = None` | `QueryBuilder` |
| PHP | `expression: string, params: array [] = []` | `Self` |
| Ruby | `expression, params = []` | `untyped` |
| Node | `expression: string, params: unknown[] = []` | `QueryBuilder` |

#### `join`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `table: str, on_clause: str` | `QueryBuilder` |
| PHP | `table: string, on: string` | `Self` |
| Ruby | `table, on_clause` | `untyped` |
| Node | `table: string, onClause: string` | `QueryBuilder` |

#### `left_join`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `table: str, on_clause: str` | `QueryBuilder` |
| PHP | `table: string, on: string` | `Self` |
| Ruby | `table, on_clause` | `untyped` |
| Node | `table: string, onClause: string` | `QueryBuilder` |

#### `limit`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `count: int, offset: int = None` | `QueryBuilder` |
| PHP | `count: int, offset: ?int null = null` | `Self` |
| Ruby | `count, offset = nil` | `untyped` |
| Node | `count: number, offset?: number` | `QueryBuilder` |

#### `or_where`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `condition: str, params: list = None` | `QueryBuilder` |
| PHP | `condition: string, params: array [] = []` | `Self` |
| Ruby | `condition, params = []` | `untyped` |
| Node | `condition: string, params: unknown[] = []` | `QueryBuilder` |

#### `order_by`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `expression: str` | `QueryBuilder` |
| PHP | `expression: string` | `Self` |
| Ruby | `expression` | `untyped` |
| Node | `expression: string` | `QueryBuilder` |

#### `select`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `*columns` | `QueryBuilder` |
| PHP | `*columns: string` | `Self` |
| Ruby | `*columns` | `untyped` |
| Node | `...cols: string[]` | `QueryBuilder` |

#### `where`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `condition: str, params: list = None` | `QueryBuilder` |
| PHP | `condition: string, params: array [] = []` | `Self` |
| Ruby | `condition, params = []` | `untyped` |
| Node | `condition: string, params: unknown[] = []` | `QueryBuilder` |

## Validator

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `email` | `field` | `field` | `field` | `field` | ℹ️ return type differs |
| `errors` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `in_list` | `field, allowed` | `field, allowed` | `field, allowed` | `field, allowed` | ℹ️ return type differs |
| `integer` | `field` | `field` | `field` | `field` | ℹ️ return type differs |
| `is_valid` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `max` | `field, maximum` | `field, maximum` | `field, maximum` | `field, maximum` | ℹ️ return type differs |
| `max_length` | `field, length` | `field, length` | `field, length` | `field, length` | ℹ️ return type differs |
| `min` | `field, minimum` | `field, minimum` | `field, minimum` | `field, minimum` | ℹ️ return type differs |
| `min_length` | `field, length` | `field, length` | `field, length` | `field, length` | ℹ️ return type differs |
| `regex` | `field, pattern` | `field, pattern` | `field, pattern` | `field, pattern` | ℹ️ return type differs |
| `required` | `*fields` | `*fields` | `*fields` | `...fields` | ℹ️ return type differs |

### Mismatch Details

#### `email`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `field: str` | `Validator` |
| PHP | `field: string` | `Self` |
| Ruby | `field` | `untyped` |
| Node | `field: string` | `Self` |

#### `errors`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list]` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `list` |

#### `in_list`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `field: str, allowed: list` | `Validator` |
| PHP | `field: string, allowed: array` | `Self` |
| Ruby | `field, allowed` | `untyped` |
| Node | `field: string, allowed: unknown[]` | `Self` |

#### `integer`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `field: str` | `Validator` |
| PHP | `field: string` | `Self` |
| Ruby | `field` | `untyped` |
| Node | `field: string` | `Self` |

#### `is_valid`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `bool` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `bool` |

#### `max`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `field: str, maximum` | `Validator` |
| PHP | `field: string, maximum: int|float` | `Self` |
| Ruby | `field, maximum` | `untyped` |
| Node | `field: string, maximum: number` | `Self` |

#### `max_length`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `field: str, length: int` | `Validator` |
| PHP | `field: string, length: int` | `Self` |
| Ruby | `field, length` | `untyped` |
| Node | `field: string, length: number` | `Self` |

#### `min`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `field: str, minimum` | `Validator` |
| PHP | `field: string, minimum: int|float` | `Self` |
| Ruby | `field, minimum` | `untyped` |
| Node | `field: string, minimum: number` | `Self` |

#### `min_length`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `field: str, length: int` | `Validator` |
| PHP | `field: string, length: int` | `Self` |
| Ruby | `field, length` | `untyped` |
| Node | `field: string, length: number` | `Self` |

#### `regex`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `field: str, pattern: str` | `Validator` |
| PHP | `field: string, pattern: string` | `Self` |
| Ruby | `field, pattern` | `untyped` |
| Node | `field: string, pattern: RegExp | string` | `Self` |

#### `required`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `*fields` | `Validator` |
| PHP | `*fields: string` | `Self` |
| Ruby | `*fields` | `untyped` |
| Node | `...fields: string[]` | `Self` |

## HtmlElement

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `add_html_helpers` | `namespace` | `namespace` | `namespace` | `h` | ✅ |

## Testing

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `assert_equal` | `args, expected` | `args, expected` | `args, expected` | `args, expected` | ℹ️ return type differs |
| `assert_false` | `args` | `args` | `args` | `args` | ℹ️ return type differs |
| `assert_raises` | `exception_class, args` | `exceptionClass, args` | `exception_class, args` | `errorClass, args` | ℹ️ return type differs |
| `assert_true` | `args` | `args` | `args` | `args` | ℹ️ return type differs |
| `reset` | `()` | `()` | `()` | `()` | ✅ |
| `run_all` | `quiet, failfast` | `quiet, failfast` | `()` | `options` | ℹ️ return type differs |
| `tests` | `*assertions` | `assertions, fn, name` | `*assertions, handler` | `...assertions` | ⚠️ param count differs |

### Mismatch Details

#### `assert_equal`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `args: tuple, expected` | `untyped` |
| PHP | `args: array, expected: mixed` | `list` |
| Ruby | `args, expected` | `untyped` |
| Node | `args: unknown[], expected: unknown` | `Assertion` |

#### `assert_false`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `args: tuple` | `untyped` |
| PHP | `args: array` | `list` |
| Ruby | `args` | `untyped` |
| Node | `args: unknown[]` | `Assertion` |

#### `assert_raises`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `exception_class: type, args: tuple` | `untyped` |
| PHP | `exceptionClass: string, args: array` | `list` |
| Ruby | `exception_class, args` | `untyped` |
| Node | `errorClass: new (...a: unknown[]) => Error, args: unknown[]` | `Assertion` |

#### `assert_true`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `args: tuple` | `untyped` |
| PHP | `args: array` | `list` |
| Ruby | `args` | `untyped` |
| Node | `args: unknown[]` | `Assertion` |

#### `run_all`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `quiet: bool = False, failfast: bool = False` | `dict` |
| PHP | `quiet: bool false = false, failfast: bool false = false` | `list` |
| Ruby | `quiet: false, failfast: false` | `untyped` |
| Node | `options: { quiet?: boolean; failfast?: boolean } = {}` | `TestResults` |

#### `tests`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `*assertions` | `untyped` |
| PHP | `assertions: array, fn: callable, name: string 'anonymous' = 'anonymous'` | `None` |
| Ruby | `*assertions, name: nil, &block` | `untyped` |
| Node | `...assertions: Assertion[]` | `untyped` |

## Messenger

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `capture` | `to, subject, body, html, cc, bcc, reply_to, from_address, from_name, attachments` | `to, subject, body, html, cc, bcc, replyTo, attachments, headers` | `to, subject, body` | `to, subject, body, html, cc, bcc, replyTo?, attachments, from?` | ℹ️ return type differs |
| `clear` | `folder` | `folder` | `()` | `folder?` | ✅ |
| `count` | `folder` | `folder` | `()` | `folder?` | ✅ |
| `create_messenger` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `delete` | `uid, folder` | `msgId` | `msg_id` | `msgId` | ✅ |
| `folders` | `()` | `()` | `()` | `()` | ✅ |
| `inbox` | `folder, limit, offset` | `folder, limit, offset` | `limit, offset` | `limit, offset, folder` | ✅ |
| `mark_read` | `uid, folder` | `uid, folder` | `uid` | `uid, folder` | ✅ |
| `read` | `uid, folder, mark_read` | `uid, folder, markRead` | `uid` | `uid, folder` | ℹ️ return type differs |
| `search` | `folder, subject, sender, since, before, unseen_only, limit` | `folder, subject, sender, since, before, unseenOnly, limit` | `limit` | `folder, subject?, sender?, since?, before?, unseenOnly, limit` | ✅ |
| `seed` | `count, seed` | `count` | `()` | `count` | ℹ️ return type differs |
| `send` | `to, subject, body, html, text, cc, bcc, reply_to, attachments, headers` | `to, subject, body, html, text, cc, bcc, replyTo, attachments, headers` | `to, subject, body, headers` | `to, subject, body, html, text?, cc?, bcc?, replyTo?, attachments?, headers?` | ℹ️ return type differs |
| `test_connection` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `test_imap_connection` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `unread` | `folder` | `folder` | `()` | `folder` | ✅ |
| `unread_count` | `()` | `()` | `()` | `()` | ✅ |

### Mismatch Details

#### `capture`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `to: str | list[str], subject: str, body: str, html: bool = False, cc: list[str] = None, bcc: list[str] = None, reply_to: str = None, from_address: str = '', from_name: str = '', attachments: list = None` | `dict` |
| PHP | `to: string|array, subject: string, body: string, html: bool false = false, cc: array [] = [], bcc: array [] = [], replyTo: ?string null = null, attachments: array [] = [], headers: array [] = []` | `list` |
| Ruby | `to:, subject:, body:, html: false, cc: [], bcc: [], reply_to: nil, from_address: nil, from_name: nil, attachments: []` | `untyped` |
| Node | `to: string | string[], subject: string, body: string, html: boolean = false, cc: string[] = [], bcc: string[] = [], replyTo?: string, attachments: string[] = [], from?: string` | `SendResult` |

#### `create_messenger`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `**kwargs` | `Messenger` |
| PHP | `` | `Self` |
| Ruby | `**options` | `untyped` |
| Node | `` | `Messenger|DevMailbox` |

#### `read`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `uid: str | bytes, folder: str = 'INBOX', mark_read: bool = True` | `dict` |
| PHP | `uid: int, folder: string 'INBOX' = 'INBOX', markRead: bool true = true` | `list|None` |
| Ruby | `uid, folder: "INBOX", mark_read: true` | `untyped` |
| Node | `uid: string, folder: string = "INBOX"` | `ImapFullMessage` |

#### `seed`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `count: int = 5, seed: int = None` | `int` |
| PHP | `count: int 5 = 5` | `None` |
| Ruby | `count: 5` | `untyped` |
| Node | `count: number = 5` | `None` |

#### `send`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `to: str | list[str], subject: str, body: str, html: bool = False, text: str = None, cc: str | list[str] = None, bcc: str | list[str] = None, reply_to: str = None, attachments: list = None, headers: dict = None` | `dict` |
| PHP | `to: string|array, subject: string, body: string, html: bool false = false, text: ?string null = null, cc: array|string [] = [], bcc: array|string [] = [], replyTo: ?string null = null, attachments: array [] = [], headers: array [] = []` | `list` |
| Ruby | `to:, subject:, body:, html: false, text: nil, cc: [], bcc: [], reply_to: nil, attachments: [], headers: {}` | `untyped` |
| Node | `to: string | string[], subject: string, body: string, html: boolean = false, text?: string, cc?: string | string[], bcc?: string | string[], replyTo?: string, attachments?: string[], headers?: Record<string, string>` | `SendResult` |

#### `test_connection`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `Promise<` |

#### `test_imap_connection`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `Promise<` |

## Logger

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `configure` | `log_dir, level, production` | `logDir, development, minLevel` | `root_dir` | `options` | ✅ |
| `debug` | `message` | `message, context` | `message, context` | `message, data?` | ✅ |
| `error` | `message` | `message, context` | `message, context` | `message, data?` | ✅ |
| `get_request_id` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `info` | `message` | `message, context` | `message, context` | `message, data?` | ✅ |
| `set_request_id` | `request_id` | `requestId` | `id` | `id` | ✅ |
| `warning` | `message` | `message, context` | `message, context` | `message, data?` | ✅ |

### Mismatch Details

#### `get_request_id`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `str|None` |
| PHP | `` | `str|None` |
| Ruby | `` | `untyped` |
| Node | `` | `str|undefined` |

## AI

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `generate_context` | `tool_name` | `toolName` | `tool_name` | `toolName` | ✅ |
| `install_all` | `root` | `root` | `root` | `root` | ✅ |
| `install_selected` | `root, selection` | `root, selection` | `root, selection` | `root, selection` | ✅ |
| `is_installed` | `root, tool` | `root, tool` | `root, tool` | `root, tool` | ✅ |
| `show_menu` | `root` | `root` | `root` | `root` | ✅ |

## Request

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `bearer_token` | `()` | `()` | `()` | `()` | ✅ |
| `header` | `name` | `name` | `name` | `name` | ℹ️ return type differs |
| `param` | `key, default` | `key, default` | `key, default` | `key, defaultValue?` | ✅ |
| `parse_body` | `()` | `()` | `()` | `()` | ℹ️ return type differs |

### Mismatch Details

#### `header`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `name: str` | `str|None` |
| PHP | `name: string` | `str|None` |
| Ruby | `name` | `untyped` |
| Node | `name: string` | `str|undefined` |

#### `parse_body`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict|str|None` |
| PHP | `` | `mixed` |
| Ruby | `` | `untyped` |
| Node | `` | `None` |

## Response

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `add_header` | `name, value` | `name, value` | `key, value` | `name, value` | ℹ️ return type differs |
| `cookie` | `name, value, path, max_age, http_only, secure, same_site` | `name, value, options` | `name, value, opts` | `name, value, options?` | ℹ️ return type differs |
| `error` | `code, message, status_code` | `code, message, status` | `code, message, status_code` | `code, message, status?` | ℹ️ return type differs |
| `error_response` | `code, message, status` | `code, message, status` | `code, message, status` | `code, message, status` | ✅ |
| `file` | `file_path, download_name` | `path, contentType, download` | `path, content_type` | `filePath, options?` | ℹ️ return type differs |
| `get_framework_frond` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `get_frond` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `header` | `name, value` | `name, value` | `name, value` | `name, value` | ℹ️ return type differs |
| `html` | `content, status_code` | `content, status` | `content, status_or_opts` | `content, status?` | ℹ️ return type differs |
| `json` | `data, status_code` | `data, status` | `data, status_or_opts` | `data, status?` | ℹ️ return type differs |
| `redirect` | `url, status_code` | `url, status` | `url, status_or_opts` | `url, code?` | ℹ️ return type differs |
| `render` | `template, data` | `templateName, data, status, templateDir` | `template_path, data` | `templateName, data?, status?, templateDir?` | ℹ️ return type differs |
| `send` | `data, status_code, content_type` | `data, statusCode, contentType` | `data, content_type` | `data, statusCode?, contentType?` | ℹ️ return type differs |
| `set_frond` | `engine` | `frond` | `engine` | `engine` | ✅ |
| `status` | `code` | `code` | `code` | `code` | ℹ️ return type differs |
| `stream` | `source, content_type` | `source, contentType` | `content_type, handler` | `source, contentType` | ℹ️ return type differs |
| `text` | `content, status_code` | `content, status` | `content, status_or_opts` | `content, status?` | ℹ️ return type differs |
| `xml` | `content, status_code` | `content, status` | `content` | `content, status?` | ℹ️ return type differs |

### Mismatch Details

#### `add_header`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `name: str, value: str` | `Response` |
| PHP | `name: string, value: string` | `Self` |
| Ruby | `key, value` | `untyped` |
| Node | `name: string, value: string` | `None` |

#### `cookie`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `name: str, value: str, path: str = '/', max_age: int = 3600, http_only: bool = True, secure: bool = False, same_site: str = 'Lax'` | `Response` |
| PHP | `name: string, value: string, options: array [] = []` | `Self` |
| Ruby | `name, value, opts = {}` | `untyped` |
| Node | `name: string, value: string, options?: CookieOptions` | `Tina4Response` |

#### `error`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `code: str, message: str, status_code: int = 400` | `Response` |
| PHP | `code: string, message: string, status: int 400 = 400` | `Self` |
| Ruby | `code, message, status_code = 400` | `untyped` |
| Node | `code: string, message: string, status?: number` | `Tina4Response` |

#### `file`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `file_path: str, download_name: str = None` | `Response` |
| PHP | `path: string, contentType: ?string null = null, download: bool false = false` | `Self` |
| Ruby | `path, content_type: nil, download: false` | `untyped` |
| Node | `filePath: string, options?: { download?: boolean; contentType?: string }` | `Tina4Response` |

#### `get_framework_frond`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `Frond` |
| Ruby | `` | `untyped` |
| Node | `` | `InstanceType<any>|None` |

#### `get_frond`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `Frond` |
| Ruby | `` | `untyped` |
| Node | `` | `InstanceType<any>` |

#### `header`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `name: str, value: str` | `Response` |
| PHP | `name: string, value: string` | `Self` |
| Ruby | `name, value = nil` | `untyped` |
| Node | `name: string, value: string | number | readonly string[]` | `Tina4Response` |

#### `html`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `content: str, status_code: int = None` | `Response` |
| PHP | `content: string, status: int 200 = 200` | `Self` |
| Ruby | `content, status_or_opts = nil, status: nil` | `untyped` |
| Node | `content: string, status?: number` | `Tina4Response` |

#### `json`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `data, status_code: int = None` | `Response` |
| PHP | `data: mixed, status: int 200 = 200` | `Self` |
| Ruby | `data, status_or_opts = nil, status: nil` | `untyped` |
| Node | `data: unknown, status?: number` | `Tina4Response` |

#### `redirect`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `url: str, status_code: int = 302` | `Response` |
| PHP | `url: string, status: int 302 = 302` | `Self` |
| Ruby | `url, status_or_opts = nil, status: nil` | `untyped` |
| Node | `url: string, code?: number` | `Tina4Response` |

#### `render`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `template: str, data: dict = None` | `Response` |
| PHP | `templateName: string, data: array [] = [], status: int 200 = 200, templateDir: string 'src/templates' = 'src/templates'` | `Self` |
| Ruby | `template_path, data = {}, status: 200, template_dir: nil` | `untyped` |
| Node | `templateName: string, data?: Record<string, unknown>, status?: number, templateDir?: string` | `Tina4Response` |

#### `send`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `data = None, status_code: int = None, content_type: str = None` | `Response` |
| PHP | `data: mixed null = null, statusCode: ?int null = null, contentType: ?string null = null` | `Self` |
| Ruby | `data = nil, status_code: nil, content_type: nil` | `untyped` |
| Node | `data: unknown, statusCode?: number, contentType?: string` | `Tina4Response` |

#### `status`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `code: int` | `Response` |
| PHP | `code: int` | `Self` |
| Ruby | `code = nil` | `untyped` |
| Node | `code: number` | `Tina4Response` |

#### `stream`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `source, content_type: str = 'text/event-stream'` | `Response` |
| PHP | `source: callable, contentType: string 'text/event-stream' = 'text/event-stream'` | `Self` |
| Ruby | `content_type: "text/event-stream", &block` | `untyped` |
| Node | `source: AsyncIterable<string | Buffer>, contentType: string = "text/event-stream"` | `Tina4Response` |

#### `text`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `content: str, status_code: int = None` | `Response` |
| PHP | `content: string, status: int 200 = 200` | `Self` |
| Ruby | `content, status_or_opts = nil, status: nil` | `untyped` |
| Node | `content: string, status?: number` | `Tina4Response` |

#### `xml`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `content: str, status_code: int = None` | `Response` |
| PHP | `content: string, status: int 200 = 200` | `Self` |
| Ruby | `content, status: 200` | `untyped` |
| Node | `content: string, status?: number` | `Tina4Response` |

## Middleware

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `after_log` | `request, response` | `request, response` | `request, response` | `req, res` | ℹ️ return type differs |
| `before_cors` | `request, response` | `request, response` | `request, response` | `req, res` | ℹ️ return type differs |
| `before_csrf` | `request, response` | `request, response` | `request, response` | `req, res` | ℹ️ return type differs |
| `before_log` | `request, response` | `request, response` | `request, response` | `req, res` | ℹ️ return type differs |
| `before_rate_limit` | `request, response` | `request, response` | `request, response` | `req, res` | ℹ️ return type differs |
| `before_security` | `request, response` | `request, response` | `request, response` | `req, res` | ℹ️ return type differs |
| `check` | `ip` | `ip` | `ip` | `ip` | ℹ️ return type differs |
| `get_global` | `()` | `()` | `()` | `()` | ✅ |
| `is_preflight` | `request` | `method` | `request` | `method` | ✅ |
| `reset` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `run_after` | `middleware_classes, request, response` | `middlewareClasses, request, response` | `middleware_classes, request, response` | `classes, req, res` | ℹ️ return type differs |
| `run_before` | `middleware_classes, request, response` | `middlewareClasses, request, response` | `middleware_classes, request, response` | `classes, req, res` | ℹ️ return type differs |
| `use` | `middleware_class` | `class` | `klass` | `fn` | ✅ |

### Mismatch Details

#### `after_log`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `request, response` | `untyped` |
| PHP | `request: Request, response: Response` | `list` |
| Ruby | `request, response` | `untyped` |
| Node | `req: Tina4Request, res: Tina4Response` | `[Tina4Request, Tina4Response]` |

#### `before_cors`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `request, response` | `untyped` |
| PHP | `request: Request, response: Response` | `list` |
| Ruby | `request, response` | `untyped` |
| Node | `req: Tina4Request, res: Tina4Response` | `[Tina4Request, Tina4Response]` |

#### `before_csrf`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `request, response` | `untyped` |
| PHP | `request: Request, response: Response` | `list` |
| Ruby | `request, response` | `untyped` |
| Node | `req: Tina4Request, res: Tina4Response` | `[Tina4Request, Tina4Response]` |

#### `before_log`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `request, response` | `untyped` |
| PHP | `request: Request, response: Response` | `list` |
| Ruby | `request, response` | `untyped` |
| Node | `req: Tina4Request, res: Tina4Response` | `[Tina4Request, Tina4Response]` |

#### `before_rate_limit`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `request, response` | `untyped` |
| PHP | `request: Request, response: Response` | `list` |
| Ruby | `request, response` | `untyped` |
| Node | `req: Tina4Request, res: Tina4Response` | `[Tina4Request, Tina4Response]` |

#### `before_security`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `request, response` | `untyped` |
| PHP | `request: Request, response: Response` | `list` |
| Ruby | `request, response` | `untyped` |
| Node | `req: Tina4Request, res: Tina4Response` | `[Tina4Request, Tina4Response]` |

#### `check`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `ip: str` | `untyped` |
| PHP | `ip: string` | `list` |
| Ruby | `ip` | `untyped` |
| Node | `ip: string` | `[bool,` |

#### `reset`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `None` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `None` |

#### `run_after`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `middleware_classes, request, response` | `untyped` |
| PHP | `middlewareClasses: array, request: Request, response: Response` | `list` |
| Ruby | `middleware_classes, request, response` | `untyped` |
| Node | `classes: any[], req: Tina4Request, res: Tina4Response` | `[Tina4Request, Tina4Response]` |

#### `run_before`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `middleware_classes, request, response` | `untyped` |
| PHP | `middlewareClasses: array, request: Request, response: Response` | `list` |
| Ruby | `middleware_classes, request, response` | `untyped` |
| Node | `classes: any[], req: Tina4Request, res: Tina4Response` | `[Tina4Request, Tina4Response, bool]` |

## AutoCrud

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `clear` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `discover` | `models_dir, prefix` | `modelsDir` | `models_dir` | `discoveredModels, prefix` | ✅ |
| `generate_routes` | `()` | `()` | `()` | `()` | ✅ |
| `models` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `register` | `model_class, prefix` | `modelClass` | `model_class` | `model, prefix` | ℹ️ return type differs |

### Mismatch Details

#### `clear`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `dict` |
| Ruby | `` | `untyped` |
| Node | `` | `None` |

#### `models`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `dict` |
| Ruby | `` | `untyped` |
| Node | `` | `Map<str, DiscoveredModel>` |

#### `register`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `model_class, prefix: str = '/api'` | `untyped` |
| PHP | `modelClass: string` | `Self` |
| Ruby | `model_class` | `untyped` |
| Node | `model: DiscoveredModel, prefix: string = "/api"` | `None` |

## SqlTranslation

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `auto_increment_syntax` | `sql, engine` | `sql, dialect` | `sql, engine` | `sql, engine` | ✅ |
| `boolean_to_int` | `sql` | `sql` | `sql` | `sql` | ✅ |
| `clear` | `()` | `()` | `()` | `()` | ✅ |
| `clear_tag` | `tag` | `tag` | `tag` | `tag` | ✅ |
| `concat_pipes_to_func` | `sql` | `sql` | `sql` | `sql` | ✅ |
| `delete` | `key` | `key` | `key` | `key` | ✅ |
| `get` | `key, default` | `key` | `key, default` | `key` | ✅ |
| `has` | `key` | `key` | `key` | `key` | ✅ |
| `ilike_to_like` | `sql` | `sql` | `sql` | `sql` | ✅ |
| `limit_to_rows` | `sql` | `sql` | `sql` | `sql` | ✅ |
| `limit_to_top` | `sql` | `sql` | `sql` | `sql` | ✅ |
| `placeholder_style` | `sql, style` | `sql, style` | `sql, style` | `sql, style` | ✅ |
| `query_key` | `sql, params` | `sql, params` | `sql, params` | `sql, params?` | ✅ |
| `remember` | `key, ttl, factory` | `key, ttl, factory` | `key, ttl, handler` | `key, ttl, factory` | ✅ |
| `set` | `key, value, ttl, tags` | `key, value, ttl, tags` | `key, value` | `key, value, ttl?, tags` | ✅ |
| `size` | `()` | `()` | `()` | `()` | ✅ |
| `sweep` | `()` | `()` | `()` | `()` | ✅ |

## Metrics

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `file_detail` | `file_path` | `filePath` | `file_path` | `filePath` | ✅ |
| `full_analysis` | `root` | `root` | `root` | `root` | ✅ |
| `quick_metrics` | `root` | `root` | `root` | `root` | ✅ |

## ErrorOverlay

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `is_debug_mode` | `()` | `()` | `()` | `()` | ✅ |
| `render_error_overlay` | `exception, request` | `e, request` | `exception` | `error, request?` | ✅ |
| `render_production_error` | `status_code, message` | `statusCode, message, path` | `()` | `statusCode, message, path` | ✅ |

## DotEnv

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `all_env` | `()` | `()` | `()` | `()` | ✅ |
| `get_env` | `key, default` | `key, default` | `key, default` | `key, defaultValue?` | ℹ️ return type differs |
| `has_env` | `key` | `key` | `key` | `key` | ✅ |
| `is_truthy` | `val` | `val` | `val` | `val` | ✅ |
| `load_env` | `file_path, override` | `path, overwrite` | `root_dir` | `path?` | ℹ️ return type differs |
| `require_env` | `*keys` | `key` | `*keys` | `key` | ℹ️ return type differs |
| `reset_env` | `()` | `()` | `()` | `()` | ✅ |

### Mismatch Details

#### `get_env`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `key: str, default: str = None` | `str|None` |
| PHP | `key: string, default: ?string null = null` | `str|None` |
| Ruby | `key, default = nil` | `untyped` |
| Node | `key: string, defaultValue?: string` | `str|undefined` |

#### `load_env`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `file_path: str = '.env', override: bool = False` | `dict` |
| PHP | `path: string '.env' = '.env', overwrite: bool false = false` | `None` |
| Ruby | `root_dir = Dir.pwd` | `untyped` |
| Node | `path?: string` | `dict` |

#### `require_env`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `*keys` | `dict` |
| PHP | `key: string` | `str` |
| Ruby | `*keys` | `untyped` |
| Node | `key: string` | `str` |

## DevAdmin

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `capture` | `method, path, status, duration_ms, headers, body_size, ip` | `errorType, message, traceback, file, line` | `error_type, message` | `errorType, message, traceback, file, line` | ⚠️ param count differs |
| `clear` | `category` | `category` | `()` | `category?` | ✅ |
| `clear_all` | `()` | `()` | `()` | `()` | ✅ |
| `clear_resolved` | `()` | `()` | `()` | `()` | ✅ |
| `count` | `()` | `()` | `()` | `folder?` | ✅ |
| `get` | `category, level, limit, offset` | `category` | `()` | `category?, limit` | ✅ |
| `health` | `()` | `()` | `()` | `()` | ✅ |
| `log` | `category, message, data, level` | `category, level, message` | `category, level, message` | `category, level, message, data?` | ✅ |
| `register` | `()` | `()` | `()` | `router` | ⚠️ param count differs |
| `reset` | `()` | `()` | `()` | `()` | ✅ |
| `resolve` | `error_id` | `id` | `id` | `process.cwd(), "node_modules", "tina4-nodejs", "packages", "core", "public", "js", "tina4-dev-admin.min.js"` | ⚠️ param count differs |
| `stats` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `unresolved_count` | `()` | `()` | `()` | `()` | ✅ |

### Mismatch Details

#### `capture`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `method: str, path: str, status: int, duration_ms: float, headers: dict = None, body_size: int = 0, ip: str = ''` | `untyped` |
| PHP | `errorType: string, message: string, traceback: string '' = '', file: string '' = '', line: int 0 = 0` | `None` |
| Ruby | `error_type:, message:, traceback: "", file: "", line: 0` | `untyped` |
| Node | `errorType: string, message: string, traceback = "", file = "", line = 0` | `None` |

#### `register`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `None` |
| Ruby | `` | `untyped` |
| Node | `router: Router` | `None` |

#### `resolve`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `error_id: str` | `bool` |
| PHP | `id: string` | `bool` |
| Ruby | `id` | `untyped` |
| Node | `process.cwd(), "node_modules", "tina4-nodejs", "packages", "core", "public", "js", "tina4-dev-admin.min.js"` | `untyped` |

#### `stats`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `RequestStats` |

## Service

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `clear` | `()` | `()` | `()` | `()` | ✅ |
| `discover` | `service_dir` | `serviceDir` | `service_dir` | `serviceDir?` | ℹ️ return type differs |
| `is_running` | `name` | `name` | `name` | `name` | ✅ |
| `list` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `match_cron` | `pattern, now` | `pattern, now` | `pattern, time` | `pattern, now?` | ✅ |
| `register` | `name, handler, interval, cron, daemon, max_retries` | `name, handler, options` | `name, handler, options, handler` | `name, handler, options` | ✅ |
| `start` | `()` | `name` | `name` | `name?` | ✅ |
| `stop` | `()` | `name` | `name` | `name?` | ✅ |

### Mismatch Details

#### `discover`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `service_dir: str = ''` | `_list[str]` |
| PHP | `serviceDir: string '' = ''` | `list` |
| Ruby | `service_dir = nil` | `untyped` |
| Node | `serviceDir?: string` | `list` |

#### `list`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `_list[dict]` |
| PHP | `` | `dict` |
| Ruby | `` | `untyped` |
| Node | `` | `list` |

## ScssCompiler

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `add_import_path` | `path` | `path` | `path` | `path` | ✅ |
| `compile` | `source` | `source` | `source` | `source` | ✅ |
| `compile_file` | `path` | `path` | `scss_file, output_dir, base_dir` | `filePath` | ✅ |
| `compile_scss` | `scss_dir, output, minify` | `scssDir, output, minify` | `content, base_dir` | `scssDir, output, minify` | ✅ |
| `set_variable` | `name, value` | `name, value` | `name, value` | `name, value` | ✅ |

## RateLimiter

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `apply` | `request, response` | `request, response` | `ip, response` | `request, response` | ℹ️ return type differs |
| `before_rate_limit` | `request, response` | `request, response` | `request, response` | `request, response` | ℹ️ return type differs |
| `check` | `ip` | `ip` | `ip` | `ip` | ℹ️ return type differs |
| `reset` | `()` | `()` | `ip` | `()` | ✅ |

### Mismatch Details

#### `apply`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `request, response` | `untyped` |
| PHP | `request: Request, response: Response` | `list` |
| Ruby | `ip, response` | `untyped` |
| Node | `request: Tina4Request, response: Tina4Response` | `[Tina4Request, Tina4Response]` |

#### `before_rate_limit`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `request, response` | `untyped` |
| PHP | `request: Request, response: Response` | `list` |
| Ruby | `request, response` | `untyped` |
| Node | `request: Tina4Request, response: Tina4Response` | `[Tina4Request, Tina4Response]` |

#### `check`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `ip: str` | `tuple[bool, dict]` |
| PHP | `ip: string` | `list` |
| Ruby | `ip` | `untyped` |
| Node | `ip: string` | `RateLimitResult` |

## Server

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `handle` | `request` | `request` | `env` | `rawReq, rawRes` | ⚠️ param count differs |
| `start` | `host, port, no_browser, no_reload` | `()` | `()` | `config?` | ℹ️ return type differs |
| `stop` | `()` | `()` | `()` | `()` | ✅ |

### Mismatch Details

#### `handle`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `request: Request` | `Response` |
| PHP | `request: Request` | `Response` |
| Ruby | `env` | `untyped` |
| Node | `rawReq: IncomingMessage, rawRes: ServerResponse` | `None` |

#### `start`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `host: str | None = None, port: int | None = None, no_browser: bool = True, no_reload: bool = False` | `untyped` |
| PHP | `` | `None` |
| Ruby | `` | `untyped` |
| Node | `config?: Tina4Config` | `Promise<` |

## TestClient

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `delete` | `path, headers` | `path, headers` | `path, headers` | `path, options?` | ✅ |
| `get` | `path, headers` | `path, headers` | `path, headers` | `path, options?` | ✅ |
| `json` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `patch` | `path, json, body, headers` | `path, json, body, headers` | `path, body, headers` | `path, options?` | ✅ |
| `post` | `path, json, body, headers` | `path, json, body, headers` | `path, body, headers` | `path, options?` | ✅ |
| `put` | `path, json, body, headers` | `path, json, body, headers` | `path, body, headers` | `path, options?` | ✅ |
| `text` | `()` | `()` | `()` | `()` | ✅ |

### Mismatch Details

#### `json`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict|list|None` |
| PHP | `` | `list|None` |
| Ruby | `` | `untyped` |
| Node | `` | `unknown` |

## WebSocketBackplane

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `close` | `()` | `()` | `()` | `()` | ✅ |
| `create_backplane` | `url` | `url` | `()` | `url?` | ℹ️ return type differs |
| `publish` | `channel, message` | `channel, message` | `channel, message` | `channel, message` | ✅ |
| `subscribe` | `channel, callback` | `channel, callback` | `channel, handler` | `channel, callback` | ✅ |
| `unsubscribe` | `channel` | `channel` | `channel` | `channel` | ✅ |

### Mismatch Details

#### `create_backplane`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `url: str | None = None` | `WebSocketBackplane|None` |
| PHP | `url: ?string null = null` | `WebSocketBackplaneInterface|None` |
| Ruby | `url: nil` | `untyped` |
| Node | `url?: string` | `WebSocketBackplane|None` |

## DatabaseResult

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `column_info` | `()` | `()` | `()` | `()` | ✅ |
| `size` | `()` | `()` | `()` | `()` | ✅ |
| `to_array` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `to_csv` | `()` | `()` | `", headers` | `()` | ⚠️ param count differs |
| `to_json` | `()` | `()` | `()` | `()` | ✅ |
| `to_paginate` | `page, per_page` | `()` | `()` | `page, perPage` | ✅ |

### Mismatch Details

#### `to_array`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list` |
| PHP | `` | `list<int, dict` |
| Ruby | `` | `untyped` |
| Node | `` | `list` |

#### `to_csv`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `str` |
| PHP | `` | `str` |
| Ruby | `separator: ", ", headers: true` | `untyped` |
| Node | `` | `str` |

## DevReload

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
