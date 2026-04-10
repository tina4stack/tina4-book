# Tina4 Signature Parity Report

> Auto-generated on 2026-04-10

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
| Session | 17 | 16 | 1 | 0 |
| Migration | 13 | 11 | 2 | 0 |
| MCP | 13 | 13 | 0 | 0 |
| Frond | 10 | 10 | 0 | 0 |
| GraphQL | 13 | 13 | 0 | 0 |
| Api | 9 | 9 | 0 | 0 |
| Cache | 7 | 7 | 0 | 0 |
| Container | 5 | 5 | 0 | 0 |
| Events | 8 | 8 | 0 | 0 |
| WebSocket | 14 | 7 | 5 | 2 |
| WSDL | 5 | 0 | 0 | 5 |
| Swagger | 1 | 0 | 0 | 1 |
| I18n | 7 | 7 | 0 | 0 |
| Seeder | 33 | 33 | 0 | 0 |
| QueryBuilder | 16 | 16 | 0 | 0 |
| Validator | 11 | 11 | 0 | 0 |
| HtmlElement | 1 | 0 | 0 | 1 |
| Testing | 8 | 1 | 0 | 7 |
| Messenger | 10 | 4 | 2 | 4 |
| Logger | 7 | 7 | 0 | 0 |
| AI | 5 | 5 | 0 | 0 |
| Request | 4 | 0 | 0 | 4 |
| Response | 18 | 15 | 0 | 3 |
| Middleware | 13 | 13 | 0 | 0 |
| AutoCrud | 5 | 0 | 0 | 5 |
| SqlTranslation | 17 | 17 | 0 | 0 |
| Metrics | 3 | 0 | 0 | 3 |

## ORM

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `all` | `limit, offset, include, order_by` | `limit, offset, include, orderBy` | `()` | `where?, params?, include?, orderBy?` | ✅ |
| `belongs_to` | `related_class, foreign_key` | `relatedClass, foreignKey` | `name` | `foreignKey` | ℹ️ return type differs |
| `cached` | `sql, params, ttl, limit, offset, include` | `sql, params, ttl, limit, offset, include` | `sql, params` | `sql, params?, ttl, limit, offset, include?` | ✅ |
| `camel_to_snake` | `name` | `name` | `name` | `name` | ✅ |
| `clear_cache` | `()` | `()` | `()` | `()` | ✅ |
| `clear_rel_cache` | `()` | `()` | `()` | `()` | ✅ |
| `count` | `conditions, params` | `conditions, params` | `conditions, params` | `conditions?, params?` | ✅ |
| `create` | `data` | `data` | `attributes` | `data` | ✅ |
| `create_table` | `()` | `()` | `()` | `()` | ✅ |
| `delete` | `()` | `()` | `()` | `()` | ✅ |
| `eager_load` | `instances, include_list` | `instances, include, db` | `instances, include_list` | `instances, includeList` | ✅ |
| `exists` | `pk_value` | `pkValue` | `pk_value` | `pkValue` | ✅ |
| `find` | `filter, limit, offset, order_by, include` | `filter, limit, offset, orderBy, include` | `filter` | `filter?, limit, offset, orderBy?, include?` | ✅ |
| `find_by_id` | `pk_value, include` | `id, include` | `id` | `id, include?` | ✅ |
| `find_or_fail` | `pk_value` | `id` | `id` | `id` | ✅ |
| `force_delete` | `()` | `()` | `()` | `()` | ✅ |
| `get_db` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `get_db_column` | `prop` | `property` | `property` | `prop` | ℹ️ return type differs |
| `has_many` | `related_class, foreign_key, limit, offset` | `relatedClass, foreignKey, limit, offset` | `name` | `foreignKey, limit, offset` | ℹ️ return type differs |
| `has_one` | `related_class, foreign_key` | `relatedClass, foreignKey` | `name` | `foreignKey` | ℹ️ return type differs |
| `load` | `filter, params, include` | `filter, params, include` | `filter, params` | `filter?, params?, include?` | ✅ |
| `query` | `()` | `()` | `()` | `()` | ✅ |
| `restore` | `()` | `()` | `()` | `()` | ✅ |
| `save` | `()` | `()` | `()` | `()` | ✅ |
| `scope` | `name, filter_sql, params` | `name, filterSql, params` | `name, filter_sql, params` | `name, filterSql, params?` | ✅ |
| `select` | `sql, params, limit, offset, include` | `sql, params, limit, offset, include` | `*fields` | `sql, params?` | ✅ |
| `select_one` | `sql, params, include` | `sql, params, include` | `sql, params` | `sql, params?, include?` | ✅ |
| `snake_to_camel` | `name` | `name` | `name` | `name` | ✅ |
| `to_array` | `()` | `()` | `()` | `()` | ✅ |
| `to_assoc` | `include` | `include` | `()` | `include?` | ✅ |
| `to_dict` | `include` | `include` | `()` | `include?` | ✅ |
| `to_json` | `include` | `include` | `()` | `include?` | ✅ |
| `to_list` | `()` | `()` | `()` | `()` | ✅ |
| `to_object` | `()` | `()` | `()` | `()` | ✅ |
| `validate` | `()` | `()` | `()` | `()` | ✅ |
| `where` | `filter_sql, params, limit, offset, include` | `filterSql, params, limit, offset, include` | `conditions, params` | `conditions, params?, limit, offset, include?` | ✅ |
| `with_trashed` | `filter_sql, params, limit, offset` | `filterSql, params, limit, offset` | `conditions, params` | `conditions?, params?, limit?, offset?` | ✅ |

