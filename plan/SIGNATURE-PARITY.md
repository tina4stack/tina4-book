# Tina4 Signature Parity Report

> Auto-generated on 2026-04-09

Compares public method signatures (params + return types) across Python, PHP, Ruby, and Node.js.
Methods are matched by normalised snake_case name. ✅ = full parity, ⚠️ = mismatch or missing.

## Summary

| Feature | Methods | ✅ Match | ⚠️ Mismatch | ⚠️ Missing |
|---------|--------:|--------:|------------:|----------:|
| ORM | 35 | 16 | 15 | 4 |
| Queue | 14 | 3 | 9 | 2 |
| Job | 7 | 4 | 3 | 0 |
| Auth | 8 | 6 | 2 | 0 |
| Database | 29 | 4 | 9 | 16 |
| Router | 18 | 2 | 11 | 5 |
| Session | 17 | 6 | 7 | 4 |
| Migration | 11 | 0 | 7 | 4 |
| MCP | 5 | 2 | 2 | 1 |
| Frond | 8 | 3 | 5 | 0 |
| GraphQL | 12 | 1 | 7 | 4 |

## ORM

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `all` | `limit, offset, include` | `limit, offset, include` | `limit, offset, order_by, include` | `unknown>), where?, params?, include?` | ⚠️ param count differs |
| `belongs_to` | `related_class, foreign_key` | `relatedClass, foreignKey` | `name, class_name, foreign_key` | `relatedClass, unknown>), foreignKey` | ⚠️ return type differs |
| `cached` | `sql, params, ttl, limit, offset` | `sql, params, ttl, limit, offset, include` | `sql, params, ttl, limit, offset, include` | `unknown>), sql, params?, ttl` | ⚠️ param count differs |
| `clear_cache` | `()` | `()` | `()` | `()` | ✅ |
| `clear_rel_cache` | — | `()` | — | `()` | ⚠️ missing: Python, Ruby |
| `count` | `conditions, params` | `conditions, params` | `conditions, params` | `conditions?, params?` | ✅ |
| `create` | `data, **kwargs` | `data` | `attributes` | `unknown>), data, unknown>` | ⚠️ param count differs |
| `create_table` | `()` | `()` | `()` | `()` | ✅ |
| `delete` | `()` | `()` | `()` | `()` | ✅ |
| `eager_load` | — | `include, db` | `instances, include_list` | — | ⚠️ missing: Python, Node |
| `exists` | `pk_value` | `()` | `pk_value` | `id` | ⚠️ param count differs |
| `find` | `filter, limit, offset, order_by, include` | `filter, limit, offset, orderBy, include` | `filter, limit, offset, order_by, include, **extra_filter` | `unknown>), filter?, unknown>, limit, offset, orderBy?, include?` | ⚠️ param count differs |
| `find_by_id` | `pk_value, include` | `id, include` | `id` | `unknown>), id, include?` | ⚠️ param count differs |
| `find_or_fail` | `pk_value` | `id` | `id` | `unknown>), id` | ⚠️ param count differs |
| `force_delete` | `()` | `()` | `()` | `()` | ✅ |
| `get_db` | — | `()` | — | `()` | ⚠️ missing: Python, Ruby |
| `get_db_column` | — | `property` | — | `prop` | ⚠️ missing: Python, Ruby |
| `has_many` | `related_class, foreign_key, limit, offset` | `relatedClass, foreignKey, limit, offset` | `name, class_name, foreign_key` | `relatedClass, unknown>), foreignKey, limit, offset` | ⚠️ return type differs |
| `has_one` | `related_class, foreign_key` | `relatedClass, foreignKey` | `name, class_name, foreign_key` | `relatedClass, unknown>), foreignKey` | ⚠️ return type differs |
| `load` | `filter, params, include` | `filter, params, include` | `filter, params, include` | `filter?, params?, include?` | ✅ |
| `query` | `()` | `()` | `()` | `()` | ✅ |
| `restore` | `()` | `()` | `()` | `()` | ✅ |
| `save` | `()` | `()` | `()` | `()` | ✅ |
| `scope` | `name, filter_sql, params` | `name, filterSql, params` | `name, filter_sql, params` | `name, filterSql, params?` | ✅ |
| `select` | `sql, params, limit, offset, include` | `sql, params, limit, offset, include` | `*fields` | `unknown>), sql, params?` | ⚠️ param count differs |
| `select_one` | `sql, params, include` | `sql, params, include` | `sql, params, include` | `unknown>), sql, params?, include?` | ⚠️ param count differs |
| `to_array` | `()` | `()` | `()` | `()` | ✅ |
| `to_assoc` | `include` | `include` | `include` | `include?` | ✅ |
| `to_dict` | `include` | `include` | `include` | `include?` | ✅ |
| `to_json` | `include` | `include` | `include, **_args` | `include?` | ✅ |
| `to_list` | `()` | `()` | `()` | `()` | ✅ |
| `to_object` | `()` | `()` | `include` | `()` | ⚠️ param count differs |
| `validate` | `()` | `()` | `()` | `()` | ✅ |
| `where` | `filter_sql, params, limit, offset, include` | `filterSql, params, limit, offset, include` | `conditions, params, include` | `unknown>), conditions, params?, limit, offset, include?` | ⚠️ param count differs |
| `with_trashed` | `filter_sql, params, limit, offset` | `filterSql, params, limit, offset` | `conditions, params, limit, offset` | `unknown>), conditions?, params?, limit?, offset?` | ⚠️ param count differs |

