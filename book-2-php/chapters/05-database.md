# Chapter 5: Database

## 1. From Arrays to Real Data

In Chapters 2 and 3, all our data lived in PHP arrays that reset every time the server restarted. That is fine for learning routing and responses, but real applications need persistent storage. This chapter covers Tina4's database layer -- raw queries, parameterised queries, transactions, schema inspection, helper methods, and migrations.

Tina4 supports five database engines: SQLite, PostgreSQL, MySQL, Microsoft SQL Server, and Firebird. The API is the same across all of them. You switch databases by changing one line in `.env`.

---

## 2. Connecting to a Database

### The Default: SQLite

When you scaffold a project with `tina4 init`, Tina4 creates a SQLite database at `data/app.db`. The default `.env` includes:

```env
TINA4_DEBUG=true
```

With no explicit `DATABASE_URL`, Tina4 defaults to `sqlite:///data/app.db`. That is why the health check at `/health` already shows `"database": "connected"` without any configuration.

### Connection Strings for Other Databases

Set `DATABASE_URL` in `.env` to use a different engine:

```env
# SQLite (explicit)
DATABASE_URL=sqlite:///data/app.db

# PostgreSQL
DATABASE_URL=postgres://localhost:5432/myapp

# MySQL
DATABASE_URL=mysql://localhost:3306/myapp

# Microsoft SQL Server
DATABASE_URL=mssql://localhost:1433/myapp

# Firebird
DATABASE_URL=firebird://localhost:3050/path/to/database.fdb
```

### Separate Credentials

If you prefer to keep credentials out of the connection string (recommended for production), use separate environment variables:

```env
DATABASE_URL=postgres://localhost:5432/myapp
DATABASE_USERNAME=myuser
DATABASE_PASSWORD=secretpassword
```

Tina4 merges these with the connection string at startup. The credentials in the separate variables take precedence over any embedded in the URL.

### Verifying the Connection

After updating `.env`, restart the server and check:

```bash
curl http://localhost:7145/health
```

```json
{
  "status": "ok",
  "database": "connected",
  "uptime_seconds": 3,
  "version": "3.0.0",
  "framework": "tina4-php"
}
```

If the database is not reachable, you will see `"database": "disconnected"` with an error message.

---

## 3. Getting the Database Object

In your route handlers, access the database via the global `Tina4\Database` class:

```php
<?php
use Tina4\Route;
use Tina4\Database;

Route::get("/api/test-db", function ($request, $response) {
    $db = Database::getConnection();

    $result = $db->fetch("SELECT 1 + 1 AS answer");

    return $response->json($result);
});
```

```bash
curl http://localhost:7145/api/test-db
```

```json
{"answer": 2}
```

`Database::getConnection()` returns the active database connection. You call methods like `fetch()`, `execute()`, and `fetchOne()` on this object.

---

## 4. Raw Queries

### fetch() -- Get Multiple Rows

```php
$db = Database::getConnection();

// Returns an array of associative arrays
$products = $db->fetch("SELECT * FROM products WHERE price > 50");
```

Each row is an associative array with column names as keys:

```php
// $products looks like:
[
    ["id" => 1, "name" => "Keyboard", "price" => 79.99],
    ["id" => 4, "name" => "Standing Desk", "price" => 549.99]
]
```

### fetchOne() -- Get a Single Row

```php
$product = $db->fetchOne("SELECT * FROM products WHERE id = 1");
// Returns: ["id" => 1, "name" => "Keyboard", "price" => 79.99]
```

If no row matches, `fetchOne()` returns `null`.

### execute() -- Run a Statement

For INSERT, UPDATE, DELETE, and DDL statements that do not return rows:

```php
$db->execute("INSERT INTO products (name, price) VALUES ('Widget', 9.99)");
$db->execute("UPDATE products SET price = 89.99 WHERE id = 1");
$db->execute("DELETE FROM products WHERE id = 5");
$db->execute("CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, message TEXT, created_at TEXT)");
```