### Mismatch Details

#### `belongs_to`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `related_class, foreign_key: str = None` | `Self|None` |
| PHP | `relatedClass: string, foreignKey: ?string null = null` | `Self|None` |
| Ruby | `name, class_name: nil, foreign_key: nil` | `None` |
| Node | `relatedClass: typeof BaseModel & (new (data?: Record<string, unknown>) => R), foreignKey: string` | `Self|None` |

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

#### `has_many`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `related_class, foreign_key: str = None, limit: int = 100, offset: int = 0` | `list` |
| PHP | `relatedClass: string, foreignKey: ?string null = null, limit: int 100 = 100, offset: int 0 = 0` | `list` |
| Ruby | `name, class_name: nil, foreign_key: nil` | `None` |
| Node | `relatedClass: typeof BaseModel & (new (data?: Record<string, unknown>) => R), foreignKey: string, limit: number = 100, offset: number = 0` | `list` |

#### `has_one`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `related_class, foreign_key: str = None` | `Self|None` |
| PHP | `relatedClass: string, foreignKey: ?string null = null` | `Self|None` |
| Ruby | `name, class_name: nil, foreign_key: nil` | `None` |
| Node | `relatedClass: typeof BaseModel & (new (data?: Record<string, unknown>) => R), foreignKey: string` | `Self|None` |

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
| `fetch` | `sql, params, limit, offset` | `sql, params, limit, offset` | `sql, params` | `sql, params?, limit?, offset?` | ✅ |
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
| `destroy` | `session_id` | `()` | `()` | `sessionId` | ⚠️ param count differs |
| `flash` | `key, value` | `key, value` | `key, value` | `key, value?` | ✅ |
| `gc` | `max_lifetime` | `maxLifetime` | `max_lifetime` | `maxLifetime` | ✅ |
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

#### `destroy`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `session_id: str` | `untyped` |
| PHP | `` | `None` |
| Ruby | `` | `untyped` |
| Node | `sessionId: string` | `None` |

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
| `migrate` | `db, migration_folder, delimiter` | `()` | `()` | `()` | ⚠️ param count differs |
| `record_migration` | `name, batch, passed` | `name, batch, passed` | `name, batch` | `name, batch` | ✅ |
| `remove_migration_record` | `name` | `name` | `name` | `migration.name` | ✅ |
| `rollback` | `db, migration_folder, delimiter` | `steps` | `steps` | `steps` | ✅ |
| `status` | `db, migration_folder` | `()` | `()` | `()` | ⚠️ param count differs |
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
| Node | `description: string, options?: { migrationsDir?: string }` | `Promise<` |

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
| Python | `db, migration_folder: str = 'migrations', delimiter: str = ';'` | `list` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `MigrationResult` |