### Mismatch Details

#### `all`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `limit: int = 100, offset: int = 0, include: list[str] = None` | `list[Self]` |
| PHP | `limit: int 100 = 100, offset: int 0 = 0, include: ?array null = null` | `list[Self]` |
| Ruby | `limit: nil, offset: nil, order_by: nil, include: nil` | `list[Self]` |
| Node | `unknown>) => T, where?: string, params?: unknown[], include?: string[]` | `list[Self]` |

#### `belongs_to`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `related_class, foreign_key: str = None` | `Self|None` |
| PHP | `relatedClass: string, foreignKey: ?string null = null` | `Self|None` |
| Ruby | `name, class_name: nil, foreign_key: nil` | `None` |
| Node | `relatedClass: typeof BaseModel & (new (data?: Record<string, unknown>) => R), foreignKey: string` | `Self|None` |

#### `cached`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `sql: str, params: list = None, ttl: int = 60, limit: int = 20, offset: int = 0` | `list[Self]` |
| PHP | `sql: string, params: array [] = [], ttl: int 60 = 60, limit: int 20 = 20, offset: int 0 = 0, include: ?array null = null` | `list[Self]` |
| Ruby | `sql, params = [], ttl: 60, limit: 20, offset: 0, include: nil` | `list[Self]` |
| Node | `unknown>) => T, sql: string, params?: unknown[], ttl = 60` | `list[Self]` |

#### `clear_rel_cache`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `None` |
| Ruby | — not implemented — | — |
| Node | `` | `None` |

#### `create`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `data: dict = None, **kwargs` | `Self` |
| PHP | `data: array [] = []` | `Self` |
| Ruby | `attributes = {}` | `Self` |
| Node | `unknown>) => T, data: Record<string, unknown>` | `Self` |

#### `eager_load`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `include: array, db: DatabaseAdapter` | `None` |
| Ruby | `instances, include_list` | `untyped` |
| Node | — not implemented — | — |

#### `exists`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `pk_value` | `bool` |
| PHP | `` | `bool` |
| Ruby | `pk_value` | `bool` |
| Node | `id: unknown` | `bool` |

#### `find`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `filter: dict = None, limit: int = 100, offset: int = 0, order_by: str = None, include: list[str] = None` | `list[Self]` |
| PHP | `filter: array [] = [], limit: int 100 = 100, offset: int 0 = 0, orderBy: ?string null = null, include: ?array null = null` | `list[Self]` |
| Ruby | `filter = {}, limit: 100, offset: 0, order_by: nil, include: nil, **extra_filter` | `list[Self]` |
| Node | `unknown>) => T, filter?: Record<string, unknown>, limit = 100, offset = 0, orderBy?: string, include?: string[]` | `list[Self]` |

#### `find_by_id`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `pk_value, include: list[str] = None` | `Self|None` |
| PHP | `id: int|string, include: ?array null = null` | `Self|None` |
| Ruby | `id` | `Self|None` |
| Node | `unknown>) => T, id: unknown, include?: string[]` | `Self|None` |

#### `find_or_fail`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `pk_value` | `Self` |
| PHP | `id: int|string` | `Self` |
| Ruby | `id` | `Self` |
| Node | `unknown>) => T, id: unknown` | `Self` |

#### `get_db`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `DatabaseAdapter|None` |
| Ruby | — not implemented — | — |
| Node | `` | `DatabaseAdapter` |

#### `get_db_column`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `property: string` | `str` |
| Ruby | — not implemented — | — |
| Node | `prop: string` | `str` |

#### `has_many`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `related_class, foreign_key: str = None, limit: int = 100, offset: int = 0` | `list[Self]` |
| PHP | `relatedClass: string, foreignKey: ?string null = null, limit: int 100 = 100, offset: int 0 = 0` | `list[Self]` |
| Ruby | `name, class_name: nil, foreign_key: nil` | `None` |
| Node | `relatedClass: typeof BaseModel & (new (data?: Record<string, unknown>) => R), foreignKey: string, limit: number = 100, offset: number = 0` | `list[Self]` |

#### `has_one`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `related_class, foreign_key: str = None` | `Self|None` |
| PHP | `relatedClass: string, foreignKey: ?string null = null` | `Self|None` |
| Ruby | `name, class_name: nil, foreign_key: nil` | `None` |
| Node | `relatedClass: typeof BaseModel & (new (data?: Record<string, unknown>) => R), foreignKey: string` | `Self|None` |

#### `select`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `sql: str, params: list = None, limit: int = 20, offset: int = 0, include: list[str] = None` | `list[Self]` |
| PHP | `sql: string, params: array [] = [], limit: int 20 = 20, offset: int 0 = 0, include: ?array null = null` | `list[Self]` |
| Ruby | `*fields` | `untyped` |
| Node | `unknown>) => T, sql: string, params?: unknown[]` | `list[Self]` |

#### `select_one`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `sql: str, params: list = None, include: list[str] = None` | `Self|None` |
| PHP | `sql: string, params: array [] = [], include: ?array null = null` | `Self|None` |
| Ruby | `sql, params = [], include: nil` | `Self|None` |
| Node | `unknown>) => T, sql: string, params?: unknown[], include?: string[]` | `Self|None` |

#### `to_object`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `dict` |
| Ruby | `include: nil` | `dict` |
| Node | `` | `dict` |

