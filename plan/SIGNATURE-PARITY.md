# Tina4 Signature Parity Report

> Auto-generated on 2026-04-08

Compares public method signatures (params + return types) across Python, PHP, Ruby, and Node.js.
Methods are matched by normalised snake_case name. ✅ = full parity, ⚠️ = mismatch or missing.

## Summary

| Feature | Methods | ✅ Match | ⚠️ Mismatch | ⚠️ Missing |
|---------|--------:|--------:|------------:|----------:|
| ORM | 72 | 4 | 17 | 51 |
| Queue | 29 | 2 | 10 | 17 |
| Job | 24 | 0 | 1 | 23 |
| Auth | 37 | 3 | 5 | 29 |
| Database | 58 | 3 | 8 | 47 |
| Router | 42 | 3 | 9 | 30 |
| Session | 27 | 5 | 7 | 15 |
| Migration | 34 | 0 | 2 | 32 |
| MCP | 32 | 2 | 2 | 28 |
| Frond | 79 | 4 | 4 | 71 |
| GraphQL | 52 | 1 | 7 | 44 |

## ORM

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `all` | `limit, offset, include` | `limit, offset, include` | `limit, offset, order_by, include` | `unknown>), where?, params?, include?` | ⚠️ return type differs |
| `auto_crud` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `auto_discover_db` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `auto_map` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `belongs_to` | `related_class, foreign_key` | `relatedClass, foreignKey` | `name, class_name, foreign_key` | `relatedClass, unknown>), foreignKey` | ⚠️ return type differs |
| `cached` | `sql, params, ttl, limit, offset` | `sql, params, ttl, limit, offset, include` | — | — | ⚠️ missing: Ruby, Node |
| `clear_cache` | `()` | `()` | — | — | ⚠️ missing: Ruby, Node |
| `clear_rel_cache` | — | `()` | — | `()` | ⚠️ missing: Python, Ruby |
| `count` | `conditions, params` | `conditions, params` | `conditions, params` | `conditions?, params?` | ✅ |
| `create` | `data, **kwargs` | `data` | `attributes` | `unknown>), data, unknown>` | ⚠️ return type differs |
| `create_table` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `db` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `delete` | `()` | `()` | `()` | — | ⚠️ missing: Node |
| `eager_load` | — | `include, db` | `instances, include_list` | — | ⚠️ missing: Python, Node |
| `errors` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `exists` | `pk_value` | `()` | — | — | ⚠️ missing: Ruby, Node |
| `field_mapping` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `fill` | — | `data` | — | — | ⚠️ missing: Python, Ruby, Node |
| `find` | `filter, limit, offset, order_by, include` | `filter, limit, offset, orderBy, include` | `filter, limit, offset, order_by, include, **extra_filter` | `unknown>), filter?, unknown>, limit, offset, orderBy?, include?` | ⚠️ return type differs |
| `find_by_filter` | — | — | `filter` | — | ⚠️ missing: Python, PHP, Node |
| `find_by_id` | `pk_value, include` | `id, include` | `id` | — | ⚠️ missing: Node |
| `find_or_fail` | `pk_value` | `id` | `id` | — | ⚠️ missing: Node |
| `force_delete` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `from_hash` | — | — | `hash` | — | ⚠️ missing: Python, PHP, Node |
| `get_data` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `get_db` | — | `()` | — | `()` | ⚠️ missing: Python, Ruby |
| `get_db_column` | — | `property` | — | `prop` | ⚠️ missing: Python, Ruby |
| `get_db_data` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `get_pk_column` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `get_pk_field` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `get_primary_key_value` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `get_reverse_mapping` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `has_many` | `related_class, foreign_key, limit, offset` | `relatedClass, foreignKey, limit, offset` | `name, class_name, foreign_key` | `relatedClass, unknown>), foreignKey, limit, offset` | ⚠️ return type differs |
| `has_one` | `related_class, foreign_key` | `relatedClass, foreignKey` | `name, class_name, foreign_key` | `relatedClass, unknown>), foreignKey` | ⚠️ return type differs |
| `load` | `filter, params, include` | `filter, params, include` | `filter, params, include` | `filter?, params?, include?` | ✅ |
| `load_belongs_to` | — | — | `name` | — | ⚠️ missing: Python, PHP, Node |
| `load_has_many` | — | — | `name` | — | ⚠️ missing: Python, PHP, Node |
| `load_has_one` | — | — | `name` | — | ⚠️ missing: Python, PHP, Node |
| `mark_as_existing` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `persisted` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `query` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `query_belongs_to` | — | — | `related_class, foreign_key` | — | ⚠️ missing: Python, PHP, Node |
| `query_has_many` | — | — | `related_class, foreign_key, limit, offset` | — | ⚠️ missing: Python, PHP, Node |
| `query_has_one` | — | — | `related_class, foreign_key` | — | ⚠️ missing: Python, PHP, Node |
| `register_model` | — | — | — | `name, modelClass` | ⚠️ missing: Python, PHP, Ruby |
| `relationship_definitions` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `restore` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `save` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `scope` | `name, filter_sql, params` | `name, filterSql, params` | `name, filter_sql, params` | `name, filterSql, params?` | ✅ |
| `select` | `sql, params, limit, offset, include` | `sql, params, limit, offset, include` | `*fields` | `unknown>), sql, params?` | ⚠️ return type differs |
| `select_one` | `sql, params, include` | `sql, params, include` | `sql, params, include` | `unknown>), sql, params?, include?` | ⚠️ return type differs |
| `self.camel_to_snake` | — | — | `name` | — | ⚠️ missing: Python, PHP, Node |
| `self.snake_to_camel` | — | — | `name` | — | ⚠️ missing: Python, PHP, Node |
| `set_adapter` | — | — | — | `adapter` | ⚠️ missing: Python, PHP, Ruby |
| `set_db` | — | `db` | — | — | ⚠️ missing: Python, Ruby, Node |
| `set_global_db` | — | `db` | — | — | ⚠️ missing: Python, Ruby, Node |
| `set_rel_cache` | — | `name, value` | — | — | ⚠️ missing: Python, Ruby, Node |
| `soft_delete` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `soft_delete_field` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `to_array` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `to_assoc` | `include` | `include` | — | `include?` | ⚠️ missing: Ruby |
| `to_db_hash` | — | — | `exclude_nil` | — | ⚠️ missing: Python, PHP, Node |
| `to_dict` | `include` | `include` | — | `include?` | ⚠️ missing: Ruby |
| `to_h` | — | — | `include` | — | ⚠️ missing: Python, PHP, Node |
| `to_json` | `include` | `include` | `include, **_args` | `include?` | ✅ |
| `to_list` | `()` | `()` | — | `()` | ⚠️ missing: Ruby |
| `to_object` | `()` | `()` | — | `()` | ⚠️ missing: Ruby |
| `to_s` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `validate` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `validate_fields` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `where` | `filter_sql, params, limit, offset, include` | `filterSql, params, limit, offset, include` | `conditions, params, include` | `unknown>), conditions, params?, limit, offset, include?` | ⚠️ return type differs |
| `with_trashed` | `filter_sql, params, limit, offset` | `filterSql, params, limit, offset` | `conditions, params, limit, offset` | `unknown>), conditions?, params?, limit?, offset?` | ⚠️ return type differs |

### Mismatch Details

#### `all`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `limit: int = 100, offset: int = 0, include: list[str] = None` | `untyped` |
| PHP | `limit: int 100 = 100, offset: int 0 = 0, include: ?array null = null` | `list` |
| Ruby | `limit: nil, offset: nil, order_by: nil, include: nil` | `untyped` |
| Node | `unknown>) => T, where?: string, params?: unknown[], include?: string[]` | `list[T]` |

#### `auto_crud`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `auto_discover_db`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `auto_map`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `belongs_to`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `related_class, foreign_key: str = None` | `untyped` |
| PHP | `relatedClass: string, foreignKey: ?string null = null` | `?Self` |
| Ruby | `name, class_name: nil, foreign_key: nil` | `untyped` |
| Node | `relatedClass: typeof BaseModel & (new (data?: Record<string, unknown>) => R), foreignKey: string` | `R | None` |

#### `cached`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `sql: str, params: list = None, ttl: int = 60, limit: int = 20, offset: int = 0` | `untyped` |
| PHP | `sql: string, params: array [] = [], ttl: int 60 = 60, limit: int 20 = 20, offset: int 0 = 0, include: ?array null = null` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `clear_cache`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `None` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

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
| Python | `data: dict = None, **kwargs` | `untyped` |
| PHP | `data: array [] = []` | `Self` |
| Ruby | `attributes = {}` | `untyped` |
| Node | `unknown>) => T, data: Record<string, unknown>` | `T` |

#### `create_table`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `bool` |
| PHP | `` | `bool` |
| Ruby | `` | `untyped` |
| Node | `` | `None` |

#### `db`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `delete`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `bool` |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `eager_load`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `include: array, db: DatabaseAdapter` | `None` |
| Ruby | `instances, include_list` | `untyped` |
| Node | — not implemented — | — |

#### `errors`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `exists`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `pk_value` | `bool` |
| PHP | `` | `bool` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `field_mapping`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `fill`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `data: array` | `Self` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `find`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `filter: dict = None, limit: int = 100, offset: int = 0, order_by: str = None, include: list[str] = None` | `untyped` |
| PHP | `filter: array [] = [], limit: int 100 = 100, offset: int 0 = 0, orderBy: ?string null = null, include: ?array null = null` | `list` |
| Ruby | `filter = {}, limit: 100, offset: 0, order_by: nil, include: nil, **extra_filter` | `untyped` |
| Node | `unknown>) => T, filter?: Record<string, unknown>, limit = 100, offset = 0, orderBy?: string, include?: string[]` | `list[T]` |

#### `find_by_filter`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `filter` | `untyped` |
| Node | — not implemented — | — |

#### `find_by_id`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `pk_value, include: list[str] = None` | `untyped` |
| PHP | `id: int|string, include: ?array null = null` | `?Self` |
| Ruby | `id` | `untyped` |
| Node | — not implemented — | — |

