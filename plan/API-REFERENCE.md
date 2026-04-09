# Tina4 API Reference

> Auto-generated on 2026-04-09

This document lists all public classes and methods extracted from the 4 Tina4 framework implementations.

## ORM

### Python — `ORM` (`orm/model.py`)

| Method | 
|--------|
| `query()` |
| `save()` |
| `delete()` |
| `force_delete()` |
| `restore()` |
| `create(data: dict=None, **kwargs)` |
| `find_by_id(pk_value, include: list[str]=None)` |
| `find(filter: dict=None, limit: int=100, offset: int=0, order_by: str=None, include: list[str]=None)` |
| `load(filter: str=None, params: list=None, include: list[str]=None)` |
| `find_or_fail(pk_value)` |
| `exists(pk_value)` |
| `all(limit: int=100, offset: int=0, include: list[str]=None, order_by: str=None)` |
| `select(sql: str, params: list=None, limit: int=20, offset: int=0, include: list[str]=None)` |
| `select_one(sql: str, params: list=None, include: list[str]=None)` |
| `where(filter_sql: str, params: list=None, limit: int=20, offset: int=0, include: list[str]=None)` |
| `with_trashed(filter_sql: str='1=1', params: list=None, limit: int=20, offset: int=0)` |
| `count(conditions: str=None, params: list=None)` |
| `create_table()` |
| `cached(sql: str, params: list=None, ttl: int=60, limit: int=20, offset: int=0)` |
| `clear_cache()` |
| `clear_rel_cache(instances: list=None)` |
| `get_db()` |
| `get_db_column(prop: str)` |
| `eager_load(instances: list, include_list: list[str])` |
| `has_one(related_class, foreign_key: str=None)` |
| `has_many(related_class, foreign_key: str=None, limit: int=100, offset: int=0)` |
| `belongs_to(related_class, foreign_key: str=None)` |
| `scope(name: str, filter_sql: str, params: list=None)` |
| `validate()` |
| `to_dict(include: list[str]=None)` |
| `to_assoc(include: list[str]=None)` |
| `to_object()` |
| `to_array()` |
| `to_list()` |
| `to_json(include: list[str]=None)` |

### PHP — `User` (`ORM.php`)

| Method | 
|--------|
| `setGlobalDb($db)` |
| `query()` |
| `create($data = [])` |
| `__set($name, $value)` |
| `__get($name)` |
| `__isset($name)` |
| `__unset($name)` |
| `setDb($db)` |
| `getDb()` |
| `fill($data)` |
| `save()` |
| `findById($id, $include = null)` |
| `load($filter = null, $params = [], $include = null)` |
| `delete()` |
| `find($filter = [], $limit = 100, $offset = 0, $orderBy = null, $include = null)` |
| `all($limit = 100, $offset = 0, $include = null, $orderBy = null)` |
| `count($conditions = null, $params = [])` |
| `toDict($include = null)` |
| `toAssoc($include = null)` |
| `toObject()` |
| `toArray()` |
| `toList()` |
| `toJson($include = null)` |
| `exists()` |
| `getPrimaryKeyValue()` |
| `getDbColumn($property)` |
| `select($sql, $params = [], $limit = 20, $offset = 0, $include = null)` |
| `selectOne($sql, $params = [], $include = null)` |
| `where($filterSql, $params = [], $limit = 20, $offset = 0, $include = null)` |
| `findOrFail($id)` |
| `forceDelete()` |
| `restore()` |
| `withTrashed($filterSql = '1=1', $params = [], $limit = 20, $offset = 0)` |
| `validate()` |
| `scope($name, $filterSql, $params = [])` |
| `__callStatic($name, $arguments)` |
| `hasOne($relatedClass, $foreignKey = null)` |
| `hasMany($relatedClass, $foreignKey = null, $limit = 100, $offset = 0)` |
| `belongsTo($relatedClass, $foreignKey = null)` |
| `createTable()` |
| `cached($sql, $params = [], $ttl = 60, $limit = 20, $offset = 0, $include = null)` |
| `clearCache()` |
| `getData()` |
| `markAsExisting()` |
| `eagerLoad(array &$instances, $include, $db)` |
| `setRelCache($name, $value)` |
| `clearRelCache()` |

### Ruby — `Tina4` (`orm.rb`)

| Method | 
|--------|
| `self.snake_to_camel(name)` |
| `self.camel_to_snake(name)` |
| `load(filter = nil, params = [], include: nil)` |
| `errors(@errors
    end

    # Convert to hash using Ruby attribute names.
    # Optionally include relationships via the include keyword.
    def to_h(include: nil)` |
| `to_json(include: nil, **_args)` |
| `to_s("#<#{self.class.name} #{to_h}>"
    end

    def select(*fields)` |
| `to_db_hash(exclude_nil: false)` |
| `validate_fields(self.class.field_definitions.each do |name, opts|
        value = __send__(name)` |
| `load_has_one(name)` |
| `load_has_many(name)` |
| `load_belongs_to(name)` |
| `query_has_one(related_class, foreign_key: nil)` |
| `query_has_many(related_class, foreign_key: nil, limit: 100, offset: 0)` |
| `query_belongs_to(related_class, foreign_key: nil)` |

### Node — `BaseModel` (`orm/src/baseModel.ts`)

| Method | 
|--------|
| `getDbColumn(prop: string)` |
| `getDbData()` |
| `getReverseMapping()` |
| `query()` |
| `findById(T extends BaseModel>(this: new (data?: Record<string, unk...)` |
| `create(T extends BaseModel>(
    this: new (data?: Record<string...)` |
| `find(T extends BaseModel>(
    this: new (data?: Record<string...)` |
| `load(filter?: string, params?: unknown[], include?: string[])` |
| `all(T extends BaseModel>(
    this: new (data?: Record<string...)` |
| `where(T extends BaseModel>(
    this: new (data?: Record<string...)` |
| `save()` |
| `delete()` |
| `toDict(include?: string[])` |
| `toAssoc(include?: string[])` |
| `toObject()` |
| `toArray()` |
| `toList()` |
| `toJson(include?: string[])` |
| `validate()` |
| `createTable()` |
| `findOrFail(T extends BaseModel>(this: new (data?: Record<string, unk...)` |
| `exists(id: unknown)` |
| `cached(T extends BaseModel>(
    this: new (data?: Record<string...)` |
| `clearCache()` |
| `select(T extends BaseModel>(
    this: new (data?: Record<string...)` |
| `selectOne(T extends BaseModel>(
    this: new (data?: Record<string...)` |
| `forceDelete()` |
| `restore()` |
| `withTrashed(T extends BaseModel>(
    this: new (data?: Record<string...)` |
| `count(conditions?: string, params?: unknown[])` |
| `scope(name: string,
    filterSql: string,
    params?: unknown[],)` |
| `hasOne(T extends BaseModel, R extends BaseModel>(
    this: T,
 ...)` |
| `hasMany(T extends BaseModel, R extends BaseModel>(
    this: T,
 ...)` |
| `belongsTo(T extends BaseModel, R extends BaseModel>(
    this: T,
 ...)` |
| `registerModel(name: string, modelClass: typeof BaseModel)` |
| `eagerLoad(instances: BaseModel[], includeList: string[])` |
| `clearRelCache()` |

## Router

### Python — `RouteRef` (`core/router.py`)

| Method | 
|--------|
| `secure()` |
| `no_auth()` |
| `cache(max_age: int | None=None)` |

### Python — `RouteGroup` (`core/router.py`)

| Method | 
|--------|
| `get(path: str, handler, **options)` |
| `post(path: str, handler, **options)` |
| `put(path: str, handler, **options)` |
| `patch(path: str, handler, **options)` |
| `delete(path: str, handler, **options)` |
| `any(path: str, handler, **options)` |
| `group(prefix: str, callback, middleware=None)` |

### Python — `Router` (`core/router.py`)

| Method | 
|--------|
| `group(prefix: str, callback, middleware=None)` |
| `websocket(path: str, handler)` |
| `match_ws(path: str)` |
| `all_ws()` |
| `get_web_socket_routes()` |
| `use(middleware_class)` |
| `get(path: str, handler, **options)` |
| `post(path: str, handler, **options)` |
| `put(path: str, handler, **options)` |
| `patch(path: str, handler, **options)` |
| `delete(path: str, handler, **options)` |
| `any(path: str, handler, **options)` |
| `add(method: str, path: str, handler, **options)` |
| `match(method: str, path: str)` |
| `get_routes()` |
| `list_routes()` |
| `clear()` |

### PHP — `RouteDiscovery` (`RouteDiscovery.php`)

| Method | 
|--------|
| `scan($routesDir)` |
| `directoryToUrlPath($dirPath)` |

### PHP — `Router` (`Router.php`)

| Method | 
|--------|
| `use($class)` |
| `get($path, $callback)` |
| `post($path, $callback)` |
| `put($path, $callback)` |
| `patch($path, $callback)` |
| `delete($path, $callback)` |
| `any($path, $callback)` |
| `group($prefix, $callback, $middleware = [])` |
| `middleware($middleware)` |
| `cache()` |
| `noCache()` |
| `swagger($meta)` |
| `secure()` |
| `noAuth()` |
| `match($method, $path)` |
| `dispatch($request, $response)` |
| `getRoutes()` |
| `listRoutes()` |
| `count()` |
| `websocket($path, $handler)` |
| `getWebSocketRoutes()` |
| `clear()` |

### Ruby — `Tina4` (`router.rb`)

| Method | 
|--------|
| `secure(@auth_required = true
      self
    end

    # Opt out of the secure-by-default auth on write routes.
    # Returns self for chaining: Router.post("/login")` |
| `no_auth(@auth_required = false
      self
    end

    # Mark this route as cacheable.
    # Returns self for chaining: Router.get("/path")` |
| `cache(@cached = true
      self
    end

    # Returns params hash if matched, false otherwise
    def match?(request_path, request_method = nil)` |
| `match_path(request_path)` |
| `run_middleware(request, response)` |
| `normalize_path(path)` |
| `compile_pattern(path)` |
| `cast_param(value, type)` |

### Node — `RouteRef` (`core/src/router.ts`)

| Method | 
|--------|
| `secure()` |
| `noAuth()` |
| `cache()` |
| `use(middlewareClass: any)` |
| `getClassMiddlewares()` |
| `clearClassMiddlewares()` |
| `addRoute(definition: RouteDefinition)` |
| `get(path: string, handler: RouteHandler, middlewares?: Middle...)` |
| `post(path: string, handler: RouteHandler, middlewares?: Middle...)` |
| `put(path: string, handler: RouteHandler, middlewares?: Middle...)` |
| `patch(path: string, handler: RouteHandler, middlewares?: Middle...)` |
| `delete(path: string, handler: RouteHandler, middlewares?: Middle...)` |
| `any(path: string, handler: RouteHandler, middlewares?: Middle...)` |
| `group(prefix: string, callback: (group: RouteGroup)` |
| `callback(group)` |
| `match(method: string, pathname: string)` |
| `getRoutes()` |
| `allRoutes()` |
| `listRoutes()` |
| `websocket(path: string, handler: WebSocketRouteHandler)` |
| `getWebSocketRoutes()` |
| `matchWebSocket(pathname: string)` |
| `clear()` |

## Database

### Python — `MongoDBAdapter` (`database/mongodb.py`)

| Method | 
|--------|
| `connect(connection_string: str, username: str='', password: str='', **kwargs)` |
| `close()` |
| `execute(sql: str, params: list=None)` |
| `fetch(sql: str, params: list=None, limit: int=100, offset: int=0)` |
| `fetch_one(sql: str, params: list=None)` |
| `insert(table: str, data: dict)` |
| `update(table: str, data: dict, filter_sql: str='', params: list=None)` |
| `delete(table: str, filter_sql: str='', params: list=None)` |
| `start_transaction()` |
| `commit()` |
| `rollback()` |
| `table_exists(name: str)` |
| `get_tables()` |
| `get_columns(table: str)` |
| `get_next_id(table: str, pk_column: str='id')` |
| `get_database_type()` |

### Python — `ODBCAdapter` (`database/odbc.py`)

| Method | 
|--------|
| `connect(connection_string: str, username: str='', password: str='', **kwargs)` |
| `close()` |
| `execute(sql: str, params: list=None)` |
| `fetch(sql: str, params: list=None, limit: int=100, offset: int=0)` |
| `fetch_one(sql: str, params: list=None)` |
| `insert(table: str, data: dict)` |
| `update(table: str, data: dict, filter_sql: str='', params: list=None)` |
| `delete(table: str, filter_sql: str='', params: list=None)` |
| `start_transaction()` |
| `commit()` |
| `rollback()` |
| `table_exists(name: str)` |
| `get_tables()` |
| `get_columns(table: str)` |
| `get_database_type()` |

### Python — `MongoDBSessionHandler` (`session_handlers/mongodb_handler.py`)

| Method | 
|--------|
| `read(session_id: str)` |
| `write(session_id: str, data: dict, ttl: int=0)` |
| `destroy(session_id: str)` |
| `gc(max_lifetime: int)` |
| `close()` |

### PHP — `CachedDatabase` (`Database/CachedDatabase.php`)

| Method | 
|--------|
| `cacheStats()` |
| `cacheClear()` |
| `open()` |
| `close()` |
| `query($sql, $params = [])` |
| `fetch($sql, $params = [], $limit = 100, $offset = 0)` |
| `fetchOne($sql, $params = [])` |
| `execute($sql, $params = [])` |
| `insert($table, $data)` |
| `update($table, $data, $where = '', $whereParams = [])` |
| `delete($table, $filter = '', $whereParams = [])` |
| `executeMany($sql, $paramsList = [])` |
| `tableExists($table)` |
| `getColumns($table)` |
| `getTables()` |
| `lastInsertId()` |
| `startTransaction()` |
| `commit()` |
| `rollback()` |
| `error()` |
| `getAdapter()` |

### PHP — `Database` (`Database/Database.php`)

| Method | 
|--------|
| `create($url, $autoCommit = null, $username = '', $password = '', $pool = 0)` |
| `fromEnv($envKey = 'DATABASE_URL', $autoCommit = null)` |
| `getAdapter()` |
| `poolSize()` |
| `activeCount()` |
| `checkout()` |
| `checkin($adapter)` |
| `closeAll()` |
| `query($sql, $params = [])` |
| `fetch($sql, $params = [], $limit = 100, $offset = 0)` |
| `fetchOne($sql, $params = [])` |
| `execute($sql, $params = [])` |
| `exec($sql, $params = [])` |
| `insert($table, $data)` |
| `update($table, $data, $filterSql = '', $params = [])` |
| `delete($table, $filter = '', $whereParams = [])` |
| `open()` |
| `close()` |
| `lastInsertId()` |
| `startTransaction()` |
| `commit()` |
| `rollback()` |
| `tableExists($tableName)` |
| `getTables()` |
| `getColumns($tableName)` |
| `getError()` |
| `getLastId()` |
| `getNextId($table, $pkColumn = 'id', $generatorName = null)` |
| `executeMany($sql, $paramsList = [])` |
| `error()` |
| `getConnection($envKey = 'DATABASE_URL')` |
| `supportedSchemes()` |
| `isSupported($scheme)` |
| `cacheStats()` |
| `cacheClear()` |

### PHP — `DatabaseResult` (`Database/DatabaseResult.php`)

| Method | 
|--------|
| `columnInfo()` |
| `toJson()` |
| `toCsv()` |
| `toArray()` |
| `toPaginate()` |
| `current()` |
| `key()` |
| `next()` |
| `rewind()` |
| `valid()` |
| `count()` |
| `offsetExists($offset)` |
| `offsetGet($offset)` |
| `offsetSet($offset, $value)` |
| `offsetUnset($offset)` |
| `jsonSerialize()` |

### PHP — `MongoDBAdapter` (`Database/MongoDBAdapter.php`)

| Method | 
|--------|
| `open()` |
| `close()` |
| `query($sql, $params = [])` |
| `fetch($sql, $params = [], $limit = 100, $offset = 0)` |
| `fetchOne($sql, $params = [])` |
| `execute($sql, $params = [])` |
| `executeMany($sql, $paramsList = [])` |
| `insert($table, $data)` |
| `update($table, $data, $where = '', $whereParams = [])` |
| `delete($table, $filter = '', $whereParams = [])` |
| `tableExists($table)` |
| `getTables()` |
| `getColumns($table)` |
| `lastInsertId()` |
| `startTransaction()` |
| `commit()` |
| `rollback()` |
| `error()` |
| `getConnection()` |
| `getDatabase()` |

### PHP — `ODBCAdapter` (`Database/ODBCAdapter.php`)

| Method | 
|--------|
| `open()` |
| `close()` |
| `query($sql, $params = [])` |
| `fetch($sql, $params = [], $limit = 100, $offset = 0)` |
| `fetchOne($sql, $params = [])` |
| `execute($sql, $params = [])` |
| `executeMany($sql, $paramsList = [])` |
| `insert($table, $data)` |
| `update($table, $data, $where = '', $whereParams = [])` |
| `delete($table, $filter = '', $whereParams = [])` |
| `tableExists($table)` |
| `getTables()` |
| `getColumns($table)` |
| `lastInsertId()` |
| `startTransaction()` |
| `commit()` |
| `rollback()` |
| `error()` |
| `getConnection()` |
| `getConnectionString()` |

### PHP — `DatabaseUrl` (`DatabaseUrl.php`)

| Method | 
|--------|
| `fromEnv($envKey = 'DATABASE_URL')` |
| `getDriverClass()` |
| `getDsn()` |
| `toSafeString()` |

### PHP — `DatabaseSessionHandler` (`Session/DatabaseSessionHandler.php`)

| Method | 
|--------|
| `read($sessionId)` |
| `write($sessionId, $data)` |
| `delete($sessionId)` |
| `gc($ttl)` |
| `close()` |

### Ruby — `Tina4` (`database.rb`)

| Method | 
|--------|
| `checkout(@mutex.synchronize do
        idx = @index
        @index = (@index + 1)` |
| `checkin(_driver)` |
| `close_all(@mutex.synchronize do
        @drivers.each_with_index do |driver, i|
          if driver
            driver.close rescue nil
            @drivers[i] = nil
          end
        end
      end
    end

    # Number of connections that have been created.
    def active_count
      @mutex.synchronize do
        @drivers.count { |d| !d.nil? }
      end
    end

    def size
      @pool_size
    end
  end

  class Database
    attr_reader :driver, :driver_name, :connected, :pool

    DRIVERS = {
      "sqlite" => "Tina4::Drivers::SqliteDriver",
      "sqlite3" => "Tina4::Drivers::SqliteDriver",
      "postgres" => "Tina4::Drivers::PostgresDriver",
      "postgresql" => "Tina4::Drivers::PostgresDriver",
      "mysql" => "Tina4::Drivers::MysqlDriver",
      "mssql" => "Tina4::Drivers::MssqlDriver",
      "sqlserver" => "Tina4::Drivers::MssqlDriver",
      "firebird" => "Tina4::Drivers::FirebirdDriver",
      "mongodb" => "Tina4::Drivers::MongodbDriver",
      "mongo" => "Tina4::Drivers::MongodbDriver",
      "odbc" => "Tina4::Drivers::OdbcDriver"
    }.freeze

    # Static factory — cross-framework consistency: Database.create(url)` |