#### `where`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `filter_sql: str, params: list = None, limit: int = 20, offset: int = 0, include: list[str] = None` | `list[Self]` |
| PHP | `filterSql: string, params: array [] = [], limit: int 20 = 20, offset: int 0 = 0, include: ?array null = null` | `list[Self]` |
| Ruby | `conditions, params = [], include: nil` | `list[Self]` |
| Node | `unknown>) => T, conditions: string, params?: unknown[], limit: number = 20, offset: number = 0, include?: string[]` | `list[Self]` |

#### `with_trashed`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `filter_sql: str = '1=1', params: list = None, limit: int = 20, offset: int = 0` | `list[Self]` |
| PHP | `filterSql: string = '1=1', params: array [] = [], limit: int 20 = 20, offset: int 0 = 0` | `list[Self]` |
| Ruby | `conditions = "1=1", params = [], limit: 20, offset: 0` | `list[Self]` |
| Node | `unknown>) => T, conditions?: string, params?: unknown[], limit?: number, offset?: number` | `list[Self]` |

## Queue

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `clear` | `()` | `()` | `()` | `()` | ✅ |
| `consume` | `topic, job_id, poll_interval, iterations` | `topic, id, pollInterval` | `topic, id, poll_interval, iterations, &block` | `topic?, id?, pollInterval, iterations` | ⚠️ return type differs |
| `dead_letters` | `()` | `()` | `()` | `maxRetries?` | ⚠️ return type differs |
| `failed` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `get_topic` | — | `()` | — | `()` | ⚠️ missing: Python, Ruby |
| `pop` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `pop_by_id` | `job_id` | `id` | `id` | `id` | ⚠️ return type differs |
| `process` | — | `handlerOrQueue, queueOrHandlerOrOptions, options` | — | `handler, options?` | ⚠️ missing: Python, Ruby |
| `produce` | `topic, data, priority, delay_seconds` | `topic, payload, delay` | `topic, payload, priority` | `topic, payload, delay?, priority` | ⚠️ param count differs |
| `purge` | `status` | `status` | `status` | `status, maxRetries?` | ⚠️ param count differs |
| `push` | `data, priority, delay_seconds` | `payload, delay, priority` | `payload, priority, delay_seconds` | `payload, delay?, priority` | ✅ |
| `retry` | `job_id, delay_seconds` | `jobId, delaySeconds` | `delay_seconds` | `delaySeconds?` | ⚠️ param count differs |
| `retry_failed` | `()` | `()` | `()` | `maxRetries?` | ⚠️ param count differs |
| `size` | `status` | `status` | `status` | `status` | ✅ |

### Mismatch Details

#### `consume`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `topic: str = None, job_id: str = None, poll_interval: float = 1.0, iterations: int = 0` | `untyped` |
| PHP | `topic: string '' = '', id: ?string null = null, pollInterval: float 1.0 = 1.0` | `\Generator` |
| Ruby | `topic = nil, id: nil, poll_interval: 1.0, iterations: 0, &block` | `untyped` |
| Node | `topic?: string, id?: string, pollInterval: number = 1000, iterations: number = 0` | `AsyncGenerator<dict>` |

#### `dead_letters`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list[dict]` |
| PHP | `` | `list[list]` |
| Ruby | `` | `list[dict]` |
| Node | `maxRetries?: number` | `list[dict]` |

#### `failed`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list[dict]` |
| PHP | `` | `list[list]` |
| Ruby | `` | `list[dict]` |
| Node | `` | `list[dict]` |

#### `get_topic`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `str` |
| Ruby | — not implemented — | — |
| Node | `` | `str` |

#### `pop`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `Job|None` |
| PHP | `` | `list|None` |
| Ruby | `` | `Job|None` |
| Node | `` | `dict|None` |

#### `pop_by_id`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `job_id: str` | `Job|None` |
| PHP | `id: string` | `list|None` |
| Ruby | `id` | `untyped` |
| Node | `id: string` | `dict|None` |

#### `process`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `handlerOrQueue: callable|string, queueOrHandlerOrOptions: callable|string|array '' = '', options: array [] = []` | `None` |
| Ruby | — not implemented — | — |
| Node | `handler: (job: QueueJob) => Promise<void> | void, options?: ProcessOptions` | `None` |

#### `produce`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `topic: str, data: dict, priority: int = 0, delay_seconds: int = 0` | `untyped` |
| PHP | `topic: string, payload: mixed, delay: int 0 = 0` | `str` |
| Ruby | `topic, payload, priority = 0` | `untyped` |
| Node | `topic: string, payload: unknown, delay?: number, priority: number = 0` | `str` |

#### `purge`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `status: str = 'completed'` | `int` |
| PHP | `status: string` | `int` |
| Ruby | `status` | `int` |
| Node | `status: string, maxRetries?: number` | `int` |

#### `retry`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `job_id: str, delay_seconds: int = 0` | `bool` |
| PHP | `jobId: string, delaySeconds: int 0 = 0` | `bool` |
| Ruby | `delay_seconds = 0` | `bool` |
| Node | `delaySeconds?: number` | `bool` |

#### `retry_failed`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `int` |
| PHP | `` | `int` |
| Ruby | `` | `int` |
| Node | `maxRetries?: number` | `int` |

## Job

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `complete` | `()` | `()` | `()` | `()` | ✅ |
| `fail` | `error` | `reason` | `reason` | `reason?` | ✅ |
| `reject` | `reason` | `reason` | `reason` | `reason?` | ✅ |
| `retry` | `delay_seconds` | `delaySeconds` | `delay_seconds, queue` | `delaySeconds?` | ⚠️ param count differs |
| `to_array` | `()` | `()` | `()` | `()` | ✅ |
| `to_hash` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `to_json` | `()` | `()` | `*_args` | `()` | ⚠️ param count differs |

