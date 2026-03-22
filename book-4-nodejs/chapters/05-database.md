# Chapter 5: Database

## 1. From Arrays to Real Data

In Chapters 2 and 3, all your data lived in TypeScript arrays. Server restart. Data gone. That works for learning routing and responses. Real applications need persistent storage.

This chapter covers Tina4's database layer: raw queries, parameterised queries, transactions, schema inspection, helper methods, and migrations.

Tina4 speaks to five database engines: SQLite, PostgreSQL, MySQL, Microsoft SQL Server, and Firebird. The API is identical across all of them. One line in `.env` switches the engine.

---

## 2. Connecting to a Database

### The Default: SQLite

When you scaffold a project with `tina4 init`, Tina4 drops a SQLite database at `data/app.db`. The default `.env` includes:

```env
TINA4_DEBUG=true
```

With no explicit `DATABASE_URL`, Tina4 defaults to `sqlite:///data/app.db`. That is why the health check at `/health` shows `"database": "connected"` with zero configuration.

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

```env
DATABASE_URL=postgres://localhost:5432/myapp
DATABASE_USERNAME=myuser
DATABASE_PASSWORD=secretpassword
```

### Verifying the Connection

```bash
curl http://localhost:7148/health
```

```json
{
  "status": "ok",
  "database": "connected",
  "uptime_seconds": 3,
  "version": "3.0.0",
  "framework": "tina4-nodejs"
}
```

---

## 3. Getting the Database Object

In your route handlers, access the database via the `Database` class:

```typescript
import { Router, Database } from "tina4-nodejs";

Router.get("/api/test-db", async (req, res) => {
    const db = Database.getConnection();

    const result = await db.fetch("SELECT 1 + 1 AS answer");

    return res.json(result);
});
```

```bash
curl http://localhost:7148/api/test-db
```

```json
{"answer": 2}
```

`Database.getConnection()` returns the active database connection. Call `fetch()`, `execute()`, and `fetchOne()` on this object. All database methods are async. All return Promises.

---

## 4. Raw Queries

### fetch() -- Get Multiple Rows

```typescript
const db = Database.getConnection();

const products = await db.fetch("SELECT * FROM products WHERE price > 50");
```

Each row is a plain object with column names as keys:

```typescript
// products looks like:
[
    { id: 1, name: "Keyboard", price: 79.99 },
    { id: 4, name: "Standing Desk", price: 549.99 }
]
```

### fetchOne() -- Get a Single Row

```typescript
const product = await db.fetchOne("SELECT * FROM products WHERE id = 1");
// Returns: { id: 1, name: "Keyboard", price: 79.99 }
```

If no row matches, `fetchOne()` returns `null`.

### execute() -- Run a Statement

For INSERT, UPDATE, DELETE, and DDL statements that do not return rows:

```typescript
await db.execute("INSERT INTO products (name, price) VALUES ('Widget', 9.99)");
await db.execute("UPDATE products SET price = 89.99 WHERE id = 1");
await db.execute("DELETE FROM products WHERE id = 5");
await db.execute("CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY, message TEXT, created_at TEXT)");
```

### Full Example: A Simple Query Route

```typescript
import { Router, Database } from "tina4-nodejs";

Router.get("/api/products", async (req, res) => {
    const db = Database.getConnection();

    const products = await db.fetch("SELECT * FROM products ORDER BY name");

    return res.json({
        products,
        count: products.length
    });
});
```

---

## 5. Parameterised Queries

Never concatenate user input into SQL strings. That door leads to SQL injection:

```typescript
// NEVER do this:
await db.fetch(`SELECT * FROM products WHERE name = '${userInput}'`);
```

Instead, use parameterised queries:

```typescript
const db = Database.getConnection();

// Named parameters
const product = await db.fetchOne(
    "SELECT * FROM products WHERE id = :id",
    { id: 42 }
);

// Positional parameters
const products = await db.fetch(
    "SELECT * FROM products WHERE price BETWEEN ? AND ? ORDER BY price",
    [10.00, 100.00]
);
```

### A Safe Search Endpoint

```typescript
import { Router, Database } from "tina4-nodejs";

Router.get("/api/products/search", async (req, res) => {
    const db = Database.getConnection();

    const q = req.query.q ?? "";
    const maxPrice = parseFloat(req.query.max_price ?? "99999");

    if (!q) {
        return res.status(400).json({ error: "Query parameter 'q' is required" });
    }

    const products = await db.fetch(
        "SELECT * FROM products WHERE name LIKE :query AND price <= :maxPrice ORDER BY name",
        { query: `%${q}%`, maxPrice }
    );

    return res.json({
        query: q,
        max_price: maxPrice,
        results: products,
        count: products.length
    });
});
```