#### `status`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `db, migration_folder: str = 'migrations'` | `dict` |
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
| `execute` | `query, variables, context` | `query, variables` | `query` | `query, variables?` | ℹ️ return type differs |
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
| PHP | `query: string, variables: ?array null = null` | `list` |
| Ruby | `query, variables: {}, context: {}, operation_name: nil` | `untyped` |
| Node | `query: string, variables?: Record<string, unknown>` | `GraphQLResult` |

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
| `broadcast` | `path, message, exclude` | `message, excludeIds, path` | `message` | `message, excludeIds?, path?` | ⚠️ param count differs |
| `broadcast_to_room` | `room_name, message, exclude_self` | `roomName, message, excludeIds` | `room_name, message` | `roomName, message, excludeIds?` | ✅ |
| `build_frame` | — | — | `opcode, data` | `opcode, payload, fin` | ⚠️ missing: Python, PHP |
| `close` | `code, reason` | `clientId, code, reason` | `()` | `clientId, code, reason` | ⚠️ param count differs |
| `compute_accept_key` | — | `key` | — | `key` | ⚠️ missing: Python, Ruby |
| `get_clients` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `get_room_connections` | `room_name` | `roomName` | `room_name` | `roomName` | ✅ |
| `join_room` | `room_name` | `clientId, roomName` | `room_name` | `clientId, roomName` | ⚠️ param count differs |
| `leave_room` | `room_name` | `clientId, roomName` | `room_name` | `clientId, roomName` | ⚠️ param count differs |
| `on` | `event, handler` | `event, handler` | `event, handler` | `event, handler` | ℹ️ return type differs |
| `room_count` | `room_name` | `roomName` | `room_name` | `roomName` | ✅ |
| `send` | `message` | `clientId, message` | `message` | `clientId, message` | ⚠️ param count differs |
| `start` | `()` | `()` | `()` | `()` | ✅ |
| `stop` | `()` | `()` | `()` | `()` | ✅ |

### Mismatch Details

#### `broadcast`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str, message: str | bytes, exclude: str = None` | `untyped` |
| PHP | `message: string, excludeIds: ?array null = null, path: ?string null = null` | `None` |
| Ruby | `message, exclude: nil, path: nil` | `untyped` |
| Node | `message: string, excludeIds?: string[], path?: string` | `None` |

#### `build_frame`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `opcode, data` | `untyped` |
| Node | `opcode: number, payload: Buffer, fin: boolean = true` | `Buffer` |

#### `close`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `code: int = CLOSE_NORMAL, reason: str = ''` | `untyped` |
| PHP | `clientId: string, code: int 1000 = 1000, reason: string '' = ''` | `None` |
| Ruby | `code: 1000, reason: ""` | `untyped` |
| Node | `clientId: string, code: number = 1000, reason: string = ""` | `None` |

#### `compute_accept_key`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `key: string` | `str` |
| Ruby | — not implemented — | — |
| Node | `key: string` | `str` |

#### `get_clients`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `Map<str, WebSocketClient>` |

#### `join_room`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `room_name: str` | `None` |
| PHP | `clientId: string, roomName: string` | `None` |
| Ruby | `room_name` | `untyped` |
| Node | `clientId: string, roomName: string` | `None` |

#### `leave_room`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `room_name: str` | `None` |
| PHP | `clientId: string, roomName: string` | `None` |
| Ruby | `room_name` | `untyped` |
| Node | `clientId: string, roomName: string` | `None` |

#### `on`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `event: str, handler: Callable` | `untyped` |
| PHP | `event: string, handler: callable` | `Self` |
| Ruby | `event, &block` | `untyped` |
| Node | `event: string, handler: Function` | `WebSocketServer` |

#### `send`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `message: str | bytes` | `untyped` |
| PHP | `clientId: string, message: string` | `None` |
| Ruby | `message` | `untyped` |
| Node | `clientId: string, message: string` | `None` |

## WSDL

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `generate_wsdl` | `()` | — | `endpoint_url` | `endpointUrl?` | ⚠️ missing: PHP |
| `handle` | `()` | `()` | `()` | — | ⚠️ missing: Node |
| `on_request` | `request` | — | `request` | `_request` | ⚠️ missing: PHP |
| `on_result` | `result` | — | `result` | `result` | ⚠️ missing: PHP |
| `wsdl_operation` | `response_schema` | — | `()` | — | ⚠️ missing: PHP, Node |

### Mismatch Details

#### `generate_wsdl`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `str` |
| PHP | — not implemented — | — |
| Ruby | `endpoint_url` | `untyped` |
| Node | `endpointUrl?: string` | `str` |

#### `handle`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `str` |
| PHP | `` | `Response` |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `on_request`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `request` | `untyped` |
| PHP | — not implemented — | — |
| Ruby | `request` | `untyped` |
| Node | `_request: unknown` | `None` |