#### `find_or_fail`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `pk_value` | `untyped` |
| PHP | `id: int|string` | `Self` |
| Ruby | `id` | `untyped` |
| Node | — not implemented — | — |

#### `force_delete`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `bool` |
| Ruby | `` | `untyped` |
| Node | `` | `None` |

#### `from_hash`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `hash` | `untyped` |
| Node | — not implemented — | — |

#### `get_data`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `get_db`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `?DatabaseAdapter` |
| Ruby | — not implemented — | — |
| Node | `` | `DatabaseAdapter` |

#### `get_db_column`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `property: string` | `str` |
| Ruby | — not implemented — | — |
| Node | `prop: string` | `str` |

#### `get_db_data`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `dict` |

#### `get_pk_column`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `str` |

#### `get_pk_field`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `str` |

#### `get_primary_key_value`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `int|str|None` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `get_reverse_mapping`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `dict` |

#### `has_many`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `related_class, foreign_key: str = None, limit: int = 100, offset: int = 0` | `untyped` |
| PHP | `relatedClass: string, foreignKey: ?string null = null, limit: int 100 = 100, offset: int 0 = 0` | `list` |
| Ruby | `name, class_name: nil, foreign_key: nil` | `untyped` |
| Node | `relatedClass: typeof BaseModel & (new (data?: Record<string, unknown>) => R), foreignKey: string, limit: number = 100, offset: number = 0` | `list[R]` |

#### `has_one`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `related_class, foreign_key: str = None` | `untyped` |
| PHP | `relatedClass: string, foreignKey: ?string null = null` | `?Self` |
| Ruby | `name, class_name: nil, foreign_key: nil` | `untyped` |
| Node | `relatedClass: typeof BaseModel & (new (data?: Record<string, unknown>) => R), foreignKey: string` | `R | None` |

#### `load_belongs_to`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `name` | `untyped` |
| Node | — not implemented — | — |

#### `load_has_many`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `name` | `untyped` |
| Node | — not implemented — | — |

#### `load_has_one`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `name` | `untyped` |
| Node | — not implemented — | — |

#### `mark_as_existing`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `None` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `persisted`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `query`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `'QueryBuilder'` |
| PHP | `` | `QueryBuilder` |
| Ruby | `` | `untyped` |
| Node | `` | `QueryBuilder` |

#### `query_belongs_to`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `related_class, foreign_key: nil` | `untyped` |
| Node | — not implemented — | — |

#### `query_has_many`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `related_class, foreign_key: nil, limit: 100, offset: 0` | `untyped` |
| Node | — not implemented — | — |

#### `query_has_one`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `related_class, foreign_key: nil` | `untyped` |
| Node | — not implemented — | — |

#### `register_model`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `name: string, modelClass: typeof BaseModel` | `None` |

#### `relationship_definitions`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `restore`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `bool` |
| Ruby | `` | `untyped` |
| Node | `` | `None` |

#### `save`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `Self|false` |
| Ruby | `` | `untyped` |
| Node | `` | `Self | false` |

#### `select`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `sql: str, params: list = None, limit: int = 20, offset: int = 0, include: list[str] = None` | `list` |
| PHP | `sql: string, params: array [] = [], limit: int 20 = 20, offset: int 0 = 0, include: ?array null = null` | `list` |
| Ruby | `*fields` | `untyped` |
| Node | `unknown>) => T, sql: string, params?: unknown[]` | `list[T]` |

#### `select_one`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `sql: str, params: list = None, include: list[str] = None` | `untyped` |
| PHP | `sql: string, params: array [] = [], include: ?array null = null` | `?Self` |
| Ruby | `sql, params = [], include: nil` | `untyped` |
| Node | `unknown>) => T, sql: string, params?: unknown[], include?: string[]` | `T | None` |

#### `self.camel_to_snake`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `name` | `untyped` |
| Node | — not implemented — | — |

#### `self.snake_to_camel`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `name` | `untyped` |
| Node | — not implemented — | — |

#### `set_adapter`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `adapter` | `untyped` |

#### `set_db`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `db: DatabaseAdapter` | `Self` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `set_global_db`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `db: DatabaseAdapter` | `None` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `set_rel_cache`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `name: string, value: mixed` | `None` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `soft_delete`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `soft_delete_field`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `to_array`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `list[unknown]` |

#### `to_assoc`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `include: list[str] = None` | `dict` |
| PHP | `include: ?array null = null` | `list` |
| Ruby | — not implemented — | — |
| Node | `include?: string[]` | `dict` |

#### `to_db_hash`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `exclude_nil: false` | `untyped` |
| Node | — not implemented — | — |

#### `to_dict`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `include: list[str] = None` | `dict` |
| PHP | `include: ?array null = null` | `list` |
| Ruby | — not implemented — | — |
| Node | `include?: string[]` | `dict` |

#### `to_h`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `include: nil` | `untyped` |
| Node | — not implemented — | — |

#### `to_list`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list` |
| PHP | `` | `list` |
| Ruby | — not implemented — | — |
| Node | `` | `list[unknown]` |

#### `to_object`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `object` |
| Ruby | — not implemented — | — |
| Node | `` | `dict` |

#### `to_s`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `validate`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list[str]` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `list[str]` |

#### `validate_fields`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `where`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `filter_sql: str, params: list = None, limit: int = 20, offset: int = 0, include: list[str] = None` | `list` |
| PHP | `filterSql: string, params: array [] = [], limit: int 20 = 20, offset: int 0 = 0, include: ?array null = null` | `list` |
| Ruby | `conditions, params = [], include: nil` | `untyped` |
| Node | `unknown>) => T, conditions: string, params?: unknown[], limit: number = 20, offset: number = 0, include?: string[]` | `list[T]` |

#### `with_trashed`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `filter_sql: str = '1=1', params: list = None, limit: int = 20, offset: int = 0` | `untyped` |
| PHP | `filterSql: string = '1=1', params: array [] = [], limit: int 20 = 20, offset: int 0 = 0` | `list` |
| Ruby | `conditions = "1=1", params = [], limit: 20, offset: 0` | `untyped` |
| Node | `unknown>) => T, conditions?: string, params?: unknown[], limit?: number, offset?: number` | `list[T]` |

## Queue

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `backend` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `clear` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `complete` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `consume` | `topic, job_id, poll_interval, iterations` | `topic, id, pollInterval` | `topic, id, poll_interval, iterations, &block` | `topic?, id?, pollInterval, iterations` | ⚠️ return type differs |
| `dead_letters` | `()` | `()` | `()` | `maxRetries?` | ⚠️ return type differs |
| `fail` | — | `reason` | — | — | ⚠️ missing: Python, Ruby, Node |
| `failed` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `get_base_path` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `get_external_backend` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `get_max_retries` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `get_topic` | — | `()` | — | `()` | ⚠️ missing: Python, Ruby |
| `pop` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `pop_by_id` | `job_id` | `id` | `id` | `id` | ⚠️ return type differs |
| `process` | — | `handlerOrQueue, queueOrHandlerOrOptions, options` | — | `handler, options?` | ⚠️ missing: Python, Ruby |
| `process_email` | — | — | — | `job` | ⚠️ missing: Python, PHP, Ruby |
| `produce` | `topic, data, priority, delay_seconds` | `topic, payload, delay` | `topic, payload, priority` | `topic, payload, delay?, priority` | ⚠️ param count differs |
| `purge` | `status` | `status` | `status` | `status, maxRetries?` | ⚠️ param count differs |
| `push` | `data, priority, delay_seconds` | `payload, delay, priority` | `payload, priority, delay_seconds` | `payload, delay?, priority` | ✅ |
| `reject` | — | `reason` | — | — | ⚠️ missing: Python, Ruby, Node |
| `resolve_backend_arg` | — | — | `backend` | — | ⚠️ missing: Python, PHP, Node |
| `retry` | `job_id, delay_seconds` | `jobId, delaySeconds` | `delay_seconds` | `delaySeconds?` | ⚠️ param count differs |
| `retry_failed` | `()` | `()` | `()` | `maxRetries?` | ⚠️ param count differs |
| `self.parse_amqp_url` | — | — | `url` | — | ⚠️ missing: Python, PHP, Node |
| `self.resolve_backend` | — | — | `name` | — | ⚠️ missing: Python, PHP, Node |
| `self.resolve_kafka_config` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `self.resolve_mongo_config` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `self.resolve_rabbitmq_config` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `size` | `status` | `status` | `status` | `status` | ✅ |
| `to_array` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |

### Mismatch Details

#### `backend`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `clear`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `int` |
| PHP | `` | `None` |
| Ruby | `` | `untyped` |
| Node | `` | `None` |

#### `complete`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `None` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `consume`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `topic: str = None, job_id: str = None, poll_interval: float = 1.0, iterations: int = 0` | `untyped` |
| PHP | `topic: string '' = '', id: ?string null = null, pollInterval: float 1.0 = 1.0` | `\Generator` |
| Ruby | `topic = nil, id: nil, poll_interval: 1.0, iterations: 0, &block` | `untyped` |
| Node | `topic?: string, id?: string, pollInterval: number = 1000, iterations: number = 0` | `AsyncGenerator<QueueJob>` |

#### `dead_letters`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list[dict]` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `maxRetries?: number` | `list[QueueJob]` |

#### `fail`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `reason: string '' = ''` | `None` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `failed`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list[dict]` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `list[QueueJob]` |

#### `get_base_path`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `str` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `get_external_backend`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `?QueueBackend` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `get_max_retries`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `int` |

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
| Python | `` | `Job | None` |
| PHP | `` | `?list` |
| Ruby | `` | `untyped` |
| Node | `` | `QueueJob | None` |

#### `pop_by_id`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `job_id: str` | `Job | None` |
| PHP | `id: string` | `?list` |
| Ruby | `id` | `untyped` |
| Node | `id: string` | `QueueJob | None` |

#### `process`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `handlerOrQueue: callable|string, queueOrHandlerOrOptions: callable|string|array '' = '', options: array [] = []` | `None` |
| Ruby | — not implemented — | — |
| Node | `handler: (job: QueueJob) => Promise<void> | void, options?: ProcessOptions` | `None` |

