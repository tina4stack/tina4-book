# Chapter 6: ORM

## 1. From SQL to Objects

In Chapter 5 you wrote raw SQL for every operation. That works, but it gets tedious. You end up writing the same `INSERT INTO products (name, price, ...) VALUES (:name, :price, ...)` patterns over and over. The ORM (Object-Relational Mapper) lets you work with PHP classes instead. You define a class, map it to a table, and call methods like `save()`, `load()`, and `delete()`.

Tina4's ORM is minimal by design. It does not try to hide SQL completely -- it gives you convenient methods for common operations and stays out of the way when you need raw queries.

---

## 2. Defining a Model

ORM models live in `src/orm/`. Every `.php` file in that directory is auto-loaded, just like route files.

Create `src/orm/Product.php`:

```php
<?php
use Tina4\ORM;

class Product extends ORM
{
    public int $id;
    public string $name;
    public string $category = "Uncategorized";
    public float $price = 0.00;
    public bool $inStock = true;
    public string $createdAt;
    public string $updatedAt;

    // Map to the "products" table
    public string $tableName = "products";

    // Primary key field
    public string $primaryKey = "id";
}
```

That is a complete model. Let us break it down:

- **Extends `ORM`** -- This gives you `save()`, `load()`, `delete()`, `select()`, and other methods.
- **Public properties** -- Each property maps to a database column. The property name is `camelCase` and the column name is `snake_case`. Tina4 converts between them automatically: `inStock` maps to `in_stock`, `createdAt` maps to `created_at`.
- **`$tableName`** -- The database table this model maps to. If you omit it, Tina4 infers it from the class name: `Product` becomes `products`, `OrderItem` becomes `order_items`.
- **`$primaryKey`** -- The primary key column. Defaults to `"id"`.
- **Default values** -- Properties with defaults (like `$category = "Uncategorized"`) are used when creating new records without specifying those fields.

---

## 3. Field Types

Use PHP type declarations on your properties. Tina4 uses these types when generating DDL and validating data:

| PHP Type | Database Type (SQLite) | Database Type (PostgreSQL) | Notes |
|----------|----------------------|---------------------------|-------|
| `int` | INTEGER | INTEGER | Whole numbers |
| `string` | TEXT | VARCHAR(255) | Text fields |
| `float` | REAL | DOUBLE PRECISION | Decimal numbers |
| `bool` | INTEGER | BOOLEAN | SQLite stores as 0/1 |
| `?string` | TEXT (nullable) | VARCHAR(255) NULL | Nullable with `?` prefix |

### Nullable Fields

Use PHP's nullable type syntax:

```php
public ?string $description = null;
public ?float $discount = null;
```

A nullable property allows `null` values in the database column.

### Primary Keys and Auto-Increment

By default, Tina4 treats the `$primaryKey` field as auto-incrementing. When you call `save()` on a new object (where the primary key is not set), the database generates the ID:

```php
$product = new Product();
$product->name = "Widget";
$product->price = 9.99;
$product->save();

echo $product->id; // Auto-generated: 1, 2, 3, ...
```

---

## 4. Creating and Saving Records

### save() -- Insert or Update

The `save()` method inserts a new record or updates an existing one, depending on whether the primary key is set:

```php
<?php
use Tina4\Route;

Route::post("/api/products", function ($request, $response) {
    $body = $request->body;

    $product = new Product();
    $product->name = $body["name"];
    $product->category = $body["category"] ?? "Uncategorized";
    $product->price = (float) ($body["price"] ?? 0);
    $product->inStock = (bool) ($body["in_stock"] ?? true);
    $product->save();

    return $response->json($product->toDict(), 201);
});
```

```bash
curl -X POST http://localhost:7145/api/products \
  -H "Content-Type: application/json" \
  -d '{"name": "Wireless Keyboard", "category": "Electronics", "price": 79.99}'
```

```json
{
  "id": 1,
  "name": "Wireless Keyboard",
  "category": "Electronics",
  "price": 79.99,
  "in_stock": true,
  "created_at": "2026-03-22 14:30:00",
  "updated_at": "2026-03-22 14:30:00"
}
```

### Updating an Existing Record

When `id` is already set, `save()` performs an UPDATE:

```php
Route::put("/api/products/{id:int}", function ($request, $response) {
    $product = new Product();
    $product->load($request->params["id"]);

    if (empty($product->id)) {
        return $response->json(["error" => "Product not found"], 404);
    }

    $body = $request->body;
    $product->name = $body["name"] ?? $product->name;
    $product->price = (float) ($body["price"] ?? $product->price);
    $product->category = $body["category"] ?? $product->category;
    $product->save();

    return $response->json($product->toDict());
});
```

---

## 5. Loading Records

### load() -- Get by Primary Key

```php
$product = new Product();
$product->load(42);

if (empty($product->id)) {
    // Product with ID 42 not found
}
```

`load()` populates the object's properties from the database row matching the primary key. If no row matches, the properties remain at their default values (or unset).

### A Simple Get Endpoint

```php
Route::get("/api/products/{id:int}", function ($request, $response) {
    $product = new Product();
    $product->load($request->params["id"]);

    if (empty($product->id)) {
        return $response->json(["error" => "Product not found"], 404);
    }

    return $response->json($product->toDict());
});
```

```bash
curl http://localhost:7145/api/products/1
```

```json
{
  "id": 1,
  "name": "Wireless Keyboard",
  "category": "Electronics",
  "price": 79.99,
  "in_stock": true,
  "created_at": "2026-03-22 14:30:00",
  "updated_at": "2026-03-22 14:30:00"
}
```

---

## 6. Deleting Records

### delete()

```php
Route::delete("/api/products/{id:int}", function ($request, $response) {
    $product = new Product();
    $product->load($request->params["id"]);

    if (empty($product->id)) {
        return $response->json(["error" => "Product not found"], 404);
    }

    $product->delete();

    return $response->json(null, 204);
});
```

`delete()` removes the row from the database. The object still exists in memory but the database row is gone.

---

## 7. Querying with select()

The `select()` method lets you find records with filters, ordering, and pagination:

### Basic Select

```php
$product = new Product();
$products = $product->select("*");
```

Returns an array of Product objects with all records.

### Filtering

```php
$product = new Product();

// Simple filter
$electronics = $product->select("*", "category = :category", ["category" => "Electronics"]);

// Multiple conditions
$affordable = $product->select("*", "price < :maxPrice AND in_stock = :inStock", [
    "maxPrice" => 100,
    "inStock" => 1
]);
```

### Ordering

```php
$product = new Product();
$sorted = $product->select("*", "", [], "price DESC");
```

The fourth argument is the ORDER BY clause.

### Pagination

```php
$product = new Product();

$page = 1;
$perPage = 10;
$offset = ($page - 1) * $perPage;

$products = $product->select("*", "", [], "name ASC", $perPage, $offset);
```

The fifth argument is LIMIT, the sixth is OFFSET.

### A Full List Endpoint with Filters

```php
<?php
use Tina4\Route;

Route::get("/api/products", function ($request, $response) {
    $product = new Product();

    $category = $request->query["category"] ?? "";
    $minPrice = (float) ($request->query["min_price"] ?? 0);
    $maxPrice = (float) ($request->query["max_price"] ?? 999999);
    $page = (int) ($request->query["page"] ?? 1);
    $perPage = (int) ($request->query["per_page"] ?? 20);
    $sort = $request->query["sort"] ?? "name";
    $order = strtoupper($request->query["order"] ?? "ASC");

    // Build filter
    $conditions = [];
    $params = [];

    if (!empty($category)) {
        $conditions[] = "category = :category";
        $params["category"] = $category;
    }

    $conditions[] = "price >= :minPrice AND price <= :maxPrice";
    $params["minPrice"] = $minPrice;
    $params["maxPrice"] = $maxPrice;

    $filter = implode(" AND ", $conditions);

    // Validate sort field
    $allowedSorts = ["name", "price", "category", "created_at"];
    if (!in_array($sort, $allowedSorts)) {
        $sort = "name";
    }
    if ($order !== "ASC" && $order !== "DESC") {
        $order = "ASC";
    }

    $offset = ($page - 1) * $perPage;

    $products = $product->select("*", $filter, $params, $sort . " " . $order, $perPage, $offset);

    $results = array_map(fn($p) => $p->toDict(), $products);

    return $response->json([
        "products" => $results,
        "page" => $page,
        "per_page" => $perPage,
        "count" => count($results)
    ]);
});
```

```bash
curl "http://localhost:7145/api/products?category=Electronics&sort=price&order=DESC&page=1&per_page=5"
```