### Full Example: A Simple Query Route

```php
<?php
use Tina4\Route;
use Tina4\Database;

Route::get("/api/products", function ($request, $response) {
    $db = Database::getConnection();

    $products = $db->fetch("SELECT * FROM products ORDER BY name");

    return $response->json([
        "products" => $products,
        "count" => count($products)
    ]);
});
```

```bash
curl http://localhost:7145/api/products
```

```json
{
  "products": [
    {"id": 1, "name": "Keyboard", "price": 79.99, "in_stock": 1},
    {"id": 2, "name": "Mouse", "price": 29.99, "in_stock": 1},
    {"id": 3, "name": "Monitor", "price": 399.99, "in_stock": 0}
  ],
  "count": 3
}
```

---

## 5. Parameterised Queries

Never concatenate user input into SQL strings. This is how SQL injection attacks happen:

```php
// NEVER do this:
$db->fetch("SELECT * FROM products WHERE name = '" . $userInput . "'");
```

Instead, use parameterised queries. Pass parameters as the second argument:

```php
$db = Database::getConnection();

// Named parameters
$product = $db->fetchOne(
    "SELECT * FROM products WHERE id = :id",
    ["id" => 42]
);

// Positional parameters
$products = $db->fetch(
    "SELECT * FROM products WHERE price BETWEEN ? AND ? ORDER BY price",
    [10.00, 100.00]
);
```

The database driver handles escaping. Your input is never part of the SQL string.

### A Safe Search Endpoint

```php
<?php
use Tina4\Route;
use Tina4\Database;

Route::get("/api/products/search", function ($request, $response) {
    $db = Database::getConnection();

    $q = $request->query["q"] ?? "";
    $maxPrice = (float) ($request->query["max_price"] ?? 99999);

    if (empty($q)) {
        return $response->json(["error" => "Query parameter 'q' is required"], 400);
    }

    $products = $db->fetch(
        "SELECT * FROM products WHERE name LIKE :query AND price <= :maxPrice ORDER BY name",
        ["query" => "%" . $q . "%", "maxPrice" => $maxPrice]
    );

    return $response->json([
        "query" => $q,
        "max_price" => $maxPrice,
        "results" => $products,
        "count" => count($products)
    ]);
});
```

```bash
curl "http://localhost:7145/api/products/search?q=key&max_price=100"
```

```json
{
  "query": "key",
  "max_price": 100,
  "results": [
    {"id": 1, "name": "Wireless Keyboard", "price": 79.99, "in_stock": 1}
  ],
  "count": 1
}
```

---

## 6. Transactions

When you need multiple operations to succeed or fail together, use transactions:

```php
<?php
use Tina4\Route;
use Tina4\Database;

Route::post("/api/orders", function ($request, $response) {
    $db = Database::getConnection();
    $body = $request->body;

    try {
        $db->startTransaction();

        // Create the order
        $db->execute(
            "INSERT INTO orders (customer_id, total, status) VALUES (:customerId, :total, 'pending')",
            ["customerId" => $body["customer_id"], "total" => $body["total"]]
        );

        // Get the new order ID
        $order = $db->fetchOne("SELECT last_insert_rowid() AS id");
        $orderId = $order["id"];

        // Create order items
        foreach ($body["items"] as $item) {
            $db->execute(
                "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (:orderId, :productId, :qty, :price)",
                [
                    "orderId" => $orderId,
                    "productId" => $item["product_id"],
                    "qty" => $item["quantity"],
                    "price" => $item["price"]
                ]
            );

            // Decrease stock
            $db->execute(
                "UPDATE products SET stock = stock - :qty WHERE id = :productId",
                ["qty" => $item["quantity"], "productId" => $item["product_id"]]
            );
        }

        $db->commit();

        return $response->json(["order_id" => $orderId, "status" => "created"], 201);
    } catch (\Exception $e) {
        $db->rollback();
        return $response->json(["error" => "Order failed: " . $e->getMessage()], 500);
    }
});
```