#### `process_email`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `job` | `untyped` |

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
| Ruby | `status` | `untyped` |
| Node | `status: string, maxRetries?: number` | `int` |

#### `reject`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `reason: string '' = ''` | `None` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `resolve_backend_arg`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `backend` | `untyped` |
| Node | — not implemented — | — |

#### `retry`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `job_id: str, delay_seconds: int = 0` | `bool` |
| PHP | `jobId: string, delaySeconds: int 0 = 0` | `bool` |
| Ruby | `delay_seconds = 0` | `untyped` |
| Node | `delaySeconds?: number` | `bool` |

#### `retry_failed`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `int` |
| PHP | `` | `int` |
| Ruby | `` | `untyped` |
| Node | `maxRetries?: number` | `int` |

#### `self.parse_amqp_url`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `url` | `untyped` |
| Node | — not implemented — | — |

#### `self.resolve_backend`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `name = nil` | `untyped` |
| Node | — not implemented — | — |

#### `self.resolve_kafka_config`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `self.resolve_mongo_config`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `self.resolve_rabbitmq_config`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `to_array`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

## Job

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `clear` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `complete` | `()` | `()` | `()` | — | ⚠️ missing: Node |
| `consume` | — | — | — | `topic?, id?, pollInterval, iterations` | ⚠️ missing: Python, PHP, Ruby |
| `data` | `()` | — | — | — | ⚠️ missing: PHP, Ruby, Node |
| `dead_letters` | — | — | — | `maxRetries?` | ⚠️ missing: Python, PHP, Ruby |
| `fail` | `error` | `reason` | `reason` | — | ⚠️ missing: Node |
| `failed` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `get_max_retries` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `get_topic` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `increment_attempts` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `pop` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `pop_by_id` | — | — | — | `id` | ⚠️ missing: Python, PHP, Ruby |
| `process` | — | — | — | `handler, options?` | ⚠️ missing: Python, PHP, Ruby |
| `process_email` | — | — | — | `job` | ⚠️ missing: Python, PHP, Ruby |
| `produce` | — | — | — | `topic, payload, delay?, priority` | ⚠️ missing: Python, PHP, Ruby |
| `purge` | — | — | — | `status, maxRetries?` | ⚠️ missing: Python, PHP, Ruby |
| `push` | — | — | — | `payload, delay?, priority` | ⚠️ missing: Python, PHP, Ruby |
| `reject` | `reason` | `reason` | `reason` | — | ⚠️ missing: Node |
| `retry` | `delay_seconds` | `delaySeconds` | `queue, delay_seconds` | `delaySeconds?` | ⚠️ return type differs |
| `retry_failed` | — | — | — | `maxRetries?` | ⚠️ missing: Python, PHP, Ruby |
| `size` | — | — | — | `status` | ⚠️ missing: Python, PHP, Ruby |
| `to_array` | `()` | `()` | `()` | — | ⚠️ missing: Node |
| `to_hash` | `()` | `()` | `()` | — | ⚠️ missing: Node |
| `to_json` | `()` | `()` | `*_args` | — | ⚠️ missing: Node |

### Mismatch Details

#### `clear`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `None` |

#### `complete`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `None` |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `consume`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `topic?: string, id?: string, pollInterval: number = 1000, iterations: number = 0` | `AsyncGenerator<QueueJob>` |

#### `data`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `dead_letters`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `maxRetries?: number` | `list[QueueJob]` |

#### `fail`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `error: str = ''` | `untyped` |
| PHP | `reason: string '' = ''` | `None` |
| Ruby | `reason = ""` | `untyped` |
| Node | — not implemented — | — |

#### `failed`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `list[QueueJob]` |

#### `get_max_retries`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `int` |

#### `get_topic`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `str` |

#### `increment_attempts`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `pop`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `QueueJob | None` |

#### `pop_by_id`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `id: string` | `QueueJob | None` |

#### `process`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `handler: (job: QueueJob) => Promise<void> | void, options?: ProcessOptions` | `None` |

#### `process_email`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `job` | `untyped` |

#### `produce`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `topic: string, payload: unknown, delay?: number, priority: number = 0` | `str` |

#### `purge`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `status: string, maxRetries?: number` | `int` |

#### `push`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `payload: unknown, delay?: number, priority: number = 0` | `str` |

#### `reject`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `reason: str = ''` | `untyped` |
| PHP | `reason: string '' = ''` | `None` |
| Ruby | `reason = ""` | `untyped` |
| Node | — not implemented — | — |

#### `retry`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `delay_seconds: int = 0` | `untyped` |
| PHP | `delaySeconds: int 0 = 0` | `None` |
| Ruby | `queue:, delay_seconds: 0` | `untyped` |
| Node | `delaySeconds?: number` | `bool` |

#### `retry_failed`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `maxRetries?: number` | `int` |

#### `size`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `status: string = "pending"` | `int` |

#### `to_array`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `to_hash`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `to_json`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `str` |
| PHP | `` | `str` |
| Ruby | `*_args` | `untyped` |
| Node | — not implemented — | — |

## Auth

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `auth_handler` | — | — | `&block` | — | ⚠️ missing: Python, PHP, Node |
| `auth_middleware` | — | — | — | `secret?, algorithm` | ⚠️ missing: Python, PHP, Ruby |
| `authenticate_request` | `headers` | `headers` | `headers` | `headers, string | string[] | undefined>, secret?, algorithm` | ⚠️ return type differs |
| `authenticate_request_static` | `headers` | — | — | — | ⚠️ missing: PHP, Ruby, Node |
| `base64url_decode` | — | — | `str` | — | ⚠️ missing: Python, PHP, Node |
| `base64url_encode` | — | — | `data` | — | ⚠️ missing: Python, PHP, Node |
| `bearer_auth` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `before_request` | `request, response` | — | — | — | ⚠️ missing: PHP, Ruby, Node |
| `check_password` | `password, hashed` | `password, hash` | `password, hash` | `"secret123", hash` | ✅ |
| `default_auth_handler` | — | — | `env` | — | ⚠️ missing: Python, PHP, Node |
| `default_secure_auth` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `ensure_keys` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `generate_keys` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `get_payload` | `token` | `token` | `token` | `token` | ⚠️ return type differs |
| `get_payload_static` | `token` | — | — | — | ⚠️ missing: PHP, Ruby, Node |
| `get_token` | `payload, expires_in` | `payload, expiresIn` | `payload, expires_in` | `payload, unknown>, expiresIn` | ⚠️ param count differs |
| `get_token_static` | `payload, expires_in` | — | — | — | ⚠️ missing: PHP, Ruby, Node |
| `hash_password` | `password, salt, iterations` | `password, salt, iterations` | `password, salt, iterations` | `password, salt?, iterations` | ✅ |
| `hmac_decode` | — | — | `token, secret` | — | ⚠️ missing: Python, PHP, Node |
| `hmac_encode` | — | — | `claims, secret` | — | ⚠️ missing: Python, PHP, Node |
| `hmac_secret` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `middleware` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `next` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `private_key` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `private_key_path` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `public_key` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `public_key_path` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `refresh_token` | `token, expires_in` | `token, expiresIn` | `token, expires_in` | `token, expiresIn` | ⚠️ return type differs |
| `refresh_token_static` | `token, expires_in` | — | — | — | ⚠️ missing: PHP, Ruby, Node |
| `res` | — | — | — | `{ error, 401` | ⚠️ missing: Python, PHP, Ruby |
| `setup` | — | — | `root_dir` | — | ⚠️ missing: Python, PHP, Node |
| `use_hmac` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `valid_token` | `token` | `token` | `token` | `token` | ⚠️ return type differs |
| `valid_token_detail` | — | — | `token` | — | ⚠️ missing: Python, PHP, Node |
| `valid_token_static` | `token` | — | — | — | ⚠️ missing: PHP, Ruby, Node |
| `validate_api_key` | `provided, expected` | `provided, expected` | `provided, expected` | `provided, expected?` | ✅ |
| `validate_api_key_static` | `provided, expected` | — | — | — | ⚠️ missing: PHP, Ruby, Node |

### Mismatch Details

#### `auth_handler`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `&block` | `untyped` |
| Node | — not implemented — | — |

#### `auth_middleware`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `secret?: string, algorithm: string = "HS256"` | `Middleware` |

#### `authenticate_request`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `headers: dict` | `dict | None` |
| PHP | `headers: array` | `?list` |
| Ruby | `headers` | `untyped` |
| Node | `headers: Record<string, string | string[] | undefined>, secret?: string, algorithm: string = "HS256"` | `dict | None` |

#### `authenticate_request_static`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `headers: dict` | `dict | None` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `base64url_decode`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `str` | `untyped` |
| Node | — not implemented — | — |

#### `base64url_encode`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `data` | `untyped` |
| Node | — not implemented — | — |

#### `bearer_auth`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `before_request`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `request, response` | `untyped` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `default_auth_handler`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `env` | `untyped` |
| Node | — not implemented — | — |

#### `default_secure_auth`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `ensure_keys`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `generate_keys`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `get_payload`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `token: str` | `dict | None` |
| PHP | `token: string` | `?list` |
| Ruby | `token` | `untyped` |
| Node | `token: string` | `dict | None` |

#### `get_payload_static`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `token: str` | `dict | None` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `get_token`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `payload: dict, expires_in: int = None` | `str` |
| PHP | `payload: array, expiresIn: int 3600 = 3600` | `str` |
| Ruby | `payload, expires_in: 60` | `untyped` |
| Node | `payload: Record<string, unknown>, expiresIn: number = 3600` | `str` |

#### `get_token_static`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `payload: dict, expires_in: int = 60` | `str` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `hmac_decode`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `token, secret` | `untyped` |
| Node | — not implemented — | — |

#### `hmac_encode`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `claims, secret` | `untyped` |
| Node | — not implemented — | — |

#### `hmac_secret`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `middleware`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `callable` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `next`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `untyped` |