### Mismatch Details

#### `retry`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `delay_seconds: int = 0` | `untyped` |
| PHP | `delaySeconds: int 0 = 0` | `None` |
| Ruby | `delay_seconds: 0, queue: nil` | `untyped` |
| Node | `delaySeconds?: number` | `None` |

#### `to_hash`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `dict` |

#### `to_json`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `str` |
| PHP | `` | `str` |
| Ruby | `*_args` | `untyped` |
| Node | `` | `str` |

## Auth

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `authenticate_request` | `headers` | `headers` | `headers` | `headers, string | string[] | undefined>, secret?, algorithm` | ⚠️ param count differs |
| `check_password` | `password, hashed` | `password, hash` | `password, hash` | `"secret123", hash` | ✅ |
| `get_payload` | `token` | `token` | `token` | `token` | ✅ |
| `get_token` | `payload, expires_in` | `payload, expiresIn` | `payload, expires_in` | `payload, unknown>, expiresIn` | ⚠️ param count differs |
| `hash_password` | `password, salt, iterations` | `password, salt, iterations` | `password, salt, iterations` | `password, salt?, iterations` | ✅ |
| `refresh_token` | `token, expires_in` | `token, expiresIn` | `token, expires_in` | `token, expiresIn` | ✅ |
| `valid_token` | `token` | `token` | `token` | `token` | ✅ |
| `validate_api_key` | `provided, expected` | `provided, expected` | `provided, expected` | `provided, expected?` | ✅ |

### Mismatch Details

#### `authenticate_request`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `headers: dict` | `dict|None` |
| PHP | `headers: array` | `dict|None` |
| Ruby | `headers` | `untyped` |
| Node | `headers: Record<string, string | string[] | undefined>, secret?: string, algorithm: string = "HS256"` | `dict|None` |

#### `get_token`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `payload: dict, expires_in: int = None` | `str` |
| PHP | `payload: array, expiresIn: int 3600 = 3600` | `str` |
| Ruby | `payload, expires_in: 60` | `untyped` |
| Node | `payload: Record<string, unknown>, expiresIn: number = 3600` | `str` |

## Database

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `active_count` | `()` | — | `()` | — | ⚠️ missing: PHP, Node |
| `cache_clear` | `()` | `()` | `()` | — | ⚠️ missing: Node |
| `cache_stats` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `checkin` | `adapter` | — | `_driver` | — | ⚠️ missing: PHP, Node |
| `checkout` | `()` | — | `()` | — | ⚠️ missing: PHP, Node |
| `close` | `()` | `()` | `()` | `()` | ✅ |
| `close_all` | `()` | — | `()` | — | ⚠️ missing: PHP, Node |
| `commit` | `()` | `()` | — | `()` | ⚠️ missing: Ruby |
| `create` | — | `url, autoCommit, username, password, pool` | — | `url, username?, password?, pool` | ⚠️ missing: Python, Ruby |
| `delete` | `table, filter_sql, params` | `table, filter, whereParams` | `table, filter` | `table, filter?, unknown>` | ⚠️ return type differs |
| `execute` | `sql, params` | `sql, params` | `sql, params` | `sql, params?` | ⚠️ return type differs |
| `execute_many` | `sql, params_list` | `sql, paramsList` | `sql, params_list` | `sql, paramSets` | ⚠️ return type differs |
| `fetch` | `sql, params, limit, offset` | `sql, params, limit, offset` | `sql, params, limit, offset` | `sql, params?, limit?, offset?` | ✅ |
| `fetch_one` | `sql, params` | `sql, params` | `sql, params` | `sql, params?` | ⚠️ return type differs |
| `from_env` | — | `envKey, autoCommit` | — | `envKey, pool` | ⚠️ missing: Python, Ruby |
| `get_active_pool_count` | — | `()` | — | `()` | ⚠️ missing: Python, Ruby |
| `get_adapter` | — | `()` | — | `()` | ⚠️ missing: Python, Ruby |
| `get_columns` | `table` | `tableName` | — | `tableName` | ⚠️ missing: Ruby |
| `get_error` | `()` | `()` | `()` | `()` | ✅ |
| `get_last_id` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `get_next_id` | `table, pk_column, generator_name` | `table, pkColumn, generatorName` | `table, pk_column, generator_name` | `table, pkColumn, generatorName?` | ✅ |
| `get_pool_size` | — | `()` | — | `()` | ⚠️ missing: Python, Ruby |
| `get_tables` | `()` | `()` | — | `()` | ⚠️ missing: Ruby |
| `insert` | `table, data` | `table, data` | `table, data` | `table, data, unknown>` | ⚠️ return type differs |
| `rollback` | `()` | `()` | — | `()` | ⚠️ missing: Ruby |
| `size` | `()` | — | `()` | — | ⚠️ missing: PHP, Node |
| `start_transaction` | `()` | `()` | — | `()` | ⚠️ missing: Ruby |
| `table_exists` | `name` | `tableName` | `()` | `name` | ⚠️ param count differs |
| `update` | `table, data, filter_sql, params` | `table, data, filterSql, params` | `table, data, filter` | `table, data, unknown>, filter?, unknown>` | ⚠️ return type differs |

### Mismatch Details