If any step fails, `rollback()` undoes everything. The database is never left in a half-finished state.

**Important:** You must call `commit()` to save the changes. If you forget, the transaction will be rolled back when the connection closes.

---

## 7. Schema Inspection

Tina4 provides methods to inspect your database structure at runtime:

### getTables()

```php
$db = Database::getConnection();
$tables = $db->getTables();
```

Returns an array of table names:

```php
["orders", "order_items", "products", "users"]
```

### getColumns()

```php
$columns = $db->getColumns("products");
```

Returns an array of column definitions:

```php
[
    ["name" => "id", "type" => "INTEGER", "nullable" => false, "primary" => true],
    ["name" => "name", "type" => "TEXT", "nullable" => false, "primary" => false],
    ["name" => "price", "type" => "REAL", "nullable" => true, "primary" => false],
    ["name" => "in_stock", "type" => "INTEGER", "nullable" => true, "primary" => false]
]
```

### tableExists()

```php
if ($db->tableExists("products")) {
    // Table exists, safe to query
}
```

### A Schema Info Endpoint

```php
<?php
use Tina4\Route;
use Tina4\Database;

Route::get("/api/schema", function ($request, $response) {
    $db = Database::getConnection();
    $tables = $db->getTables();

    $schema = [];
    foreach ($tables as $table) {
        $schema[$table] = $db->getColumns($table);
    }

    return $response->json(["tables" => $schema]);
});
```

---

## 8. Batch Operations with executeMany()

Insert or update many rows efficiently:

```php
$db = Database::getConnection();

$products = [
    ["name" => "Widget A", "price" => 9.99],
    ["name" => "Widget B", "price" => 14.99],
    ["name" => "Widget C", "price" => 19.99],
    ["name" => "Widget D", "price" => 24.99]
];

$db->executeMany(
    "INSERT INTO products (name, price) VALUES (:name, :price)",
    $products
);
```

`executeMany()` prepares the statement once and executes it for each item in the array. This is significantly faster than calling `execute()` in a loop because the SQL only needs to be parsed once.

---

## 9. Helper Methods: insert(), update(), delete()

Tina4 provides shorthand methods so you do not have to write SQL for simple operations.

### insert()

```php
$db = Database::getConnection();

// Insert a single row
$db->insert("products", [
    "name" => "Wireless Mouse",
    "price" => 34.99,
    "in_stock" => 1
]);

// Insert multiple rows
$db->insert("products", [
    ["name" => "USB Cable", "price" => 9.99, "in_stock" => 1],
    ["name" => "HDMI Cable", "price" => 14.99, "in_stock" => 1],
    ["name" => "DisplayPort Cable", "price" => 19.99, "in_stock" => 0]
]);
```

### update()

```php
// Update rows matching a filter
$db->update("products", ["price" => 39.99, "in_stock" => 1], "id = :id", ["id" => 7]);
```

The third argument is the WHERE clause, and the fourth is the parameters for it.

### delete()

```php
// Delete rows matching a filter
$db->delete("products", "id = :id", ["id" => 7]);
```

These helper methods generate the SQL for you. They are convenient for simple CRUD operations but do not replace raw queries for complex joins, subqueries, or aggregations.

---

## 10. Migrations

Migrations are versioned SQL scripts that evolve your database schema over time. Instead of manually running `CREATE TABLE` statements, you write migration files and Tina4 applies them in order.

### Creating a Migration

Use the CLI:

```bash
tina4 migrate:create create_products_table
```

```
Created migration: src/migrations/20260322143000_create_products_table.sql
```

The filename starts with a timestamp so migrations always run in chronological order.

Edit the generated file `src/migrations/20260322143000_create_products_table.sql`:

```sql
-- UP
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL DEFAULT 'Uncategorized',
    price REAL NOT NULL DEFAULT 0.00,
    in_stock INTEGER NOT NULL DEFAULT 1,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- DOWN
DROP TABLE IF EXISTS products;
```