#### `private_key`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `private_key_path`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `public_key`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `public_key_path`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `refresh_token`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `token: str, expires_in: int = None` | `str | None` |
| PHP | `token: string, expiresIn: int 3600 = 3600` | `?str` |
| Ruby | `token, expires_in: 60` | `untyped` |
| Node | `token: string, expiresIn: number = 3600` | `str | None` |

#### `refresh_token_static`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `token: str, expires_in: int = 60` | `str | None` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `res`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `{ error: "Unauthorized" }, 401` | `untyped` |

#### `setup`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `root_dir = Dir.pwd` | `untyped` |
| Node | — not implemented — | — |

#### `use_hmac`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `valid_token`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `token: str` | `dict | None` |
| PHP | `token: string` | `?list` |
| Ruby | `token` | `untyped` |
| Node | `token: string` | `bool | dict` |

#### `valid_token_detail`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `token` | `untyped` |
| Node | — not implemented — | — |

#### `valid_token_static`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `token: str` | `dict | None` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `validate_api_key_static`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `provided: str, expected: str = None` | `bool` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

## Database

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `active_count` | `()` | — | `()` | — | ⚠️ missing: PHP, Node |
| `adapter` | `()` | — | — | — | ⚠️ missing: PHP, Ruby, Node |
| `autocommit` | `value` | — | — | — | ⚠️ missing: PHP, Ruby, Node |
| `cache_clear` | `()` | `()` | `()` | — | ⚠️ missing: Node |
| `cache_get` | — | — | `key` | — | ⚠️ missing: Python, PHP, Node |
| `cache_invalidate` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `cache_key` | — | — | `sql, params` | — | ⚠️ missing: Python, PHP, Node |
| `cache_set` | — | — | `key, value` | — | ⚠️ missing: Python, PHP, Node |
| `cache_stats` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `checkin` | `adapter` | — | `_driver` | — | ⚠️ missing: PHP, Node |
| `checkout` | `()` | — | `()` | — | ⚠️ missing: PHP, Node |
| `close` | `()` | `()` | `()` | `()` | ✅ |
| `close_all` | `()` | — | `()` | — | ⚠️ missing: PHP, Node |
| `columns` | — | — | `table_name` | — | ⚠️ missing: Python, PHP, Node |
| `commit` | `()` | `()` | — | `()` | ⚠️ missing: Ruby |
| `connect` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `create` | — | `url, autoCommit, username, password, pool` | — | `url, username?, password?, pool` | ⚠️ missing: Python, Ruby |
| `create_driver` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `current_driver` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `delete` | `table, filter_sql, params` | `table, filter, whereParams` | `table, filter` | — | ⚠️ missing: Node |
| `detect_driver` | — | — | `conn` | — | ⚠️ missing: Python, PHP, Node |
| `ensure_sequence_table` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `error` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `exec` | — | `sql, params` | — | — | ⚠️ missing: Python, Ruby, Node |
| `execute` | `sql, params` | `sql, params` | `sql, params` | `sql, params?` | ⚠️ return type differs |
| `execute_many` | `sql, params_list` | `sql, paramsList` | `sql, params_list` | `sql, paramSets` | ⚠️ return type differs |
| `fetch` | `sql, params, limit, offset` | `sql, params, limit, offset` | `sql, params, limit, offset` | `sql, params?, limit?, offset?` | ✅ |
| `fetch_one` | `sql, params` | `sql, params` | `sql, params` | — | ⚠️ missing: Node |
| `from_env` | — | `envKey, autoCommit` | — | `envKey, pool` | ⚠️ missing: Python, Ruby |
| `get_active_pool_count` | — | `()` | — | `()` | ⚠️ missing: Python, Ruby |
| `get_adapter` | — | `()` | — | `()` | ⚠️ missing: Python, Ruby |
| `get_columns` | `table` | `tableName` | — | `tableName` | ⚠️ missing: Ruby |
| `get_connection` | — | `envKey` | — | — | ⚠️ missing: Python, Ruby, Node |
| `get_database_type` | `()` | — | — | — | ⚠️ missing: PHP, Ruby, Node |
| `get_error` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `get_last_id` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `get_next_id` | `table, pk_column, generator_name` | `table, pkColumn, generatorName` | `table, pk_column, generator_name` | `table, pkColumn, generatorName?` | ✅ |
| `get_pool_size` | — | `()` | — | `()` | ⚠️ missing: Python, Ruby |
| `get_tables` | `()` | `()` | — | `()` | ⚠️ missing: Ruby |
| `insert` | `table, data` | `table, data` | `table, data` | `table, data, unknown>` | ⚠️ return type differs |
| `is_supported` | — | `scheme` | — | — | ⚠️ missing: Python, Ruby, Node |
| `last_insert_id` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `open` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `pool` | `()` | — | — | — | ⚠️ missing: PHP, Ruby, Node |
| `query` | — | `sql, params` | — | — | ⚠️ missing: Python, Ruby, Node |
| `register_function` | `name, num_params, func, deterministic` | — | — | — | ⚠️ missing: PHP, Ruby, Node |
| `rollback` | `()` | `()` | — | `()` | ⚠️ missing: Ruby |
| `row_value` | — | — | `row, key` | — | ⚠️ missing: Python, PHP, Node |
| `sequence_next` | — | — | `seq_name, table, pk_column` | — | ⚠️ missing: Python, PHP, Node |
| `set_adapter` | — | — | — | `adapter` | ⚠️ missing: Python, PHP, Ruby |
| `size` | `()` | — | `()` | — | ⚠️ missing: PHP, Node |
| `start_transaction` | `()` | `()` | — | `()` | ⚠️ missing: Ruby |
| `supported_schemes` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `table_exists` | `name` | `tableName` | `()` | `name` | ⚠️ param count differs |
| `tables` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `transaction` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `truthy` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `update` | `table, data, filter_sql, params` | `table, data, filterSql, params` | `table, data, filter` | `table, data, unknown>, filter?, unknown>` | ⚠️ return type differs |

### Mismatch Details

#### `active_count`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `int` |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `adapter`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `DatabaseAdapter` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `autocommit`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `value: bool` | `untyped` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `cache_clear`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `None` |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `cache_get`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `key` | `untyped` |
| Node | — not implemented — | — |

#### `cache_invalidate`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `cache_key`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `sql, params` | `untyped` |
| Node | — not implemented — | — |

#### `cache_set`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `key, value` | `untyped` |
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

#### `columns`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `table_name` | `untyped` |
| Node | — not implemented — | — |

#### `commit`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `None` |
| Ruby | — not implemented — | — |
| Node | `` | `None` |

#### `connect`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `create`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `url: string, autoCommit: ?bool null = null, username: string '' = '', password: string '' = '', pool: int 0 = 0` | `Self` |
| Ruby | — not implemented — | — |
| Node | `url: string, username?: string, password?: string, pool: number = 0` | `Promise<Database>` |

#### `create_driver`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `current_driver`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `delete`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `table: str, filter_sql: str | dict | list = '', params: list = None` | `DatabaseResult` |
| PHP | `table: string, filter: string|array '' = '', whereParams: array [] = []` | `bool` |
| Ruby | `table, filter = {}` | `untyped` |
| Node | — not implemented — | — |

#### `detect_driver`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `conn` | `untyped` |
| Node | — not implemented — | — |

#### `ensure_sequence_table`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `error`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `?str` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `exec`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `sql: string, params: array [] = []` | `bool` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `execute`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `sql: str, params: list = None` | `untyped` |
| PHP | `sql: string, params: array [] = []` | `bool|DatabaseResult` |
| Ruby | `sql, params = []` | `untyped` |
| Node | `sql: string, params?: unknown[]` | `bool | unknown` |

#### `execute_many`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `sql: str, params_list: list[list] = None` | `DatabaseResult` |
| PHP | `sql: string, paramsList: array [] = []` | `int` |
| Ruby | `sql, params_list = []` | `untyped` |
| Node | `sql: string, paramSets: unknown[][]` | `list[unknown]` |

#### `fetch_one`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `sql: str, params: list = None` | `dict | None` |
| PHP | `sql: string, params: array [] = []` | `?list` |
| Ruby | `sql, params = []` | `untyped` |
| Node | — not implemented — | — |

#### `from_env`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `envKey: string 'DATABASE_URL' = 'DATABASE_URL', autoCommit: ?bool null = null` | `?Self` |
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
| PHP | `tableName: string` | `list` |
| Ruby | — not implemented — | — |
| Node | `tableName: string` | `untyped` |

#### `get_connection`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `envKey: string 'DATABASE_URL' = 'DATABASE_URL'` | `?Self` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `get_database_type`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `str` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `get_error`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `str | None` |
| PHP | `` | `?str` |
| Ruby | `` | `untyped` |
| Node | `` | `str | None` |

#### `get_last_id`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `int|str` |
| Ruby | `` | `untyped` |
| Node | `` | `str | int` |

#### `get_pool_size`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `int` |
| Ruby | — not implemented — | — |
| Node | `` | `int` |

#### `get_tables`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list[str]` |
| PHP | `` | `list` |
| Ruby | — not implemented — | — |
| Node | `` | `list[str]` |

#### `insert`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `table: str, data: dict | list` | `DatabaseResult` |
| PHP | `table: string, data: array` | `bool` |
| Ruby | `table, data` | `untyped` |
| Node | `table: string, data: Record<string, unknown>` | `DatabaseWriteResult` |

#### `is_supported`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `scheme: string` | `bool` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `last_insert_id`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `int|str` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `open`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `None` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `pool`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `ConnectionPool | None` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `query`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `sql: string, params: array [] = []` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `register_function`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `name: str, num_params: int, func: callable, deterministic: bool = True` | `untyped` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `rollback`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `untyped` |
| PHP | `` | `None` |
| Ruby | — not implemented — | — |
| Node | `` | `None` |

#### `row_value`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `row, key` | `untyped` |
| Node | — not implemented — | — |

#### `sequence_next`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `seq_name, table: nil, pk_column: "id"` | `untyped` |
| Node | — not implemented — | — |

#### `set_adapter`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `adapter` | `untyped` |

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