#### `on_result`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `result` | `untyped` |
| PHP | — not implemented — | — |
| Ruby | `result` | `untyped` |
| Node | `result: Record<string, unknown>` | `dict` |

#### `wsdl_operation`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `response_schema: dict = None` | `untyped` |
| PHP | — not implemented — | — |
| Ruby | `output: {}` | `untyped` |
| Node | — not implemented — | — |

## Swagger

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `generate` | `routes` | — | `()` | — | ⚠️ missing: PHP, Node |

### Mismatch Details

#### `generate`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `routes: list[dict]` | `dict` |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

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
| `from` | `table_name, db` | `table, db` | `table_name` | `tableName, db?` | ℹ️ return type differs |
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

#### `from`

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
| `add_html_helpers` | `namespace` | — | — | `h` | ⚠️ missing: PHP, Ruby |

### Mismatch Details

#### `add_html_helpers`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `namespace` | `untyped` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `h` | `untyped` |

## Testing

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `assert_equal` | `args, expected` | `args, expected` | `expected, actual, message` | `args, expected` | ℹ️ return type differs |
| `assert_false` | `args` | `args` | — | `args` | ⚠️ missing: Ruby |
| `assert_raises` | `exception_class, args` | `exceptionClass, args` | `exception_class, message` | — | ⚠️ missing: Node |
| `assert_true` | `args` | `args` | — | `args` | ⚠️ missing: Ruby |
| `reset` | — | `()` | `()` | — | ⚠️ missing: Python, Node |
| `run_all` | — | `quiet, failfast` | `()` | — | ⚠️ missing: Python, Node |
| `run_all_tests` | `quiet, failfast` | — | — | `options` | ⚠️ missing: PHP, Ruby |
| `tests` | `*assertions` | `assertions, fn, name` | — | `...assertions` | ⚠️ missing: Ruby |

### Mismatch Details

#### `assert_equal`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `args: tuple, expected` | `untyped` |
| PHP | `args: array, expected: mixed` | `list` |
| Ruby | `expected, actual, message = nil` | `untyped` |
| Node | `args: unknown[], expected: unknown` | `Assertion` |

#### `assert_false`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `args: tuple` | `untyped` |
| PHP | `args: array` | `list` |
| Ruby | — not implemented — | — |
| Node | `args: unknown[]` | `Assertion` |

#### `assert_raises`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `exception_class: type, args: tuple` | `untyped` |
| PHP | `exceptionClass: string, args: array` | `list` |
| Ruby | `exception_class, message = nil` | `untyped` |
| Node | — not implemented — | — |

#### `assert_true`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `args: tuple` | `untyped` |
| PHP | `args: array` | `list` |
| Ruby | — not implemented — | — |
| Node | `args: unknown[]` | `Assertion` |

#### `reset`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `None` |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `run_all`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `quiet: bool false = false, failfast: bool false = false` | `list` |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `run_all_tests`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `quiet: bool = False, failfast: bool = False` | `dict` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `options: { quiet?: boolean; failfast?: boolean } = {}` | `TestResults` |

#### `tests`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `*assertions` | `untyped` |
| PHP | `assertions: array, fn: callable, name: string 'anonymous' = 'anonymous'` | `None` |
| Ruby | — not implemented — | — |
| Node | `...assertions: Assertion[]` | `untyped` |

## Messenger

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `create_messenger` | `()` | — | `()` | — | ⚠️ missing: PHP, Node |
| `folders` | `()` | `()` | `()` | — | ⚠️ missing: Node |
| `inbox` | `folder, limit, offset` | `folder, limit, offset` | `()` | `limit, offset, folder` | ✅ |
| `mark_read` | `uid, folder` | — | — | `uid, folder` | ⚠️ missing: PHP, Ruby |
| `read` | `uid, folder, mark_read` | `uid, folder, markRead` | `uid` | `uid, folder` | ℹ️ return type differs |
| `search` | `folder, subject, sender, since, before, unseen_only, limit` | `folder, subject, sender, since, before, unseenOnly, limit` | `()` | `query, folder` | ⚠️ param count differs |
| `send` | `to, subject, body, html, text, cc, bcc, reply_to, attachments, headers` | `to, subject, body, html, text, cc, bcc, replyTo, attachments, headers` | `to, subject, body, headers` | `options` | ⚠️ param count differs |
| `test_connection` | `()` | `()` | `()` | `()` | ℹ️ return type differs |
| `test_imap_connection` | `()` | — | — | `()` | ⚠️ missing: PHP, Ruby |
| `unread` | `folder` | `folder` | `()` | `folder` | ✅ |