```bash
curl "http://localhost:7148/api/products/search?q=key&max_price=100"
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

```typescript
import { Router, Database } from "tina4-nodejs";

Router.post("/api/orders", async (req, res) => {
    const db = Database.getConnection();
    const body = req.body;

    try {
        await db.startTransaction();

        await db.execute(
            "INSERT INTO orders (customer_id, total, status) VALUES (:customerId, :total, 'pending')",
            { customerId: body.customer_id, total: body.total }
        );

        const order = await db.fetchOne("SELECT last_insert_rowid() AS id");
        const orderId = order.id;

        for (const item of body.items) {
            await db.execute(
                "INSERT INTO order_items (order_id, product_id, quantity, price) VALUES (:orderId, :productId, :qty, :price)",
                {
                    orderId,
                    productId: item.product_id,
                    qty: item.quantity,
                    price: item.price
                }
            );

            await db.execute(
                "UPDATE products SET stock = stock - :qty WHERE id = :productId",
                { qty: item.quantity, productId: item.product_id }
            );
        }

        await db.commit();

        return res.status(201).json({ order_id: orderId, status: "created" });
    } catch (e) {
        await db.rollback();
        return res.status(500).json({ error: `Order failed: ${e.message}` });
    }
});
```

---

## 7. Schema Inspection

### getTables()

```typescript
const db = Database.getConnection();
const tables = await db.getTables();
// Returns: ["orders", "order_items", "products", "users"]
```

### getColumns()

```typescript
const columns = await db.getColumns("products");
// Returns: [
//     { name: "id", type: "INTEGER", nullable: false, primary: true },
//     { name: "name", type: "TEXT", nullable: false, primary: false },
//     ...
// ]
```

### tableExists()

```typescript
if (await db.tableExists("products")) {
    // Table exists, safe to query
}
```

---

## 8. Batch Operations with executeMany()

Insert or update many rows efficiently:

```typescript
const db = Database.getConnection();

const products = [
    { name: "Widget A", price: 9.99 },
    { name: "Widget B", price: 14.99 },
    { name: "Widget C", price: 19.99 },
    { name: "Widget D", price: 24.99 }
];

await db.executeMany(
    "INSERT INTO products (name, price) VALUES (:name, :price)",
    products
);
```

---

## 9. Helper Methods: insert(), update(), delete()

### insert()

```typescript
const db = Database.getConnection();

await db.insert("products", {
    name: "Wireless Mouse",
    price: 34.99,
    in_stock: 1
});

// Insert multiple rows
await db.insert("products", [
    { name: "USB Cable", price: 9.99, in_stock: 1 },
    { name: "HDMI Cable", price: 14.99, in_stock: 1 }
]);
```

### update()

```typescript
await db.update("products", { price: 39.99, in_stock: 1 }, "id = :id", { id: 7 });
```

### delete()

```typescript
await db.delete("products", "id = :id", { id: 7 });
```

---

## 10. Migrations

Migrations are versioned SQL scripts. They evolve your database schema over time. Each migration runs once. Never again.

### Creating a Migration

```bash
tina4 migrate:create create_products_table
```

```
Created migration: src/migrations/20260322143000_create_products_table.sql
```

Edit the generated file:

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

### Running Migrations

```bash
tina4 migrate
```

```
Running migrations...
  [APPLIED] 20260322143000_create_products_table.sql
Migrations complete. 1 applied.
```

### Checking Status and Rolling Back

```bash
tina4 migrate:status
tina4 migrate:rollback
```

---

## 11. Query Caching

Enable query caching in `.env`:

```env
TINA4_DB_CACHE=true
```

Identical queries with identical parameters return cached results. The cache invalidates itself when you call `execute()`, `insert()`, `update()`, or `delete()` on the same table.

```typescript
// Force a fresh query (bypass cache)
const products = await db.fetch("SELECT * FROM products", [], { noCache: true });

// Clear the entire cache
await db.clearCache();
```

---

## 12. Exercise: Build a Notes App

Build a notes application backed by SQLite. Create the database table via a migration and build a full CRUD API.

### Requirements

1. Create a migration for a `notes` table with: `id`, `title`, `content`, `tag`, `created_at`, `updated_at`

2. Build these API endpoints:

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/notes` | List all notes. Support `?tag=` and `?search=` filters. |
| `GET` | `/api/notes/{id:int}` | Get a single note. 404 if not found. |
| `POST` | `/api/notes` | Create a note. Validate title and content are not empty. |
| `PUT` | `/api/notes/{id:int}` | Update a note. 404 if not found. |
| `DELETE` | `/api/notes/{id:int}` | Delete a note. 204 on success, 404 if not found. |

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

```bash
tina4 migrate
```

### Routes

Create `src/routes/notes.ts`:

```typescript
import { Router, Database } from "tina4-nodejs";

Router.get("/api/notes", async (req, res) => {
    const db = Database.getConnection();
    const tag = req.query.tag ?? "";
    const search = req.query.search ?? "";

    let sql = "SELECT * FROM notes";
    const params: Record<string, any> = {};
    const conditions: string[] = [];

    if (tag) {
        conditions.push("tag = :tag");
        params.tag = tag;
    }

    if (search) {
        conditions.push("(title LIKE :search OR content LIKE :search)");
        params.search = `%${search}%`;
    }

    if (conditions.length > 0) {
        sql += " WHERE " + conditions.join(" AND ");
    }

    sql += " ORDER BY updated_at DESC";

    const notes = await db.fetch(sql, params);

    return res.json({ notes, count: notes.length });
});

Router.get("/api/notes/{id:int}", async (req, res) => {
    const db = Database.getConnection();
    const id = req.params.id;

    const note = await db.fetchOne("SELECT * FROM notes WHERE id = :id", { id });

    if (note === null) {
        return res.status(404).json({ error: "Note not found", id });
    }

    return res.json(note);
});

Router.post("/api/notes", async (req, res) => {
    const db = Database.getConnection();
    const body = req.body;

    const errors: string[] = [];
    if (!body.title) errors.push("Title is required");
    if (!body.content) errors.push("Content is required");

    if (errors.length > 0) {
        return res.status(400).json({ errors });
    }

    await db.execute(
        "INSERT INTO notes (title, content, tag) VALUES (:title, :content, :tag)",
        {
            title: body.title,
            content: body.content,
            tag: body.tag ?? "general"
        }
    );

    const note = await db.fetchOne("SELECT * FROM notes WHERE id = last_insert_rowid()");

    return res.status(201).json(note);
});

Router.put("/api/notes/{id:int}", async (req, res) => {
    const db = Database.getConnection();
    const id = req.params.id;
    const body = req.body;

    const existing = await db.fetchOne("SELECT * FROM notes WHERE id = :id", { id });

    if (existing === null) {
        return res.status(404).json({ error: "Note not found", id });
    }

    await db.execute(
        "UPDATE notes SET title = :title, content = :content, tag = :tag, updated_at = CURRENT_TIMESTAMP WHERE id = :id",
        {
            title: body.title ?? existing.title,
            content: body.content ?? existing.content,
            tag: body.tag ?? existing.tag,
            id
        }
    );

    const note = await db.fetchOne("SELECT * FROM notes WHERE id = :id", { id });

    return res.json(note);
});

Router.delete("/api/notes/{id:int}", async (req, res) => {
    const db = Database.getConnection();
    const id = req.params.id;

    const existing = await db.fetchOne("SELECT * FROM notes WHERE id = :id", { id });

    if (existing === null) {
        return res.status(404).json({ error: "Note not found", id });
    }

    await db.execute("DELETE FROM notes WHERE id = :id", { id });

    return res.status(204).json(null);
});
```

**Expected output for create (Status: `201 Created`):**

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

---

## 14. Gotchas

### 1. Forgetting await

**Problem:** Database operations return `Promise {<pending>}` instead of results.

**Cause:** You forgot to `await` the database call. All Tina4 database methods are async.

**Fix:** Always `await` database calls: `const result = await db.fetch(...)`.

### 2. Connection String Formats

**Problem:** The database will not connect.

**Cause:** Each database engine expects a specific URL format. A common mistake is omitting the port.

**Fix:** Always include the port. Default ports: PostgreSQL 5432, MySQL 3306, MSSQL 1433, Firebird 3050.

### 3. SQLite File Paths

**Problem:** SQLite creates a new empty database instead of using the existing one.

**Cause:** Use three slashes for a relative path: `sqlite:///data/app.db`. Four slashes for absolute: `sqlite:////var/data/app.db`.

### 4. Parameterised Queries with LIKE

**Problem:** `WHERE name LIKE '%:q%'` does not work.

**Cause:** Parameters inside quotes are literal text, not placeholders.

**Fix:** Include the `%` in the parameter value: `{ q: "%" + search + "%" }`. The SQL should be `WHERE name LIKE :q`.

### 5. Boolean Values in SQLite

**Problem:** SQLite stores booleans as integers (1 and 0).

**Fix:** Cast in your TypeScript code: `inStock: Boolean(row.in_stock)`.

### 6. Migration Already Applied

**Problem:** You edited a migration file and ran `tina4 migrate` again, but nothing changed.

**Cause:** Once applied, a migration will not run again.

**Fix:** Create a new migration for schema changes. Do not edit applied migrations.

### 7. fetch() Returns Empty Array, Not Null

**Problem:** You check `if (result === null)` but it never matches when the table is empty.

**Cause:** `fetch()` always returns an array. Only `fetchOne()` returns `null`.

**Fix:** Check with `if (result.length === 0)`.