The `-- UP` section runs when applying the migration. The `-- DOWN` section runs when rolling back.

### Running Migrations

```bash
tina4 migrate
```

```
Running migrations...
  [APPLIED] 20260322143000_create_products_table.sql
Migrations complete. 1 applied.
```

### Checking Migration Status

```bash
tina4 migrate:status
```

```
Migration                                    Status     Applied At
---------                                    ------     ----------
20260322143000_create_products_table.sql      applied    2026-03-22 14:30:00
20260322150000_create_orders_table.sql        pending    -
```

### Rolling Back

```bash
tina4 migrate:rollback
```

```
Rolling back last migration...
  [ROLLED BACK] 20260322150000_create_orders_table.sql
Rollback complete. 1 rolled back.
```

This runs the `-- DOWN` section of the most recently applied migration.

### A Real Migration Sequence

Here is what a typical project's migrations look like:

```
src/migrations/
├── 20260322143000_create_products_table.sql
├── 20260322143100_create_users_table.sql
├── 20260322143200_create_orders_table.sql
├── 20260322143300_create_order_items_table.sql
└── 20260323091500_add_email_index_to_users.sql
```

The last migration might look like:

```sql
-- UP
CREATE INDEX idx_users_email ON users (email);

-- DOWN
DROP INDEX IF EXISTS idx_users_email;
```

Migrations are applied in filename order. Each migration runs only once -- Tina4 tracks which ones have been applied in a `_migrations` table.

---

## 11. Query Caching

For read-heavy applications, enable query caching:

```env
TINA4_DB_CACHE=true
```

When enabled, Tina4 caches the results of `fetch()` and `fetchOne()` calls. Identical queries with identical parameters return cached results instead of hitting the database again.

The cache is automatically invalidated when you call `execute()`, `insert()`, `update()`, or `delete()` on the same table.

You can also control caching per-query:

```php
// Force a fresh query (bypass cache)
$products = $db->fetch("SELECT * FROM products", [], false); // third arg = use cache

// Clear the entire cache
$db->clearCache();
```

---

## 12. Exercise: Build a Notes App

Build a notes application backed by SQLite. Create the database table via a migration and build a full CRUD API.

### Requirements

1. Create a migration that creates a `notes` table with columns:
   - `id` -- integer, primary key, auto-increment
   - `title` -- text, not null
   - `content` -- text, not null
   - `tag` -- text, default "general"
   - `created_at` -- text, default current timestamp
   - `updated_at` -- text, default current timestamp

2. Build these API endpoints:

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/notes` | List all notes. Support `?tag=` and `?search=` filters. |
| `GET` | `/api/notes/{id:int}` | Get a single note. 404 if not found. |
| `POST` | `/api/notes` | Create a note. Validate title and content are not empty. |
| `PUT` | `/api/notes/{id:int}` | Update a note. 404 if not found. |
| `DELETE` | `/api/notes/{id:int}` | Delete a note. 204 on success, 404 if not found. |

### Test with:

```bash
# Create
curl -X POST http://localhost:7145/api/notes \
  -H "Content-Type: application/json" \
  -d '{"title": "Shopping List", "content": "Milk, eggs, bread", "tag": "personal"}'

# List all
curl http://localhost:7145/api/notes

# Search
curl "http://localhost:7145/api/notes?search=shopping"

# Filter by tag
curl "http://localhost:7145/api/notes?tag=personal"

# Get one
curl http://localhost:7145/api/notes/1

# Update
curl -X PUT http://localhost:7145/api/notes/1 \
  -H "Content-Type: application/json" \
  -d '{"title": "Updated Shopping List", "content": "Milk, eggs, bread, butter"}'

# Delete
curl -X DELETE http://localhost:7145/api/notes/1
```

---

## 13. Solution

### Migration

Create `src/migrations/20260322143000_create_notes_table.sql`:

```sql
-- UP
CREATE TABLE notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    content TEXT NOT NULL,
    tag TEXT NOT NULL DEFAULT 'general',
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- DOWN
DROP TABLE IF EXISTS notes;
```

Run the migration:

```bash
tina4 migrate
```

```
Running migrations...
  [APPLIED] 20260322143000_create_notes_table.sql