#### `supported_schemes`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `table_exists`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `name: str` | `bool` |
| PHP | `tableName: string` | `bool` |
| Ruby | `` | `untyped` |
| Node | `name: string` | `bool` |

#### `tables`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `transaction`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `truthy`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

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
| `add` | `method, path, handler, **options` | — | — | — | ⚠️ missing: PHP, Ruby, Node |
| `add_route` | — | — | `method, path, handler, auth_handler, swagger_meta, middleware, template` | `definition` | ⚠️ missing: Python, PHP |
| `all_routes` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `all_ws` | `()` | — | — | — | ⚠️ missing: PHP, Ruby, Node |
| `any` | `path, handler, **options` | `path, callback` | `path, middleware, swagger_meta, template, &block` | `path, handler, middlewares?, meta?` | ⚠️ return type differs |
| `cache` | `max_age` | `()` | `()` | `()` | ⚠️ param count differs |
| `callback` | — | — | — | `group` | ⚠️ missing: Python, PHP, Ruby |
| `cast_param` | — | — | `value, type` | — | ⚠️ missing: Python, PHP, Node |
| `clear` | `()` | `()` | `()` | `()` | ✅ |
| `clear_class_middlewares` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `compile_pattern` | — | — | `path` | — | ⚠️ missing: Python, PHP, Node |
| `count` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `delete` | `path, handler, **options` | `path, callback` | `path, middleware, swagger_meta, template, &block` | — | ⚠️ missing: Node |
| `dispatch` | — | `request, response` | — | — | ⚠️ missing: Python, Ruby, Node |
| `find_route` | — | — | `path, method` | — | ⚠️ missing: Python, PHP, Node |
| `find_ws_route` | — | — | `path` | — | ⚠️ missing: Python, PHP, Node |
| `get` | `path, handler, **options` | `path, callback` | `path, middleware, swagger_meta, template, &block` | `path, handler, middlewares?, meta?` | ⚠️ return type differs |
| `get_class_middlewares` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `get_routes` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `get_web_socket_routes` | — | `()` | — | `()` | ⚠️ missing: Python, Ruby |
| `group` | `prefix, callback, middleware` | `prefix, callback, middleware` | `prefix, auth_handler, middleware, &block` | — | ⚠️ missing: Node |
| `list_routes` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `load_routes` | — | — | `directory` | — | ⚠️ missing: Python, PHP, Node |
| `match` | `method, path` | `method, path` | `()` | `method, pathname` | ⚠️ return type differs |
| `match_path` | — | — | `request_path` | — | ⚠️ missing: Python, PHP, Node |
| `match_web_socket` | — | — | — | `pathname` | ⚠️ missing: Python, PHP, Ruby |
| `match_ws` | `path` | — | — | — | ⚠️ missing: PHP, Ruby, Node |
| `method_index` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `middleware` | — | `middleware` | — | — | ⚠️ missing: Python, Ruby, Node |
| `no_auth` | — | `()` | `()` | `()` | ⚠️ missing: Python |
| `no_cache` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `normalize_path` | — | — | `path` | — | ⚠️ missing: Python, PHP, Node |
| `patch` | `path, handler, **options` | `path, callback` | `path, middleware, swagger_meta, template, &block` | `path, handler, middlewares?, meta?` | ⚠️ return type differs |
| `post` | `path, handler, **options` | `path, callback` | `path, middleware, swagger_meta, template, &block` | `path, handler, middlewares?, meta?` | ⚠️ return type differs |
| `put` | `path, handler, **options` | `path, callback` | `path, middleware, swagger_meta, template, &block` | `path, handler, middlewares?, meta?` | ⚠️ return type differs |
| `routes` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `run_middleware` | — | — | `request, response` | — | ⚠️ missing: Python, PHP, Node |
| `secure` | `()` | `()` | `()` | `()` | ✅ |
| `swagger` | — | `meta` | — | — | ⚠️ missing: Python, Ruby, Node |
| `use` | — | `class` | `klass` | `middlewareClass` | ⚠️ missing: Python |
| `websocket` | `path, handler` | `path, handler` | `path, &block` | `path, handler` | ✅ |
| `ws_routes` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |

### Mismatch Details

#### `add`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `method: str, path: str, handler, **options` | `'RouteRef'` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `add_route`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `method, path, handler, auth_handler: nil, swagger_meta: {}, middleware: [], template: nil` | `untyped` |
| Node | `definition: RouteDefinition` | `RouteRef` |

#### `all_routes`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `list[RouteDefinition]` |

#### `all_ws`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list[dict]` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

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

#### `callback`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `group` | `untyped` |

#### `cast_param`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `value, type` | `untyped` |
| Node | — not implemented — | — |

#### `clear_class_middlewares`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `None` |

#### `compile_pattern`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `path` | `untyped` |
| Node | — not implemented — | — |

#### `count`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `int` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `delete`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str, handler, **options` | `RouteRef` |
| PHP | `path: string, callback: callable` | `Self` |
| Ruby | `path, middleware: [], swagger_meta: {}, template: nil, &block` | `untyped` |
| Node | — not implemented — | — |

#### `dispatch`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `request: Request, response: Response` | `Response` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `find_route`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `path, method` | `untyped` |
| Node | — not implemented — | — |

#### `find_ws_route`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `path` | `untyped` |
| Node | — not implemented — | — |

#### `get`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str, handler, **options` | `RouteRef` |
| PHP | `path: string, callback: callable` | `Self` |
| Ruby | `path, middleware: [], swagger_meta: {}, template: nil, &block` | `untyped` |
| Node | `path: string, handler: RouteHandler, middlewares?: Middleware[], meta?: RouteMeta` | `RouteRef` |

#### `get_class_middlewares`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `list[any]` |

#### `get_routes`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `list[dict]` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `list[RouteDefinition]` |

#### `get_web_socket_routes`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `list` |
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

#### `load_routes`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `directory` | `untyped` |
| Node | — not implemented — | — |

#### `match`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `method: str, path: str` | `tuple[dict | None, dict]` |
| PHP | `method: string, path: string` | `?list` |
| Ruby | `` | `untyped` |
| Node | `method: string, pathname: string` | `MatchResult | None` |

#### `match_path`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `request_path` | `untyped` |
| Node | — not implemented — | — |

#### `match_web_socket`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `pathname: string` | `WebSocketRouteDefinition | None` |

#### `match_ws`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `path: str` | `tuple[dict | None, dict]` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `method_index`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `middleware`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `middleware: array` | `Self` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `no_auth`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `Self` |
| Ruby | `` | `untyped` |
| Node | `` | `Self` |

#### `no_cache`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `Self` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `normalize_path`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `path` | `untyped` |
| Node | — not implemented — | — |

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

#### `routes`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `run_middleware`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `request, response` | `untyped` |
| Node | — not implemented — | — |

#### `swagger`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `meta: array` | `Self` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `use`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `class: string` | `None` |
| Ruby | `klass` | `untyped` |
| Node | `middlewareClass: any` | `None` |

#### `ws_routes`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

## Session

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `all` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `clear` | `()` | `()` | `()` | `()` | ✅ |
| `cookie_header` | `cookie_name` | `cookieName` | `cookie_name` | `cookieName` | ✅ |
| `create_handler` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `delete` | `key` | `key` | `key` | — | ⚠️ missing: Node |
| `destroy` | `session_id` | `()` | `()` | `sessionId` | ⚠️ param count differs |
| `ensure_loaded` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `extract_session_id` | — | — | `env` | — | ⚠️ missing: Python, PHP, Node |
| `flash` | `key, value` | `key, value` | `key, value` | `key, value?` | ⚠️ return type differs |
| `gc` | `max_lifetime` | `()` | `max_age` | `_maxLifetime` | ⚠️ param count differs |
| `get` | `key, default` | `key, default` | `key, default` | `key, defaultValue?` | ⚠️ return type differs |
| `get_flash` | `key, default` | `key, default` | `key, default` | `key, defaultValue?` | ⚠️ return type differs |
| `get_session_id` | — | `()` | — | `()` | ⚠️ missing: Python, Ruby |
| `has` | `key` | `key` | `()` | `key` | ⚠️ param count differs |
| `is_started` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `load_session` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `mkdir_sync` | — | — | — | `this.storagePath, { recursive` | ⚠️ missing: Python, PHP, Ruby |
| `read` | `session_id` | — | — | `sessionId` | ⚠️ missing: PHP, Ruby |
| `regenerate` | `()` | `()` | `()` | `()` | ✅ |
| `save` | `()` | `()` | `()` | `()` | ✅ |
| `session_id` | `()` | — | — | — | ⚠️ missing: PHP, Ruby, Node |
| `set` | `key, value` | `key, value` | `key, value` | `key, value` | ✅ |
| `set_handler` | — | — | — | `handler` | ⚠️ missing: Python, PHP, Ruby |
| `start` | `session_id` | `sessionId` | — | `sessionId?` | ⚠️ missing: Ruby |
| `to_hash` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `unlink_sync` | — | — | — | `fullPath` | ⚠️ missing: Python, PHP, Ruby |
| `write` | `session_id, data, ttl` | — | — | `sessionId, data, ttl` | ⚠️ missing: PHP, Ruby |

### Mismatch Details

#### `all`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `dict` |

#### `create_handler`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `delete`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `key: str` | `untyped` |
| PHP | `key: string` | `None` |
| Ruby | `key` | `untyped` |
| Node | — not implemented — | — |

#### `destroy`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `session_id: str` | `untyped` |
| PHP | `` | `None` |
| Ruby | `` | `untyped` |
| Node | `sessionId: string` | `None` |

#### `ensure_loaded`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `extract_session_id`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `env` | `untyped` |
| Node | — not implemented — | — |

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
| Node | `` | `str | None` |

#### `has`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `key: str` | `bool` |
| PHP | `key: string` | `bool` |
| Ruby | `` | `untyped` |
| Node | `key: string` | `bool` |

#### `is_started`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `bool` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `load_session`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `mkdir_sync`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `this.storagePath, { recursive: true }` | `untyped` |