| `self.create(url, username: "", password: "", pool: 0)` |
| `self.from_env(env_key: "DATABASE_URL", pool: 0)` |
| `connect(@driver.connect(@connection_string, username: @username, password: @password)` |
| `close(if @pool
        @pool.close_all
      elsif @driver && @connected
        @driver.close
      end
      @connected = false
    end

    # Get the current driver — from pool (round-robin)` |
| `current_driver(if @pool
        @pool.checkout
      else
        @driver
      end
    end

    # ── Query Cache ──────────────────────────────────────────────

    def cache_stats
      @cache_mutex.synchronize do
        {
          enabled: @cache_enabled,
          hits: @cache_hits,
          misses: @cache_misses,
          size: @query_cache.size,
          ttl: @cache_ttl
        }
      end
    end

    def cache_clear
      @cache_mutex.synchronize do
        @query_cache.clear
        @cache_hits = 0
        @cache_misses = 0
      end
    end

    def fetch(sql, params = [], limit: 100, offset: nil)` |
| `fetch_one(sql, params = [])` |
| `insert(table, data)` |
| `update(table, data, filter = {})` |
| `delete(table, filter = {})` |
| `get_error(@last_error
    end

    # Return the last insert ID from execute()` |
| `get_last_id(current_driver.last_insert_id
    rescue
      nil
    end

    # Execute a write statement. Returns true/false for simple writes.
    # Returns DatabaseResult if SQL contains RETURNING, CALL, EXEC, or SELECT.
    def execute(sql, params = [])` |
| `execute_many(sql, params_list = [])` |
| `transaction(drv = current_driver
      drv.begin_transaction
      yield self
      drv.commit
    rescue => e
      drv.rollback
      raise e
    end

    # Begin a transaction without a block — matches PHP/Python/Node API.
    def start_transaction
      current_driver.begin_transaction
    end

    # Commit the current transaction — matches PHP/Python/Node API.
    def commit
      current_driver.commit
    end

    # Roll back the current transaction — matches PHP/Python/Node API.
    def rollback
      current_driver.rollback
    end

    def tables
      current_driver.tables
    end

    # Cross-framework alias for tables — matches PHP/Python/Node get_tables.
    alias get_tables tables

    def columns(table_name)` |
| `get_adapter(current_driver
    end

    # Returns the configured pool size, or 1 for single-connection mode.
    def pool_size
      @pool_size > 0 ? @pool_size : 1
    end

    # Number of connections currently created (lazy pool connections counted)` |
| `active_count(if @pool
        @pool.active_count
      else
        @connected ? 1 : 0
      end
    end

    # Check out a driver from the pool (or return the single driver)` |
| `ensure_sequence_table(return if table_exists?("tina4_sequences")` |
| `sequence_next(seq_name, table: nil, pk_column: "id")` |
| `row_value(row, key)` |
| `cache_key(sql, params)` |
| `cache_get(key)` |
| `cache_set(key, value)` |
| `cache_invalidate(@cache_mutex.synchronize { @query_cache.clear }
    end

    def detect_driver(conn)` |
| `create_driver(klass_name = DRIVERS[@driver_name]
      raise "Unknown database driver: #{@driver_name}" unless klass_name
      klass = Object.const_get(klass_name)` |

### Ruby — `Tina4` (`database_result.rb`)

| Method | 
|--------|
| `each(&block)` |
| `first(@records.first
    end

    def last
      @records.last
    end

    def empty?
      @records.empty?
    end

    def [](index)` |
| `length(@count
    end

    def size
      @count
    end

    def success?
      @error.nil?
    end

    def to_array
      @records.map do |record|
        record.is_a?(Hash)` |
| `to_json(*_args)` |
| `to_csv(separator: ",", headers: true)` |
| `to_paginate(page: nil, per_page: nil)` |
| `to_crud(table_name: "data", primary_key: "id", editable: true)` |
| `column_info(return @column_info_cache if @column_info_cache

      table = extract_table_from_sql

      if @db && table
        begin
          @column_info_cache = query_column_metadata(table)` |
| `extract_table_from_sql(return nil if @sql.nil? || @sql.empty?

      if (m = @sql.match(/\bFROM\s+["']?(\w+)` |
| `query_column_metadata(table)` |
| `normalize_columns(raw_cols)` |
| `parse_type_size(type_str)` |
| `fallback_column_info(return [] if @records.empty?
      keys = @records.first.is_a?(Hash)` |
| `escape_csv(value, separator)` |

### Node — `DatabaseSessionHandler` (`core/src/sessionHandlers/databaseHandler.ts`)

| Method | 
|--------|
| `read(sessionId: string)` |
| `write(sessionId: string, data: SessionData, ttl: number)` |
| `destroy(sessionId: string)` |
| `gc(_maxLifetime: number)` |

### Node — `MongodbAdapter` (`orm/src/adapters/mongodb.ts`)

