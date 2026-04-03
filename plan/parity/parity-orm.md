# Tina4 v3 — Developer-Facing API Parity Audit

> **Generated:** 2026-04-03 | **Version:** v3.10.67
> **Scope:** Every developer-facing method, compared across Python, PHP, Ruby, Node.js
> **Format:** Method name | signature per framework | return type | parity issues | documented?

---

## 1. ORM (Model)

### 1.1 Instance Methods — CRUD

#### `save()`
| Framework | Return | Notes |
|-----------|--------|-------|
| Python | `self` | Returns self for chaining |
| PHP | `bool` | true on success |
| Ruby | `bool` | true on success |
| Node.js | `void` | Throws on error |

- **PARITY ISSUE:** Python returns `self`, PHP/Ruby return `bool`, Node returns `void`
- **FIX:** Align on `bool` (Python should return bool, Node should return bool)
- **Documented?** CLAUDE.md: Python says `self` (correct). PHP says `bool` (correct). Ruby says `Boolean` (correct). Node not shown.

#### `delete()`
| Framework | Return |
|-----------|--------|
| Python | `None` |
| PHP | `bool` |
| Ruby | `bool` |
| Node.js | `void` |

- **PARITY ISSUE:** Python/Node return void, PHP/Ruby return bool
- **Documented?** All 4 CLAUDE.md: yes, but return types differ

#### `force_delete()` / `forceDelete()`
| Framework | Return |
|-----------|--------|
| Python | `None` |
| PHP | `bool` |
| Ruby | `bool` |
| Node.js | `void` |

- **PARITY ISSUE:** Same as delete() — void vs bool
- **Documented?** All 4 CLAUDE.md: yes

#### `restore()`
| Framework | Return |
|-----------|--------|
| Python | `None` |
| PHP | `bool` |
| Ruby | `bool` |
| Node.js | `void` |

- **PARITY ISSUE:** Same pattern
- **Documented?** All 4 CLAUDE.md: yes

#### `load(sql, params, include)`
| Framework | Signature | Return |
|-----------|-----------|--------|
| Python | `load(sql: str, params=None, include=None)` | `bool` |
| PHP | `load(string $sql, array $params=[], ?array $include=null)` | `bool` |
| Ruby | `load(sql, params=[], include: nil)` | `bool` |
| Node.js | `load(sql: string, params?: unknown[], include?: string[])` | `boolean` |

- **PARITY: OK** -- all match
- **Documented?** All 4 CLAUDE.md: yes, just fixed this session

#### `validate()`
| Framework | Return |
|-----------|--------|
| Python | `list[str]` |
| PHP | `array` |
| Ruby | `Array` |
| Node.js | `string[]` |

- **PARITY: OK** -- all return list of error strings, empty = valid
- **Documented?** All 4 CLAUDE.md: yes

### 1.2 Instance Methods — Serialization

#### `to_dict()` / `toDict()` / `to_h()`
| Framework | Primary Name | `include` param? |
|-----------|-------------|-----------------|
| Python | `to_dict(include=None)` | YES |
| PHP | `toArray($include=null)` | YES |
| Ruby | `to_h(include: nil)` | YES |
| Node.js | `toDict(include?)` | YES |

- **PARITY ISSUE:** PHP primary name is `toArray()`, not `toDict()`. `toDict` is an alias in PHP.
- **Aliases exist:** Python: `to_object`. PHP: `toDict`, `toObject`. Ruby: `to_hash`, `to_dict`, `to_object`. Node: `toObject`.
- **Documented?** All CLAUDE.md: yes. Book chapters: partially.

#### `to_json()` / `toJson()`
| Framework | `include` param? |
|-----------|-----------------|
| Python | YES |
| PHP | NO |
| Ruby | YES |
| Node.js | NO |

- **PARITY ISSUE:** PHP and Node.js don't support `include` on toJson
- **Documented?** All CLAUDE.md: yes

#### `to_array()` / `toArray()` and `to_list()` / `toList()`
- **PARITY: OK** -- all return list of values, to_list is alias for to_array
- **PARITY ISSUE:** PHP's `toArray()` returns a dict (it's the primary dict method), while Python/Ruby/Node's `toArray()` returns a flat list of values. **Different semantics for the same name.**
- **Documented?** All CLAUDE.md: yes

### 1.3 Instance Methods — Relationships (Imperative)

#### `has_one()` / `hasOne()` / `query_has_one()`
| Framework | Name | Params |
|-----------|------|--------|
| Python | `has_one(related_class, foreign_key=None)` | class + optional FK |
| PHP | `hasOne(string $relatedClass, ?string $foreignKey=null)` | class name string + optional FK |
| Ruby | `query_has_one(related_class, foreign_key: nil)` | class + keyword FK |
| Node.js | `hasOne<R>(relatedClass, foreignKey: string)` | class + required FK |

- **PARITY ISSUE:** Ruby uses `query_has_one` (different name). Node.js FK is required (others optional).
- **Documented?** All CLAUDE.md: yes. Book Ch7 (ORM relationships): yes.