```json
{
  "products": [
    {"id": 4, "name": "Standing Desk", "category": "Electronics", "price": 549.99, "in_stock": true},
    {"id": 1, "name": "Wireless Keyboard", "category": "Electronics", "price": 79.99, "in_stock": true}
  ],
  "page": 1,
  "per_page": 5,
  "count": 2
}
```

---

## 8. Creating Tables from Models

Instead of writing a migration manually, you can generate the table from your model:

```php
$product = new Product();
$product->createTable();
```

This reads the properties, types, and defaults from the model class and generates the appropriate `CREATE TABLE` statement for your database engine.

You can also use the CLI:

```bash
tina4 orm:create-table Product
```

```
Created table "products" with 7 columns.
```

This is convenient during early development. For production, use migrations (Chapter 5) so schema changes are versioned and reversible.

---

## 9. Relationships

### hasMany -- One-to-Many

A user has many posts:

Create `src/orm/User.php`:

```php
<?php
use Tina4\ORM;

class User extends ORM
{
    public int $id;
    public string $name;
    public string $email;
    public string $createdAt;

    public string $tableName = "users";
    public string $primaryKey = "id";

    public function posts(): array
    {
        return $this->hasMany(Post::class, "user_id");
    }
}
```

Create `src/orm/Post.php`:

```php
<?php
use Tina4\ORM;

class Post extends ORM
{
    public int $id;
    public int $userId;
    public string $title;
    public string $body;
    public string $createdAt;

    public string $tableName = "posts";
    public string $primaryKey = "id";

    public function user(): ?User
    {
        return $this->belongsTo(User::class, "user_id");
    }

    public function comments(): array
    {
        return $this->hasMany(Comment::class, "post_id");
    }
}
```

The second argument to `hasMany()` is the foreign key column on the related table. `$this->hasMany(Post::class, "user_id")` means: find all rows in `posts` where `user_id` equals this user's ID.

### hasOne -- One-to-One

```php
public function profile(): ?Profile
{
    return $this->hasOne(Profile::class, "user_id");
}
```

`hasOne()` works like `hasMany()` but returns a single object instead of an array.

### belongsTo -- Inverse Relationship

The inverse of `hasMany`. A post belongs to a user:

```php
public function user(): ?User
{
    return $this->belongsTo(User::class, "user_id");
}
```

`belongsTo(User::class, "user_id")` means: load the User where `users.id` equals `this->user_id`.

### Using Relationships

```php
Route::get("/api/users/{id:int}", function ($request, $response) {
    $user = new User();
    $user->load($request->params["id"]);

    if (empty($user->id)) {
        return $response->json(["error" => "User not found"], 404);
    }

    $posts = $user->posts();

    return $response->json([
        "user" => $user->toDict(),
        "posts" => array_map(fn($p) => $p->toDict(), $posts),
        "post_count" => count($posts)
    ]);
});
```

```bash
curl http://localhost:7145/api/users/1
```

```json
{
  "user": {"id": 1, "name": "Alice", "email": "alice@example.com"},
  "posts": [
    {"id": 1, "user_id": 1, "title": "First Post", "body": "Hello world!"},
    {"id": 3, "user_id": 1, "title": "Second Post", "body": "Another one."}
  ],
  "post_count": 2
}
```

---

## 10. Eager Loading

Calling relationship methods inside a loop creates the N+1 query problem. If you load 100 users and then call `$user->posts()` for each one, that is 101 queries (1 for users + 100 for posts).

Use the `include` parameter with `select()` to eager-load relationships:

```php
$user = new User();
$users = $user->select("*", "", [], "name ASC", 20, 0, ["posts"]);
```

The seventh argument is an array of relationship names to include. This runs just 2 queries (one for users, one for all related posts) and stitches the results together.

### toDict() with Nested Includes

When eager loading is active, `toDict()` includes the related data:

```php
$user = new User();
$users = $user->select("*", "", [], "", 0, 0, ["posts"]);

$result = array_map(fn($u) => $u->toDict(), $users);

return $response->json($result);
```

```json
[
  {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "posts": [
      {"id": 1, "title": "First Post", "body": "Hello world!"},
      {"id": 3, "title": "Second Post", "body": "Another one."}
    ]
  },
  {
    "id": 2,
    "name": "Bob",
    "email": "bob@example.com",
    "posts": [
      {"id": 2, "title": "Bob's Post", "body": "Hi there."}
    ]
  }
]
```