#### `active_count`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `int` |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `cache_clear`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `None` |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `cache_stats`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `untyped` |

#### `checkin`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `adapter: DatabaseAdapter` | `None` |
| PHP | — not implemented — | — |
| Ruby | `_driver` | `untyped` |
| Node | — not implemented — | — |

#### `checkout`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `DatabaseAdapter` |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `close_all`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `None` |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `commit`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `None` |
| Ruby | — not implemented — | — |
| Node | `` | `None` |

#### `create`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `url: string, autoCommit: ?bool null = null, username: string '' = '', password: string '' = '', pool: int 0 = 0` | `Self` |
| Ruby | — not implemented — | — |
| Node | `url: string, username?: string, password?: string, pool: number = 0` | `Promise<Database>` |

#### `delete`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `table: str, filter_sql: str | dict | list = '', params: list = None` | `DatabaseResult` |
| PHP | `table: string, filter: string|array '' = '', whereParams: array [] = []` | `bool` |
| Ruby | `table, filter = {}` | `untyped` |
| Node | `table: string, filter?: Record<string, unknown>` | `DatabaseWriteResult` |

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
| PHP | `sql: string, paramsList: array [] = []` | `list[bool]` |
| Ruby | `sql, params_list = []` | `untyped` |
| Node | `sql: string, paramSets: unknown[][]` | `list` |

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
| Python | — not implemented — | — |
| PHP | `envKey: string 'DATABASE_URL' = 'DATABASE_URL', autoCommit: ?bool null = null` | `Self|None` |
| Ruby | — not implemented — | — |
| Node | `envKey = "DATABASE_URL", pool: number = 0` | `Promise<Database>` |

#### `get_active_pool_count`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `int` |
| Ruby | — not implemented — | — |
| Node | `` | `int` |

#### `get_adapter`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `DatabaseAdapter` |
| Ruby | — not implemented — | — |
| Node | `` | `DatabaseAdapter` |

#### `get_columns`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `table: str` | `list[dict]` |
| PHP | `tableName: string` | `list[dict]` |
| Ruby | — not implemented — | — |
| Node | `tableName: string` | `untyped` |

#### `get_last_id`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `int|str` |
| Ruby | `` | `untyped` |
| Node | `` | `str|int` |

#### `get_pool_size`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `DatabaseAdapter` |
| Ruby | — not implemented — | — |
| Node | `` | `int` |

#### `get_tables`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list[str]` |
| PHP | `` | `list[str]` |
| Ruby | — not implemented — | — |
| Node | `` | `list[str]` |

#### `insert`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `table: str, data: dict | list` | `DatabaseResult` |
| PHP | `table: string, data: array` | `bool` |
| Ruby | `table, data` | `untyped` |
| Node | `table: string, data: Record<string, unknown>` | `DatabaseWriteResult` |

#### `rollback`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `None` |
| Ruby | — not implemented — | — |
| Node | `` | `None` |

#### `size`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `int` |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `start_transaction`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `None` |
| Ruby | — not implemented — | — |
| Node | `` | `None` |

#### `table_exists`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `name: str` | `bool` |
| PHP | `tableName: string` | `bool` |
| Ruby | `` | `untyped` |
| Node | `name: string` | `bool` |

#### `update`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `table: str, data: dict, filter_sql: str = '', params: list = None` | `DatabaseResult` |
| PHP | `table: string, data: array, filterSql: string '' = '', params: array [] = []` | `bool` |
| Ruby | `table, data, filter = {}` | `untyped` |
| Node | `table: string, data: Record<string, unknown>, filter?: Record<string, unknown>` | `DatabaseWriteResult` |

## Router

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `add_route` | — | — | `method, path, handler, auth_handler, swagger_meta, middleware, template` | `definition` | ⚠️ missing: Python, PHP |
| `any` | `path, handler, **options` | `path, callback` | `path, middleware, swagger_meta, template, &block` | `path, handler, middlewares?, meta?` | ⚠️ return type differs |
| `cache` | `max_age` | `()` | `()` | `()` | ⚠️ param count differs |
| `clear` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `delete` | `path, handler, **options` | `path, callback` | `path, middleware, swagger_meta, template, &block` | `path, handler, middlewares?, meta?` | ⚠️ return type differs |
| `get` | `path, handler, **options` | `path, callback` | `path, middleware, swagger_meta, template, &block` | `path, handler, middlewares?, meta?` | ⚠️ return type differs |
| `get_routes` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `get_web_socket_routes` | — | `()` | — | `()` | ⚠️ missing: Python, Ruby |
| `group` | `prefix, callback, middleware` | `prefix, callback, middleware` | `prefix, auth_handler, middleware, &block` | — | ⚠️ missing: Node |
| `list_routes` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `match` | `method, path` | `method, path` | `()` | `method, pathname` | ⚠️ return type differs |
| `no_auth` | — | `()` | `()` | `()` | ⚠️ missing: Python |
| `patch` | `path, handler, **options` | `path, callback` | `path, middleware, swagger_meta, template, &block` | `path, handler, middlewares?, meta?` | ⚠️ return type differs |
| `post` | `path, handler, **options` | `path, callback` | `path, middleware, swagger_meta, template, &block` | `path, handler, middlewares?, meta?` | ⚠️ return type differs |
| `put` | `path, handler, **options` | `path, callback` | `path, middleware, swagger_meta, template, &block` | `path, handler, middlewares?, meta?` | ⚠️ return type differs |
| `secure` | `()` | `()` | `()` | `()` | ✅ |
| `use` | — | `class` | `klass` | `middlewareClass` | ⚠️ missing: Python |
| `websocket` | `path, handler` | `path, handler` | `path, &block` | `path, handler` | ✅ |