#### `has_many()` / `hasMany()` / `query_has_many()`
| Framework | Name | limit/offset? |
|-----------|------|--------------|
| Python | `has_many(related_class, fk=None, limit=100, offset=0)` | YES |
| PHP | `hasMany($relatedClass, $fk=null, $limit=100, $offset=0)` | YES |
| Ruby | `query_has_many(related_class, fk: nil, limit: 100, offset: 0)` | YES |
| Node.js | `hasMany<R>(relatedClass, foreignKey: string)` | NO |

- **PARITY ISSUE:** Node.js instance `hasMany()` missing limit/offset params
- **Documented?** All CLAUDE.md: yes

#### `belongs_to()` / `belongsTo()` / `query_belongs_to()`
- **PARITY: OK** (Ruby naming aside)
- **Documented?** All CLAUDE.md: yes

### 1.4 Class/Static Methods — Finders

#### `find(pk_value, include?)` / `findById()`
| Framework | Type | Params | Return |
|-----------|------|--------|--------|
| Python | classmethod | `(pk_value, include=None)` | `ORM \| None` |
| PHP | **instance** | `findById(int\|string $id)` | `self` |
| Ruby | classmethod | `find(id_or_filter, filter=nil, **kwargs)` | `ORM \| nil` |
| Node.js | static | `findById(id, include?)` | `T \| null` |

- **MAJOR PARITY ISSUE:** PHP `findById()` is an INSTANCE method, not a class/static method. All others are class methods.
- **PARITY ISSUE:** PHP returns `self` (populates current instance); others return a new instance or nil.
- **PARITY ISSUE:** Ruby `find()` is overloaded (accepts ID, hash filter, or kwargs) -- others only accept PK.
- **Documented?** CLAUDE.md: yes but PHP shows it as instance method (matches code but breaks parity).

#### `find_or_fail()` / `findOrFail()`
| Framework | Type | Return on miss |
|-----------|------|---------------|
| Python | classmethod | raises `ValueError` |
| PHP | **instance** | throws exception |
| Ruby | classmethod | raises error |
| Node.js | static | throws `Error` |

- **PARITY ISSUE:** PHP is instance method (same issue as findById)
- **Documented?** All CLAUDE.md: yes

#### `create(data)`
- **PARITY: OK** -- all are class/static methods, accept dict/hash, return saved instance
- **Documented?** All CLAUDE.md: yes

### 1.5 Class/Static Methods — Queries

#### `all()`
| Framework | Type | Params | Return |
|-----------|------|--------|--------|
| Python | classmethod | `(limit=100, offset=0, include=None)` | `(list, int)` tuple |
| PHP | **instance** | `($limit=100, $offset=0)` | `array` (dict with data/total/limit/offset) |
| Ruby | classmethod | `(limit: nil, offset: nil, order_by: nil, include: nil)` | `Array` |
| Node.js | static | `findAll(where?, params?, include?)` | `T[]` |

- **MAJOR PARITY ISSUES:**
  1. PHP is instance method
  2. Python returns tuple `(instances, count)`, PHP returns dict, Ruby/Node return array only
  3. Node.js method is called `findAll` not `all`, and uses where/params instead of limit/offset
  4. Ruby has `order_by` param, others don't
- **Documented?** CLAUDE.md: yes but inconsistently

#### `select(sql, params)`
| Framework | Type | Return |
|-----------|------|--------|
| Python | classmethod | `(list, int)` tuple |
| PHP | **instance** | `array` |
| Ruby | classmethod | `Array` |
| Node.js | static | `T[]` |

- **PARITY ISSUE:** PHP is instance method. Python returns tuple, others return array.
- **Documented?** All CLAUDE.md: yes

#### `select_one()` / `selectOne()`
| Framework | Type | Params | Return |
|-----------|------|--------|--------|
| Python | classmethod | `(sql, params=None, include=None)` | `ORM \| None` |
| PHP | **instance** | `($sql, $params=[], $include=null)` | `?static` |
| Ruby | classmethod | `(sql, params=[], include: nil)` | `ORM \| nil` |
| Node.js | static | `(sql, params?, include?)` | `T \| null` |

- **PARITY ISSUE:** PHP is instance method; all others are class/static
- **PARITY: OK** on params and return type
- **Documented?** All CLAUDE.md: yes

#### `where(filter, params)`
| Framework | Type | Params | Return |
|-----------|------|--------|--------|
| Python | classmethod | `(filter_sql, params=None, limit=20, offset=0, include=None)` | `(list, int)` |
| PHP | **instance** | `($filterSql, $params=[], $limit=20, $offset=0)` | `array` |
| Ruby | classmethod | `(conditions, params=[], include: nil)` | `Array` |
| Node.js | N/A | uses `findAll(where, params, include)` instead | `T[]` |

- **PARITY ISSUES:**
  1. PHP is instance method
  2. Node.js doesn't have a separate `where()` — uses `findAll` with where param
  3. Ruby missing limit/offset
  4. Python returns tuple, others return array
- **Documented?** Python/PHP/Ruby CLAUDE.md: yes. Node.js: no separate `where()` documented.