### Nested Eager Loading

Load multiple levels deep with dot notation:

```php
$user = new User();
$users = $user->select("*", "", [], "", 0, 0, ["posts", "posts.comments"]);
```

This loads users, their posts, and each post's comments in 3 queries total.

---

## 11. Soft Delete

If your model has a `deletedAt` property, Tina4 supports soft delete -- marking records as deleted without actually removing them from the database:

```php
<?php
use Tina4\ORM;

class Post extends ORM
{
    public int $id;
    public string $title;
    public string $body;
    public ?string $deletedAt = null;

    public string $tableName = "posts";
    public string $primaryKey = "id";
    public bool $softDelete = true;
}
```

With `$softDelete = true`:

- `$post->delete()` sets `deleted_at` to the current timestamp instead of deleting the row
- `select()` automatically excludes rows where `deleted_at` is not null
- `$post->forceDelete()` permanently removes the row

### Restoring Soft-Deleted Records

```php
$post = new Post();
$post->load(5); // Load even if soft-deleted
$post->deletedAt = null;
$post->save();
```

### Including Soft-Deleted Records in Queries

```php
$post = new Post();
$allPosts = $post->select("*", "", [], "", 0, 0, [], true); // eighth arg = include deleted
```

---

## 12. NumericField for Prices

When working with money, floating-point arithmetic causes rounding errors. Use the `NumericField` type for precise decimal values:

```php
<?php
use Tina4\ORM;
use Tina4\NumericField;

class Product extends ORM
{
    public int $id;
    public string $name;
    public NumericField $price;
    public NumericField $discount;

    public string $tableName = "products";
    public string $primaryKey = "id";
}
```

`NumericField` maps to `DECIMAL` or `NUMERIC` in the database and handles precision correctly. When you access `$product->price`, you get a value that compares and calculates accurately for financial operations.

---

## 13. Auto-CRUD

One of Tina4's most powerful features is auto-CRUD -- it automatically generates REST endpoints for any ORM model.

Add the `$autoCrud` property to your model:

```php
<?php
use Tina4\ORM;

class Product extends ORM
{
    public int $id;
    public string $name;
    public string $category = "Uncategorized";
    public float $price = 0.00;
    public bool $inStock = true;

    public string $tableName = "products";
    public string $primaryKey = "id";
    public bool $autoCrud = true;
}
```

With `$autoCrud = true`, Tina4 automatically registers these routes:

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/products` | List all with pagination |
| `GET` | `/api/products/{id}` | Get one by ID |
| `POST` | `/api/products` | Create a new record |
| `PUT` | `/api/products/{id}` | Update a record |
| `DELETE` | `/api/products/{id}` | Delete a record |

The endpoint prefix is derived from the table name: `products` becomes `/api/products`.

```bash
curl http://localhost:7145/api/products
```

```json
{
  "data": [
    {"id": 1, "name": "Wireless Keyboard", "category": "Electronics", "price": 79.99, "in_stock": true},
    {"id": 2, "name": "Yoga Mat", "category": "Fitness", "price": 29.99, "in_stock": true}
  ],
  "total": 2,
  "page": 1,
  "per_page": 20
}
```

Auto-CRUD supports query parameters for filtering, sorting, and pagination out of the box:

```bash
curl "http://localhost:7145/api/products?category=Electronics&sort=price&order=desc&page=1&per_page=10"
```

You can still define custom routes alongside auto-CRUD. Your custom routes take precedence over the auto-generated ones.

---

## 14. Exercise: Build a Blog

Build a blog with three models: User, Post, and Comment. Use relationships, eager loading, and auto-CRUD.

### Requirements

1. Create three models in `src/orm/`:

   **User** -- `users` table:
   - `id` (int, primary key)
   - `name` (string)
   - `email` (string)
   - `createdAt` (string)
   - Has many posts

   **Post** -- `posts` table:
   - `id` (int, primary key)
   - `userId` (int, foreign key)
   - `title` (string)
   - `body` (string)
   - `published` (bool, default false)
   - `createdAt` (string)
   - Belongs to user, has many comments

   **Comment** -- `comments` table:
   - `id` (int, primary key)
   - `postId` (int, foreign key)
   - `authorName` (string)
   - `body` (string)
   - `createdAt` (string)
   - Belongs to post

2. Create migrations for all three tables.

3. Build custom endpoints:

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/api/blog/posts` | List published posts with author info (eager load user) |
| `GET` | `/api/blog/posts/{id:int}` | Get a post with author and comments (eager load both) |
| `POST` | `/api/blog/posts/{id:int}/comments` | Add a comment to a post |

