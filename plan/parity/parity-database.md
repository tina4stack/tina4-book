# Parity Audit: Database

> **Generated:** 2026-04-03 | **Version:** v3.10.67

## Status: HIGH PARITY (95%)

Connection strings, query methods, transactions, pooling, ID generation, and schema introspection are consistent. Minor return type differences are intentional per-language conventions.

---

## Constructor / Factory

| Framework | Signature | Notes |
|-----------|-----------|-------|
| Python | `Database(url, username=None, password=None, pool=0)` | Reads DATABASE_URL env if not given |
| PHP | `Database::create()` or `Database(url, autoCommit, username, password, pool)` | Static factory preferred |
| Ruby | `Database.new(connection_string, username=nil, password=nil, driver_name=nil, pool=0)` | Auto-detects driver |
| Node.js | `await Database.create(url, username?, password?, pool?)` | Async factory required |

- [ ] **PARITY: OK** — all accept URL + credentials + pool size
- [ ] **Documented?** All CLAUDE.md: yes

## Connection URL Format

- [ ] **PARITY: OK** — identical format across all 4:

```
sqlite:///path/to/db.sqlite
postgres://user:pass@host:5432/db
mysql://user:pass@host:3306/db
mssql://user:pass@host:1433/db
firebird://user:pass@host:3050/path/to/db.fdb
mongodb://user:pass@host:27017/db
odbc:///DSN=MyDSN
```

## Query Methods

### `fetch(sql, params, limit, offset)`

| Framework | Signature | Return |
|-----------|-----------|--------|
| Python | `fetch(sql, params=None, limit=100, offset=0)` | `DatabaseResult` |
| PHP | `fetch(sql, params=[], limit=100, offset=0)` | `DatabaseResult` |
| Ruby | `fetch(sql, params=[], limit: 100, offset: nil)` | `DatabaseResult` |
| Node.js | `fetch(sql, params?, limit?, offset?)` | `DatabaseResult` |

- [ ] **PARITY: OK** — param order and defaults consistent
- [ ] **Documented?** All CLAUDE.md: yes

### `fetch_one()` / `fetchOne()`

| Framework | Signature | Return |
|-----------|-----------|--------|
| Python | `fetch_one(sql, params=None)` | `dict \| None` |
| PHP | `fetchOne(sql, params=[])` | `array \| null` |
| Ruby | `fetch_one(sql, params=[])` | `Hash \| nil` |
| Node.js | `fetchOne(sql, params?)` | `Record \| null` |

- [ ] **PARITY: OK**
- [ ] **Documented?** All CLAUDE.md: yes

### `execute(sql, params)`

| Framework | Signature | Return |
|-----------|-----------|--------|
| Python | `execute(sql, params=None)` | `DatabaseResult` |
| PHP | `execute(sql, params=[])` | `bool` |
| Ruby | `execute(sql, params=[])` | `hash` |
| Node.js | `execute(sql, params?)` | `unknown` |

- [ ] **PARITY ISSUE:** Return types differ — Python returns `DatabaseResult`, PHP returns `bool`, Ruby returns hash, Node returns unknown
- [ ] **Documented?** All CLAUDE.md: yes but return types differ

## DatabaseResult Format

| Field | Python | PHP | Ruby | Node.js |
|-------|--------|-----|------|---------|
| `records` | `list[dict]` | `array` | `Array[Hash]` | `T[]` |
| `count` | `int` | `int` | `int` | `number` |
| `limit` | N/A | `int` | `int` | `number` |
| `offset` | N/A | `int` | `int` | `number` |
| `columns` | N/A | `array` | N/A | `string[]` |
| `affected_rows` | `int` | N/A | N/A | N/A |
| `error` | `str \| None` | N/A | N/A | N/A |

- [ ] **PARITY ISSUE:** Python has `affected_rows` and `error` fields that others lack
- [ ] **PARITY ISSUE:** Python missing `limit`/`offset` on DatabaseResult
- [ ] **Documented?** Partially — format not shown in most CLAUDE.md files

## Transaction Methods

| Framework | Begin | Commit | Rollback |
|-----------|-------|--------|----------|
| Python | `start_transaction()` | `commit()` | `rollback()` |
| PHP | `startTransaction()` | `commit()` | `rollback()` |
| Ruby | `transaction { \|db\| ... }` (block) | `commit()` | `rollback()` |
| Node.js | `startTransaction()` | `commit()` | `rollback()` |

- [ ] **PARITY: OK** — Ruby adds block syntax for auto-rollback on exception
- [ ] **Documented?** All CLAUDE.md: yes

## ID Generation

### `get_next_id()` / `getNextId()`

| Framework | Signature |
|-----------|-----------|
| Python | `get_next_id(table, pk_column="id", generator_name=None)` |
| PHP | `getNextId(table, pkColumn="id", generatorName=null)` |
| Ruby | `get_next_id(table, pk_column: "id", generator_name: nil)` |
| Node.js | `getNextId(table, pkColumn?, generatorName?)` |

- [ ] **PARITY: OK** — all use same strategy (tina4_sequences table for SQLite/MySQL/MSSQL, sequences for PostgreSQL, generators for Firebird)
- [ ] **Documented?** All CLAUDE.md: yes

## Schema Introspection

| Method | Python | PHP | Ruby | Node.js |
|--------|--------|-----|------|---------|
| Table exists | `table_exists(name)` | `tableExists(name)` | `table_exists?(name)` | `tableExists(name)` |
| List tables | `get_tables()` | `getTables()` | `tables` | `getTables()` |
| List columns | `get_columns(table)` | N/A (via adapter) | `columns(table)` | `getColumns(table)` |

- [ ] **MINOR ISSUE:** PHP `get_columns` is on adapter, not Database class
- [ ] **Documented?** Partially

## Environment Variables

- [ ] **PARITY: OK** — all use same env vars:

| Var | Default |
|-----|---------|
| `DATABASE_URL` | varies |
| `DATABASE_USERNAME` | empty |
| `DATABASE_PASSWORD` | empty |
| `TINA4_AUTOCOMMIT` | false |
| `TINA4_DB_CACHE` | false |
| `TINA4_DB_CACHE_TTL` | 30 |
| `TINA4_MAX_UPLOAD_SIZE` | 10485760 |

## Issues to Fix

| # | Issue | Severity | Status |
|---|-------|----------|--------|
| 1 | ~~`execute()` return type differs~~ | MEDIUM | FIXED — all return bool for writes, DatabaseResult for RETURNING/CALL/EXEC. Python has last_error/get_error(). |
| 2 | Python DatabaseResult missing `limit`/`offset` fields | LOW | PARKED — minor |
| 3 | PHP `get_columns` on adapter not Database class | LOW | PARKED — minor |
| 4 | Node.js missing `cache_stats()` API | LOW | PARKED — minor |

## Documentation Gaps

| # | Gap |
|---|-----|
| 1 | DatabaseResult format not documented in most CLAUDE.md files |
| 2 | `execute()` return type differences not flagged anywhere |