Migrations complete. 1 applied.
```

### Routes

Create `src/routes/notes.php`:

```php
<?php
use Tina4\Route;
use Tina4\Database;

// List all notes with optional filters
Route::get("/api/notes", function ($request, $response) {
    $db = Database::getConnection();

    $tag = $request->query["tag"] ?? "";
    $search = $request->query["search"] ?? "";

    $sql = "SELECT * FROM notes";
    $params = [];
    $conditions = [];

    if (!empty($tag)) {
        $conditions[] = "tag = :tag";
        $params["tag"] = $tag;
    }

    if (!empty($search)) {
        $conditions[] = "(title LIKE :search OR content LIKE :search)";
        $params["search"] = "%" . $search . "%";
    }

    if (!empty($conditions)) {
        $sql .= " WHERE " . implode(" AND ", $conditions);
    }

    $sql .= " ORDER BY updated_at DESC";

    $notes = $db->fetch($sql, $params);

    return $response->json([
        "notes" => $notes,
        "count" => count($notes)
    ]);
});

// Get a single note
Route::get("/api/notes/{id:int}", function ($request, $response) {
    $db = Database::getConnection();
    $id = $request->params["id"];

    $note = $db->fetchOne("SELECT * FROM notes WHERE id = :id", ["id" => $id]);

    if ($note === null) {
        return $response->json(["error" => "Note not found", "id" => $id], 404);
    }

    return $response->json($note);
});

// Create a note
Route::post("/api/notes", function ($request, $response) {
    $db = Database::getConnection();
    $body = $request->body;

    // Validate
    $errors = [];
    if (empty($body["title"])) {
        $errors[] = "Title is required";
    }
    if (empty($body["content"])) {
        $errors[] = "Content is required";
    }
    if (!empty($errors)) {
        return $response->json(["errors" => $errors], 400);
    }

    $db->execute(
        "INSERT INTO notes (title, content, tag) VALUES (:title, :content, :tag)",
        [
            "title" => $body["title"],
            "content" => $body["content"],
            "tag" => $body["tag"] ?? "general"
        ]
    );

    $note = $db->fetchOne("SELECT * FROM notes WHERE id = last_insert_rowid()");

    return $response->json($note, 201);
});

// Update a note
Route::put("/api/notes/{id:int}", function ($request, $response) {
    $db = Database::getConnection();
    $id = $request->params["id"];
    $body = $request->body;

    $existing = $db->fetchOne("SELECT * FROM notes WHERE id = :id", ["id" => $id]);

    if ($existing === null) {
        return $response->json(["error" => "Note not found", "id" => $id], 404);
    }

    $db->execute(
        "UPDATE notes SET title = :title, content = :content, tag = :tag, updated_at = CURRENT_TIMESTAMP WHERE id = :id",
        [
            "title" => $body["title"] ?? $existing["title"],
            "content" => $body["content"] ?? $existing["content"],
            "tag" => $body["tag"] ?? $existing["tag"],
            "id" => $id
        ]
    );

    $note = $db->fetchOne("SELECT * FROM notes WHERE id = :id", ["id" => $id]);

    return $response->json($note);
});