4. Enable auto-CRUD on the User model for admin access at `/api/users`.

### Test with:

```bash
# Create a user (via auto-CRUD)
curl -X POST http://localhost:7145/api/users \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com"}'

# Create a post
curl -X POST http://localhost:7145/api/blog/posts \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "title": "My First Post", "body": "Hello world!", "published": true}'

# List posts
curl http://localhost:7145/api/blog/posts

# Add a comment
curl -X POST http://localhost:7145/api/blog/posts/1/comments \
  -H "Content-Type: application/json" \
  -d '{"author_name": "Bob", "body": "Great post!"}'

# Get post with comments
curl http://localhost:7145/api/blog/posts/1
```

---

## 15. Solution

### Migrations

Create `src/migrations/20260322150000_create_users_table.sql`:

```sql
-- UP
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- DOWN
DROP TABLE IF EXISTS users;
```

Create `src/migrations/20260322150100_create_posts_table.sql`:

```sql
-- UP
CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    body TEXT NOT NULL,
    published INTEGER NOT NULL DEFAULT 0,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

-- DOWN
DROP TABLE IF EXISTS posts;
```

Create `src/migrations/20260322150200_create_comments_table.sql`:

```sql
-- UP
CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER NOT NULL,
    author_name TEXT NOT NULL,
    body TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (post_id) REFERENCES posts(id)
);

-- DOWN
DROP TABLE IF EXISTS comments;
```

Run them:

```bash
tina4 migrate
```

```
Running migrations...
  [APPLIED] 20260322150000_create_users_table.sql
  [APPLIED] 20260322150100_create_posts_table.sql
  [APPLIED] 20260322150200_create_comments_table.sql
Migrations complete. 3 applied.
```

### Models

Create `src/orm/User.php`:

```php
<?php
use Tina4\ORM;

class User extends ORM
{
    public int $id;
    public string $name;
    public string $email;
    public string $createdAt;

    public string $tableName = "users";
    public string $primaryKey = "id";
    public bool $autoCrud = true;

    public function posts(): array
    {
        return $this->hasMany(Post::class, "user_id");
    }
}
```

Create `src/orm/Post.php`:

```php
<?php
use Tina4\ORM;

class Post extends ORM
{
    public int $id;
    public int $userId;
    public string $title;
    public string $body;
    public bool $published = false;
    public string $createdAt;

    public string $tableName = "posts";
    public string $primaryKey = "id";

    public function user(): ?User
    {
        return $this->belongsTo(User::class, "user_id");
    }

    public function comments(): array
    {
        return $this->hasMany(Comment::class, "post_id");
    }
}
```

Create `src/orm/Comment.php`:

```php
<?php
use Tina4\ORM;

class Comment extends ORM
{
    public int $id;
    public int $postId;
    public string $authorName;
    public string $body;
    public string $createdAt;

    public string $tableName = "comments";
    public string $primaryKey = "id";

    public function post(): ?Post
    {
        return $this->belongsTo(Post::class, "post_id");
    }
}
```

### Routes

Create `src/routes/blog.php`:

```php
<?php
use Tina4\Route;

// List published posts with author
Route::get("/api/blog/posts", function ($request, $response) {
    $post = new Post();
    $posts = $post->select("*", "published = :published", ["published" => 1], "created_at DESC", 0, 0, ["user"]);

    $results = array_map(fn($p) => $p->toDict(), $posts);

    return $response->json([
        "posts" => $results,
        "count" => count($results)
    ]);
});

// Get a single post with author and comments
Route::get("/api/blog/posts/{id:int}", function ($request, $response) {
    $post = new Post();
    $post->load($request->params["id"]);

    if (empty($post->id)) {
        return $response->json(["error" => "Post not found"], 404);
    }

    $user = $post->user();
    $comments = $post->comments();

    $result = $post->toDict();
    $result["user"] = $user ? $user->toDict() : null;
    $result["comments"] = array_map(fn($c) => $c->toDict(), $comments);
    $result["comment_count"] = count($comments);

    return $response->json($result);
});

// Create a post
Route::post("/api/blog/posts", function ($request, $response) {
    $body = $request->body;

    if (empty($body["title"]) || empty($body["body"]) || empty($body["user_id"])) {
        return $response->json(["error" => "title, body, and user_id are required"], 400);
    }

    $post = new Post();
    $post->userId = (int) $body["user_id"];
    $post->title = $body["title"];
    $post->body = $body["body"];
    $post->published = (bool) ($body["published"] ?? false);
    $post->save();

    return $response->json($post->toDict(), 201);
});

// Add a comment to a post
Route::post("/api/blog/posts/{id:int}/comments", function ($request, $response) {
    $postId = $request->params["id"];

    // Verify post exists
    $post = new Post();
    $post->load($postId);

    if (empty($post->id)) {
        return $response->json(["error" => "Post not found"], 404);
    }

    $body = $request->body;

    if (empty($body["author_name"]) || empty($body["body"])) {
        return $response->json(["error" => "author_name and body are required"], 400);
    }

    $comment = new Comment();
    $comment->postId = $postId;
    $comment->authorName = $body["author_name"];
    $comment->body = $body["body"];
    $comment->save();

    return $response->json($comment->toDict(), 201);
});
```

**Expected output for GET /api/blog/posts/1:**

```json
{
  "id": 1,
  "user_id": 1,
  "title": "My First Post",
  "body": "Hello world!",
  "published": true,
  "created_at": "2026-03-22 15:00:00",
  "user": {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com"
  },
  "comments": [
    {
      "id": 1,
      "post_id": 1,
      "author_name": "Bob",
      "body": "Great post!",
      "created_at": "2026-03-22 15:01:00"
    }
  ],
  "comment_count": 1
}
```

---

## 16. Gotchas

### 1. Table Naming Convention

**Problem:** Your model class is `OrderItem` but queries fail because the table does not exist.

**Cause:** Tina4 converts `OrderItem` to `order_items` (plural, snake_case). If your table is named `order_item` (singular), it will not match.

**Fix:** Set `$tableName` explicitly: `public string $tableName = "order_item";`. Or rename your table to match the convention.

### 2. Null Handling

**Problem:** A field that should be nullable causes errors when the value is null.

**Cause:** The PHP property is declared as `string` instead of `?string`. PHP 8.1+ enforces type declarations strictly.

**Fix:** Use nullable types: `public ?string $description = null;`. The `?` prefix allows null values.

### 3. Relationship Foreign Key Direction

**Problem:** You write `$this->hasMany(Post::class, "id")` and get wrong results.

**Cause:** The foreign key argument is the column on the related table, not the current table. `hasMany(Post::class, "user_id")` means "find posts where posts.user_id = this.id", not "find posts where posts.id = this.user_id".

**Fix:** The foreign key is always on the "many" side. For `hasMany`, it is the column on the child table. For `belongsTo`, it is the column on the current table.

### 4. camelCase to snake_case Mapping

**Problem:** You have a property `$userId` but the database column is `user_id`. Queries return null for this field.

**Cause:** Tina4 automatically converts between `camelCase` (PHP) and `snake_case` (database). If your database column is `userid` (no underscore), the mapping breaks.

**Fix:** Use consistent naming. PHP properties should be `camelCase` and database columns should be `snake_case`. If your column names differ, you may need to adjust them or override the mapping.

### 5. Forgetting save()

**Problem:** You set properties on a model but the database does not change.

**Cause:** You forgot to call `$model->save()`. Setting properties only changes the in-memory object.

**Fix:** Always call `save()` after modifying properties that should be persisted.

### 6. Auto-CRUD Endpoint Conflicts

**Problem:** Your custom route at `/api/products/{id}` does not work after enabling auto-CRUD on the Product model.

**Cause:** Both your custom route and the auto-CRUD route match the same path. The first one registered wins.

**Fix:** Custom routes defined in `src/routes/` files are loaded before auto-CRUD routes, so they take precedence. If that is not the behavior you want, use a different path for your custom route (e.g., `/api/shop/products/{id}`).

### 7. select() Returns Objects, Not Arrays

**Problem:** You try to use array syntax (`$result["name"]`) on the result of `select()` and get an error.

**Cause:** `select()` returns an array of model objects, not associative arrays. Each item is an instance of your model class.

**Fix:** Access properties with object syntax: `$result->name`. Or convert to an array with `$result->toDict()`.