### Mismatch Details

#### `create_messenger`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `**kwargs` | `Messenger` |
| PHP | — not implemented — | — |
| Ruby | `**options` | `untyped` |
| Node | — not implemented — | — |

#### `folders`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `mark_read`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `uid: str | bytes, folder: str = 'INBOX'` | `untyped` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `uid: string, folder: string = "INBOX"` | `None` |

#### `read`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `uid: str | bytes, folder: str = 'INBOX', mark_read: bool = True` | `dict` |
| PHP | `uid: int, folder: string 'INBOX' = 'INBOX', markRead: bool true = true` | `list|None` |
| Ruby | `uid, folder: "INBOX", mark_read: true` | `untyped` |
| Node | `uid: string, folder: string = "INBOX"` | `ImapFullMessage` |

#### `search`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `folder: str = 'INBOX', subject: str = None, sender: str = None, since: str = None, before: str = None, unseen_only: bool = False, limit: int = 50` | `list` |
| PHP | `folder: string 'INBOX' = 'INBOX', subject: ?string null = null, sender: ?string null = null, since: ?string null = null, before: ?string null = null, unseenOnly: bool false = false, limit: int 20 = 20` | `list` |
| Ruby | `folder: "INBOX", subject: nil, sender: nil, since: nil, before: nil, unseen_only: false, limit: 20` | `untyped` |
| Node | `query: string, folder: string = "INBOX"` | `list` |

#### `send`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `to: str | list[str], subject: str, body: str, html: bool = False, text: str = None, cc: str | list[str] = None, bcc: str | list[str] = None, reply_to: str = None, attachments: list = None, headers: dict = None` | `dict` |
| PHP | `to: string|array, subject: string, body: string, html: bool false = false, text: ?string null = null, cc: array|string [] = [], bcc: array|string [] = [], replyTo: ?string null = null, attachments: array [] = [], headers: array [] = []` | `list` |
| Ruby | `to:, subject:, body:, html: false, text: nil, cc: [], bcc: [], reply_to: nil, attachments: [], headers: {}` | `untyped` |
| Node | `options: SendOptions` | `SendResult` |

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
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
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
| `bearer_token` | — | `()` | `()` | — | ⚠️ missing: Python, Node |
| `header` | — | `name` | `name` | — | ⚠️ missing: Python, Node |
| `param` | `key, default` | — | `key` | — | ⚠️ missing: PHP, Node |
| `parse_body` | — | — | `()` | `req` | ⚠️ missing: Python, PHP |

### Mismatch Details

#### `bearer_token`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `str|None` |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `header`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `name: string` | `str|None` |
| Ruby | `name` | `untyped` |
| Node | — not implemented — | — |

#### `param`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `key: str, default = None` | `untyped` |
| PHP | — not implemented — | — |
| Ruby | `key` | `untyped` |
| Node | — not implemented — | — |

#### `parse_body`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | `req: Tina4Request` | `None` |

## Response

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `cookie` | `name, value, path, max_age, http_only, secure, same_site` | `name, value, options` | `name, value, opts` | `name, value, options?` | ℹ️ return type differs |
| `error` | `code, message, status_code` | `code, message, status` | `code, message, status_code` | `code, message, status?` | ℹ️ return type differs |
| `error_response` | `code, message, status` | `code, message, status` | `code, message, status` | `code, message, status` | ✅ |
| `file` | `file_path, download_name` | `path, contentType, download` | `path, content_type` | `filePath, options?` | ℹ️ return type differs |
| `get_framework_frond` | `()` | `()` | — | — | ⚠️ missing: Ruby, Node |
| `get_frond` | `()` | `()` | — | — | ⚠️ missing: Ruby, Node |
| `header` | `name, value` | `name, value` | `name, value` | `name, value` | ℹ️ return type differs |
| `html` | `content, status_code` | `content, status` | `content, status_or_opts` | `content, status?` | ℹ️ return type differs |
| `json` | `data, status_code` | `data, status` | `data, status_or_opts` | `data, status?` | ℹ️ return type differs |
| `redirect` | `url, status_code` | `url, status` | `url, status_or_opts` | `url, code?` | ℹ️ return type differs |
| `render` | `template, data` | `templateName, data, status, templateDir` | `template_path, data` | `templateName, data?, status?, templateDir?` | ℹ️ return type differs |
| `send` | `data, status_code, content_type` | `data, statusCode, contentType` | `data, content_type` | `data, statusCode?, contentType?` | ℹ️ return type differs |
| `set_frond` | `engine` | `frond` | — | — | ⚠️ missing: Ruby, Node |
| `status` | `code` | `code` | `code` | `code` | ℹ️ return type differs |
| `stream` | `source, content_type` | `source, contentType` | `content_type, handler` | `source, contentType` | ℹ️ return type differs |
| `template` | `template, data` | `templateName, data, status, templateDir` | `template_path, data` | `name, data?, status?, templateDir?` | ℹ️ return type differs |
| `text` | `content, status_code` | `content, status` | `content, status_or_opts` | `content, status?` | ℹ️ return type differs |
| `xml` | `content, status_code` | `content, status` | `content` | `content, status?` | ℹ️ return type differs |