#### `read`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `session_id: str` | `dict` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `sessionId: string` | `SessionData | None` |

#### `session_id`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `str | None` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `set_handler`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `handler: SessionHandler` | `None` |

#### `start`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `session_id: str = None` | `str` |
| PHP | `sessionId: ?string null = null` | `str` |
| Ruby | — not implemented — | — |
| Node | `sessionId?: string` | `str` |

#### `to_hash`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `unlink_sync`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `fullPath` | `untyped` |

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
| `classify` | — | — | `name` | — | ⚠️ missing: Python, PHP, Node |
| `completed_migrations` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `completed_migrations_with_batch` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `create` | — | — | `name` | — | ⚠️ missing: Python, PHP, Node |
| `create_migration` | `description, migration_folder` | — | — | `description, options?` | ⚠️ missing: PHP, Ruby |
| `down` | — | — | `db` | — | ⚠️ missing: Python, PHP, Node |
| `ensure_migration_table` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `ensure_tracking_table` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `execute_ruby_migration` | — | — | `file, direction` | — | ⚠️ missing: Python, PHP, Node |
| `execute_sql_file` | — | — | `file` | — | ⚠️ missing: Python, PHP, Node |
| `extract_class_name` | — | — | `content` | — | ⚠️ missing: Python, PHP, Node |
| `firebird` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `firebird_column_exists` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `get_applied_migrations` | — | `()` | — | `()` | ⚠️ missing: Python, Ruby |
| `get_last_batch_migrations` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `get_migration_files` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `get_next_batch` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `get_pending_migrations` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `is_migration_applied` | — | — | — | `name` | ⚠️ missing: Python, PHP, Ruby |
| `migrate` | `db, migration_folder, delimiter` | `()` | `()` | `adapter?, options?` | ⚠️ return type differs |
| `migration_sort_key` | — | — | `filename` | — | ⚠️ missing: Python, PHP, Node |
| `next_batch_number` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `pending_migrations` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `record_migration` | — | — | `name, batch, passed` | `name, batch` | ⚠️ missing: Python, PHP |
| `remove_migration_record` | — | — | `name` | `name` | ⚠️ missing: Python, PHP |
| `resolve_migrations_dir` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `rollback` | `db, migration_folder, delimiter` | `()` | `steps` | — | ⚠️ missing: Node |
| `rollback_migration` | — | — | `name` | — | ⚠️ missing: Python, PHP, Node |
| `run_migration` | — | — | `file, batch` | — | ⚠️ missing: Python, PHP, Node |
| `should_skip_for_firebird` | — | — | `stmt` | — | ⚠️ missing: Python, PHP, Node |
| `split_sql_statements` | — | — | `sql, delimiter` | — | ⚠️ missing: Python, PHP, Node |
| `status` | `db, migration_folder` | `()` | `()` | `adapter?, options?` | ⚠️ return type differs |
| `sync_models` | — | — | — | `models` | ⚠️ missing: Python, PHP, Ruby |
| `up` | — | — | `db` | — | ⚠️ missing: Python, PHP, Node |

### Mismatch Details

#### `classify`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `name` | `untyped` |
| Node | — not implemented — | — |

#### `completed_migrations`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `completed_migrations_with_batch`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `create`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `name` | `untyped` |
| Node | — not implemented — | — |

#### `create_migration`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `description: str, migration_folder: str = 'migrations'` | `str` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `description: string, options?: { migrationsDir?: string }` | `Promise<` |

#### `down`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `db` | `untyped` |
| Node | — not implemented — | — |

#### `ensure_migration_table`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `None` |

#### `ensure_tracking_table`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `execute_ruby_migration`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `file, direction` | `untyped` |
| Node | — not implemented — | — |

#### `execute_sql_file`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `file` | `untyped` |
| Node | — not implemented — | — |

#### `extract_class_name`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `content` | `untyped` |
| Node | — not implemented — | — |

#### `firebird`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `firebird_column_exists`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `get_applied_migrations`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `list` |
| Ruby | — not implemented — | — |
| Node | `` | `list<` |

#### `get_last_batch_migrations`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `list<` |

#### `get_migration_files`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `get_next_batch`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `int` |

#### `get_pending_migrations`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `is_migration_applied`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `name: string` | `bool` |

#### `migrate`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `db, migration_folder: str = 'migrations', delimiter: str = ';'` | `list[str]` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `adapter?: DatabaseAdapter, options?: { migrationsDir?: string; delimiter?: string }` | `Promise<MigrationResult>` |

#### `migration_sort_key`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `filename` | `untyped` |
| Node | — not implemented — | — |

#### `next_batch_number`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `pending_migrations`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `record_migration`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `name, batch, passed: 1` | `untyped` |
| Node | `name: string, batch: number` | `None` |

#### `remove_migration_record`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `name` | `untyped` |
| Node | `name: string` | `None` |

#### `resolve_migrations_dir`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `rollback`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `db, migration_folder: str = 'migrations', delimiter: str = ';'` | `list[str]` |
| PHP | `` | `list` |
| Ruby | `steps = 1` | `untyped` |
| Node | — not implemented — | — |

#### `rollback_migration`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `name` | `untyped` |
| Node | — not implemented — | — |

#### `run_migration`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `file, batch` | `untyped` |
| Node | — not implemented — | — |

#### `should_skip_for_firebird`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `stmt` | `untyped` |
| Node | — not implemented — | — |

#### `split_sql_statements`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `sql, delimiter = ";"` | `untyped` |
| Node | — not implemented — | — |

#### `status`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `db, migration_folder: str = 'migrations'` | `dict` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `adapter?: DatabaseAdapter, options?: { migrationsDir?: string }` | `Promise<MigrationStatus>` |

#### `sync_models`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `models: DiscoveredModel[]` | `None` |

#### `up`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `db` | `untyped` |
| Node | — not implemented — | — |

## MCP

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `clear_instances` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `decode_request` | — | `data` | — | — | ⚠️ missing: Python, Ruby, Node |
| `encode_error` | — | `requestId, code, message, data` | — | — | ⚠️ missing: Python, Ruby, Node |
| `encode_notification` | — | `method, params` | — | — | ⚠️ missing: Python, Ruby, Node |
| `encode_response` | — | `requestId, result` | — | — | ⚠️ missing: Python, Ruby, Node |
| `from_callable` | — | `callable` | — | — | ⚠️ missing: Python, Ruby, Node |
| `from_reflection` | — | `ref` | — | — | ⚠️ missing: Python, Ruby, Node |
| `get_instances` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `get_name` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `get_path` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `get_tables` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `handle_message` | `raw_data` | `rawData` | `raw_data` | `rawData, unknown>` | ⚠️ param count differs |
| `is_localhost` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `lookup_invoice` | — | `invoiceNo` | — | — | ⚠️ missing: Python, Ruby, Node |
| `register` | — | `server` | — | — | ⚠️ missing: Python, Ruby, Node |
| `register_from_attributes` | — | `object` | — | — | ⚠️ missing: Python, Ruby, Node |
| `register_resource` | `uri, handler, description, mime_type` | `uri, handler, description, mimeType` | `uri, handler, description, mime_type` | `uri, handler, description, mimeType` | ✅ |
| `register_routes` | `router_module` | `()` | `()` | — | ⚠️ missing: Node |
| `register_tool` | `name, handler, description, schema` | `name, handler, description, schema` | `name, handler, description, schema` | `name, handler, unknown>), description, schema?` | ⚠️ param count differs |
| `resources` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `self._default_mcp_server` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `self.decode_request` | — | — | `data` | — | ⚠️ missing: Python, PHP, Node |
| `self.encode_error` | — | — | `request_id, code, message, data` | — | ⚠️ missing: Python, PHP, Node |
| `self.encode_notification` | — | — | `method, params` | — | ⚠️ missing: Python, PHP, Node |
| `self.encode_response` | — | — | `request_id, result` | — | ⚠️ missing: Python, PHP, Node |
| `self.is_localhost` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `self.mcp_resource` | — | — | `uri, description, mime_type, server, &block` | — | ⚠️ missing: Python, PHP, Node |
| `self.mcp_tool` | — | — | `name, description, server, &block` | — | ⚠️ missing: Python, PHP, Node |
| `self.register` | — | — | `server` | — | ⚠️ missing: Python, PHP, Node |
| `self.schema_from_method` | — | — | `method_obj` | — | ⚠️ missing: Python, PHP, Node |
| `tools` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `write_claude_config` | `port` | `port` | `port` | `port` | ✅ |

### Mismatch Details

#### `clear_instances`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `None` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `decode_request`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `data: string|array` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `encode_error`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `requestId: mixed, code: int, message: string, data: mixed null = null` | `str` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `encode_notification`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `method: string, params: mixed null = null` | `str` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `encode_response`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `requestId: mixed, result: mixed` | `str` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `from_callable`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `callable: callable` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `from_reflection`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `ref: \ReflectionFunctionAbstract` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `get_instances`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `get_name`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `str` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `get_path`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `str` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `get_tables`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `handle_message`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `raw_data: str | dict` | `str` |
| PHP | `rawData: string|array` | `str` |
| Ruby | `raw_data` | `untyped` |
| Node | `rawData: string | Record<string, unknown>` | `str` |

#### `is_localhost`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `bool` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `lookup_invoice`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `invoiceNo: string` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `register`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `server: McpServer` | `None` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `register_from_attributes`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `object: object` | `None` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

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

#### `resources`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `self._default_mcp_server`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `self.decode_request`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `data` | `untyped` |
| Node | — not implemented — | — |

#### `self.encode_error`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `request_id, code, message, data = nil` | `untyped` |
| Node | — not implemented — | — |

#### `self.encode_notification`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `method, params = nil` | `untyped` |
| Node | — not implemented — | — |

#### `self.encode_response`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `request_id, result` | `untyped` |
| Node | — not implemented — | — |

#### `self.is_localhost`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `self.mcp_resource`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `uri, description: "", mime_type: "application/json", server: nil, &block` | `untyped` |
| Node | — not implemented — | — |

#### `self.mcp_tool`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `name, description: "", server: nil, &block` | `untyped` |
| Node | — not implemented — | — |