### Mismatch Details

#### `add_route`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `method, path, handler, auth_handler: nil, swagger_meta: {}, middleware: [], template: nil` | `untyped` |
| Node | `definition: RouteDefinition` | `RouteRef` |

#### `any`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str, handler, **options` | `RouteRef` |
| PHP | `path: string, callback: callable` | `Self` |
| Ruby | `path, middleware: [], swagger_meta: {}, template: nil, &block` | `untyped` |
| Node | `path: string, handler: RouteHandler, middlewares?: Middleware[], meta?: RouteMeta` | `RouteRef` |

#### `cache`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `max_age: int | None = None` | `untyped` |
| PHP | `` | `Self` |
| Ruby | `` | `untyped` |
| Node | `` | `Self` |

#### `clear`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `list[dict]` |
| Ruby | `` | `untyped` |
| Node | `` | `None` |

#### `delete`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str, handler, **options` | `RouteRef` |
| PHP | `path: string, callback: callable` | `Self` |
| Ruby | `path, middleware: [], swagger_meta: {}, template: nil, &block` | `untyped` |
| Node | `path: string, handler: RouteHandler, middlewares?: Middleware[], meta?: RouteMeta` | `RouteRef` |

#### `get`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str, handler, **options` | `RouteRef` |
| PHP | `path: string, callback: callable` | `Self` |
| Ruby | `path, middleware: [], swagger_meta: {}, template: nil, &block` | `untyped` |
| Node | `path: string, handler: RouteHandler, middlewares?: Middleware[], meta?: RouteMeta` | `RouteRef` |

#### `get_routes`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list[dict]` |
| PHP | `` | `list[dict]` |
| Ruby | `` | `untyped` |
| Node | `` | `list[RouteDefinition]` |

#### `get_web_socket_routes`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `list[dict]` |
| Ruby | — not implemented — | — |
| Node | `` | `list[WebSocketRouteDefinition]` |

#### `group`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `prefix: str, callback, middleware = None` | `untyped` |
| PHP | `prefix: string, callback: callable, middleware: array [] = []` | `None` |
| Ruby | `prefix, auth_handler: nil, middleware: [], &block` | `untyped` |
| Node | — not implemented — | — |

#### `list_routes`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list[dict]` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `list[RouteInfo]` |

#### `match`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `method: str, path: str` | `tuple[dict|None, dict]` |
| PHP | `method: string, path: string` | `list` |
| Ruby | `` | `untyped` |
| Node | `method: string, pathname: string` | `MatchResult|None` |

#### `no_auth`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `Self` |
| Ruby | `` | `untyped` |
| Node | `` | `Self` |

#### `patch`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str, handler, **options` | `RouteRef` |
| PHP | `path: string, callback: callable` | `Self` |
| Ruby | `path, middleware: [], swagger_meta: {}, template: nil, &block` | `untyped` |
| Node | `path: string, handler: RouteHandler, middlewares?: Middleware[], meta?: RouteMeta` | `RouteRef` |

#### `post`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str, handler, **options` | `RouteRef` |
| PHP | `path: string, callback: callable` | `Self` |
| Ruby | `path, middleware: [], swagger_meta: {}, template: nil, &block` | `untyped` |
| Node | `path: string, handler: RouteHandler, middlewares?: Middleware[], meta?: RouteMeta` | `RouteRef` |

#### `put`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str, handler, **options` | `RouteRef` |
| PHP | `path: string, callback: callable` | `Self` |
| Ruby | `path, middleware: [], swagger_meta: {}, template: nil, &block` | `untyped` |
| Node | `path: string, handler: RouteHandler, middlewares?: Middleware[], meta?: RouteMeta` | `RouteRef` |

#### `use`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `class: string` | `None` |
| Ruby | `klass` | `untyped` |
| Node | `middlewareClass: any` | `None` |

## Session

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `all` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `clear` | `()` | `()` | `()` | `()` | ✅ |
| `cookie_header` | `cookie_name` | `cookieName` | `cookie_name` | `cookieName` | ✅ |
| `delete` | `key` | `key` | `key` | `key` | ✅ |
| `destroy` | `session_id` | `()` | `()` | `sessionId` | ⚠️ param count differs |
| `flash` | `key, value` | `key, value` | `key, value` | `key, value?` | ⚠️ return type differs |
| `gc` | `max_lifetime` | `()` | `max_age` | `_maxLifetime` | ⚠️ param count differs |
| `get` | `key, default` | `key, default` | `key, default` | `key, defaultValue?` | ⚠️ return type differs |
| `get_flash` | `key, default` | `key, default` | `key, default` | `key, defaultValue?` | ⚠️ return type differs |
| `get_session_id` | — | `()` | — | `()` | ⚠️ missing: Python, Ruby |
| `has` | `key` | `key` | `()` | `key` | ⚠️ param count differs |
| `read` | `session_id` | — | — | `sessionId` | ⚠️ missing: PHP, Ruby |
| `regenerate` | `()` | `()` | `()` | `()` | ✅ |
| `save` | `()` | `()` | `()` | `()` | ✅ |
| `set` | `key, value` | `key, value` | `key, value` | `key, value` | ✅ |
| `start` | `session_id` | `sessionId` | — | `sessionId?` | ⚠️ missing: Ruby |
| `write` | `session_id, data, ttl` | — | — | `sessionId, data, ttl` | ⚠️ missing: PHP, Ruby |