### Mismatch Details

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
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `get_frond`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `Frond` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

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

#### `set_frond`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `engine` | `untyped` |
| PHP | `frond: Frond` | `None` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

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

#### `template`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `template: str, data: dict = None` | `Response` |
| PHP | `templateName: string, data: array [] = [], status: int 200 = 200, templateDir: string 'src/templates' = 'src/templates'` | `Self` |
| Ruby | `template_path, data = {}, status: 200, template_dir: nil` | `untyped` |
| Node | `name: string, data?: Record<string, unknown>, status?: number, templateDir?: string` | `Tina4Response` |

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
| Python | `ip: str` | `tuple[bool, dict]` |
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
| `clear` | `()` | — | `()` | — | ⚠️ missing: PHP, Node |
| `discover` | `models_dir, prefix` | `modelsDir` | — | — | ⚠️ missing: Ruby, Node |
| `generate_routes` | — | `()` | `()` | — | ⚠️ missing: Python, Node |
| `models` | `()` | — | `()` | — | ⚠️ missing: PHP, Node |
| `register` | `model_class, prefix` | `modelClass` | `model_class` | — | ⚠️ missing: Node |

### Mismatch Details

#### `clear`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `discover`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `models_dir: str = 'src/orm', prefix: str = '/api'` | `untyped` |
| PHP | `modelsDir: string` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `generate_routes`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `list` |
| Ruby | `prefix: "/api"` | `untyped` |
| Node | — not implemented — | — |

#### `models`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `register`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `model_class, prefix: str = '/api'` | `untyped` |
| PHP | `modelClass: string` | `Self` |
| Ruby | `model_class` | `untyped` |
| Node | — not implemented — | — |

## SqlTranslation

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `auto_increment_syntax` | `sql, engine` | `sql, dialect` | `sql, engine` | `sql, engine` | ✅ |
| `boolean_to_int` | `sql` | `sql` | `sql` | `sql` | ✅ |
| `clear` | `()` | `()` | `()` | `()` | ✅ |
| `clear_tag` | `tag` | `tag` | `tag` | `tag` | ✅ |
| `concat_pipes_to_func` | `sql` | `sql` | `sql` | `sql` | ✅ |
| `delete` | `table, filter_sql, params` | `key` | `key` | `key` | ℹ️ return type differs |
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

### Mismatch Details

#### `delete`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `table: str, filter_sql: str | dict | list = '', params: list = None` | `DatabaseResult` |
| PHP | `key: string` | `bool` |
| Ruby | `key` | `untyped` |
| Node | `key: string` | `bool` |

## Metrics

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `file_detail` | — | `filePath` | `file_path` | `filePath` | ⚠️ missing: Python |
| `full_analysis` | — | `root` | `root` | `root` | ⚠️ missing: Python |
| `quick_metrics` | — | `root` | `root` | `root` | ⚠️ missing: Python |

### Mismatch Details

#### `file_detail`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `filePath: string` | `list` |
| Ruby | `file_path` | `untyped` |
| Node | `filePath: string` | `dict` |

#### `full_analysis`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `root: string "src" = "src"` | `list` |
| Ruby | `root = 'src'` | `untyped` |
| Node | `root: string = "src"` | `dict` |

#### `quick_metrics`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `root: string "src" = "src"` | `list` |
| Ruby | `root = 'src'` | `untyped` |
| Node | `root: string = "src"` | `dict` |