#### `self.register`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `server` | `untyped` |
| Node | — not implemented — | — |

#### `self.schema_from_method`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `method_obj` | `untyped` |
| Node | — not implemented — | — |

#### `tools`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

## Frond

| Method | Python | PHP | Ruby | Node | Return Match |
|--------|--------|-----|------|------|:------------:|
| `add_filter` | `name, fn` | `name, fn` | `name, &blk` | `name, fn` | ✅ |
| `add_global` | `name, value` | `name, value` | `name, value` | `name, value` | ✅ |
| `add_test` | `name, fn` | `name, fn` | `name, &blk` | `name, fn` | ✅ |
| `apply_math` | — | — | `left, op, right` | — | ⚠️ missing: Python, PHP, Node |
| `clear_cache` | `()` | `()` | `()` | `()` | ✅ |
| `default_filters` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `default_tests` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `dup` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `each` | — | — | `&block` | — | ⚠️ missing: Python, PHP, Node |
| `eval_arithmetic` | — | — | `expr, context` | — | ⚠️ missing: Python, PHP, Node |
| `eval_collection_literal` | — | — | `expr, context` | — | ⚠️ missing: Python, PHP, Node |
| `eval_comparison` | — | — | `expr, context, eval_fn` | — | ⚠️ missing: Python, PHP, Node |
| `eval_concat` | — | — | `expr, context` | — | ⚠️ missing: Python, PHP, Node |
| `eval_expr` | — | — | `expr, context` | — | ⚠️ missing: Python, PHP, Node |
| `eval_filter_arg` | — | — | `arg, context` | — | ⚠️ missing: Python, PHP, Node |
| `eval_function_call` | — | — | `expr, context` | — | ⚠️ missing: Python, PHP, Node |
| `eval_inline_if` | — | — | `expr, context` | — | ⚠️ missing: Python, PHP, Node |
| `eval_literal` | — | — | `expr` | — | ⚠️ missing: Python, PHP, Node |
| `eval_null_coalesce` | — | — | `expr, context` | — | ⚠️ missing: Python, PHP, Node |
| `eval_ternary` | — | — | `expr, context` | — | ⚠️ missing: Python, PHP, Node |
| `eval_test` | — | — | `value_expr, test_name, args_str, context, eval_fn` | — | ⚠️ missing: Python, PHP, Node |
| `eval_var` | — | — | `expr, context` | — | ⚠️ missing: Python, PHP, Node |
| `eval_var_inner` | — | — | `expr, context` | — | ⚠️ missing: Python, PHP, Node |
| `eval_var_raw` | — | — | `expr, context` | — | ⚠️ missing: Python, PHP, Node |
| `execute` | — | — | `source, context` | — | ⚠️ missing: Python, PHP, Node |
| `execute_cached` | — | — | `tokens, context` | — | ⚠️ missing: Python, PHP, Node |
| `execute_with_tokens` | — | — | `source, tokens, context` | — | ⚠️ missing: Python, PHP, Node |
| `extract_blocks` | — | — | `source` | — | ⚠️ missing: Python, PHP, Node |
| `fetch` | — | — | `key, *args, &block` | — | ⚠️ missing: Python, PHP, Node |
| `find_colon` | — | — | `expr` | — | ⚠️ missing: Python, PHP, Node |
| `find_outside_quotes` | — | — | `expr, needle` | — | ⚠️ missing: Python, PHP, Node |
| `find_ternary` | — | — | `expr` | — | ⚠️ missing: Python, PHP, Node |
| `get` | — | — | — | `target, prop` | ⚠️ missing: Python, PHP, Ruby |
| `get_filters` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `get_globals` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `get_own_property_descriptor` | — | — | — | `target, prop` | ⚠️ missing: Python, PHP, Ruby |
| `get_template_dir` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `handle_autoescape` | — | — | `tokens, start, context` | — | ⚠️ missing: Python, PHP, Node |
| `handle_cache` | — | — | `tokens, start, context` | — | ⚠️ missing: Python, PHP, Node |
| `handle_for` | — | — | `tokens, start, context` | — | ⚠️ missing: Python, PHP, Node |
| `handle_from_import` | — | — | `content, context` | — | ⚠️ missing: Python, PHP, Node |
| `handle_if` | — | — | `tokens, start, context` | — | ⚠️ missing: Python, PHP, Node |
| `handle_include` | — | — | `content, context` | — | ⚠️ missing: Python, PHP, Node |
| `handle_macro` | — | — | `tokens, start, context` | — | ⚠️ missing: Python, PHP, Node |
| `handle_set` | — | — | `content, context` | — | ⚠️ missing: Python, PHP, Node |
| `handle_spaceless` | — | — | `tokens, start, context` | — | ⚠️ missing: Python, PHP, Node |
| `has` | — | — | — | `target, prop` | ⚠️ missing: Python, PHP, Ruby |
| `has_comparison` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `is_a` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `key` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `keys` | — | — | `@parent.is_a?(LoopContext` | — | ⚠️ missing: Python, PHP, Node |
| `load_template` | — | — | `name` | — | ⚠️ missing: Python, PHP, Node |
| `matched_parens` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `merge` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `own_keys` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `parse_args` | — | — | `raw` | — | ⚠️ missing: Python, PHP, Node |
| `parse_filter_chain` | — | — | `expr` | — | ⚠️ missing: Python, PHP, Node |
| `register_builtin_globals` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `render` | `template, data` | `template, data` | `template, data` | `template, data?, unknown>` | ⚠️ param count differs |
| `render_string` | `source, data` | `source, data, templateName` | `source, data` | `source, data?, unknown>` | ⚠️ param count differs |
| `render_tokens` | — | — | `tokens, context` | — | ⚠️ missing: Python, PHP, Node |
| `render_with_blocks` | — | — | `parent_source, context, child_blocks` | — | ⚠️ missing: Python, PHP, Node |
| `resolve` | — | — | `expr, context` | — | ⚠️ missing: Python, PHP, Node |
| `respond_to_missing` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `sandbox` | `allowed_filters, allowed_tags, allowed_vars` | `filters, tags, vars` | `filters, tags, vars` | `filters?, tags?, vars?` | ⚠️ return type differs |
| `self.escape_html` | — | — | `str` | — | ⚠️ missing: Python, PHP, Node |
| `self.generate_form_jwt` | — | — | `descriptor` | — | ⚠️ missing: Python, PHP, Node |
| `self.generate_form_token` | — | — | `descriptor` | — | ⚠️ missing: Python, PHP, Node |
| `self.generate_form_token_value` | — | — | `descriptor` | — | ⚠️ missing: Python, PHP, Node |
| `set` | — | — | — | `target, prop, value` | ⚠️ missing: Python, PHP, Ruby |
| `split_args_toplevel` | — | — | `str` | — | ⚠️ missing: Python, PHP, Node |
| `split_on_pipe` | — | — | `expr` | — | ⚠️ missing: Python, PHP, Node |
| `stringify_keys` | — | — | `hash` | — | ⚠️ missing: Python, PHP, Node |
| `strip_tag` | — | — | `raw` | — | ⚠️ missing: Python, PHP, Node |
| `to_h` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `to_string` | — | — | — | `()` | ⚠️ missing: Python, PHP, Ruby |
| `tokenize` | — | — | `source` | — | ⚠️ missing: Python, PHP, Node |
| `truthy` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `unsandbox` | `()` | `()` | `()` | `()` | ⚠️ return type differs |

### Mismatch Details

#### `apply_math`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `left, op, right` | `untyped` |
| Node | — not implemented — | — |

#### `default_filters`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `default_tests`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `dup`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `each`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `&block` | `untyped` |
| Node | — not implemented — | — |

#### `eval_arithmetic`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr, context` | `untyped` |
| Node | — not implemented — | — |

#### `eval_collection_literal`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr, context` | `untyped` |
| Node | — not implemented — | — |

#### `eval_comparison`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr, context, eval_fn = nil` | `untyped` |
| Node | — not implemented — | — |

#### `eval_concat`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr, context` | `untyped` |
| Node | — not implemented — | — |

#### `eval_expr`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr, context` | `untyped` |
| Node | — not implemented — | — |

#### `eval_filter_arg`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `arg, context` | `untyped` |
| Node | — not implemented — | — |

#### `eval_function_call`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr, context` | `untyped` |
| Node | — not implemented — | — |

#### `eval_inline_if`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr, context` | `untyped` |
| Node | — not implemented — | — |

#### `eval_literal`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr` | `untyped` |
| Node | — not implemented — | — |

#### `eval_null_coalesce`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr, context` | `untyped` |
| Node | — not implemented — | — |

#### `eval_ternary`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr, context` | `untyped` |
| Node | — not implemented — | — |

#### `eval_test`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `value_expr, test_name, args_str, context, eval_fn = nil` | `untyped` |
| Node | — not implemented — | — |

#### `eval_var`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr, context` | `untyped` |
| Node | — not implemented — | — |

#### `eval_var_inner`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr, context` | `untyped` |
| Node | — not implemented — | — |

#### `eval_var_raw`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr, context` | `untyped` |
| Node | — not implemented — | — |

#### `execute`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `source, context` | `untyped` |
| Node | — not implemented — | — |

#### `execute_cached`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `tokens, context` | `untyped` |
| Node | — not implemented — | — |

#### `execute_with_tokens`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `source, tokens, context` | `untyped` |
| Node | — not implemented — | — |

#### `extract_blocks`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `source` | `untyped` |
| Node | — not implemented — | — |

#### `fetch`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `key, *args, &block` | `untyped` |
| Node | — not implemented — | — |

#### `find_colon`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr` | `untyped` |
| Node | — not implemented — | — |

#### `find_outside_quotes`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr, needle` | `untyped` |
| Node | — not implemented — | — |

#### `find_ternary`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr` | `untyped` |
| Node | — not implemented — | — |

#### `get`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `target, prop: string` | `untyped` |

#### `get_filters`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `get_globals`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `get_own_property_descriptor`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `target, prop: string` | `untyped` |