| Method | 
|--------|
| `connect()` |
| `execute(sql: string, params?: unknown[])` |
| `executeAsync(sql: string, params?: unknown[])` |
| `executeMany(sql: string, paramsList: unknown[][])` |
| `executeManyAsync(sql: string, paramsList: unknown[][])` |
| `query(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `queryAsync(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `fetch(T = Record<string, unknown>>(sql: string, params?: unknow...)` |
| `fetchAsync(T = Record<string, unknown>>(sql: string, params?: unknow...)` |
| `fetchOne(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `fetchOneAsync(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `insert(table: string, data: Record<string, unknown> | Record<str...)` |
| `insertAsync(table: string, data: Record<string, unknown> | Record<str...)` |
| `update(table: string, data: Record<string, unknown>, filter: Rec...)` |
| `updateAsync(table: string, data: Record<string, unknown>, filter: Rec...)` |
| `delete(table: string, filter: Record<string, unknown> | string |...)` |
| `deleteAsync(table: string, filter: Record<string, unknown> | string |...)` |
| `startTransaction()` |
| `startTransactionAsync()` |
| `commit()` |
| `commitAsync()` |
| `rollback()` |
| `rollbackAsync()` |
| `tables()` |
| `tablesAsync()` |
| `columns(table: string)` |
| `columnsAsync(table: string)` |
| `lastInsertId()` |
| `close()` |
| `tableExists(name: string)` |
| `tableExistsAsync(name: string)` |
| `createTable(name: string, columns: Record<string, FieldDefinition>)` |
| `createTableAsync(name: string, columns: Record<string, FieldDefinition>)` |
| `getTableColumnsAsync(table: string)` |

### Node — `OdbcAdapter` (`orm/src/adapters/odbc.ts`)

| Method | 
|--------|
| `connect()` |
| `execute(sql: string, params?: unknown[])` |
| `executeMany(sql: string, paramsList: unknown[][])` |
| `query(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `fetch(T = Record<string, unknown>>(sql: string, params?: unknow...)` |
| `fetchOne(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `insert(table: string, data: Record<string, unknown>)` |
| `update(table: string, data: Record<string, unknown>, filter: Rec...)` |
| `delete(table: string, filter: Record<string, unknown> | string |...)` |
| `startTransaction()` |
| `commit()` |
| `rollback()` |
| `tables()` |
| `columns(table: string)` |
| `tableExists(name: string)` |
| `createTable(name: string, columns: Record<string, FieldDefinition>)` |
| `getTableColumns(name: string)` |
| `addColumn(table: string, colName: string, def: FieldDefinition)` |
| `executeAsync(sql: string, params?: unknown[])` |
| `executeManyAsync(sql: string, paramsList: unknown[][])` |
| `queryAsync(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `fetchAsync(T = Record<string, unknown>>(
    sql: string,
    params...)` |
| `fetchOneAsync(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `insertAsync(table: string, data: Record<string, unknown>)` |
| `updateAsync(table: string, data: Record<string, unknown>, filter: Rec...)` |
| `deleteAsync(table: string,
    filter: Record<string, unknown> | stri...)` |
| `startTransactionAsync()` |
| `commitAsync()` |
| `rollbackAsync()` |
| `tablesAsync()` |
| `columnsAsync(table: string)` |
| `tableExistsAsync(name: string)` |
| `createTableAsync(name: string, columns: Record<string, FieldDefinition>)` |
| `getTableColumnsAsync(name: string)` |
| `addColumnAsync(table: string, colName: string, def: FieldDefinition)` |
| `lastInsertId()` |
| `close()` |

### Node — `CachedDatabaseAdapter` (`orm/src/cachedDatabase.ts`)

| Method | 
|--------|
| `cacheStats()` |
| `cacheClear()` |
| `execute(sql: string, params?: unknown[])` |
| `executeMany(sql: string, paramsList: unknown[][])` |
| `query(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `fetch(T = Record<string, unknown>>(sql: string, params?: unknow...)` |
| `fetchOne(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `insert(table: string, data: Record<string, unknown> | Record<str...)` |
| `update(table: string, data: Record<string, unknown>, filter: Rec...)` |
| `delete(table: string, filter: Record<string, unknown> | string |...)` |
| `startTransaction()` |
| `commit()` |
| `rollback()` |
| `tables()` |
| `columns(table: string)` |
| `lastInsertId()` |
| `close()` |
| `tableExists(name: string)` |
| `createTable(name: string, columns: Record<string, FieldDefinition>)` |
| `getAdapter()` |

### Node — `Database` (`orm/src/database.ts`)

| Method | 
|--------|
| `create(url: string, username?: string, password?: string, pool: ...)` |
| `setAdapter(adapter)` |
| `fromEnv(envKey = "DATABASE_URL", pool: number = 0)` |
| `getAdapter()` |
| `poolSize()` |
| `activeCount()` |
| `checkout()` |
| `checkin(_adapter: DatabaseAdapter)` |
| `closeAll()` |
| `fetch(sql: string, params?: unknown[], limit?: number, offset?:...)` |
| `fetchOne(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `execute(sql: string, params?: unknown[])` |
| `insert(table: string, data: Record<string, unknown>)` |
| `update(table: string, data: Record<string, unknown>, filter?: Re...)` |
| `delete(table: string, filter?: Record<string, unknown>)` |
| `close()` |
| `startTransaction()` |
| `commit()` |
| `rollback()` |
| `tableExists(name: string)` |
| `getTables()` |
| `getColumns(tableName: string)` |
| `executeMany(sql: string, paramSets: unknown[][])` |
| `getError()` |
| `cacheStats()` |
| `cacheClear()` |
| `getLastId()` |
| `getNextId(table: string, pkColumn = "id", generatorName?: string)` |

### Node — `DatabaseResult` (`orm/src/databaseResult.ts`)

| Method | 
|--------|
| `toJson()` |
| `toCsv()` |
| `toArray()` |
| `toPaginate(page = 1, perPage = 10)` |
| `at(index: number)` |
| `toJSON()` |
| `columnInfo()` |

## Auth

### Python — `Auth` (`auth/__init__.py`)

| Method | 
|--------|
| `get_token(payload: dict, expires_in: int=None)` |
| `valid_token(token: str)` |
| `get_payload(token: str)` |
| `refresh_token(token: str, expires_in: int=None)` |
| `get_token_static(payload: dict, expires_in: int=60)` |
| `valid_token_static(token: str)` |
| `get_payload_static(token: str)` |
| `refresh_token_static(token: str, expires_in: int=60)` |
| `authenticate_request_static(headers: dict)` |
| `hash_password(password: str, salt: str=None, iterations: int=260000)` |
| `check_password(password: str, hashed: str)` |
| `validate_api_key(provided: str, expected: str=None)` |
| `authenticate_request(headers: dict)` |

### Python — `AuthMiddleware` (`auth/__init__.py`)

| Method | 
|--------|
| `before_request(request, response)` |

### PHP — `Auth` (`Auth.php`)

| Method | 
|--------|
| `getToken($payload, $expiresIn = 3600)` |
| `validToken($token)` |
| `getPayload($token)` |
| `hashPassword($password, $salt = null, $iterations = 260000)` |
| `checkPassword($password, $hash)` |
| `middleware()` |
| `refreshToken($token, $expiresIn = 3600)` |
| `authenticateRequest($headers)` |
| `validateApiKey($provided, $expected = null)` |

### Node — `Auth` (`core/src/auth.ts`)

| Method | 
|--------|
| `next()` |

## Queue

### Python — `Queue` (`queue/__init__.py`)

| Method | 
|--------|
| `push(data: dict, priority: int=0, delay_seconds: int=0)` |
| `pop()` |
| `pop_batch(count: int)` |
| `get_topic()` |
| `process(handler, topic: str=None, max_jobs, batch_size)` |
| `size(status: str='pending')` |
| `purge(status: str='completed')` |
| `retry_failed(max_retries: int=None)` |
| `failed()` |
| `dead_letters(max_retries: int=None)` |
| `retry(job_id: str, delay_seconds: int=0)` |
| `clear()` |
| `produce(topic: str, data: dict, priority: int=0, delay_seconds: int=0)` |
| `consume(topic: str=None, job_id: str=None, poll_interval: float=1.0, iterations: int=0, batch_size: int=1)` |
| `pop_by_id(job_id: str)` |

### PHP — `Queue` (`Queue.php`)

| Method | 
|--------|
| `push($payload, $delay = 0, $priority = 0)` |
| `pop()` |
| `popBatch($count)` |
| `process($handlerOrQueue, $queueOrHandlerOrOptions = '', $options = [])` |
| `size($status = 'pending')` |
| `clear()` |
| `writeFailed($topic, $jobData)` |
| `failed()` |
| `retry($jobId, $delaySeconds = 0)` |
| `deadLetters($maxRetries = null)` |
| `purge($status)` |
| `retryFailed($maxRetries = null)` |
| `produce($topic, $payload, $priority = 0, $delaySeconds = 0)` |
| `consume($topic = '', $id = null, $pollInterval = 1.0, $batchSize = 1)` |
| `popById($id)` |
| `getTopic()` |

### Ruby — `Tina4` (`queue.rb`)

| Method | 
|--------|
| `push(payload, priority: 0, delay_seconds: 0)` |
| `pop_batch(count)` |
| `retry(job_id = nil, delay_seconds: 0)` |
| `dead_letters(max_retries: nil)` |
| `purge(status)` |
| `retry_failed(max_retries: nil)` |
| `produce(topic, payload, priority: 0, delay_seconds: 0)` |
| `consume(topic = nil, id: nil, poll_interval: 1.0, iterations: 0, batch_size: 1, &block)` |
| `pop_by_id(id)` |
| `size(status: "pending")` |
| `get_topic(@topic
    end

    # Consume all available jobs and pass each to handler, then stop.
    #
    # Simpler alternative to consume()` |
| `process(topic: nil, max_jobs: nil, batch_size: 1, &handler)` |
| `backend(@backend
    end

    # Resolve the default backend from env vars.
    def self.resolve_backend(name = nil)` |
| `resolve_backend_arg(backend)` |
| `self.resolve_rabbitmq_config(config = {}
      url = ENV["TINA4_QUEUE_URL"]
      if url
        config = parse_amqp_url(url)` |
| `self.resolve_kafka_config(config = {}
      url = ENV["TINA4_QUEUE_URL"]
      if url
        config[:brokers] = url.sub("kafka://", "")` |
| `self.resolve_mongo_config(config = {}
      uri = ENV["TINA4_MONGO_URI"]
      config[:uri] = uri if uri
      config[:host] = ENV.fetch("TINA4_MONGO_HOST", "localhost")` |
| `self.parse_amqp_url(url)` |

### Node — `Queue` (`core/src/queue.ts`)

| Method | 
|--------|
| `push(queue: string, payload: unknown, delay?: number)` |
| `pop(queue: string)` |
| `size(queue: string)` |
| `clear(queue: string)` |
| `popBatch(count: number)` |
| `process(handler: (job: QueueJob | QueueJob[])` |
| `failed()` |
| `retry(jobId?: string, delaySeconds?: number)` |
| `deadLetters(maxRetries?: number)` |
| `purge(status: string, maxRetries?: number)` |
| `retryFailed(maxRetries?: number)` |
| `produce(topic: string, payload: unknown, priority: number = 0, de...)` |
| `popById(id: string)` |
| `getTopic()` |
| `getMaxRetries()` |

## Session

### Python — `SessionHandler` (`session/__init__.py`)

| Method | 
|--------|
| `read(session_id: str)` |
| `write(session_id: str, data: dict, ttl: int)` |
| `destroy(session_id: str)` |
| `gc(max_lifetime: int)` |

### Python — `FileSessionHandler` (`session/__init__.py`)

| Method | 
|--------|
| `read(session_id: str)` |
| `write(session_id: str, data: dict, ttl: int)` |
| `destroy(session_id: str)` |
| `gc(max_lifetime: int)` |

### Python — `DatabaseSessionHandler` (`session/__init__.py`)

| Method | 
|--------|
| `read(session_id: str)` |
| `write(session_id: str, data: dict, ttl: int)` |
| `destroy(session_id: str)` |
| `gc(max_lifetime: int)` |

### Python — `Session` (`session/__init__.py`)

| Method | 
|--------|
| `session_id()` |
| `get_session_id()` |
| `start(session_id: str=None)` |
| `get(key: str, default=None)` |
| `set(key: str, value)` |
| `delete(key: str)` |
| `has(key: str)` |
| `all()` |
| `clear()` |
| `save()` |
| `destroy()` |
| `regenerate()` |
| `flash(key: str, value=None)` |
| `get_flash(key: str, default=None)` |
| `cookie_header(cookie_name: str='tina4_session')` |
| `gc()` |

### PHP — `MongoSessionHandler` (`Session/MongoSessionHandler.php`)

| Method | 
|--------|
| `read($sessionId)` |
| `write($sessionId, $data)` |
| `delete($sessionId)` |
| `close()` |

### PHP — `RedisSessionHandler` (`Session/RedisSessionHandler.php`)

| Method | 
|--------|
| `read($sessionId)` |
| `write($sessionId, $data)` |
| `delete($sessionId)` |
| `exists($sessionId)` |
| `touch($sessionId)` |
| `close()` |

### PHP — `ValkeySessionHandler` (`Session/ValkeySessionHandler.php`)

| Method | 
|--------|
| `read($sessionId)` |
| `write($sessionId, $data)` |
| `delete($sessionId)` |
| `exists($sessionId)` |
| `touch($sessionId)` |
| `close()` |

### PHP — `Session` (`Session.php`)

| Method | 
|--------|
| `start($sessionId = null)` |
| `get($key, $default = null)` |
| `set($key, $value)` |
| `delete($key)` |
| `destroy()` |
| `clear()` |
| `all()` |
| `has($key)` |
| `regenerate()` |
| `flash($key, $value = null)` |
| `getFlash($key, $default = null)` |
| `getSessionId()` |
| `cookieHeader($cookieName = 'tina4_session')` |
| `isStarted()` |
| `read($sessionId)` |
| `write($sessionId, $data, $ttl = 0)` |
| `save()` |
| `gc()` |

### Ruby — `Tina4` (`session.rb`)

| Method | 
|--------|
| `delete(key)` |
| `clear(@data = {}
      @modified = true
    end

    def to_hash
      @data.dup
    end

    def save
      return unless @modified
      @handler.write(@id, @data)` |
| `destroy(@handler.destroy(@id)` |
| `get(key, default = nil)` |
| `set(key, value)` |
| `all(@data.dup
    end

    # Flash data: set a value that is removed after next read.
    # Call with value to set, call without value to get (and remove)` |
| `flash(key, value = nil)` |
| `get_flash(key, default = nil)` |
| `regenerate(old_id = @id
      @id = SecureRandom.hex(32)` |
| `start(session_id = nil)` |
| `get_session_id(@id
    end

    # Reads raw session data for a given session ID from backend storage.
    # Returns the data hash or nil.
    def read(session_id)` |
| `write(session_id, data, ttl = nil)` |
| `gc(max_age = nil)` |
| `cookie_header(cookie_name = nil)` |
| `extract_session_id(env)` |
| `load_session(existing = @handler.read(@id)` |
| `create_handler(case @options[:handler].to_sym
      when :file
        Tina4::SessionHandlers::FileHandler.new(@options[:handler_options])` |
| `to_hash(ensure_loaded
      @session.to_hash
    end

    private

    def ensure_loaded
      @session ||= Session.new(@env, @options)` |

### Node — `FileSessionHandler` (`core/src/session.ts`)

| Method | 
|--------|
| `read(sessionId: string)` |
| `write(sessionId: string, data: SessionData, ttl: number)` |
| `destroy(sessionId: string)` |
| `writeFileSync(this.filePath(sessionId)` |
| `gc(_maxLifetime: number)` |
| `setHandler(handler: SessionHandler)` |
| `start(sessionId?: string)` |
| `get(key: string, defaultValue?: unknown)` |
| `set(key: string, value: unknown)` |
| `delete(key: string)` |
| `all()` |
| `clear()` |
| `has(key: string)` |
| `regenerate()` |
| `flash(key: string, value?: unknown)` |
| `getFlash(key: string, defaultValue?: unknown)` |
| `getSessionId()` |
| `cookieHeader(cookieName: string = "tina4_session")` |
| `save()` |

## Migration

### PHP — `Migration` (`Migration.php`)

| Method | 
|--------|
| `migrate()` |
| `rollback($steps = 1)` |
| `status()` |
| `getAppliedMigrations()` |
| `getPendingMigrations()` |
| `getMigrationFiles()` |
| `getApplied()` |
| `getPending()` |
| `getFiles()` |
| `create($description, $kind = 'sql')` |
| `up(\$db)` |
| `down(\$db)` |
| `recordMigration($fileName, $batch, $passed = 1)` |
| `removeMigrationRecord($fileName)` |

### PHP — `for` (`MigrationBase.php`)

| Method | 
|--------|
| `up($db)` |
| `down($db)` |
| `up($db)` |
| `down($db)` |

### Ruby — `Tina4` (`migration.rb`)

| Method | 
|--------|
| `migrate(pending = pending_migrations
      if pending.empty?
        Tina4::Log.info("No pending migrations")` |
| `rollback(steps = 1)` |
| `status({
        completed: completed_migrations,
        pending: pending_migrations.map { |f| File.basename(f)` |
| `create(description, kind = "ruby")` |
| `record_migration(name, batch, passed: 1)` |
| `remove_migration_record(name)` |
| `get_applied(completed_migrations
    end

    # Get list of pending migration filenames (public alias for pending_migrations)` |
| `get_pending(pending_migrations.map { |f| File.basename(f)` |
| `get_files(migration_files = Dir.glob(File.join(@migrations_dir, "*.sql")` |
| `resolve_migrations_dir(src_dir = File.join(Dir.pwd, "src", "migrations")` |
| `ensure_tracking_table(unless @db.table_exists?(TRACKING_TABLE)` |
| `completed_migrations(result = @db.fetch("SELECT migration_name FROM #{TRACKING_TABLE} WHERE passed = 1 ORDER BY id")` |
| `completed_migrations_with_batch(result = @db.fetch("SELECT id, migration_name, batch FROM #{TRACKING_TABLE} WHERE passed = 1 ORDER BY id")` |
| `next_batch_number(result = @db.fetch_one("SELECT MAX(batch)` |
| `pending_migrations(return [] unless Dir.exist?(@migrations_dir)` |
| `migration_sort_key(filename)` |
| `run_migration(file, batch)` |
| `rollback_migration(name)` |
| `execute_ruby_migration(file, direction)` |
| `split_sql_statements(sql, delimiter = ";")` |
| `execute_sql_file(file)` |
| `should_skip_for_firebird(stmt)` |
| `classify(name)` |
| `extract_class_name(content)` |
| `up(db)` |
| `down(db)` |

### Node — `Migration` (`orm/src/migration.ts`)

| Method | 
|--------|
| `typeof(db as any)` |
| `up()` |
| `recordMigration(name, batch)` |
| `removeMigrationRecord(migration.name)` |
| `readdirSync(dir)` |
| `mkdirSync(dir, { recursive: true })` |
| `writeFileSync(upPath, upTemplate, "utf-8")` |
| `migrate()` |
| `rollback(steps = 1)` |
| `status()` |
| `create(description: string, kind: "sql" | "class" = "sql")` |
| `getApplied()` |
| `getPending()` |
| `getFiles()` |

## GraphQL

### Python — `Parser` (`graphql/__init__.py`)

| Method | 
|--------|
| `peek()` |
| `advance()` |
| `expect(type: str, value: str=None)` |
| `match(type: str, value: str=None)` |
| `parse()` |

### Python — `Schema` (`graphql/__init__.py`)

| Method | 
|--------|
| `add_type(name: str, fields: dict[str, str])` |
| `add_query(name: str, config: dict)` |
| `add_mutation(name: str, config: dict)` |
| `from_orm(orm_class)` |

### Python — `GraphQL` (`graphql/__init__.py`)

| Method | 
|--------|
| `execute(query: str, variables: dict=None, context: dict=None)` |
| `execute_json(query: str, variables: dict=None, context: dict=None)` |
| `schema_sdl()` |
| `introspect()` |

### PHP — `GraphQL` (`GraphQL.php`)

| Method | 
|--------|
| `addType($name, $fields)` |
| `addQuery($name, $args, $returnType, $resolver)` |
| `addMutation($name, $args, $returnType, $resolver)` |
| `execute($query, $variables = null)` |
| `schemaSdl()` |
| `introspect()` |
| `getTypes()` |
| `getQueries()` |
| `getMutations()` |
| `fromOrm($ormInstance)` |
| `parse()` |
| `peek($offset = 0)` |
| `advance()` |
| `expect($type, $value = null)` |
| `match($type, $value = null)` |

### Ruby — `Tina4` (`graphql.rb`)

| Method | 
|--------|
| `of_type(@of_type
    end

    # Parse a type string like "String", "String!", "[String]", "[Int!]!"
    def self.parse(type_str)` |
| `get_type(name)` |
| `add_query(name, type:, args: {}, description: nil, &resolve)` |
| `add_mutation(name, type:, args: {}, description: nil, &resolve)` |
| `from_orm(klass)` |
| `register_scalars(GraphQLType::SCALARS.each do |s|
        @types[s] = GraphQLType.new(s, :scalar)` |
| `ruby_field_to_gql(field_type)` |
| `parse(document = { kind: :document, definitions: [] }
      while current
        skip(:comma)` |
| `tokenize(src)` |
| `read_string(src, i)` |
| `read_number(src, i)` |
| `current(@tokens[@pos]
    end

    def peek(offset = 0)` |
| `advance(tok = @tokens[@pos]
      @pos += 1
      tok
    end

    def expect(type, value = nil)` |
| `match(type, value = nil)` |
| `skip(type, value = nil)` |
| `parse_definition(tok = current
      if tok.nil?
        raise GraphQLError, "Unexpected end of input"
      end

      if tok.type == :keyword && tok.value == "fragment"
        return parse_fragment
      end

      if tok.type == :keyword && (tok.value == "query" || tok.value == "mutation")` |
| `parse_operation(op = advance.value.to_sym  # :query or :mutation
      name = match(:name)` |
| `parse_variable_definitions(expect(:punct, "(")` |
| `parse_type_ref(if match(:punct, "[")` |
| `parse_selection_set(expect(:punct, "{")` |
| `parse_field(name_tok = expect(:name)` |
| `parse_arguments(expect(:punct, "(")` |
| `parse_value(tok = current
      case tok.type
      when :string
        advance
        tok.value
      when :number
        advance
        tok.value.include?(".")` |
| `parse_list_value(expect(:punct, "[")` |
| `parse_object_value(expect(:punct, "{")` |
| `parse_fragment_spread(expect(:spread)` |
| `parse_fragment(expect(:keyword, "fragment")` |
| `execute(document, variables: {}, context: {}, operation_name: nil)` |
| `resolve_selection(selection, fields, parent, variables, context, fragments, data, errors)` |
| `resolve_field(selection, fields, parent, variables, context, fragments, data, errors)` |
| `item_fields(hash)` |
| `resolve_args(args, variables)` |
| `resolve_value(val, variables)` |
| `resolve_variables(var_defs, provided)` |
| `coerce_value(val)` |
| `schema_sdl(sdl = ""
      @schema.types.each do |name, type_obj|
        sdl += "type #{name} {\n"
        type_obj.fields.each { |f| sdl += "  #{f[:name]}: #{f[:type]}\n" }
        sdl += "}\n\n"
      end
      unless @schema.queries.empty?
        sdl += "type Query {\n"
        @schema.queries.each do |name, config|
          args = (config[:args] || {})` |
| `introspect(queries = @schema.queries.transform_values { |v| { type: v[:type], args: v[:args] || {} } }
      mutations = @schema.mutations.transform_values { |v| { type: v[:type], args: v[:args] || {} } }
      { types: @schema.types.keys, queries: queries, mutations: mutations }
    end

    # Handle an HTTP request body (JSON string)` |
| `handle_request(body, context: {})` |
| `register_route(path = "/graphql")` |
| `graphiql_html(endpoint)` |

### Node — `ParseError` (`core/src/graphql.ts`)

| Method | 
|--------|
| `super(message)` |
| `peek()` |
| `advance()` |
| `expect(type: string, value?: string)` |
| `match(type: string, value?: string)` |
| `parse()` |
| `introspect()` |
| `addType(name: string, fields: Record<string, GraphQLField>)` |
| `addQuery(name: string,
    args: Record<string, string>,
    retur...)` |
| `addMutation(name: string,
    args: Record<string, string>,
    retur...)` |
| `execute(query: string, variables?: Record<string, unknown>)` |
| `schemaSdl()` |
| `fromOrm(modelClass: {
      tableName: string;
      fields: Reco...)` |

## MCP

### Python — `McpServer` (`mcp/__init__.py`)

| Method | 
|--------|
| `register_tool(name: str, handler, description: str='', schema: dict | None=None)` |
| `register_resource(uri: str, handler, description: str='', mime_type: str='application/json')` |
| `handle_message(raw_data: str | dict)` |
| `register_routes(router_module)` |
| `write_claude_config(port: int=7145)` |

### PHP — `McpTool` (`MCP.php`)

| Method | 
|--------|
| `lookupInvoice($invoiceNo)` |
| `getTables()` |
| `encodeResponse($requestId, $result)` |
| `encodeError($requestId, $code, $message, $data = null)` |
| `encodeNotification($method, $params = null)` |
| `decodeRequest($data)` |
| `fromCallable($callable)` |
| `fromReflection($ref)` |
| `getPath()` |
| `getName()` |
| `registerTool($name, $handler, $description = '', $schema = null)` |
| `registerResource($uri, $handler, $description = '', $mimeType = 'application/json')` |
| `registerFromAttributes($object)` |
| `handleMessage($rawData)` |
| `registerRoutes()` |
| `writeClaudeConfig($port = 7146)` |
| `isLocalhost()` |
| `getInstances()` |
| `clearInstances()` |
| `register($server)` |

### Ruby — `Tina4` (`mcp.rb`)

| Method | 
|--------|
| `self.encode_response(request_id, result)` |
| `self.encode_error(request_id, code, message, data = nil)` |
| `self.encode_notification(method, params = nil)` |
| `self.decode_request(data)` |
| `self.schema_from_method(method_obj)` |
| `register_tool(name, handler, description = "", schema = nil)` |
| `register_resource(uri, handler, description = "", mime_type = "application/json")` |
| `handle_message(raw_data)` |
| `register_routes(server   = self
      msg_path = "#{@path}/message"
      sse_path = "#{@path}/sse"

      Tina4::Router.post(msg_path)` |
| `write_claude_config(port = 7145)` |
| `tools(@tools
    end

    # Access registered resources (for testing)` |
| `resources(@resources
    end

    private

    def _handle_initialize(_params)` |
| `self._default_mcp_server(@_default_mcp_server ||= McpServer.new("/__dev/mcp", name: "Tina4 Dev Tools")` |
| `self.mcp_tool(name, description: "", server: nil, &block)` |
| `self.mcp_resource(uri, description: "", mime_type: "application/json", server: nil, &block)` |
| `self.register(server)` |

### Node — `McpServer` (`core/src/mcp.ts`)

| Method | 
|--------|
| `registerTool(name: string,
    handler: (args: Record<string, unknown>)` |
| `registerResource(uri: string,
    handler: ()` |
| `handleMessage(rawData: string | Record<string, unknown>)` |
| `registerRoutes(router: {
    post: (pattern: string, handler: (req: unkn...)` |
| `writeClaudeConfig(port = 7148)` |
| `schemaFromParams([
      { name: "sql", type: "string" },
      { name: "p...)` |

## Frond

### PHP — `Frond` (`Frond.php`)

| Method | 
|--------|
| `render($template, $data = [])` |
| `renderString($source, $data = [], $templateName = null)` |
| `clearCache()` |
| `addFilter($name, $fn)` |
| `addGlobal($name, $value)` |
| `getFilters()` |
| `getGlobals()` |
| `addTest($name, $fn)` |
| `sandbox($filters = null, $tags = null, $vars = null)` |
| `unsandbox()` |
| `renderDump($v)` |

### Ruby — `Tina4` (`frond.rb`)

| Method | 
|--------|
| `render(template, data = {})` |
| `render_string(source, data = {})` |
| `clear_cache(@compiled.clear
      @compiled_strings.clear
      @filter_chain_cache.clear
      @resolve_cache.clear
      @dotted_split_cache.clear
    end

    # Register a custom filter.
    def add_filter(name, &blk)` |
| `add_test(name, &blk)` |
| `add_global(name, value)` |
| `sandbox(filters: nil, tags: nil, vars: nil)` |
| `unsandbox(@sandbox         = false
      @allowed_filters = nil
      @allowed_tags    = nil
      @allowed_vars    = nil
      self
    end

    # Utility: HTML escape
    def self.escape_html(str)` |
| `tokenize(source)` |
| `strip_tag(raw)` |
| `load_template(name)` |
| `execute_cached(tokens, context)` |
| `execute_with_tokens(source, tokens, context)` |
| `execute(source, context)` |
| `extract_blocks(source)` |
| `render_with_blocks(parent_source, context, child_blocks)` |
| `render_tokens(tokens, context)` |
| `eval_var(expr, context)` |
| `eval_var_raw(expr, context)` |
| `eval_var_inner(expr, context)` |
| `eval_filter_arg(arg, context)` |
| `find_outside_quotes(expr, needle)` |
| `find_ternary(expr)` |
| `find_colon(expr)` |
| `parse_filter_chain(expr)` |
| `split_on_pipe(expr)` |
| `parse_args(raw)` |
| `eval_expr(expr, context)` |
| `eval_literal(expr)` |
| `eval_collection_literal(expr, context)` |
| `eval_ternary(expr, context)` |
| `eval_inline_if(expr, context)` |
| `eval_null_coalesce(expr, context)` |
| `eval_concat(expr, context)` |
| `eval_arithmetic(expr, context)` |
| `eval_function_call(expr, context)` |
| `split_args_toplevel(str)` |
| `eval_comparison(expr, context, eval_fn = nil)` |
| `eval_test(value_expr, test_name, args_str, context, eval_fn = nil)` |
| `default_tests({
        "defined"  => ->(v)` |
| `resolve(expr, context)` |
| `apply_math(left, op, right)` |
| `handle_if(tokens, start, context)` |
| `handle_for(tokens, start, context)` |
| `handle_set(content, context)` |
| `handle_include(content, context)` |
| `handle_macro(tokens, start, context)` |
| `handle_from_import(content, context)` |
| `handle_cache(tokens, start, context)` |
| `handle_spaceless(tokens, start, context)` |
| `handle_autoescape(tokens, start, context)` |
| `stringify_keys(hash)` |
| `default_filters({
        # -- Text --
        "upper"      => ->(v, *_a)` |
| `register_builtin_globals(@globals["form_token"] = ->(descriptor = "")` |
| `self.render_dump(value)` |
| `self.generate_form_jwt(descriptor = "")` |
| `self.generate_form_token(descriptor = "")` |
| `self.generate_form_token_value(descriptor = "")` |

## Cache

### Python — `ResponseCache` (`cache/__init__.py`)

| Method | 
|--------|
| `before_cache(request, response)` |
| `after_cache(request, response)` |
| `cache_stats()` |
| `clear_cache()` |

### Python — `Cache` (`core/cache.py`)

| Method | 
|--------|
| `get(key: str, default=None)` |
| `set(key: str, value, ttl: int=None, tags: list[str]=None)` |
| `delete(key: str)` |
| `clear()` |
| `clear_tag(tag: str)` |
| `has(key: str)` |
| `size()` |
| `sweep()` |
| `query_key(sql: str, params: list=None)` |
| `remember(key: str, ttl: int, factory: callable)` |

### PHP — `ResponseCache` (`Middleware/ResponseCache.php`)

| Method | 
|--------|
| `lookup($method, $url)` |
| `store($method, $url, $body, $contentType, $statusCode)` |
| `get($key)` |
| `set($key, $value, $ttl = 0)` |
| `delete($key)` |
| `cacheStats()` |
| `clearCache()` |
| `sweep()` |
| `getBackend()` |

### Ruby — `Tina4` (`response_cache.rb`)

| Method | 
|--------|
| `cache_key(method, url)` |
| `get(method, url)` |
| `cache_response(method, url, status_code, content_type, body, ttl: nil)` |
| `cache_get(key)` |
| `cache_set(key, value, ttl: 0)` |
| `cache_delete(key)` |
| `cache_stats(@mutex.synchronize do
        case @backend_name
        when "memory"
          now = Time.now.to_f
          @store.reject! { |_k, v| v.is_a?(CacheEntry)` |
| `clear_cache(@mutex.synchronize do
        @hits = 0
        @misses = 0

        case @backend_name
        when "memory"
          @store.clear
        when "file"
          Dir.glob(File.join(@cache_dir, "*.json")` |
| `sweep(case @backend_name
      when "memory"
        @mutex.synchronize do
          now = Time.now.to_f
          keys_to_remove = @store.select { |_k, v| v.is_a?(CacheEntry)` |
| `backend_name(@backend_name
    end

    private

    # ── Backend initialization ─────────────────────────────────

    def init_backend
      case @backend_name
      when "redis"
        init_redis
      when "file"
        init_file_dir
      end
    end

    def init_redis
      @redis_client = nil
      begin
        require "redis"
        parsed = parse_redis_url(@cache_url)` |
| `parse_redis_url(url)` |
| `init_file_dir(require "json"
      require "fileutils"
      FileUtils.mkdir_p(@cache_dir)` |
| `backend_get(key)` |
| `backend_set(key, entry, ttl)` |
| `backend_delete(key)` |
| `redis_get(key)` |
| `redis_set(key, entry, ttl)` |
| `redis_delete(key)` |
| `resp_get(key)` |
| `resp_command(*args)` |
| `file_key_path(key)` |
| `file_get(key)` |
| `file_set(key, entry)` |
| `file_delete(key)` |
| `cache_instance(@default_cache ||= ResponseCache.new(ttl: ENV["TINA4_CACHE_TTL"] ? ENV["TINA4_CACHE_TTL"].to_i : 60)` |
| `cache_clear` |

## WebSocket

### Python — `WebSocketConnection` (`websocket/__init__.py`)

| Method | 
|--------|
| `closed()` |
| `async send(message: str | bytes)` |
| `async send_json(data)` |
| `async broadcast(message: str | bytes, exclude_self: bool=False)` |
| `async broadcast_to(path: str, message: str | bytes)` |
| `rooms()` |
| `join_room(room_name: str)` |
| `leave_room(room_name: str)` |
| `async broadcast_to_room(room_name: str, message: str | bytes, exclude_self: bool=False)` |
| `async ping(data: bytes=b'')` |
| `async close(code: int=CLOSE_NORMAL, reason: str='')` |
| `on(event: str, handler: Callable)` |
| `on_message(handler: Callable)` |
| `on_close(handler: Callable)` |
| `on_error(handler: Callable)` |

### Python — `WebSocketManager` (`websocket/__init__.py`)

| Method | 
|--------|
| `add(ws: WebSocketConnection)` |
| `remove(ws: WebSocketConnection)` |
| `get(ws_id: str)` |
| `get_by_path(path: str)` |
| `count()` |
| `count_by_path(path: str)` |
| `async broadcast(path: str, message: str | bytes, exclude: str=None)` |
| `async broadcast_all(message: str | bytes)` |
| `async disconnect(ws_id: str)` |
| `async disconnect_all(path: str=None)` |
| `room_count(room_name: str)` |
| `get_room_connections(room_name: str)` |
| `async broadcast_to_room(room_name: str, message: str | bytes, exclude: str=None)` |

### Python — `WebSocketServer` (`websocket/__init__.py`)

| Method | 
|--------|
| `route(path: str)` |
| `on_connect(path: str)` |
| `on_disconnect(path: str)` |
| `async handle_connection(reader: asyncio.StreamReader, writer: asyncio.StreamWriter)` |
| `async start()` |
| `async stop()` |
| `handle_upgrade(reader: asyncio.StreamReader, writer: asyncio.StreamWriter)` |

### Python — `WSDL` (`wsdl/__init__.py`)

| Method | 
|--------|
| `handle()` |
| `generate_wsdl()` |
| `on_request(request)` |
| `on_result(result)` |

### PHP — `Calculator` (`WSDL.php`)

| Method | 
|--------|
| `Add($a, $b)` |
| `handle()` |

### PHP — `WebSocket` (`WebSocket.php`)

| Method | 
|--------|
| `on($event, $handler)` |
| `broadcast($message, $excludeIds = null, $path = null)` |
| `send($clientId, $message)` |
| `joinRoom($clientId, $roomName)` |
| `leaveRoom($clientId, $roomName)` |
| `getRoomConnections($roomName)` |
| `roomCount($roomName)` |
| `broadcastToRoom($roomName, $message, $excludeIds = null)` |
| `start()` |
| `getClients()` |
| `stop()` |
| `getPort()` |
| `computeAcceptKey($key)` |
| `buildHandshakeResponse($key)` |
| `parseHttpHeaders($data)` |
| `encodeFrame($message, $opcode = self::OP_TEXT)` |
| `decodeFrame($data)` |

### PHP — `at` (`WebSocketBackplane.php`)

| Method | 
|--------|
| `publish($channel, $message)` |
| `subscribe($channel, $callback)` |
| `unsubscribe($channel)` |
| `close()` |
| `publish($channel, $message)` |
| `subscribe($channel, $callback)` |
| `unsubscribe($channel)` |
| `close()` |
| `publish($channel, $message)` |
| `subscribe($channel, $callback)` |
| `unsubscribe($channel)` |
| `close()` |
| `create($url = null)` |

### PHP — `WebSocketConnection` (`WebSocketConnection.php`)

| Method | 
|--------|
| `send($message)` |
| `broadcast($message, $includeSelf = false)` |
| `close($code = WebSocket::CLOSE_NORMAL, $reason = '')` |
| `getSocket()` |

### Ruby — `Tina4` (`websocket.rb`)

| Method | 
|--------|
| `handle_upgrade(env, socket)` |
| `broadcast(message, exclude: nil, path: nil)` |
| `join_room_for(conn_id, room_name)` |
| `leave_room_for(conn_id, room_name)` |
| `room_count(room_name)` |
| `get_room_connections(room_name)` |
| `broadcast_to_room(room_name, message, exclude: nil)` |
| `emit(event, *args)` |
| `remove_from_all_rooms(conn_id)` |
| `join_room(room_name)` |
| `leave_room(room_name)` |
| `send(message)` |
| `send_pong(data)` |
| `close(code: 1000, reason: "")` |
| `read_frame(first_byte = @socket.getbyte
      return nil unless first_byte

      opcode = first_byte & 0x0F
      second_byte = @socket.getbyte
      return nil unless second_byte

      masked = (second_byte & 0x80)` |
| `build_frame(opcode, data)` |

### Ruby — `Tina4` (`websocket_backplane.rb`)

| Method | 
|--------|
| `publish(channel, message)` |
| `subscribe(channel, &block)` |
| `unsubscribe(channel)` |
| `close(raise NotImplementedError, "#{self.class}#close not implemented"
    end

    # Factory that reads TINA4_WS_BACKPLANE and returns the appropriate
    # backplane instance, or +nil+ if no backplane is configured.
    #
    # This keeps backplane usage entirely optional — callers simply check
    # +if backplane+ before publishing.
    def self.create(url: nil)` |

### Ruby — `Tina4` (`wsdl.rb`)

| Method | 
|--------|
| `handle(return generate_wsdl if @request.nil?

      method = if @request.respond_to?(:method)` |
| `on_request(request)` |
| `on_result(result)` |
| `generate_wsdl(service_name = self.class.name ? self.class.name.split("::")` |
| `discover_operations(self.class.wsdl_operations.dup
    end

    def infer_url
      return @request.url if @request && @request.respond_to?(:url)` |
| `process_soap(xml_body)` |
| `find_child(parent, local)` |
| `local_name(element)` |
| `convert_value(value, target_type)` |
| `soap_response(op_name, result)` |
| `soap_fault(code, message)` |
| `escape_xml(s)` |
| `xsd_type(ruby_type)` |

### Node — `WebSocketServer` (`core/src/websocket.ts`)

| Method | 
|--------|
| `on(event: string, handler: Function)` |
| `broadcast(message: string, excludeIds?: string[], path?: string)` |
| `send(clientId: string, message: string)` |
| `start()` |
| `stop()` |
| `getClients()` |
| `joinRoom(clientId: string, roomName: string)` |
| `leaveRoom(clientId: string, roomName: string)` |
| `getRoomConnections(roomName: string)` |
| `roomCount(roomName: string)` |
| `getClientRooms(clientId: string)` |
| `broadcastToRoom(roomName: string, message: string, excludeIds?: string[])` |
| `setBuffer(remaining)` |

### Node — `RedisBackplane` (`core/src/websocketBackplane.ts`)

| Method | 
|--------|
| `publish(channel: string, message: string)` |
| `subscribe(channel: string, callback: (message: string)` |
| `unsubscribe(channel: string)` |
| `close()` |

### Node — `WSDLService` (`core/src/wsdl.ts`)

| Method | 
|--------|
| `generateWSDL(endpointUrl?: string)` |
| `handleRequest(soapXml: string)` |
| `register(router: {
    addRoute?: (method: string, path: string, h...)` |

## Events

### PHP — `Events` (`Events.php`)

| Method | 
|--------|
| `on($event, $callback, $priority = 0)` |
| `once($event, $callback, $priority = 0)` |
| `off($event, $callback = null)` |
| `emit($event, mixed ...$args)` |
| `listeners($event)` |
| `events()` |
| `emitAsync($event, mixed ...$args)` |
| `clear()` |

### Node — `Events` (`core/src/events.ts`)

| Method | 
|--------|
| `on(event: string, callback: (...args: unknown[])` |
| `once(event: string, callback: (...args: unknown[])` |
| `off(event: string, callback?: (...args: unknown[])` |
| `emit(event: string, ...args: unknown[])` |
| `emitAsync(event: string, ...args: unknown[])` |
| `listeners(event: string)` |
| `events()` |
| `clear()` |

## Misc

### Python — `Api` (`api/__init__.py`)

| Method | 
|--------|
| `add_headers(headers: dict[str, str])` |
| `set_basic_auth(username: str, password: str)` |
| `set_bearer_token(token: str)` |
| `get(path: str='', params: dict=None)` |
| `post(path: str='', body=None, content_type: str='application/json')` |
| `put(path: str='', body=None, content_type: str='application/json')` |
| `patch(path: str='', body=None, content_type: str='application/json')` |
| `delete(path: str='', body=None)` |
| `send(method: str, path: str='', body=None, content_type: str='application/json')` |

### Python — `Container` (`container/__init__.py`)

| Method | 
|--------|
| `register(name: str, factory: callable)` |
| `singleton(name: str, factory: callable)` |
| `get(name: str)` |
| `has(name: str)` |
| `reset()` |

### Python — `CorsMiddleware` (`core/middleware.py`)

| Method | 
|--------|
| `allowed_origin(request_origin: str)` |
| `apply(request, response)` |
| `is_preflight(request)` |

### Python — `RateLimiter` (`core/middleware.py`)

| Method | 
|--------|
| `check(ip: str)` |
| `apply_headers(response, info: dict)` |

### Python — `SecurityHeadersMiddleware` (`core/middleware.py`)

| Method | 
|--------|
| `before_security(request, response)` |

### Python — `CsrfMiddleware` (`core/middleware.py`)

| Method | 
|--------|
| `before_csrf(request, response)` |

### Python — `Request` (`core/request.py`)

| Method | 
|--------|
| `from_scope(scope: dict, body: bytes=b'')` |
| `merge_route_params()` |
| `param(key: str, default=None)` |

### Python — `Response` (`core/response.py`)

| Method | 
|--------|
| `status(code: int)` |
| `header(name: str, value: str)` |
| `cookie(name: str, value: str, path: str='/', max_age: int=3600, http_only: bool=True, secure: bool=False, same_site: str='Lax')` |
| `stream(source, content_type: str='text/event-stream')` |
| `json(data, status_code: int=None)` |
| `html(content: str, status_code: int=None)` |
| `text(content: str, status_code: int=None)` |
| `error(code: str, message: str, status_code: int=400)` |
| `xml(content: str, status_code: int=None)` |
| `redirect(url: str, status_code: int=302)` |
| `file(file_path: str, download_name: str=None)` |
| `render(template: str, data: dict=None)` |
| `template(template: str, data: dict=None)` |
| `build_headers(accept_encoding: str='')` |

### Python — `AutoCrud` (`crud/__init__.py`)

| Method | 
|--------|
| `register(model_class, prefix: str='/api')` |
| `discover(models_dir: str='src/orm', prefix: str='/api')` |
| `models()` |
| `clear()` |

### Python — `DatabaseResult` (`database/adapter.py`)

| Method | 
|--------|
| `to_list()` |
| `to_paginate(page: int=1, per_page: int=20)` |
| `column_info()` |

### Python — `DatabaseAdapter` (`database/adapter.py`)

| Method | 
|--------|
| `autocommit()` |
| `autocommit(value: bool)` |
| `connect(connection_string: str, username: str='', password: str='', **kwargs)` |
| `close()` |
| `execute(sql: str, params: list=None)` |
| `execute_many(sql: str, params_list: list[list]=None)` |
| `fetch(sql: str, params: list=None, limit: int=100, offset: int=0)` |
| `fetch_one(sql: str, params: list=None)` |
| `insert(table: str, data: dict | list)` |
| `update(table: str, data: dict, filter_sql: str='', params: list=None)` |
| `delete(table: str, filter_sql: str | dict | list='', params: list=None)` |
| `start_transaction()` |
| `commit()` |
| `rollback()` |
| `table_exists(name: str)` |
| `get_tables()` |
| `get_columns(table: str)` |
| `get_database_type()` |

### Python — `SQLTranslator` (`database/adapter.py`)

| Method | 
|--------|
| `limit_to_rows(sql: str)` |
| `limit_to_top(sql: str)` |
| `concat_pipes_to_func(sql: str)` |
| `boolean_to_int(sql: str)` |
| `ilike_to_like(sql: str)` |
| `auto_increment_syntax(sql: str, engine: str)` |
| `placeholder_style(sql: str, style: str='?')` |

### Python — `ConnectionPool` (`database/connection.py`)

| Method | 
|--------|
| `checkout()` |
| `checkin(adapter: DatabaseAdapter)` |
| `close_all()` |
| `size()` |
| `active_count()` |

### Python — `Database` (`database/connection.py`)

| Method | 
|--------|
| `cache_stats()` |
| `cache_clear()` |
| `close()` |
| `get_error()` |
| `get_last_id()` |
| `execute(sql: str, params: list=None)` |
| `execute_many(sql: str, params_list: list[list]=None)` |
| `fetch(sql: str, params: list=None, limit: int=100, offset: int=0)` |
| `fetch_one(sql: str, params: list=None)` |
| `insert(table: str, data: dict | list)` |
| `update(table: str, data: dict, filter_sql: str='', params: list=None)` |
| `delete(table: str, filter_sql: str | dict | list='', params: list=None)` |
| `start_transaction()` |
| `commit()` |
| `rollback()` |
| `table_exists(name: str)` |
| `get_tables()` |
| `get_columns(table: str)` |
| `get_database_type()` |
| `autocommit()` |
| `autocommit(value: bool)` |
| `get_next_id(table: str, pk_column: str='id', generator_name: str=None)` |
| `register_function(name: str, num_params: int, func: callable, deterministic: bool=True)` |
| `adapter()` |
| `pool()` |
| `create(url: str, username: str='', password: str='', pool: int=0)` |
| `from_env(env_key: str='DATABASE_URL', pool: int=0)` |
| `get_adapter()` |
| `pool_size()` |
| `active_count()` |
| `checkout()` |
| `checkin(adapter: DatabaseAdapter)` |
| `close_all()` |

### Python — `FirebirdAdapter` (`database/firebird.py`)

| Method | 
|--------|
| `connect(connection_string: str, username: str='', password: str='', **kwargs)` |
| `close()` |
| `execute(sql: str, params: list=None)` |
| `fetch(sql: str, params: list=None, limit: int=100, offset: int=0)` |
| `fetch_one(sql: str, params: list=None)` |
| `insert(table: str, data: dict)` |
| `update(table: str, data: dict, filter_sql: str='', params: list=None)` |
| `delete(table: str, filter_sql: str='', params: list=None)` |
| `start_transaction()` |
| `commit()` |
| `rollback()` |
| `table_exists(name: str)` |
| `get_tables()` |
| `get_columns(table: str)` |
| `get_database_type()` |

### Python — `MSSQLAdapter` (`database/mssql.py`)

| Method | 
|--------|
| `connect(connection_string: str, username: str='', password: str='', **kwargs)` |
| `close()` |
| `execute(sql: str, params: list=None)` |
| `fetch(sql: str, params: list=None, limit: int=100, offset: int=0)` |
| `fetch_one(sql: str, params: list=None)` |
| `insert(table: str, data: dict)` |
| `update(table: str, data: dict, filter_sql: str='', params: list=None)` |
| `delete(table: str, filter_sql: str='', params: list=None)` |
| `start_transaction()` |
| `commit()` |
| `rollback()` |
| `table_exists(name: str)` |
| `get_tables()` |
| `get_columns(table: str)` |
| `get_database_type()` |

### Python — `MySQLAdapter` (`database/mysql.py`)

| Method | 
|--------|
| `connect(connection_string: str, username: str='', password: str='', **kwargs)` |
| `close()` |
| `execute(sql: str, params: list=None)` |
| `fetch(sql: str, params: list=None, limit: int=100, offset: int=0)` |
| `fetch_one(sql: str, params: list=None)` |
| `insert(table: str, data: dict)` |
| `update(table: str, data: dict, filter_sql: str='', params: list=None)` |
| `delete(table: str, filter_sql: str='', params: list=None)` |
| `start_transaction()` |
| `commit()` |
| `rollback()` |
| `table_exists(name: str)` |
| `get_tables()` |
| `get_columns(table: str)` |
| `get_database_type()` |

### Python — `PostgreSQLAdapter` (`database/postgres.py`)

| Method | 
|--------|
| `connect(connection_string: str, username: str='', password: str='', **kwargs)` |
| `close()` |
| `execute(sql: str, params: list=None)` |
| `fetch(sql: str, params: list=None, limit: int=100, offset: int=0)` |
| `fetch_one(sql: str, params: list=None)` |
| `insert(table: str, data: dict)` |
| `update(table: str, data: dict, filter_sql: str='', params: list=None)` |
| `delete(table: str, filter_sql: str='', params: list=None)` |
| `start_transaction()` |
| `commit()` |
| `rollback()` |
| `table_exists(name: str)` |
| `get_tables()` |
| `get_columns(table: str)` |
| `get_database_type()` |

### Python — `SQLiteAdapter` (`database/sqlite.py`)

| Method | 
|--------|
| `connect(connection_string: str, username: str='', password: str='', **kwargs)` |
| `close()` |
| `execute(sql: str, params: list=None)` |
| `execute_many(sql: str, params_list: list[list]=None)` |
| `fetch(sql: str, params: list=None, limit: int=100, offset: int=0)` |
| `fetch_one(sql: str, params: list=None)` |
| `insert(table: str, data: dict)` |
| `update(table: str, data: dict, filter_sql: str='', params: list=None)` |
| `delete(table: str, filter_sql: str='', params: list=None)` |
| `start_transaction()` |
| `commit()` |
| `rollback()` |
| `table_exists(name: str)` |
| `get_tables()` |
| `get_columns(table: str)` |
| `get_database_type()` |
| `register_function(name: str, num_params: int, func: callable, deterministic: bool=True)` |

### Python — `Log` (`debug/__init__.py`)

| Method | 
|--------|
| `init(log_dir: str='logs', level: str='info', production: bool=False)` |
| `debug(message: str, **kwargs)` |
| `info(message: str, **kwargs)` |
| `warning(message: str, **kwargs)` |
| `error(message: str, **kwargs)` |

### Python — `Frond` (`frond/engine.py`)

| Method | 
|--------|
| `sandbox(allowed_filters: list[str]=None, allowed_tags: list[str]=None, allowed_vars: list[str]=None)` |
| `unsandbox()` |
| `add_filter(name: str, fn)` |
| `add_global(name: str, value)` |
| `add_test(name: str, fn)` |
| `render(template: str, data: dict=None)` |
| `render_string(source: str, data: dict=None)` |
| `clear_cache()` |

### Python — `I18n` (`i18n/__init__.py`)

| Method | 
|--------|
| `locale()` |
| `locale(value: str)` |
| `t(key: str, **kwargs)` |
| `available_locales()` |

### Python — `Messenger` (`messenger/__init__.py`)

| Method | 
|--------|
| `add_header(name: str, value: str)` |
| `send(to: str | list[str], subject: str, body: str, html: bool=False, text: str=None, cc: str | list[str]=None, bcc: str | list[str]=None, reply_to: str=None, attachments: list=None, headers: dict=None)` |
| `send_template(to: str | list[str], subject: str, template: str, data: dict=None, **kwargs)` |
| `inbox(folder: str='INBOX', limit: int=20, offset: int=0)` |
| `unread(folder: str='INBOX')` |
| `read(uid: str | bytes, folder: str='INBOX', mark_read: bool=True)` |
| `search(folder: str='INBOX', subject: str=None, sender: str=None, since: str=None, before: str=None, unseen_only: bool=False, limit: int=50)` |
| `mark_read(uid: str | bytes, folder: str='INBOX')` |
| `mark_unread(uid: str | bytes, folder: str='INBOX')` |
| `delete(uid: str | bytes, folder: str='INBOX')` |
| `folders()` |
| `test_connection()` |
| `test_imap_connection()` |

### Python — `DevMailbox` (`messenger/__init__.py`)

| Method | 
|--------|
| `capture(to: str | list[str], subject: str, body: str, html: bool=False, cc: list[str]=None, bcc: list[str]=None, reply_to: str=None, from_address: str='', from_name: str='', attachments: list=None)` |
| `inbox(limit: int=50, offset: int=0, folder: str=None)` |
| `read(msg_id: str)` |
| `unread_count()` |
| `delete(msg_id: str)` |
| `clear(folder: str=None)` |
| `seed(count: int=5, seed: int=None)` |
| `count(folder: str=None)` |

### Python — `MigrationBase` (`migration/runner.py`)

| Method | 
|--------|
| `up(db)` |
| `down(db)` |

### Python — `Migration` (`migration/runner.py`)

| Method | 
|--------|
| `migrate()` |
| `rollback(steps: int=1)` |
| `status()` |
| `create(description: str, kind: str='sql')` |
| `get_applied()` |
| `get_pending()` |
| `get_files()` |
| `record_migration(name: str, batch: int, passed: int=1)` |
| `remove_migration_record(name: str)` |

### Python — `Field` (`orm/fields.py`)

| Method | 
|--------|
| `validate(value)` |

### Python — `QueryBuilder` (`query_builder/__init__.py`)

| Method | 
|--------|
| `from_table(table_name: str, db=None)` |
| `select(*columns)` |
| `where(condition: str, params: list=None)` |
| `or_where(condition: str, params: list=None)` |
| `join(table: str, on_clause: str)` |
| `left_join(table: str, on_clause: str)` |
| `group_by(column: str)` |
| `having(expression: str, params: list=None)` |
| `order_by(expression: str)` |
| `limit(count: int, offset: int=None)` |
| `to_sql()` |
| `get()` |
| `first()` |
| `count()` |
| `exists()` |
| `to_mongo()` |

### Python — `Job` (`queue/job.py`)

| Method | 
|--------|
| `data()` |
| `complete()` |
| `fail(error: str='')` |
| `reject(reason: str='')` |
| `retry(delay_seconds: int=0)` |
| `to_array()` |
| `to_hash()` |
| `to_json()` |

### Python — `KafkaBackend` (`queue/kafka_backend.py`)

| Method | 
|--------|
| `push(data: dict, priority: int=0, delay_seconds: int=0)` |
| `pop(queue_ref)` |
| `size(status: str='pending')` |
| `purge(status: str='completed')` |
| `retry_failed()` |
| `failed()` |
| `dead_letters()` |
| `retry_job(job_id: str, delay_seconds: int=0)` |
| `clear()` |
| `complete(job: Job)` |
| `fail(job: Job, error: str='')` |
| `retry(job: Job, delay_seconds: int=0)` |

### Python — `LiteBackend` (`queue/lite_backend.py`)

| Method | 
|--------|
| `push(data: dict, priority: int=0, delay_seconds: int=0)` |
| `pop(queue_ref)` |
| `pop_batch(count: int, queue_ref)` |
| `size(status: str='pending')` |
| `purge(status: str='completed')` |
| `retry_failed(max_retries: int=None)` |
| `failed()` |
| `dead_letters(max_retries: int=None)` |
| `retry_job(job_id: str, delay_seconds: int=0)` |
| `clear()` |
| `complete(job: Job)` |
| `fail(job: Job, error: str='')` |
| `retry(job: Job, delay_seconds: int=0)` |

### Python — `MongoBackend` (`queue/mongo_backend.py`)

| Method | 
|--------|
| `push(data: dict, priority: int=0, delay_seconds: int=0)` |
| `pop(queue_ref)` |
| `size(status: str='pending')` |
| `purge(status: str='completed')` |
| `retry_failed()` |
| `failed()` |
| `dead_letters()` |
| `retry_job(job_id: str, delay_seconds: int=0)` |
| `clear()` |
| `complete(job: Job)` |
| `fail(job: Job, error: str='')` |
| `retry(job: Job, delay_seconds: int=0)` |

### Python — `RabbitMQBackend` (`queue/rabbitmq_backend.py`)

| Method | 
|--------|
| `push(data: dict, priority: int=0, delay_seconds: int=0)` |
| `pop(queue_ref)` |
| `size(status: str='pending')` |
| `purge(status: str='completed')` |
| `retry_failed()` |
| `failed()` |
| `dead_letters()` |
| `retry_job(job_id: str, delay_seconds: int=0)` |
| `clear()` |
| `complete(job: Job)` |
| `fail(job: Job, error: str='')` |
| `retry(job: Job, delay_seconds: int=0)` |

### Python — `KafkaConnector` (`queue_backends/kafka_backend.py`)

| Method | 
|--------|
| `connect()` |
| `enqueue(topic: str, message: dict)` |
| `dequeue(topic: str)` |
| `acknowledge(topic: str, message_id: str)` |
| `reject(topic: str, message_id: str, requeue: bool=True)` |
| `size(topic: str)` |
| `clear(topic: str)` |
| `dead_letter(topic: str, message: dict)` |
| `close()` |

### Python — `MongoConnector` (`queue_backends/mongo_backend.py`)

| Method | 
|--------|
| `connect()` |
| `enqueue(topic: str, message: dict)` |
| `dequeue(topic: str)` |
| `acknowledge(topic: str, message_id: str)` |
| `reject(topic: str, message_id: str, requeue: bool=True)` |
| `size(topic: str)` |
| `clear(topic: str)` |
| `dead_letter(topic: str, message: dict)` |
| `close()` |

### Python — `RabbitMQConnector` (`queue_backends/rabbitmq_backend.py`)

| Method | 
|--------|
| `connect()` |
| `enqueue(topic: str, message: dict)` |
| `dequeue(topic: str)` |
| `acknowledge(topic: str, message_id: str)` |
| `reject(topic: str, message_id: str, requeue: bool=True)` |
| `size(topic: str)` |
| `clear(topic: str)` |
| `dead_letter(topic: str, message: dict)` |
| `close()` |

### Python — `FakeData` (`seeder/__init__.py`)

| Method | 
|--------|
| `seed(seed: int)` |
| `name()` |
| `first_name()` |
| `last_name()` |
| `email()` |
| `phone()` |
| `integer(min_val: int=0, max_val: int=10000)` |
| `decimal(min_val: float=0.0, max_val: float=1000.0, decimals: int=2)` |
| `boolean()` |
| `word()` |
| `sentence(words: int=8)` |
| `paragraph(sentences: int=4)` |
| `text(paragraphs: int=3)` |
| `date(start_year: int=2020, end_year: int=2025)` |
| `datetime_iso()` |
| `uuid()` |
| `url()` |
| `address()` |
| `color_hex()` |
| `choice(items: list)` |
| `sample(items: list, k: int)` |
| `alphanumeric(length: int=10)` |

### Python — `ServiceRunner` (`service/__init__.py`)

| Method | 
|--------|
| `register(name: str, handler: callable, interval: int=60, cron: str=None, daemon: bool=False, max_retries: int=3)` |
| `start()` |
| `stop()` |
| `status()` |
| `discover(service_dir: str='')` |

### Python — `RedisSessionHandler` (`session_handlers/redis_handler.py`)

| Method | 
|--------|
| `read(session_id: str)` |
| `write(session_id: str, data: dict, ttl: int=0)` |
| `destroy(session_id: str)` |
| `gc(max_lifetime: int)` |
| `close()` |

### Python — `ValkeySessionHandler` (`session_handlers/valkey_handler.py`)

| Method | 
|--------|
| `read(session_id: str)` |
| `write(session_id: str, data: dict, ttl: int=0)` |
| `destroy(session_id: str)` |
| `gc(max_lifetime: int)` |
| `close()` |

### Python — `Swagger` (`swagger/__init__.py`)

| Method | 
|--------|
| `generate(routes: list[dict])` |
| `generate_json(routes: list[dict])` |

### Python — `TestResponse` (`test_client/__init__.py`)

| Method | 
|--------|
| `json()` |
| `text()` |

### Python — `TestClient` (`test_client/__init__.py`)

| Method | 
|--------|
| `get(path: str, headers)` |
| `post(path: str, json, body, headers)` |
| `put(path: str, json, body, headers)` |
| `patch(path: str, json, body, headers)` |
| `delete(path: str, headers)` |

### Python — `Validator` (`validator/__init__.py`)

| Method | 
|--------|
| `required(*fields)` |
| `email(field: str)` |
| `min_length(field: str, length: int)` |
| `max_length(field: str, length: int)` |
| `integer(field: str)` |
| `min(field: str, minimum)` |
| `max(field: str, maximum)` |
| `in_list(field: str, allowed: list)` |
| `regex(field: str, pattern: str)` |
| `errors()` |
| `is_valid()` |

### Python — `WebSocketBackplane` (`websocket/backplane.py`)

| Method | 
|--------|
| `publish(channel: str, message: str)` |
| `subscribe(channel: str, callback)` |
| `unsubscribe(channel: str)` |
| `close()` |

### Python — `RedisBackplane` (`websocket/backplane.py`)

| Method | 
|--------|
| `publish(channel: str, message: str)` |
| `subscribe(channel: str, callback)` |
| `unsubscribe(channel: str)` |
| `close()` |

### Python — `NATSBackplane` (`websocket/backplane.py`)

| Method | 
|--------|
| `publish(channel: str, message: str)` |
| `subscribe(channel: str, callback)` |
| `unsubscribe(channel: str)` |
| `close()` |

### PHP — `AI` (`AI.php`)

| Method | 
|--------|
| `isInstalled($root, $tool)` |
| `showMenu($root = ".")` |
| `installSelected($root, $selection)` |
| `installAll($root = ".")` |
| `generateContext($toolName = 'claude-code')` |

### PHP — `Api` (`Api.php`)

| Method | 
|--------|
| `addCustomHeaders($headers)` |
| `setBearerToken($token)` |
| `setBasicAuth($username, $password)` |
| `get($path = '', $params = [])` |
| `post($path = '', $body = null)` |
| `put($path = '', $body = null)` |
| `patch($path = '', $body = null)` |
| `delete($path = '')` |
| `sendRequest($path = '', $method = 'GET', $body = null, $contentType = 'application/json')` |

### PHP — `App` (`App.php`)

| Method | 
|--------|
| `__destruct()` |
| `get($path, $handler)` |
| `post($path, $handler)` |
| `put($path, $handler)` |
| `delete($path, $handler)` |
| `patch($path, $handler)` |
| `addMiddleware($middleware)` |
| `onShutdown($callback)` |
| `getHealthData()` |
| `getStartTime()` |
| `isRunning()` |
| `getRoutes()` |
| `getMiddleware()` |
| `shutdown()` |
| `start()` |
| `isDevelopment()` |
| `run($host = '0.0.0.0', $port = 7145)` |
| `__invoke($request = null)` |
| `handle()` |
| `setDatabase($db)` |
| `getDatabase()` |
| `createDatabase($url, $autoCommit = null)` |

### PHP — `AutoCrud` (`AutoCrud.php`)

| Method | 
|--------|
| `register($modelClass)` |
| `discover($modelsDir)` |
| `generateRoutes()` |
| `getModels()` |

### PHP — `Container` (`Container.php`)

| Method | 
|--------|
| `register($name, $factory)` |
| `singleton($name, $factory)` |
| `get($name)` |
| `has($name)` |
| `reset()` |

### PHP — `FirebirdAdapter` (`Database/FirebirdAdapter.php`)

| Method | 
|--------|
| `open()` |
| `close()` |
| `query($sql, $params = [])` |
| `fetch($sql, $params = [], $limit = 100, $offset = 0)` |
| `fetchOne($sql, $params = [])` |
| `execute($sql, $params = [])` |
| `executeMany($sql, $paramsList = [])` |
| `insert($table, $data)` |
| `update($table, $data, $where = '', $whereParams = [])` |
| `delete($table, $filter = '', $whereParams = [])` |
| `tableExists($table)` |
| `getColumns($table)` |
| `getTables()` |
| `lastInsertId()` |
| `startTransaction()` |
| `commit()` |
| `rollback()` |
| `error()` |
| `getConnection()` |
| `getDatabase()` |

### PHP — `MSSQLAdapter` (`Database/MSSQLAdapter.php`)

| Method | 
|--------|
| `open()` |
| `close()` |
| `query($sql, $params = [])` |
| `fetch($sql, $params = [], $limit = 100, $offset = 0)` |
| `fetchOne($sql, $params = [])` |
| `execute($sql, $params = [])` |
| `executeMany($sql, $paramsList = [])` |
| `insert($table, $data)` |
| `update($table, $data, $where = '', $whereParams = [])` |
| `delete($table, $filter = '', $whereParams = [])` |
| `tableExists($table)` |
| `getColumns($table)` |
| `getTables()` |
| `lastInsertId()` |
| `startTransaction()` |
| `commit()` |
| `rollback()` |
| `error()` |
| `getConnection()` |
| `getDatabase()` |

### PHP — `MySQLAdapter` (`Database/MySQLAdapter.php`)

| Method | 
|--------|
| `open()` |
| `close()` |
| `query($sql, $params = [])` |
| `fetch($sql, $params = [], $limit = 100, $offset = 0)` |
| `fetchOne($sql, $params = [])` |
| `execute($sql, $params = [])` |
| `executeMany($sql, $paramsList = [])` |
| `insert($table, $data)` |
| `update($table, $data, $where = '', $whereParams = [])` |
| `delete($table, $filter = '', $whereParams = [])` |
| `tableExists($table)` |
| `getColumns($table)` |
| `getTables()` |
| `lastInsertId()` |
| `startTransaction()` |
| `commit()` |
| `rollback()` |
| `error()` |
| `getConnection()` |
| `getDatabase()` |

### PHP — `PostgresAdapter` (`Database/PostgresAdapter.php`)

| Method | 
|--------|
| `open()` |
| `close()` |
| `query($sql, $params = [])` |
| `fetch($sql, $params = [], $limit = 100, $offset = 0)` |
| `fetchOne($sql, $params = [])` |
| `execute($sql, $params = [])` |
| `executeMany($sql, $paramsList = [])` |
| `insert($table, $data)` |
| `update($table, $data, $where = '', $whereParams = [])` |
| `delete($table, $filter = '', $whereParams = [])` |
| `tableExists($table)` |
| `getColumns($table)` |
| `getTables()` |
| `lastInsertId()` |
| `startTransaction()` |
| `commit()` |
| `rollback()` |
| `error()` |
| `getConnection()` |
| `getDatabase()` |

### PHP — `SQLite3Adapter` (`Database/SQLite3Adapter.php`)

| Method | 
|--------|
| `open()` |
| `close()` |
| `query($sql, $params = [])` |
| `fetch($sql, $params = [], $limit = 100, $offset = 0)` |
| `exec($sql, $params = [])` |
| `execute($sql, $params = [])` |
| `executeMany($sql, $paramsList = [])` |
| `fetchOne($sql, $params = [])` |
| `insert($table, $data)` |
| `update($table, $data, $where = '', $whereParams = [])` |
| `delete($table, $filter = '', $whereParams = [])` |
| `getTables()` |
| `startTransaction()` |
| `tableExists($table)` |
| `getColumns($table)` |
| `lastInsertId()` |
| `begin()` |
| `commit()` |
| `rollback()` |
| `error()` |
| `getConnection()` |
| `getDatabase()` |

### PHP — `DevAdmin` (`DevAdmin.php`)

| Method | 
|--------|
| `register()` |
| `renderToolbar($method = 'GET', $path = '/', $matchedPattern = '', $requestId = '', $routeCount = 0)` |
| `renderDashboard()` |
| `log($category, $level, $message)` |
| `get($category = null)` |
| `clear($category = null)` |
| `count()` |
| `reset()` |
| `capture($method, $path, $status, $duration)` |
| `get($limit = 50)` |
| `stats()` |
| `clear()` |
| `reset()` |
| `capture($errorType, $message, $traceback = '', $file = '', $line = 0)` |
| `get($includeResolved = true)` |
| `unresolvedCount()` |
| `resolve($id)` |
| `clearResolved()` |
| `clearAll()` |
| `register()` |
| `reset()` |

### PHP — `DevMailbox` (`DevMailbox.php`)

| Method | 
|--------|
| `capture($to, $subject, $body, $html = false, $cc = [], $bcc = [], $replyTo = null, $attachments = [], $headers = [])` |
| `inbox($limit = 50, $offset = 0, $folder = null)` |
| `read($msgId)` |
| `unreadCount()` |
| `delete($msgId)` |
| `clear($folder = null)` |
| `seed($count = 5)` |
| `count($folder = null)` |
| `getMailboxDir()` |

### PHP — `DotEnv` (`DotEnv.php`)

| Method | 
|--------|
| `loadEnv($path = '.env', $overwrite = false)` |
| `getEnv($key, $default = null)` |
| `requireEnv($key)` |
| `hasEnv($key)` |
| `resetEnv()` |
| `allEnv()` |
| `isTruthy($val)` |

### PHP — `ErrorOverlay` (`ErrorOverlay.php`)

| Method | 
|--------|
| `render($e, $request = null)` |
| `renderProduction($statusCode = 500, $message = 'Internal Server Error', $path = '')` |
| `isDebugMode()` |

### PHP — `FakeData` (`FakeData.php`)

| Method | 
|--------|
| `seed($seed)` |
| `firstName()` |
| `lastName()` |
| `fullName()` |
| `email()` |
| `phone()` |
| `address()` |
| `city()` |
| `country()` |
| `zipCode()` |
| `company()` |
| `jobTitle()` |
| `paragraph($sentences = 3)` |
| `sentence($words = 8)` |
| `word()` |
| `integer($min = 0, $max = 1000)` |
| `float($min = 0, $max = 1000, $decimals = 2)` |
| `boolean()` |
| `date($start = '2020-01-01', $end = '2025-12-31')` |
| `uuid()` |
| `url()` |
| `ipAddress()` |
| `color()` |
| `hexColor()` |
| `creditCard()` |
| `currency()` |
| `seedDir($seedDir = 'src/seeds')` |
| `run($seeder, $count = 10)` |

### PHP — `HtmlElement` (`HtmlElement.php`)

| Method | 
|--------|
| `__invoke(mixed ...$children)` |
| `__toString()` |
| `helpers()` |

### PHP — `I18n` (`I18n.php`)

| Method | 
|--------|
| `setLocale($locale)` |
| `getLocale()` |
| `translate($key, $params = [], $locale = null)` |
| `t($key, $params = [], $locale = null)` |
| `loadTranslations($locale)` |
| `addTranslation($locale, $key, $value)` |
| `getAvailableLocales()` |

### PHP — `Job` (`Job.php`)

| Method | 
|--------|
| `complete()` |
| `fail($reason = '')` |
| `reject($reason = '')` |
| `retry($delaySeconds = 0)` |
| `toArray()` |
| `toHash()` |
| `toJson()` |

### PHP — `Log` (`Log.php`)

| Method | 
|--------|
| `configure($logDir = 'logs', $development = false, $minLevel = self::LEVEL_DEBUG)` |
| `setRequestId($requestId)` |
| `getRequestId()` |
| `debug($message, $context = [])` |
| `info($message, $context = [])` |
| `warning($message, $context = [])` |
| `error($message, $context = [])` |
| `reset()` |

### PHP — `Messenger` (`Messenger.php`)

| Method | 
|--------|
| `send($to, $subject, $body, $html = false, $text = null, $cc = [], $bcc = [], $replyTo = null, $attachments = [], $headers = [])` |
| `testConnection()` |
| `inbox($folder = 'INBOX', $limit = 20, $offset = 0)` |
| `read($uid, $folder = 'INBOX', $markRead = true)` |
| `unread($folder = 'INBOX')` |
| `search($folder = 'INBOX', $subject = null, $sender = null, $since = null, $before = null, $unseenOnly = false, $limit = 20)` |
| `folders()` |

### PHP — `MessengerFactory` (`MessengerFactory.php`)

| Method | 
|--------|
| `create()` |

### PHP — `Metrics` (`Metrics.php`)

| Method | 
|--------|
| `quickMetrics($root = "src")` |
| `fullAnalysis($root = "src")` |
| `fileDetail($filePath)` |

### PHP — `CorsMiddleware` (`Middleware/CorsMiddleware.php`)

| Method | 
|--------|
| `getHeaders($requestOrigin = null)` |
| `isPreflight($method)` |
| `handle($method, $requestOrigin = null)` |
| `getAllowedOrigins()` |
| `getAllowedMethods()` |
| `getAllowedHeaders()` |
| `beforeCors($request, $response)` |

### PHP — `CsrfMiddleware` (`Middleware/CsrfMiddleware.php`)

| Method | 
|--------|
| `beforeCsrf($request, $response)` |

### PHP — `RateLimiter` (`Middleware/RateLimiter.php`)

| Method | 
|--------|
| `check($ip)` |
| `getLimit()` |
| `getWindow()` |
| `getRequestCount($ip)` |
| `reset()` |
| `cleanup()` |
| `beforeRateLimit($request, $response)` |
| `resetStatic()` |

### PHP — `RequestLogger` (`Middleware/RequestLogger.php`)

| Method | 
|--------|
| `beforeLog($request, $response)` |
| `afterLog($request, $response)` |
| `reset()` |

### PHP — `SecurityHeaders` (`Middleware/SecurityHeaders.php`)

| Method | 
|--------|
| `beforeSecurity($request, $response)` |

### PHP — `Middleware` (`Middleware.php`)

| Method | 
|--------|
| `use($class)` |
| `runBefore($middlewareClasses, $request, $response)` |
| `runAfter($middlewareClasses, $request, $response)` |
| `getGlobal()` |
| `reset()` |

### PHP — `QueryBuilder` (`QueryBuilder.php`)

| Method | 
|--------|
| `from($table, $db = null)` |
| `select(string ...$columns)` |
| `where($condition, $params = [])` |
| `orWhere($condition, $params = [])` |
| `join($table, $on)` |
| `leftJoin($table, $on)` |
| `groupBy($column)` |
| `having($expression, $params = [])` |
| `orderBy($expression)` |
| `limit($count, $offset = null)` |
| `toSql()` |
| `get()` |
| `first()` |
| `count()` |
| `exists()` |
| `toMongo()` |

### PHP — `KafkaBackend` (`Queue/KafkaBackend.php`)

| Method | 
|--------|
| `connect()` |
| `enqueue($topic, $message)` |
| `dequeue($topic)` |
| `acknowledge($topic, $messageId)` |
| `requeue($topic, $message)` |
| `deadLetter($topic, $message)` |
| `size($topic)` |
| `close()` |

### PHP — `LiteBackend` (`Queue/LiteBackend.php`)

| Method | 
|--------|
| `enqueue($topic, $message)` |
| `dequeue($topic)` |
| `dequeueBatch($topic, $count)` |
| `acknowledge($topic, $messageId)` |
| `requeue($topic, $message)` |
| `deadLetter($topic, $message)` |
| `size($topic)` |
| `close()` |
| `count($topic, $status = 'pending')` |
| `clear($topic)` |
| `failed($topic)` |
| `retry($jobId, $topic = null, $delaySeconds = 0)` |
| `deadLetters($topic)` |
| `purge($status, $topic)` |
| `retryFailed($topic)` |
| `popById($topic, $id)` |
| `writeFailed($topic, $jobData)` |
| `getBasePath()` |

### PHP — `MongoBackend` (`Queue/MongoBackend.php`)

| Method | 
|--------|
| `connect()` |
| `enqueue($topic, $message)` |
| `dequeue($topic)` |
| `acknowledge($topic, $messageId)` |
| `requeue($topic, $message)` |
| `deadLetter($topic, $message)` |
| `size($topic)` |
| `close()` |

### PHP — `RabbitMQBackend` (`Queue/RabbitMQBackend.php`)

| Method | 
|--------|
| `connect()` |
| `enqueue($topic, $message)` |
| `dequeue($topic)` |
| `acknowledge($topic, $messageId)` |
| `requeue($topic, $message)` |
| `deadLetter($topic, $message)` |
| `size($topic)` |
| `close()` |

### PHP — `Request` (`Request.php`)

| Method | 
|--------|
| `fromGlobals()` |
| `create($method = 'GET', $path = '/', $query = null, $body = null, $headers = [], $ip = '127.0.0.1', $files = [])` |
| `isMethod($method)` |
| `wantsJson()` |
| `isJson()` |
| `header($name)` |
| `queryParam($key, $default = null)` |
| `input($key, $default = null)` |
| `bearerToken()` |

### PHP — `Response` (`Response.php`)

| Method | 
|--------|
| `getFrond()` |
| `setFrond($frond)` |
| `getFrameworkFrond()` |
| `__invoke($data = null, $statusCode = 200, $contentType = null)` |
| `status($code)` |
| `header($name, $value)` |
| `withHeaders($headers)` |
| `json($data, $status = 200)` |
| `html($content, $status = 200)` |
| `text($content, $status = 200)` |
| `xml($content, $status = 200)` |
| `redirect($url, $status = 302)` |
| `cookie($name, $value, $options = [])` |
| `error($code, $message, $status = 400)` |
| `sendError($code, $message, $status = 400)` |
| `send()` |
| `stream($source, $contentType = 'text/event-stream')` |
| `file($path, $contentType = null, $download = false)` |
| `getStatusCode()` |
| `getHeaders()` |
| `getHeader($name)` |
| `getBody()` |
| `getCookies()` |
| `isSent()` |
| `getContentType()` |
| `setBody($body)` |
| `__toString()` |
| `getJsonBody()` |
| `template($templateName, $data = [], $status = 200, $templateDir = 'src/templates')` |
| `render($templateName, $data = [], $status = 200, $templateDir = 'src/templates')` |

### PHP — `ScssCompiler` (`ScssCompiler.php`)

| Method | 
|--------|
| `compile($source)` |
| `compileFile($path)` |
| `addImportPath($path)` |
| `setVariable($name, $value)` |

### PHP — `Server` (`Server.php`)

| Method | 
|--------|
| `start()` |
| `stop()` |
| `broadcastWebSocket($message, $path = null, $excludeId = null)` |
| `removeWebSocketClient($connectionId)` |
| `removeClient($socket)` |
| `getWebSocketClientCount()` |
| `getWebSocketClients()` |
| `getHost()` |
| `getPort()` |
| `isRunning()` |
| `addReloadSubscriber($connectionId)` |
| `removeReloadSubscriber($connectionId)` |

### PHP — `ServiceRunner` (`ServiceRunner.php`)

| Method | 
|--------|
| `register($name, $handler, $options = [])` |
| `discover($serviceDir = '')` |
| `start($name = null)` |
| `stop($name = null)` |
| `list()` |
| `isRunning($name)` |
| `matchCron($pattern, $now = null)` |
| `createContext($name, $lastRun = 0)` |
| `debug($msg, $ctx = [])` |
| `info($msg, $ctx = [])` |
| `warning($msg, $ctx = [])` |
| `error($msg, $ctx = [])` |
| `setPidDir($dir)` |
| `getPidDir()` |
| `pidFilePath($name)` |
| `writePidFile($name, $pid)` |
| `removePidFile($name)` |
| `shutdown()` |
| `reset()` |

### PHP — `SqlTranslation` (`SqlTranslation.php`)

| Method | 
|--------|
| `limitToRows($sql)` |
| `limitToTop($sql)` |
| `booleanToInt($sql)` |
| `ilikeToLike($sql)` |
| `concatPipesToFunc($sql)` |
| `autoIncrementSyntax($sql, $dialect)` |
| `placeholderStyle($sql, $style)` |
| `hasReturning($sql)` |
| `extractReturning($sql)` |
| `registerFunction($name, $mapper)` |
| `applyFunctionMappings($sql)` |
| `clearFunctions()` |
| `setCacheTtl($seconds)` |
| `queryKey($sql, $params = [])` |
| `cacheGet($key)` |
| `cacheSet($key, $value, $ttl = 0)` |
| `remember($key, $ttl, $factory)` |
| `cacheSweep()` |
| `cacheClear()` |
| `cacheSize()` |
| `translate($sql, $dialect)` |

### PHP — `StaticFiles` (`StaticFiles.php`)

| Method | 
|--------|
| `tryServe($path, $basePath = '.')` |

### PHP — `Swagger` (`Swagger.php`)

| Method | 
|--------|
| `generateSpec($title = 'Tina4 API', $version = '1.0.0')` |
| `register()` |

### PHP — `TestClient` (`TestClient.php`)

| Method | 
|--------|
| `get($path, $headers = null)` |
| `post($path, $json = null, $body = null, $headers = null)` |
| `put($path, $json = null, $body = null, $headers = null)` |
| `patch($path, $json = null, $body = null, $headers = null)` |
| `delete($path, $headers = null)` |
| `json()` |
| `text()` |
| `__toString()` |

### PHP — `Testing` (`Testing.php`)

| Method | 
|--------|
| `assertEqual($args, $expected)` |
| `assertRaises($exceptionClass, $args)` |
| `assertTrue($args)` |
| `assertFalse($args)` |
| `tests($assertions, $fn, $name = 'anonymous')` |
| `runAll($quiet = false, $failfast = false)` |
| `reset()` |

### PHP — `Validator` (`Validator.php`)

| Method | 
|--------|
| `required(string ...$fields)` |
| `email($field)` |
| `minLength($field, $length)` |
| `maxLength($field, $length)` |
| `integer($field)` |
| `min($field, $minimum)` |
| `max($field, $maximum)` |
| `inList($field, $allowed)` |
| `regex($field, $pattern)` |
| `errors()` |
| `isValid()` |

### Ruby — `Tina4` (`api.rb`)

| Method | 
|--------|
| `get(path, params: {}, headers: {})` |
| `post(path, body: nil, headers: {})` |
| `put(path, body: nil, headers: {})` |
| `patch(path, body: nil, headers: {})` |
| `delete(path, headers: {})` |
| `upload(path, file_path, field_name: "file", extra_fields: {}, headers: {})` |
| `build_uri(path, params = {})` |
| `apply_headers(request, extra_headers)` |
| `execute(uri, request)` |
| `build_multipart_body(boundary, file_path, field_name, extra_fields)` |
| `json(@json ||= JSON.parse(@body)` |
| `to_s("APIResponse(status=#{@status})` |

### Ruby — `Tina4` (`cli.rb`)

| Method | 
|--------|
| `self.start(argv)` |
| `run(argv)` |
| `to_snake_case(name)` |
| `to_table_name(name)` |
| `parse_fields(fields_str)` |
| `parse_flags(args)` |
| `kill_process_on_port(port)` |
| `cmd_init(argv)` |
| `cmd_start(argv)` |
| `cmd_migrate(argv)` |
| `cmd_migrate_status(_argv)` |
| `cmd_migrate_rollback(argv)` |
| `cmd_seed(argv)` |
| `cmd_seed_create(argv)` |
| `cmd_test(argv)` |
| `cmd_version(require_relative "version"
      puts "Tina4 Ruby v#{Tina4::VERSION}"
    end

    # ── routes ────────────────────────────────────────────────────────────

    def cmd_routes
      require_relative "../tina4"
      Tina4.initialize!(Dir.pwd)` |
| `cmd_console(require_relative "../tina4"
      Tina4.initialize!(Dir.pwd)` |
| `cmd_ai(argv)` |
| `cmd_generate(argv)` |
| `generate_model(name, flags)` |
| `generate_route(name, flags)` |
| `generate_crud(name, flags)` |
| `generate_migration(name, flags = {}, fields_override: nil, table_override: nil)` |
| `generate_middleware(name, flags = {})` |
| `generate_test(name, flags = {})` |
| `generate_form(name, flags = {})` |
| `generate_view(name, flags = {})` |
| `generate_auth(_name = nil, flags = {})` |
| `cmd_help(puts <<~HELP
        Tina4 Ruby CLI

        Usage: tina4ruby COMMAND [options]

        Commands:
          init [NAME]        Initialize a new Tina4 project
          start              Start the Tina4 web server
          serve              Alias for start
          migrate            Run database migrations
          migrate:status     Show migration status (completed and pending)` |
| `resolve_config(key, cli_value)` |
| `load_routes(root_dir)` |
| `create_project_structure(dir)` |
| `create_sample_files(dir, project_name)` |

### Ruby — `Tina4` (`dev_admin.rb`)

| Method | 
|--------|
| `get(category: nil)` |
| `clear(category: nil)` |
| `count(@mutex.synchronize do
        counts = Hash.new(0)` |
| `stats(@mutex.synchronize do
        return { total: 0, avg_ms: 0.0, errors: 0, slowest_ms: 0.0 } if @requests.empty?

        durations = @requests.map(&:duration)` |
| `capture(error_type:, message:, traceback: "", file: "", line: 0)` |
| `capture_exception(exc)` |
| `unresolved_count(@mutex.synchronize do
        load_unlocked
        @errors.count { |_, e| !e[:resolved] }
      end
    end

    # Health summary (matches Python BrokenTracker interface)` |
| `health(@mutex.synchronize do
        load_unlocked
        total    = @errors.size
        resolved = @errors.count { |_, e| e[:resolved] }
        unresolved = total - resolved
        { total: total, unresolved: unresolved, resolved: resolved, healthy: unresolved.zero? }
      end
    end

    # Mark a single error as resolved.
    def resolve(id)` |
| `clear_resolved(@mutex.synchronize do
        load_unlocked
        @errors.reject! { |_, e| e[:resolved] }
        save_unlocked
      end
    end

    # Remove ALL errors.
    def clear_all
      @mutex.synchronize do
        @errors = {}
        save_unlocked
      end
    end

    # Reset (for testing)` |
| `load_unlocked(return if @errors

      if File.exist?(@store_path)` |
| `save_unlocked(# Trim to max, keeping newest last_seen
      if @errors.size > MAX_ERRORS
        sorted = @errors.values.sort_by { |e| e[:last_seen] }.last(MAX_ERRORS)` |

### Ruby — `Tina4` (`dev_mailbox.rb`)

| Method | 
|--------|
| `capture(to:, subject:, body:, html: false, cc: [], bcc: [],
                reply_to: nil, from_address: nil, from_name: nil, attachments: [])` |
| `inbox(limit: 50, offset: 0, folder: nil)` |
| `read(msg_id)` |
| `unread_count(load_all_messages.count { |m| m[:read] == false }
    end

    # Delete a message by ID
    def delete(msg_id)` |
| `clear(folder: nil)` |
| `seed(count: 5)` |
| `count(folder: nil)` |
| `ensure_dirs(FileUtils.mkdir_p(File.join(@mailbox_dir, "messages")` |
| `message_path(msg_id)` |
| `write_message(msg_id, message)` |
| `load_all_messages(pattern = File.join(@mailbox_dir, "messages", "*.json")` |
| `normalize_recipients(value)` |
| `store_attachments(msg_id, attachments)` |

### Ruby — `Tina4` (`field_types.rb`)

| Method | 
|--------|
| `self.included(base)` |

### Ruby — `Tina4` (`html_element.rb`)

| Method | 
|--------|
| `call(*args)` |
| `to_s(html = "<#{@tag}"

      @attrs.each do |key, value|
        case value
        when true
          html << " #{key}"
        when false, nil
          next
        else
          escaped = value.to_s
            .gsub("&", "&amp;")` |
| `self.html_helpers` |

### Ruby — `Tina4` (`job.rb`)

| Method | 
|--------|
| `retry(delay_seconds: 0, queue: nil)` |
| `to_array([@id, @topic, @payload, @priority, @attempts]
    end

    def to_hash
      h = {
        id: @id,
        topic: @topic,
        payload: @payload,
        created_at: @created_at.iso8601,
        attempts: @attempts,
        status: @status,
        priority: @priority
      }
      h[:available_at] = @available_at.iso8601 if @available_at
      h
    end

    def to_json(*_args)` |
| `complete(@status = :completed
    end

    # Mark this job as failed with a reason.
    def fail(reason = "")` |
| `reject(reason = "")` |

### Ruby — `Tina4` (`messenger.rb`)

| Method | 
|--------|
| `send(to:, subject:, body:, html: false, text: nil, cc: [], bcc: [],
             reply_to: nil, attachments: [], headers: {})` |
| `test_connection(smtp = Net::SMTP.new(@host, @port)` |
| `inbox(folder: "INBOX", limit: 20, offset: 0)` |
| `read(uid, folder: "INBOX", mark_read: true)` |
| `unread(folder: "INBOX")` |
| `search(folder: "INBOX", subject: nil, sender: nil, since: nil,
               before: nil, unseen_only: false, limit: 20)` |
| `folders(imap_connect do |imap|
        boxes = imap.list("", "*")` |
| `auth_method(return :plain if @username && @password

      nil
    end

    def normalize_recipients(value)` |
| `format_address(address, name = nil)` |
| `build_message(to:, subject:, body:, html:, text: nil, cc:, bcc:, reply_to:,
                      attachments:, headers:, message_id:)` |
| `build_attachment_part(attachment)` |
| `encode_header(value)` |
| `guess_mime_type(filename)` |
| `imap_connect(&block)` |
| `parse_envelope(fetch_data)` |
| `parse_full_message(fetch_data)` |
| `format_imap_address(addresses)` |
| `decode_mime_header(value)` |
| `extract_body_parts(raw)` |
| `extract_part_body(part)` |
| `build_search_criteria(subject:, sender:, since:, before:, unseen_only:)` |
| `format_imap_date(date)` |
| `self.create_messenger(**options)` |

### Ruby — `Tina4` (`metrics.rb`)

| Method | 
|--------|
| `self._resolve_root(root = 'src')` |
| `self.last_scan_root(@last_scan_root
    end

    # ── Quick Metrics ───────────────────────────────────────────

    def self.quick_metrics(root = 'src')` |
| `self.full_analysis(root = 'src')` |
| `self.file_detail(file_path)` |
| `self._has_matching_test(rel_path)` |
| `self._files_hash(root)` |
| `self._extract_imports(lines)` |
| `self._extract_functions(source, tokens, lines)` |
| `self._find_method_end(lines, start_index)` |
| `self._cyclomatic_complexity_from_source(source)` |
| `self._count_halstead(tokens)` |
| `self._maintainability_index(halstead_volume, avg_cc, loc)` |
| `self._detect_violations(functions, file_metrics)` |

### Ruby — `Tina4` (`query_builder.rb`)

| Method | 
|--------|
| `self.from(table_name, db: nil)` |
| `select(*columns)` |
| `where(condition, params = [])` |
| `or_where(condition, params = [])` |
| `join(table, on_clause)` |
| `left_join(table, on_clause)` |
| `group_by(column)` |
| `having(expression, params = [])` |
| `order_by(expression)` |
| `limit(count, offset = nil)` |
| `to_sql(sql = "SELECT #{@columns.join(', ')` |
| `get(ensure_db!
      sql = to_sql
      all_params = @params + @having_params

      @db.fetch(
        sql,
        all_params.empty? ? [] : all_params,
        limit: @limit_val || 100,
        offset: @offset_val || 0
      )` |
| `first(ensure_db!
      sql = to_sql
      all_params = @params + @having_params

      @db.fetch_one(sql, all_params.empty? ? [] : all_params)` |
| `count(ensure_db!

      # Build a count query by replacing columns
      original = @columns
      @columns = ["COUNT(*)` |
| `to_mongo(result = {}

      # -- projection --
      if @columns != ["*"]
        result[:projection] = @columns.each_with_object({})` |
| `parse_condition_to_mongo(condition, param_index)` |
| `merge_mongo_conditions(conditions)` |
| `build_where(parts = []
      @wheres.each_with_index do |(connector, condition)` |

### Ruby — `Tina4` (`rack_app.rb`)

| Method | 
|--------|
| `call(env)` |
| `handle(request)` |
| `handle_route(env, route, path_params)` |
| `try_static(path)` |
| `serve_static_file(full_path)` |
| `serve_swagger_ui(html = <<~HTML
        <!DOCTYPE html>
        <html lang="en">
        <head>
          <meta charset="UTF-8">
          <title>API Documentation</title>
          <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css">
        </head>
        <body>
          <div id="swagger-ui"></div>
          <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
          <script>
            SwaggerUIBundle({ url: '/swagger/openapi.json', dom_id: '#swagger-ui' })` |
| `serve_openapi_json(@openapi_json ||= JSON.generate(Tina4::Swagger.generate)` |
| `handle_403(path = "")` |
| `handle_404(path)` |
| `try_serve_template(path)` |
| `resolve_template(path)` |
| `build_template_cache(cache = {}
      templates_dir = File.join(@root_dir, "src", "templates")` |
| `try_serve_index_template(templates_dir = File.join(@root_dir, "src", "templates")` |
| `render_landing_page(port = ENV["PORT"] || "7145"

      # Check deployed state for each gallery item
      project_src = File.join(@root_dir, "src")` |
| `handle_500(error, env = nil)` |
| `handle_websocket_upgrade(env, ws_route, ws_params)` |
| `inject_dev_overlay(body, request_info, ai_port: false)` |

### Ruby — `Tina4` (`rate_limiter.rb`)

| Method | 
|--------|
| `check(ip)` |
| `apply(ip, response)` |
| `entry_count(@mutex.synchronize { @store.length }
    end

    private

    # Clean up expired entries periodically (every window interval)` |
| `cleanup_if_needed(now)` |

### Ruby — `Tina4` (`request.rb`)

| Method | 
|--------|
| `fetch(key, *args, &block)` |
| `delete(key, &block)` |
| `convert_key(key)` |
| `url(scheme = env["rack.url_scheme"] || "http"
      host = env["HTTP_HOST"] || env["SERVER_NAME"] || "localhost"
      port = env["SERVER_PORT"]
      url_str = "#{scheme}://#{host}"
      url_str += ":#{port}" if port && port != "80" && port != "443"
      url_str += @path
      url_str += "?#{@query_string}" unless @query_string.empty?
      url_str
    end

    # Lazy accessors
    def headers
      @headers ||= extract_headers
    end

    def cookies
      @cookies ||= parse_cookies
    end

    def session
      @session ||= Tina4::Session.new(@env)` |
| `body(@body_raw ||= read_body
    end

    # Parsed body (JSON or form data)` |
| `body_parsed(@body_parsed ||= parse_body
    end

    # Parsed query string as hash
    def query
      @query_hash ||= parse_query_to_hash(@query_string)` |
| `files(@files ||= extract_files
    end

    # Merged params: query + body + path_params (path_params highest priority)` |
| `params(@params ||= build_params
    end

    # Look up a param by symbol or string key (indifferent access shortcut)` |
| `param(key)` |
| `header(name)` |
| `json_body(@json_body ||= begin
        JSON.parse(body)` |
| `bearer_token(auth = header("authorization")` |
| `extract_client_ip(# Check X-Forwarded-For first (proxy/load balancer)` |
| `extract_headers(h = {}
      @env.each do |key, value|
        if key.start_with?("HTTP_")` |
| `parse_cookies(cookie_str = @env["HTTP_COOKIE"]
      return {} unless cookie_str && !cookie_str.empty?

      result = {}
      cookie_str.split(";")` |
| `read_body(input = @env["rack.input"]
      return "" unless input
      input.rewind if input.respond_to?(:rewind)` |
| `parse_body(if @content_type.include?("application/json")` |
| `build_params(p = IndifferentHash.new

      # Query string params
      query.each { |k, v| p[k.to_s] = v }

      # Body params
      body_parsed.each { |k, v| p[k.to_s] = v }

      # Path params (highest priority)` |
| `parse_query_to_hash(qs)` |
| `extract_files(result = {}
      return result unless @content_type.include?("multipart/form-data")` |

### Ruby — `Tina4` (`response.rb`)

| Method | 
|--------|
| `call(data = nil, status_code = 200, content_type = nil)` |
| `json(data, status_or_opts = nil, status: nil)` |
| `html(content, status_or_opts = nil, status: nil)` |
| `text(content, status_or_opts = nil, status: nil)` |
| `xml(content, status: 200)` |
| `csv(content, filename: "export.csv", status: 200)` |
| `redirect(url, status_or_opts = nil, status: nil)` |
| `file(path, content_type: nil, download: false)` |
| `render(template_path, data = {}, status: 200, template_dir: nil)` |
| `error(code, message, status_code = 400)` |
| `self.error_envelope(code, message, status = 400)` |
| `header(name, value = nil)` |
| `cookie(name, value, opts = {})` |
| `set_cookie(name, value, opts = {})` |
| `delete_cookie(name, path: "/")` |
| `add_header(key, value)` |
| `add_cors_headers(origin: "*", methods: "GET, POST, PUT, PATCH, DELETE, OPTIONS",
                         headers_list: "Content-Type, Authorization, Accept", credentials: false)` |
| `stream(content_type: "text/event-stream", &block)` |
| `send(to_rack
    end

    def to_rack
      final_headers = @headers.dup
      final_headers["set-cookie"] = @cookies.join("\n")` |
| `self.auto_detect(result, response)` |

### Ruby — `Tina4` (`seeder.rb`)

| Method | 
|--------|
| `self.seed(seed)` |
| `first_name(FIRST_NAMES[@rng.rand(FIRST_NAMES.length)` |
| `last_name(LAST_NAMES[@rng.rand(LAST_NAMES.length)` |
| `name("#{first_name} #{last_name}"
    end

    def email(from_name: nil)` |
| `phone(area = @rng.rand(200..999)` |
| `sentence(words: 6)` |
| `paragraph(sentences: 3)` |
| `text(max_length: 200)` |
| `word(WORDS[@rng.rand(WORDS.length)` |
| `slug(words: 3)` |
| `url("https://#{DOMAINS[@rng.rand(DOMAINS.length)` |
| `integer(min: 0, max: 10_000)` |
| `numeric(min: 0.0, max: 1000.0, decimals: 2)` |
| `boolean(@rng.rand(2)` |
| `datetime(start_year: 2020, end_year: 2026)` |
| `date(start_year: 2020, end_year: 2026)` |
| `timestamp(start_year: 2020, end_year: 2026)` |
| `blob(size: 64)` |
| `json_data(keys: nil)` |
| `choice(items)` |
| `city(CITIES[@rng.rand(CITIES.length)` |
| `country(COUNTRIES[@rng.rand(COUNTRIES.length)` |
| `address("#{@rng.rand(1..9999)` |
| `zip_code(@rng.rand(10_000..99_999)` |
| `company(w1 = COMPANY_WORDS[@rng.rand(COMPANY_WORDS.length)` |
| `color_hex("#%06x" % @rng.rand(0..0xFFFFFF)` |
| `uuid(h = Array.new(32)` |
| `password(length: 16)` |
| `for_field(field_def, column_name = nil)` |
| `generate_string_for(col, max_len)` |
| `self.seed_orm(orm_class, count: 10, overrides: {}, clear: false, seed: nil)` |
| `self.seed_table(table_name, columns, count: 10, overrides: {}, clear: false, seed: nil)` |
| `self.seed_batch(tasks, clear: false)` |

### Ruby — `Tina4` (`sql_translation.rb`)

| Method | 
|--------|
| `set(key, value, ttl: nil, tags: [])` |
| `get(key, default = nil)` |
| `delete(key)` |
| `clear(@mutex.synchronize { @store.clear }
    end

    # Clear all entries with a given tag.
    #
    # @param tag [String]
    # @return [Integer] number of entries removed
    def clear_tag(tag)` |
| `sweep(@mutex.synchronize do
        now = Time.now.to_f
        keys_to_remove = @store.select { |_k, v| now > v.expires_at }.keys
        keys_to_remove.each { |k| @store.delete(k)` |
| `remember(key, ttl, &block)` |
| `size` |

### Ruby — `Tina4` (`test_client.rb`)

| Method | 
|--------|
| `json(return nil if @body.nil? || @body.empty?
      JSON.parse(@body)` |
| `text(@body.to_s
    end

    def inspect
      "<TestResponse status=#{@status} content_type=#{@content_type.inspect}>"
    end
  end

  class TestClient
    # Send a GET request.
    def get(path, headers: nil)` |
| `post(path, json: nil, body: nil, headers: nil)` |
| `put(path, json: nil, body: nil, headers: nil)` |
| `patch(path, json: nil, body: nil, headers: nil)` |
| `delete(path, headers: nil)` |
| `request(method, path, json: nil, body: nil, headers: nil)` |

### Ruby — `Tina4` (`validator.rb`)

| Method | 
|--------|
| `required(*fields)` |
| `email(field)` |
| `min_length(field, length)` |
| `max_length(field, length)` |
| `integer(field)` |
| `min(field, minimum)` |
| `max(field, maximum)` |
| `in_list(field, allowed)` |
| `regex(field, pattern)` |
| `errors(@validation_errors.dup
    end

    # Return true if no validation errors have been recorded.
    def is_valid?
      @validation_errors.empty?
    end

    # Alias for is_valid? (Ruby convention)` |

### Ruby — `Tina4` (`webserver.rb`)

| Method | 
|--------|
| `free_port(port)` |
| `start(require "webrick"
      require "stringio"
      require "socket"

      # Ensure the main port is available — kill whatever is on it if needed
      begin
        test = TCPServer.new("0.0.0.0", @port)` |
| `stop(@ai_server&.shutdown
      @ai_thread&.join(5)` |

### Node — `Api` (`core/src/api.ts`)

| Method | 
|--------|
| `addCustomHeaders(headers: Record<string, string>)` |
| `setBearerToken(token: string)` |
| `setBasicAuth(username: string, password: string)` |
| `setIgnoreSsl(ignore: boolean)` |
| `get(path: string, params?: Record<string, string>)` |
| `post(path: string, body?: unknown, contentType: string = "appl...)` |
| `put(path: string, body?: unknown, contentType: string = "appl...)` |
| `patch(path: string, body?: unknown, contentType: string = "appl...)` |
| `delete(path: string, body?: unknown)` |
| `sendRequest(path: string,
        method: string,
        body?: unkn...)` |

### Node — `Container` (`core/src/container.ts`)

| Method | 
|--------|
| `register(name: string, factory: ()` |
| `singleton(name: string, factory: ()` |
| `get(T = unknown>(name: string)` |
| `has(name: string)` |
| `reset()` |

### Node — `MessageLog` (`core/src/devAdmin.ts`)

| Method | 
|--------|
| `log(category: string, level: string, message: string, data?: ...)` |
| `get(category?: string, limit = 100)` |
| `clear(category?: string)` |
| `count()` |
| `capture(method: string, path: string, status: number, duration: n...)` |
| `stats()` |
| `track(message: string, stack?: string)` |
| `resolve(id: string)` |
| `clearResolved()` |
| `inbox(folder: string = "inbox", limit: number = 50, offset: num...)` |
| `read(id: string)` |
| `seed(count = 5)` |
| `unreadCount()` |
| `add(name: string, payload?: unknown)` |
| `retryFailed()` |
| `purgeCompleted()` |
| `replay(id: string)` |
| `remove(id: string)` |
| `list()` |
| `isEnabled()` |
| `register(router: Router)` |
| `renderToolbarHtml(ctx: {
    version: string;
    method: string;
    path:...)` |
| `writeFileSync(envPath, newLines.join("\n")` |
| `clearTimeout(timeout)` |
| `join(dir, "..", "public", "js", "tina4-dev-admin.min.js")` |
| `updateConnectionUrl()` |
| `fetch('/__dev/api/connections/test', {
        method: 'POST',
...)` |
| `draw()` |

### Node — `DevMailbox` (`core/src/devMailbox.ts`)

| Method | 
|--------|
| `mkdirSync(dir, { recursive: true })` |
| `capture(options: {
    to: string | string[];
    subject: string...)` |
| `writeFileSync(join(outboxDir, `${id}.json`)` |
| `inbox(limit: number = 50, offset: number = 0, folder: string = ...)` |
| `read(msgId: string)` |
| `unreadCount()` |
| `delete(msgId: string)` |
| `clear(folder?: string)` |
| `seed(count: number = 5)` |
| `count(folder?: string)` |

### Node — `FakeData` (`core/src/fakeData.ts`)

| Method | 
|--------|
| `seed(seed: number)` |
| `firstName()` |
| `lastName()` |
| `fullName()` |
| `email()` |
| `phone()` |
| `address()` |
| `city()` |
| `country()` |
| `zipCode()` |
| `company()` |
| `jobTitle()` |
| `paragraph(sentences = 4)` |
| `sentence(words = 8)` |
| `word()` |
| `integer(min = 0, max = 10000)` |
| `float(min = 0, max = 1000, decimals = 2)` |
| `boolean()` |
| `date(start?: string, end?: string)` |
| `uuid()` |
| `url()` |
| `ipAddress()` |
| `color()` |
| `hexColor()` |
| `creditCard()` |
| `currency()` |
| `runSeeds(seedDir?: string)` |
| `run(fn: ()` |

### Node — `HtmlElement` (`core/src/htmlElement.ts`)

| Method | 
|--------|
| `toString()` |

### Node — `I18n` (`core/src/i18n.ts`)

| Method | 
|--------|
| `setLocale(locale: string)` |
| `getLocale()` |
| `t(key: string, params?: Record<string, string>, locale?: st...)` |
| `translate(key: string, params?: Record<string, string>, locale?: st...)` |
| `loadTranslations(locale: string)` |
| `addTranslation(locale: string, key: string, value: string)` |
| `getAvailableLocales()` |

### Node — `Log` (`core/src/logger.ts`)

| Method | 
|--------|
| `setRequestId(id: string | undefined)` |
| `getRequestId()` |
| `configure(options: { logDir?: string; logFile?: string })` |
| `info(message: string, data?: unknown)` |
| `debug(message: string, data?: unknown)` |
| `warning(message: string, data?: unknown)` |
| `error(message: string, data?: unknown)` |

### Node — `Messenger` (`core/src/messenger.ts`)

| Method | 
|--------|
| `send(options: SendOptions)` |
| `testConnection()` |
| `inbox(limit: number = 20, offset: number = 0, folder: string = ...)` |
| `read(uid: string, folder: string = "INBOX")` |
| `search(query: string, folder: string = "INBOX")` |
| `deleteMessage(uid: string, folder: string = "INBOX")` |
| `markRead(uid: string, folder: string = "INBOX")` |
| `unread(folder: string = "INBOX")` |
| `testImapConnection()` |

### Node — `MiddlewareChain` (`core/src/middleware.ts`)

| Method | 
|--------|
| `use(fn: Middleware)` |
| `run(req: Tina4Request, res: Tina4Response)` |
| `runBefore(classes: any[],
    req: Tina4Request,
    res: Tina4Resp...)` |
| `runAfter(classes: any[],
    req: Tina4Request,
    res: Tina4Resp...)` |
| `next()` |
| `beforeCors(req: Tina4Request, res: Tina4Response)` |
| `beforeRateLimit(req: Tina4Request, res: Tina4Response)` |
| `beforeLog(req: Tina4Request, res: Tina4Response)` |
| `afterLog(req: Tina4Request, res: Tina4Response)` |
| `beforeSecurity(req: Tina4Request, res: Tina4Response)` |
| `beforeCsrf(req: Tina4Request, res: Tina4Response)` |

### Node — `KafkaBackend` (`core/src/queueBackends/kafkaBackend.ts`)

| Method | 
|--------|
| `push(queue: string, payload: unknown, delay?: number)` |
| `pop(queue: string)` |
| `size(queue: string)` |
| `clear(queue: string)` |

### Node — `LiteBackend` (`core/src/queueBackends/liteBackend.ts`)

| Method | 
|--------|
| `mkdirSync(dir, { recursive: true })` |
| `push(queue: string, payload: unknown, delay?: number, priority...)` |
| `writeFileSync(join(dir, `${prefix}_${id}.queue-data`)` |
| `pop(queue: string, bridge: JobQueueBridge)` |
| `popBatch(queue: string, bridge: JobQueueBridge, count: number)` |
| `size(queue: string, status: string = "pending")` |
| `clear(queue: string)` |
| `failed(queue: string)` |
| `retry(queue: string, jobId: string, delaySeconds?: number)` |
| `deadLetters(queue: string, maxRetries: number = 3)` |
| `purge(queue: string, status: string, maxRetries: number = 3)` |
| `retryFailed(queue: string, maxRetries: number = 3)` |
| `popById(queue: string, id: string)` |
| `failJob(queue: string, job: QueueJob, error: string, maxRetries: ...)` |
| `retryJob(queue: string, job: QueueJob, delaySeconds?: number)` |

### Node — `MongoBackend` (`core/src/queueBackends/mongoBackend.ts`)

| Method | 
|--------|
| `push(queue: string, payload: unknown, delay?: number)` |
| `pop(queue: string)` |
| `size(queue: string)` |
| `clear(queue: string)` |

### Node — `RabbitMQBackend` (`core/src/queueBackends/rabbitmqBackend.ts`)

| Method | 
|--------|
| `push(queue: string, payload: unknown, delay?: number)` |
| `pop(queue: string)` |
| `size(queue: string)` |
| `clear(queue: string)` |
| `writeShortString(keyBuf, 0, key)` |
| `writeLongString(valBuf, 1, value)` |

### Node — `PayloadTooLargeError` (`core/src/request.ts`)

| Method | 
|--------|
| `super(`Request body (${actual} bytes)` |

### Node — `ScssCompiler` (`core/src/scss.ts`)

| Method | 
|--------|
| `compile(source: string)` |
| `compileFile(filePath: string)` |
| `addImportPath(path: string)` |
| `setVariable(name: string, value: string)` |
| `flattenBlock(scss, [], output)` |

### Node — `ServiceRunner` (`core/src/service.ts`)

| Method | 
|--------|
| `matchCronField(fields[1], hour)` |
| `executeHandler(svc)` |
| `register(name: string,
    handler: ServiceHandler,
    options: S...)` |
| `discover(serviceDir?: string)` |
| `start(name?: string)` |
| `stop(name?: string)` |
| `list()` |
| `isRunning(name: string)` |
| `remove(name: string)` |
| `clear()` |
| `watch(serviceDir?: string)` |
| `unwatch()` |

### Node — `MongoSessionHandler` (`core/src/sessionHandlers/mongoHandler.ts`)

| Method | 
|--------|
| `read(sessionId: string)` |
| `write(sessionId: string, data: SessionData, _ttl: number)` |
| `destroy(sessionId: string)` |

### Node — `RedisNpmSessionHandler` (`core/src/sessionHandlers/redisHandler.ts`)

| Method | 
|--------|
| `read(sessionId: string)` |
| `write(sessionId: string, data: SessionData, ttl: number)` |
| `destroy(sessionId: string)` |

### Node — `ValkeySessionHandler` (`core/src/sessionHandlers/valkeyHandler.ts`)

| Method | 
|--------|
| `read(sessionId: string)` |
| `write(sessionId: string, data: SessionData, ttl: number)` |
| `destroy(sessionId: string)` |

### Node — `TestResponse` (`core/src/testClient.ts`)

| Method | 
|--------|
| `json()` |
| `text()` |
| `toString()` |
| `get(path: string, options?: RequestOptions)` |
| `post(path: string, options?: RequestOptions)` |
| `put(path: string, options?: RequestOptions)` |
| `patch(path: string, options?: RequestOptions)` |
| `delete(path: string, options?: RequestOptions)` |

### Node — `Validator` (`core/src/validator.ts`)

| Method | 
|--------|
| `required(...fields: string[])` |
| `email(field: string)` |
| `minLength(field: string, length: number)` |
| `maxLength(field: string, length: number)` |
| `integer(field: string)` |
| `min(field: string, minimum: number)` |
| `max(field: string, maximum: number)` |
| `inList(field: string, allowed: unknown[])` |
| `regex(field: string, pattern: RegExp | string)` |
| `errors()` |
| `isValid()` |

### Node — `Frond` (`frond/src/engine.ts`)

| Method | 
|--------|
| `toString()` |
| `getTemplateDir()` |
| `sandbox(filters?: string[], tags?: string[], vars?: string[])` |
| `unsandbox()` |
| `addFilter(name: string, fn: FilterFn)` |
| `addGlobal(name: string, value: unknown)` |
| `addTest(name: string, fn: TestFn)` |
| `render(template: string, data?: Record<string, unknown>)` |
| `renderString(source: string, data?: Record<string, unknown>)` |
| `clearCache()` |

### Node — `FirebirdAdapter` (`orm/src/adapters/firebird.ts`)

| Method | 
|--------|
| `connect()` |
| `translateSql(sql: string)` |
| `execute(sql: string, params?: unknown[])` |
| `executeMany(sql: string, paramsList: unknown[][])` |
| `executeManyAsync(sql: string, paramsList: unknown[][])` |
| `executeAsync(sql: string, params?: unknown[])` |
| `query(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `queryAsync(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `fetch(T = Record<string, unknown>>(sql: string, params?: unknow...)` |
| `fetchAsync(T = Record<string, unknown>>(sql: string, params?: unknow...)` |
| `fetchOne(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `fetchOneAsync(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `insert(table: string, data: Record<string, unknown>)` |
| `insertAsync(table: string, data: Record<string, unknown>)` |
| `update(table: string, data: Record<string, unknown>, filter: Rec...)` |
| `updateAsync(table: string, data: Record<string, unknown>, filter: Rec...)` |
| `delete(table: string, filter: Record<string, unknown>)` |
| `deleteAsync(table: string, filter: Record<string, unknown>)` |
| `startTransaction()` |
| `startTransactionAsync()` |
| `commit()` |
| `commitAsync()` |
| `rollback()` |
| `rollbackAsync()` |
| `tables()` |
| `tablesAsync()` |
| `columns(table: string)` |
| `columnsAsync(table: string)` |
| `lastInsertId()` |
| `close()` |
| `tableExists(name: string)` |
| `tableExistsAsync(name: string)` |
| `createTable(name: string, columns: Record<string, FieldDefinition>)` |
| `createTableAsync(name: string, columns: Record<string, FieldDefinition>)` |

### Node — `MssqlAdapter` (`orm/src/adapters/mssql.ts`)

| Method | 
|--------|
| `connect()` |
| `translateSql(sql: string)` |
| `execute(sql: string, params?: unknown[])` |
| `executeMany(sql: string, paramsList: unknown[][])` |
| `executeManyAsync(sql: string, paramsList: unknown[][])` |
| `executeAsync(sql: string, params?: unknown[])` |
| `query(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `queryAsync(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `fetch(T = Record<string, unknown>>(sql: string, params?: unknow...)` |
| `fetchAsync(T = Record<string, unknown>>(sql: string, params?: unknow...)` |
| `fetchOne(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `fetchOneAsync(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `insert(table: string, data: Record<string, unknown>)` |
| `insertAsync(table: string, data: Record<string, unknown>)` |
| `update(table: string, data: Record<string, unknown>, filter: Rec...)` |
| `updateAsync(table: string, data: Record<string, unknown>, filter: Rec...)` |
| `delete(table: string, filter: Record<string, unknown>)` |
| `deleteAsync(table: string, filter: Record<string, unknown>)` |
| `startTransaction()` |
| `startTransactionAsync()` |
| `commit()` |
| `commitAsync()` |
| `rollback()` |
| `rollbackAsync()` |
| `tables()` |
| `tablesAsync()` |
| `columns(table: string)` |
| `columnsAsync(table: string)` |
| `lastInsertId()` |
| `close()` |
| `tableExists(name: string)` |
| `tableExistsAsync(name: string)` |
| `createTable(name: string, columns: Record<string, FieldDefinition>)` |
| `createTableAsync(name: string, columns: Record<string, FieldDefinition>)` |

### Node — `MysqlAdapter` (`orm/src/adapters/mysql.ts`)

| Method | 
|--------|
| `connect()` |
| `translateSql(sql: string)` |
| `execute(sql: string, params?: unknown[])` |
| `executeMany(sql: string, paramsList: unknown[][])` |
| `executeManyAsync(sql: string, paramsList: unknown[][])` |
| `executeAsync(sql: string, params?: unknown[])` |
| `query(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `queryAsync(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `fetch(T = Record<string, unknown>>(sql: string, params?: unknow...)` |
| `fetchAsync(T = Record<string, unknown>>(sql: string, params?: unknow...)` |
| `fetchOne(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `fetchOneAsync(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `insert(table: string, data: Record<string, unknown>)` |
| `insertAsync(table: string, data: Record<string, unknown>)` |
| `update(table: string, data: Record<string, unknown>, filter: Rec...)` |
| `updateAsync(table: string, data: Record<string, unknown>, filter: Rec...)` |
| `delete(table: string, filter: Record<string, unknown>)` |
| `deleteAsync(table: string, filter: Record<string, unknown>)` |
| `startTransaction()` |
| `startTransactionAsync()` |
| `commit()` |
| `commitAsync()` |
| `rollback()` |
| `rollbackAsync()` |
| `tables()` |
| `tablesAsync()` |
| `columns(table: string)` |
| `columnsAsync(table: string)` |
| `lastInsertId()` |
| `close()` |
| `tableExists(name: string)` |
| `tableExistsAsync(name: string)` |
| `createTable(name: string, columns: Record<string, FieldDefinition>)` |
| `createTableAsync(name: string, columns: Record<string, FieldDefinition>)` |

### Node — `PostgresAdapter` (`orm/src/adapters/postgres.ts`)

| Method | 
|--------|
| `connect()` |
| `execute(sql: string, params?: unknown[])` |
| `executeMany(sql: string, paramsList: unknown[][])` |
| `executeManyAsync(sql: string, paramsList: unknown[][])` |
| `executeAsync(sql: string, params?: unknown[])` |
| `query(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `queryAsync(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `fetch(T = Record<string, unknown>>(sql: string, params?: unknow...)` |
| `fetchAsync(T = Record<string, unknown>>(sql: string, params?: unknow...)` |
| `fetchOne(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `fetchOneAsync(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `insert(table: string, data: Record<string, unknown>)` |
| `insertAsync(table: string, data: Record<string, unknown>)` |
| `update(table: string, data: Record<string, unknown>, filter: Rec...)` |
| `updateAsync(table: string, data: Record<string, unknown>, filter: Rec...)` |
| `delete(table: string, filter: Record<string, unknown>)` |
| `deleteAsync(table: string, filter: Record<string, unknown>)` |
| `startTransaction()` |
| `startTransactionAsync()` |
| `commit()` |
| `commitAsync()` |
| `rollback()` |
| `rollbackAsync()` |
| `tables()` |
| `tablesAsync()` |
| `columns(table: string)` |
| `columnsAsync(table: string)` |
| `lastInsertId()` |
| `close()` |
| `tableExists(name: string)` |
| `tableExistsAsync(name: string)` |
| `createTable(name: string, columns: Record<string, FieldDefinition>)` |
| `createTableAsync(name: string, columns: Record<string, FieldDefinition>)` |
| `translateSql(sql: string)` |

### Node — `SQLiteAdapter` (`orm/src/adapters/sqlite.ts`)

| Method | 
|--------|
| `execute(sql: string, params?: unknown[])` |
| `executeMany(sql: string, paramsList: unknown[][])` |
| `query(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `fetch(T = Record<string, unknown>>(sql: string, params?: unknow...)` |
| `fetchOne(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `insert(table: string, data: Record<string, unknown> | Record<str...)` |
| `update(table: string, data: Record<string, unknown>, filter: Rec...)` |
| `delete(table: string, filter: Record<string, unknown> | string |...)` |
| `startTransaction()` |
| `commit()` |
| `rollback()` |
| `tables()` |
| `columns(table: string)` |
| `lastInsertId()` |
| `close()` |
| `tableExists(name: string)` |
| `createTable(name: string, columns: Record<string, FieldDefinition>)` |
| `getTableColumns(name: string)` |
| `addColumn(table: string, colName: string, def: FieldDefinition)` |

### Node — `FakeData` (`orm/src/fakeData.ts`)

| Method | 
|--------|
| `super(seed)` |
| `name()` |
| `numeric(min = 0, max = 1000, decimals = 2)` |
| `datetime(startYear = 2020, endYear = 2025)` |
| `forField(fieldDef: FieldDefinition, columnName?: string)` |

### Node — `QueryBuilder` (`orm/src/queryBuilder.ts`)

| Method | 
|--------|
| `from(tableName: string, db?: DatabaseAdapter)` |
| `select(...cols: string[])` |
| `where(condition: string, params: unknown[] = [])` |
| `orWhere(condition: string, params: unknown[] = [])` |
| `join(table: string, onClause: string)` |
| `leftJoin(table: string, onClause: string)` |
| `groupBy(column: string)` |
| `having(expression: string, params: unknown[] = [])` |
| `orderBy(expression: string)` |
| `limit(count: number, offset?: number)` |
| `toSql()` |
| `get(T = Record<string, unknown>>()` |
| `first(T = Record<string, unknown>>()` |
| `count()` |
| `exists()` |
| `toMongo()` |

### Node — `SQLTranslator` (`orm/src/sqlTranslation.ts`)

| Method | 
|--------|
| `limitToRows(sql: string)` |
| `limitToTop(sql: string)` |
| `concatPipesToFunc(sql: string)` |
| `booleanToInt(sql: string)` |
| `ilikeToLike(sql: string)` |
| `autoIncrementSyntax(sql: string, engine: string)` |
| `placeholderStyle(sql: string, style: string)` |
| `parseReturning(sql: string)` |
| `queryKey(sql: string, params?: unknown[])` |
| `get(T>(key: string)` |
| `set(T>(key: string, value: T, ttl?: number)` |
| `has(key: string)` |
| `delete(key: string)` |
| `sweep()` |
| `clear()` |
| `size()` |
| `remember(T>(key: string, ttl: number, factory: ()` |

### Node — `FetchResult` (`orm/src/types.ts`)

| Method | 
|--------|
| `execute(sql: string, params?: unknown[])` |
| `executeMany(sql: string, paramsList: unknown[][])` |
| `query(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `fetch(T = Record<string, unknown>>(sql: string, params?: unknow...)` |
| `fetchOne(T = Record<string, unknown>>(sql: string, params?: unknown[])` |
| `insert(table: string, data: Record<string, unknown> | Record<str...)` |
| `update(table: string, data: Record<string, unknown>, filter: Rec...)` |
| `delete(table: string, filter: Record<string, unknown> | string |...)` |
| `startTransaction()` |
| `commit()` |
| `rollback()` |
| `tables()` |
| `columns(table: string)` |
| `lastInsertId()` |
| `close()` |
| `tableExists(name: string)` |
| `createTable(name: string, columns: Record<string, FieldDefinition>)` |
| `toPaginate(page = 1, perPage = 20)` |
| `first()` |
| `last()` |
| `isEmpty()` |
| `toArray()` |
| `toJSON()` |