// Delete a note
Route::delete("/api/notes/{id:int}", function ($request, $response) {
    $db = Database::getConnection();
    $id = $request->params["id"];

    $existing = $db->fetchOne("SELECT * FROM notes WHERE id = :id", ["id" => $id]);

    if ($existing === null) {
        return $response->json(["error" => "Note not found", "id" => $id], 404);
    }

    $db->execute("DELETE FROM notes WHERE id = :id", ["id" => $id]);

    return $response->json(null, 204);
});
```

**Expected output for create:**

```json
{
  "id": 1,
  "title": "Shopping List",
  "content": "Milk, eggs, bread",
  "tag": "personal",
  "created_at": "2026-03-22 14:30:00",
  "updated_at": "2026-03-22 14:30:00"
}
```

(Status: `201 Created`)

**Expected output for list:**

```json
{
  "notes": [
    {
      "id": 1,
      "title": "Shopping List",
      "content": "Milk, eggs, bread",
      "tag": "personal",
      "created_at": "2026-03-22 14:30:00",
      "updated_at": "2026-03-22 14:30:00"
    }
  ],
  "count": 1
}
```

**Expected output for search:**

```json
{
  "notes": [
    {
      "id": 1,
      "title": "Shopping List",
      "content": "Milk, eggs, bread",
      "tag": "personal",
      "created_at": "2026-03-22 14:30:00",
      "updated_at": "2026-03-22 14:30:00"
    }
  ],
  "count": 1
}
```

**Expected output for validation error:**

```json
{"errors": ["Title is required", "Content is required"]}
```

(Status: `400 Bad Request`)

---

## 14. Gotchas

### 1. Forgetting commit()

**Problem:** You call `startTransaction()`, run your queries, but the changes disappear on the next request.

**Cause:** Without `commit()`, the transaction is rolled back when the connection closes.

**Fix:** Always call `$db->commit()` after your transaction succeeds. Use a try/catch block with `$db->rollback()` in the catch.

### 2. Connection String Formats

**Problem:** The database will not connect and you see a cryptic error about the connection string.

**Cause:** Each database engine expects a specific URL format. A common mistake is using `mysql://user:pass@host/db` when the engine expects the port.

**Fix:** Always include the port: `mysql://localhost:3306/mydb`. Here are the default ports:

| Engine | Default Port |
|--------|-------------|
| PostgreSQL | 5432 |
| MySQL | 3306 |
| MSSQL | 1433 |
| Firebird | 3050 |
| SQLite | (file path, no port) |

### 3. SQLite File Paths

**Problem:** SQLite creates a new empty database instead of using the existing one.

**Cause:** The path in `DATABASE_URL` is relative and resolves to the wrong directory, or you used `sqlite://` (two slashes) instead of `sqlite:///` (three slashes).

**Fix:** Use three slashes for a relative path: `sqlite:///data/app.db`. For an absolute path, use four slashes: `sqlite:////var/data/app.db`. The third slash separates the scheme from the path; the fourth starts the absolute path.

### 4. Parameterised Queries with LIKE

**Problem:** `WHERE name LIKE :q` with `["q" => "%search%"]` works, but `WHERE name LIKE '%:q%'` does not.

**Cause:** Parameters inside quotes are treated as literal text, not as placeholders.

**Fix:** Include the `%` wildcards in the parameter value, not in the SQL: `["q" => "%" . $search . "%"]`. The SQL should be `WHERE name LIKE :q`.

### 5. Boolean Values in SQLite

**Problem:** You insert `true` or `false` but the database stores `1` or `0`. When you read it back, you get integers, not booleans.

**Cause:** SQLite does not have a native boolean type. It stores booleans as integers.

**Fix:** Cast in your PHP code: `"in_stock" => (bool) $row["in_stock"]`. Or accept that `1` and `0` work as truthy/falsy in PHP.

### 6. Migration Already Applied

**Problem:** You edited a migration file and ran `tina4 migrate` again, but nothing changed.

**Cause:** Tina4 tracks applied migrations by filename. Once applied, a migration will not run again even if you change its contents.

**Fix:** Create a new migration for schema changes. Do not edit applied migrations. If you are in early development and want to start fresh, use `tina4 migrate:rollback` to undo and then `tina4 migrate` to reapply.

### 7. fetch() Returns Empty Array, Not Null

**Problem:** You check `if ($result === null)` but it never matches, even when the table is empty.

**Cause:** `fetch()` always returns an array. An empty result is `[]`, not `null`. Only `fetchOne()` returns `null` when no row matches.

**Fix:** Check with `if (empty($result))` or `if (count($result) === 0)`.