#### `count(conditions, params)`
| Framework | Type | Params |
|-----------|------|--------|
| Python | classmethod | `(conditions=None, params=None)` |
| PHP | **instance** | `()` -- NO PARAMS |
| Ruby | classmethod | `(conditions=nil, params=[])` |
| Node.js | static | `(conditions?, params?)` |

- **MAJOR PARITY ISSUE:** PHP `count()` is instance method with ZERO parameters. Others accept conditions/params.
- **Documented?** All CLAUDE.md: yes but PHP signature is wrong vs others

#### `with_trashed()` / `withTrashed()`
| Framework | Type | offset param name |
|-----------|------|------------------|
| Python | classmethod | `offset` |
| PHP | **instance** | `$offset` |
| Ruby | classmethod | `offset` |
| Node.js | static | `skip` |

- **PARITY ISSUE:** PHP instance method. Node.js uses `skip` not `offset`.
- **Documented?** All CLAUDE.md: yes

#### `create_table()` / `createTable()`
| Framework | Type | Params | Return |
|-----------|------|--------|--------|
| Python | classmethod | `()` | `bool` |
| PHP | **instance** | `($columns=[])` | `bool` |
| Ruby | classmethod | `()` | `bool` |
| Node.js | static | `()` | `void` |

- **PARITY ISSUE:** PHP is instance method with optional `$columns` array (unique). Node returns void.
- **Documented?** All CLAUDE.md: yes

#### `scope(name, filter, params)`
| Framework | Type | Behavior |
|-----------|------|----------|
| Python | classmethod | Registers a reusable method on the class |
| PHP | **instance** | Returns filtered results directly |
| Ruby | classmethod | Registers a method via define_singleton_method |
| Node.js | static | Returns filtered results directly |

- **MAJOR PARITY ISSUE:** Fundamentally different semantics. Python/Ruby register a named scope (decorator pattern). PHP/Node execute the query immediately and return results.
- **Documented?** All CLAUDE.md: mentioned but semantics differ

#### `query()` -> QueryBuilder
- **PARITY: OK** -- all return a QueryBuilder instance
- **Documented?** All CLAUDE.md: yes

---

## PARITY ISSUES SUMMARY — ORM

### Critical (behavior differences)

| # | Issue | Frameworks Affected | Status |
|---|-------|-------------------|--------|
| 1 | ~~PHP query methods are instance methods~~ | PHP | **BY DESIGN** — `User().where()` is same pattern in Python. Instance carries DB context. |
| 2 | **`all()` return types differ** — Python: `(list, int)` tuple, PHP: dict, Ruby/Node: array | All | TODO |
| 3 | **`select()` return types differ** — Python returns tuple, others return array | Python vs PHP/Ruby/Node | TODO |
| 4 | **`scope()` semantics differ** — Python/Ruby register a method, PHP/Node return results | All | TODO |
| 5 | **PHP `count()` has no params** — others accept conditions/params | PHP | TODO |
| 6 | **Node.js has no `where()` method** — uses findAll with where param | Node.js | TODO |
| 7 | **`save()` return type differs** — Python: self, PHP/Ruby: bool, Node: void | All | TODO |

### Moderate (naming/param differences) — ALL FIXED 2026-04-03

| # | Issue | Status |
|---|-------|--------|
| 8 | ~~Node.js `withTrashed` uses `skip` not `offset`~~ | FIXED — renamed to `offset` |
| 9 | ~~PHP `toArray()` is dict~~ | FIXED — `toDict()` is primary, `toArray()` returns values, `toAssoc()` added as alias everywhere |
| 10 | ~~`toJson()` include param missing in PHP/Node~~ | FIXED — added `include` param |
| 11 | ~~Ruby relationship methods named `query_*`~~ | FIXED — `imperative_has_one/many/belongs_to` aliases added |
| 12 | ~~Node.js `hasMany()` missing limit/offset~~ | FIXED — added `limit=100, offset=0` params |

### Documentation gaps

| # | Gap |
|---|-----|
| 1 | Book chapters don't cover `load()` new API (just fixed, book says raw SQL) |
| 2 | `scope()` semantics not explained (register vs execute) |
| 3 | Return type differences between frameworks not documented anywhere |

---

## NEXT CLASSES TO AUDIT

- [ ] 2. Router (route registration, params, middleware, groups)
- [ ] 3. Database (connect, fetch, execute, transactions)
- [ ] 4. Auth (JWT, tokens, password hashing)
- [ ] 5. Session (file, Redis, Valkey, MongoDB, database)
- [ ] 6. Template/Frond (render, globals, filters)
- [ ] 7. Request/Response (params, files, headers, cookies)
- [ ] 8. Queue (push, consume, schedule)
- [ ] 9. WebSocket (server, client, rooms)
- [ ] 10. GraphQL (schema, resolvers)
- [ ] 11. WSDL/SOAP
- [ ] 12. Localization/i18n
- [ ] 13. Events (on, emit, once, off)
- [ ] 14. Api Client (get, post, put, delete)
- [ ] 15. Swagger/OpenAPI
- [ ] 16. SCSS compiler
- [ ] 17. HTMLElement builder
- [ ] 18. DI Container
- [ ] 19. Service Runner
- [ ] 20. Seeder/FakeData