### Mismatch Details

#### `all`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `dict` |

#### `destroy`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `session_id: str` | `untyped` |
| PHP | `` | `None` |
| Ruby | `` | `untyped` |
| Node | `sessionId: string` | `None` |

#### `flash`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `key: str, value = None` | `untyped` |
| PHP | `key: string, value: mixed null = null` | `mixed` |
| Ruby | `key, value = nil` | `untyped` |
| Node | `key: string, value?: unknown` | `unknown` |

#### `gc`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `max_lifetime: int` | `untyped` |
| PHP | `` | `None` |
| Ruby | `max_age = nil` | `untyped` |
| Node | `_maxLifetime: number` | `None` |

#### `get`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `key: str, default = None` | `untyped` |
| PHP | `key: string, default: mixed null = null` | `mixed` |
| Ruby | `key, default = nil` | `untyped` |
| Node | `key: string, defaultValue?: unknown` | `unknown` |

#### `get_flash`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `key: str, default = None` | `untyped` |
| PHP | `key: string, default: mixed null = null` | `mixed` |
| Ruby | `key, default = nil` | `untyped` |
| Node | `key: string, defaultValue?: unknown` | `unknown` |

#### `get_session_id`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `str` |
| Ruby | — not implemented — | — |
| Node | `` | `str|None` |

#### `has`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `key: str` | `bool` |
| PHP | `key: string` | `bool` |
| Ruby | `` | `untyped` |
| Node | `key: string` | `bool` |

#### `read`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `session_id: str` | `dict` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `sessionId: string` | `SessionData|None` |

#### `start`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `session_id: str = None` | `str` |
| PHP | `sessionId: ?string null = null` | `str` |
| Ruby | — not implemented — | — |
| Node | `sessionId?: string` | `str` |

#### `write`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `session_id: str, data: dict, ttl: int` | `untyped` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `sessionId: string, data: SessionData, ttl: number` | `None` |

## Migration

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `create` | `description` | `description` | `name` | `description` | ⚠️ return type differs |
| `down` | — | — | `db` | `()` | ⚠️ missing: Python, PHP |
| `get_applied` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `get_files` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `get_pending` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `migrate` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `record_migration` | — | — | `name, batch, passed` | `name, batch` | ⚠️ missing: Python, PHP |
| `remove_migration_record` | — | — | `name` | `migration.name` | ⚠️ missing: Python, PHP |
| `rollback` | `steps` | `steps` | `steps` | `steps` | ⚠️ return type differs |
| `status` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `up` | — | — | `db` | `()` | ⚠️ missing: Python, PHP |

### Mismatch Details

#### `create`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `description: str` | `str` |
| PHP | `description: string` | `str` |
| Ruby | `name` | `untyped` |
| Node | `description: string` | `Promise<` |

#### `down`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `db` | `untyped` |
| Node | `` | `untyped` |

#### `get_applied`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list[dict]` |
| PHP | `` | `list[dict]` |
| Ruby | `` | `untyped` |
| Node | `` | `Promise<list[str]>` |

#### `get_files`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list[str]` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `list[str]` |

#### `get_pending`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list[dict]` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `Promise<list[str]>` |

#### `migrate`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list[str]` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `Promise<MigrationResult>` |

#### `record_migration`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `name, batch, passed: 1` | `untyped` |
| Node | `name, batch` | `untyped` |

#### `remove_migration_record`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `name` | `untyped` |
| Node | `migration.name` | `untyped` |

#### `rollback`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `steps: int = 1` | `list[str]` |
| PHP | `steps: int 1 = 1` | `list` |
| Ruby | `steps = 1` | `untyped` |
| Node | `steps = 1` | `Promise<list[str]>` |

#### `status`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `Promise<MigrationStatus>` |

#### `up`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `db` | `untyped` |
| Node | `` | `untyped` |

## MCP

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `handle_message` | `raw_data` | `rawData` | `raw_data` | `rawData, unknown>` | ⚠️ param count differs |
| `register_resource` | `uri, handler, description, mime_type` | `uri, handler, description, mimeType` | `uri, handler, description, mime_type` | `uri, handler, description, mimeType` | ✅ |
| `register_routes` | `router_module` | `()` | `()` | — | ⚠️ missing: Node |
| `register_tool` | `name, handler, description, schema` | `name, handler, description, schema` | `name, handler, description, schema` | `name, handler, unknown>), description, schema?` | ⚠️ param count differs |
| `write_claude_config` | `port` | `port` | `port` | `port` | ✅ |

### Mismatch Details

#### `handle_message`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `raw_data: str | dict` | `str` |
| PHP | `rawData: string|array` | `str` |
| Ruby | `raw_data` | `untyped` |
| Node | `rawData: string | Record<string, unknown>` | `str` |

#### `register_routes`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `router_module` | `untyped` |
| PHP | `` | `None` |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `register_tool`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `name: str, handler, description: str = '', schema: dict | None = None` | `untyped` |
| PHP | `name: string, handler: callable, description: string '' = '', schema: ?array null = null` | `None` |
| Ruby | `name, handler, description = "", schema = nil` | `untyped` |
| Node | `name: string, handler: (args: Record<string, unknown>) => unknown, description = "", schema?: JsonSchema` | `None` |