#### `get_template_dir`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `str` |

#### `handle_autoescape`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `tokens, start, context` | `untyped` |
| Node | — not implemented — | — |

#### `handle_cache`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `tokens, start, context` | `untyped` |
| Node | — not implemented — | — |

#### `handle_for`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `tokens, start, context` | `untyped` |
| Node | — not implemented — | — |

#### `handle_from_import`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `content, context` | `untyped` |
| Node | — not implemented — | — |

#### `handle_if`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `tokens, start, context` | `untyped` |
| Node | — not implemented — | — |

#### `handle_include`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `content, context` | `untyped` |
| Node | — not implemented — | — |

#### `handle_macro`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `tokens, start, context` | `untyped` |
| Node | — not implemented — | — |

#### `handle_set`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `content, context` | `untyped` |
| Node | — not implemented — | — |

#### `handle_spaceless`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `tokens, start, context` | `untyped` |
| Node | — not implemented — | — |

#### `has`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `target, prop: string` | `untyped` |

#### `has_comparison`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `is_a`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `key`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `keys`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `@parent.is_a?(LoopContext` | `untyped` |
| Node | — not implemented — | — |

#### `load_template`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `name` | `untyped` |
| Node | — not implemented — | — |

#### `matched_parens`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `merge`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `own_keys`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `untyped` |

#### `parse_args`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `raw` | `untyped` |
| Node | — not implemented — | — |

#### `parse_filter_chain`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr` | `untyped` |
| Node | — not implemented — | — |

#### `register_builtin_globals`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

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

#### `render_tokens`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `tokens, context` | `untyped` |
| Node | — not implemented — | — |

#### `render_with_blocks`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `parent_source, context, child_blocks` | `untyped` |
| Node | — not implemented — | — |

#### `resolve`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr, context` | `untyped` |
| Node | — not implemented — | — |

#### `respond_to_missing`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `sandbox`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `allowed_filters: list[str] = None, allowed_tags: list[str] = None, allowed_vars: list[str] = None` | `untyped` |
| PHP | `filters: ?array null = null, tags: ?array null = null, vars: ?array null = null` | `Self` |
| Ruby | `filters: nil, tags: nil, vars: nil` | `untyped` |
| Node | `filters?: string[], tags?: string[], vars?: string[]` | `Frond` |

#### `self.escape_html`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `str` | `untyped` |
| Node | — not implemented — | — |

#### `self.generate_form_jwt`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `descriptor = ""` | `untyped` |
| Node | — not implemented — | — |

#### `self.generate_form_token`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `descriptor = ""` | `untyped` |
| Node | — not implemented — | — |

#### `self.generate_form_token_value`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `descriptor = ""` | `untyped` |
| Node | — not implemented — | — |

#### `set`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `target, prop: string, value` | `untyped` |

#### `split_args_toplevel`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `str` | `untyped` |
| Node | — not implemented — | — |

#### `split_on_pipe`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `expr` | `untyped` |
| Node | — not implemented — | — |

#### `stringify_keys`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `hash` | `untyped` |
| Node | — not implemented — | — |

#### `strip_tag`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `raw` | `untyped` |
| Node | — not implemented — | — |

#### `to_h`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `to_string`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `` | `untyped` |

#### `tokenize`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `source` | `untyped` |
| Node | — not implemented — | — |

#### `truthy`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

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
| `coerce_value` | — | — | `val` | — | ⚠️ missing: Python, PHP, Node |
| `current` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `execute` | `query, variables, context` | `query, variables` | `document, variables, context, operation_name` | `query, variables?, unknown>` | ⚠️ return type differs |
| `execute_json` | `query, variables, context` | — | — | — | ⚠️ missing: PHP, Ruby, Node |
| `expect` | `type, value` | — | `type, value` | `type, value?` | ⚠️ missing: PHP |
| `from_orm` | `orm_class` | `ormInstance` | `klass` | `modelClass, { type, adapter?, unknown>>(sql, params?, params?` | ⚠️ return type differs |
| `get_mutations` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `get_queries` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `get_type` | — | — | `name` | — | ⚠️ missing: Python, PHP, Node |
| `get_types` | — | `()` | — | — | ⚠️ missing: Python, Ruby, Node |
| `graphiql_html` | — | — | `endpoint` | — | ⚠️ missing: Python, PHP, Node |
| `handle_request` | — | — | `body, context` | — | ⚠️ missing: Python, PHP, Node |
| `introspect` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `item_fields` | — | — | `hash` | — | ⚠️ missing: Python, PHP, Node |
| `list` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `match` | `type, value` | — | `type, value` | `type, value?` | ⚠️ missing: PHP |
| `non_null` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `of_type` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `parse` | `()` | `()` | `()` | `()` | ⚠️ return type differs |
| `parse_arguments` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `parse_definition` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `parse_field` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `parse_fragment` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `parse_fragment_spread` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `parse_list_value` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `parse_object_value` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `parse_operation` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `parse_selection_set` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `parse_type_ref` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `parse_value` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `parse_variable_definitions` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `peek` | `()` | — | `offset` | `()` | ⚠️ missing: PHP |
| `read_number` | — | — | `src, i` | — | ⚠️ missing: Python, PHP, Node |
| `read_string` | — | — | `src, i` | — | ⚠️ missing: Python, PHP, Node |
| `register_route` | — | — | `path` | — | ⚠️ missing: Python, PHP, Node |
| `register_scalars` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `resolve_args` | — | — | `args, variables` | — | ⚠️ missing: Python, PHP, Node |
| `resolve_field` | — | — | `selection, fields, parent, variables, context, fragments, data, errors` | — | ⚠️ missing: Python, PHP, Node |
| `resolve_selection` | — | — | `selection, fields, parent, variables, context, fragments, data, errors` | — | ⚠️ missing: Python, PHP, Node |
| `resolve_value` | — | — | `val, variables` | — | ⚠️ missing: Python, PHP, Node |
| `resolve_variables` | — | — | `var_defs, provided` | — | ⚠️ missing: Python, PHP, Node |
| `ruby_field_to_gql` | — | — | `field_type` | — | ⚠️ missing: Python, PHP, Node |
| `scalar` | — | — | `()` | — | ⚠️ missing: Python, PHP, Node |
| `schema_sdl` | `()` | `()` | `()` | `()` | ✅ |
| `self.parse` | — | — | `type_str` | — | ⚠️ missing: Python, PHP, Node |
| `skip` | — | — | `type, value` | — | ⚠️ missing: Python, PHP, Node |
| `super` | — | — | — | `message` | ⚠️ missing: Python, PHP, Ruby |
| `tokenize` | — | — | `src` | — | ⚠️ missing: Python, PHP, Node |

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

#### `coerce_value`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `val` | `untyped` |
| Node | — not implemented — | — |

#### `current`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `execute`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `query: str, variables: dict = None, context: dict = None` | `dict` |
| PHP | `query: string, variables: ?array null = null` | `list` |
| Ruby | `document, variables: {}, context: {}, operation_name: nil` | `untyped` |
| Node | `query: string, variables?: Record<string, unknown>` | `GraphQLResult` |

#### `execute_json`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `query: str, variables: dict = None, context: dict = None` | `str` |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

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

#### `get_mutations`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `get_queries`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `get_type`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `name` | `untyped` |
| Node | — not implemented — | — |

#### `get_types`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | `` | `list` |
| Ruby | — not implemented — | — |
| Node | — not implemented — | — |

#### `graphiql_html`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `endpoint` | `untyped` |
| Node | — not implemented — | — |

#### `handle_request`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `body, context: {}` | `untyped` |
| Node | — not implemented — | — |

#### `introspect`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `dict` |

#### `item_fields`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `hash` | `untyped` |
| Node | — not implemented — | — |

#### `list`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `match`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `type: str, value: str = None` | `Token | None` |
| PHP | — not implemented — | — |
| Ruby | `type, value = nil` | `untyped` |
| Node | `type: string, value?: string` | `Token | None` |

#### `non_null`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `of_type`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `parse`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `dict` |
| PHP | `` | `list` |
| Ruby | `` | `untyped` |
| Node | `` | `untyped` |

#### `parse_arguments`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `parse_definition`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `parse_field`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `parse_fragment`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `parse_fragment_spread`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `parse_list_value`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `parse_object_value`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `parse_operation`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `parse_selection_set`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `parse_type_ref`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `parse_value`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `parse_variable_definitions`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `peek`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | `` | `Token | None` |
| PHP | — not implemented — | — |
| Ruby | `offset = 0` | `untyped` |
| Node | `` | `Token | None` |

#### `read_number`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `src, i` | `untyped` |
| Node | — not implemented — | — |

#### `read_string`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `src, i` | `untyped` |
| Node | — not implemented — | — |

#### `register_route`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `path = "/graphql"` | `untyped` |
| Node | — not implemented — | — |

#### `register_scalars`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `resolve_args`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `args, variables` | `untyped` |
| Node | — not implemented — | — |

#### `resolve_field`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `selection, fields, parent, variables, context, fragments, data, errors` | `untyped` |
| Node | — not implemented — | — |

#### `resolve_selection`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `selection, fields, parent, variables, context, fragments, data, errors` | `untyped` |
| Node | — not implemented — | — |

#### `resolve_value`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `val, variables` | `untyped` |
| Node | — not implemented — | — |

#### `resolve_variables`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `var_defs, provided` | `untyped` |
| Node | — not implemented — | — |

#### `ruby_field_to_gql`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `field_type` | `untyped` |
| Node | — not implemented — | — |

#### `scalar`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `` | `untyped` |
| Node | — not implemented — | — |

#### `self.parse`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `type_str` | `untyped` |
| Node | — not implemented — | — |

#### `skip`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `type, value = nil` | `untyped` |
| Node | — not implemented — | — |

#### `super`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | — not implemented — | — |
| Node | `message` | `untyped` |

#### `tokenize`

| Framework | Signature | Return Type |
|-----------|-----------|-------------|
| Python | — not implemented — | — |
| PHP | — not implemented — | — |
| Ruby | `src` | `untyped` |
| Node | — not implemented — | — |