## Frond

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `add_filter` | `name, fn` | `name, fn` | `name, &blk` | `name, fn` | ✅ |
| `add_global` | `name, value` | `name, value` | `name, value` | `name, value` | ✅ |
| `add_test` | `name, fn` | `name, fn` | `name, &blk` | `name, fn` | ⚠️ return type differs |
| `clear_cache` | `()` | `()` | `()` | `()` | ✅ |
| `render` | `template, data` | `template, data` | `template, data` | `template, data?, unknown>` | ⚠️ param count differs |
| `render_string` | `source, data` | `source, data, templateName` | `source, data` | `source, data?, unknown>` | ⚠️ param count differs |
| `sandbox` | `allowed_filters, allowed_tags, allowed_vars` | `filters, tags, vars` | `filters, tags, vars` | `filters?, tags?, vars?` | ⚠️ return type differs |
| `unsandbox` | `()` | `()` | `()` | `()` | ⚠️ return type differs |

### Mismatch Details

#### `add_test`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `name: str, fn` | `untyped` |
| PHP | `name: string, fn: callable` | `dict` |
| Ruby | `name, &blk` | `untyped` |
| Node | `name: string, fn: TestFn` | `None` |

#### `render`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `template: str, data: dict = None` | `str` |
| PHP | `template: string, data: array [] = []` | `str` |
| Ruby | `template, data = {}` | `untyped` |
| Node | `template: string, data?: Record<string, unknown>` | `str` |

#### `render_string`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `source: str, data: dict = None` | `str` |
| PHP | `source: string, data: array [] = [], templateName: ?string null = null` | `str` |
| Ruby | `source, data = {}` | `untyped` |
| Node | `source: string, data?: Record<string, unknown>` | `str` |

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
| `add_mutation` | `name, config` | `name, args, returnType, resolver` | `name, type, args, description, &resolve` | `name, args, string>, returnType, resolver` | ⚠️ return type differs |
| `add_query` | `name, config` | `name, args, returnType, resolver` | `name, type, args, description, &resolve` | `name, args, string>, returnType, resolver` | ⚠️ return type differs |
| `add_type` | `name, fields` | `name, fields` | `type` | `name, fields, GraphQLField>` | ⚠️ return type differs |
| `advance` | `()` | — | `()` | `()` | ⚠️ missing: PHP |
| `execute` | `query, variables, context` | `query, variables` | `document, variables, context, operation_name` | `query, variables?, unknown>` | ⚠️ return type differs |
| `expect` | `type, value` | — | `type, value` | `type, value?` | ⚠️ missing: PHP |
| `from_orm` | `orm_class` | `ormInstance` | `klass` | `modelClass, { type, adapter?, unknown>>(sql, params?, params?` | ⚠️ return type differs |
| `introspect` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `match` | `type, value` | — | `type, value` | `type, value?` | ⚠️ missing: PHP |
| `parse` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `peek` | `()` | — | `offset` | `()` | ⚠️ missing: PHP |
| `schema_sdl` | `()` | `()` | `()` | `()` | ✅ |

### Mismatch Details

#### `add_mutation`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `name: str, config: dict` | `untyped` |
| PHP | `name: string, args: array, returnType: string, resolver: callable` | `Self` |
| Ruby | `name, type:, args: {}, description: nil, &resolve` | `untyped` |
| Node | `name: string, args: Record<string, string>, returnType: string, resolver: ResolverFn` | `GraphQL` |

#### `add_query`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `name: str, config: dict` | `untyped` |
| PHP | `name: string, args: array, returnType: string, resolver: callable` | `Self` |
| Ruby | `name, type:, args: {}, description: nil, &resolve` | `untyped` |
| Node | `name: string, args: Record<string, string>, returnType: string, resolver: ResolverFn` | `GraphQL` |

#### `add_type`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `name: str, fields: dict[str, str]` | `untyped` |
| PHP | `name: string, fields: array` | `Self` |
| Ruby | `type` | `untyped` |
| Node | `name: string, fields: Record<string, GraphQLField>` | `GraphQL` |

#### `advance`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `Token` |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | `` | `Token` |

#### `execute`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `query: str, variables: dict = None, context: dict = None` | `dict` |
| PHP | `query: string, variables: ?array null = null` | `list` |
| Ruby | `document, variables: {}, context: {}, operation_name: nil` | `untyped` |
| Node | `query: string, variables?: Record<string, unknown>` | `GraphQLResult` |

#### `expect`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `type: str, value: str = None` | `Token` |
| PHP | — not implemented — | — |
| Ruby | `type, value = nil` | `untyped` |
| Node | `type: string, value?: string` | `Token` |

#### `from_orm`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `orm_class` | `untyped` |
| PHP | `ormInstance: ORM` | `Self` |
| Ruby | `klass` | `untyped` |
| Node | `modelClass: {       tableName: string;       fields: Record<string, { type: string; primaryKey?: boolean }>;       name?: string;     }, adapter?: {       query: <T = Record<string, unknown>>(sql: string, params?: unknown[]) => T[];       execute: (sql: string, params?: unknown[]) => unknown;     }` | `GraphQL` |

#### `introspect`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `dict` |

#### `match`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `type: str, value: str = None` | `Token|None` |
| PHP | — not implemented — | — |
| Ruby | `type, value = nil` | `untyped` |
| Node | `type: string, value?: string` | `Token|None` |

#### `parse`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `untyped` |

#### `peek`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `Token|None` |
| PHP | — not implemented — | — |
| Ruby | `offset = 0` | `untyped` |
| Node | `` | `Token|None` |
