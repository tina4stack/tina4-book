# Chapter 10: API Documentation with Swagger

## 1. The 47-Endpoint Problem

Your team has 47 API endpoints and the frontend developer keeps asking "what does this endpoint accept?" You email a spreadsheet. It goes out of date. You write a wiki page. Nobody updates it. You add comments to the code. Nobody reads them.

Swagger (also called OpenAPI) solves this permanently. It generates interactive API documentation from annotations in your route files. The docs are always up to date because they come from the code itself. Your frontend developer can browse every endpoint, see the expected request and response formats, and even test endpoints directly from the browser.

Tina4 auto-generates a Swagger UI at `/swagger` from doc-block annotations on your routes. No build step. No extra tooling. Write the annotations, and the documentation appears.

---

## 2. What Swagger/OpenAPI Is

OpenAPI is a specification format for describing REST APIs. Swagger is the toolset that reads OpenAPI specs and generates documentation, client SDKs, and server stubs.

An OpenAPI spec describes:

- Every endpoint (path + HTTP method)
- What parameters each endpoint accepts (path, query, header, body)
- What each endpoint returns (response codes, response bodies)
- Data schemas (what a "User" or "Product" object looks like)
- Authentication requirements
- Grouping and tagging

Tina4 builds this spec automatically from doc-block comments in your PHP code. You never write JSON or YAML by hand.

---

## 3. Enabling Swagger

Swagger is available out of the box when `TINA4_DEBUG=true`. Navigate to:

```
http://localhost:7145/swagger
```

You should see the Swagger UI with any routes you have already defined. If you have not added any Swagger annotations yet, you will see the routes listed with default descriptions.

For production, you can explicitly enable or disable Swagger:

```env
TINA4_SWAGGER=true
```

### The Swagger JSON Endpoint

The raw OpenAPI spec is available at:

```
http://localhost:7145/swagger/json
```

```bash
curl http://localhost:7145/swagger/json
```

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "My Store API",
    "version": "1.0.0"
  },
  "paths": {
    "/api/products": {
      "get": {
        "summary": "List all products",
        "responses": {
          "200": {
            "description": "Successful response"
          }
        }
      }
    }
  }
}
```

This JSON can be imported into tools like Postman, Insomnia, or used to generate client SDKs.

---

## 4. Adding Descriptions to Routes

Add Swagger annotations as doc-block comments above your route definitions:

```php
<?php
use Tina4\Route;

/**
 * List all products
 * @description Returns a paginated list of all products in the catalog
 * @tags Products
 */
Route::get("/api/products", function ($request, $response) {
    return $response->json(["products" => []]);
});
```

The first line of the doc-block becomes the `summary`. The `@description` tag provides a longer explanation. Visit `/swagger` and you will see the endpoint listed under the "Products" group with both the summary and the description.

### Documenting Path Parameters

```php
/**
 * Get a product by ID
 * @description Returns a single product with full details including inventory status
 * @tags Products
 * @param int $id The unique product identifier
 */
Route::get("/api/products/{id:int}", function ($request, $response) {
    $id = $request->params["id"];
    return $response->json([
        "id" => $id,
        "name" => "Wireless Keyboard",
        "price" => 79.99
    ]);
});
```

The `@param` annotation tells Swagger about the path parameter. It shows up in the docs as a required field with type information.

### Documenting Query Parameters

```php
/**
 * Search products
 * @description Search the product catalog by name, category, or price range
 * @tags Products
 * @query string $q Search query (searches product name and description)
 * @query string $category Filter by category name
 * @query float $min_price Minimum price filter
 * @query float $max_price Maximum price filter
 * @query int $page Page number (default: 1)
 * @query int $limit Items per page (default: 20, max: 100)
 */
Route::get("/api/products/search", function ($request, $response) {
    $q = $request->query["q"] ?? "";
    $page = (int) ($request->query["page"] ?? 1);
    $limit = min((int) ($request->query["limit"] ?? 20), 100);

    return $response->json([
        "query" => $q,
        "page" => $page,
        "limit" => $limit,
        "results" => [],
        "total" => 0
    ]);
});
```

Each `@query` annotation adds a parameter to the Swagger docs with its type and description.

---

## 5. Documenting Request and Response Schemas

### Request Body

Use `@body` to document what the endpoint expects:

```php
/**
 * Create a new product
 * @description Creates a product in the catalog. Requires admin authentication.
 * @tags Products
 * @body {"name": "string", "category": "string", "price": "float", "in_stock": "bool", "description": "string"}
 * @response 201 {"id": "int", "name": "string", "category": "string", "price": "float", "in_stock": "bool", "created_at": "string"}
 * @response 400 {"error": "string"}
 */
Route::post("/api/products", function ($request, $response) {
    $body = $request->body;

    if (empty($body["name"])) {
        return $response->json(["error" => "Name is required"], 400);
    }

    return $response->json([
        "id" => 1,
        "name" => $body["name"],
        "category" => $body["category"] ?? "Uncategorized",
        "price" => (float) ($body["price"] ?? 0),
        "in_stock" => (bool) ($body["in_stock"] ?? true),
        "created_at" => date("c")
    ], 201);
});
```

The `@body` annotation describes the expected JSON structure. The `@response` annotation documents possible response codes and their payloads.

### Multiple Response Codes

```php
/**
 * Update a product
 * @description Update an existing product by ID. Only provided fields are updated.
 * @tags Products
 * @param int $id Product ID
 * @body {"name": "string", "category": "string", "price": "float", "in_stock": "bool"}
 * @response 200 {"id": "int", "name": "string", "category": "string", "price": "float", "in_stock": "bool", "updated_at": "string"}
 * @response 404 {"error": "string", "id": "int"}
 * @response 400 {"error": "string"}
 */
Route::put("/api/products/{id:int}", function ($request, $response) {
    $id = $request->params["id"];
    $body = $request->body;

    // Simulate not found
    if ($id > 100) {
        return $response->json(["error" => "Product not found", "id" => $id], 404);
    }

    return $response->json([
        "id" => $id,
        "name" => $body["name"] ?? "Widget",
        "category" => $body["category"] ?? "General",
        "price" => (float) ($body["price"] ?? 9.99),
        "in_stock" => (bool) ($body["in_stock"] ?? true),
        "updated_at" => date("c")
    ]);
});
```

Swagger UI shows each response code with its corresponding schema. Developers can see at a glance what a `200` looks like versus a `404`.

---

## 6. Tags for Grouping Endpoints

Tags group related endpoints in the Swagger UI. Without tags, all endpoints appear in a flat list. With tags, they are organized into collapsible sections.

```php
/**
 * List all users
 * @tags Users
 */
Route::get("/api/users", function ($request, $response) {
    return $response->json(["users" => []]);
});

/**
 * Get user by ID
 * @tags Users
 */
Route::get("/api/users/{id:int}", function ($request, $response) {
    return $response->json(["id" => $request->params["id"], "name" => "Alice"]);
});

/**
 * List all orders
 * @tags Orders
 */
Route::get("/api/orders", function ($request, $response) {
    return $response->json(["orders" => []]);
});

/**
 * Create an order
 * @tags Orders
 */
Route::post("/api/orders", function ($request, $response) {
    return $response->json(["order_id" => 1], 201);
});

/**
 * List all products
 * @tags Products
 */
Route::get("/api/products", function ($request, $response) {
    return $response->json(["products" => []]);
});
```

In the Swagger UI, you will see three sections: "Users", "Orders", and "Products". Each section expands to show its endpoints. This makes navigating a large API manageable.

### Multiple Tags

An endpoint can belong to multiple groups:

```php
/**
 * Get user's orders
 * @tags Users, Orders
 */
Route::get("/api/users/{id:int}/orders", function ($request, $response) {
    return $response->json(["orders" => []]);
});
```

This endpoint appears in both the "Users" and "Orders" sections.

---

## 7. Example Values

Add example values to make the docs more useful. Developers can see realistic data instead of just type names:

```php
/**
 * Create a new product
 * @description Creates a product in the catalog
 * @tags Products
 * @example request {"name": "Ergonomic Keyboard", "category": "Electronics", "price": 89.99, "in_stock": true, "description": "Split keyboard with adjustable tenting"}
 * @example response {"id": 42, "name": "Ergonomic Keyboard", "category": "Electronics", "price": 89.99, "in_stock": true, "created_at": "2026-03-22T14:30:00+00:00"}
 */
Route::post("/api/products", function ($request, $response) {
    $body = $request->body;

    return $response->json([
        "id" => 42,
        "name" => $body["name"],
        "category" => $body["category"] ?? "Uncategorized",
        "price" => (float) ($body["price"] ?? 0),
        "in_stock" => (bool) ($body["in_stock"] ?? true),
        "created_at" => date("c")
    ], 201);
});
```

The `@example` annotations populate the "Example Value" section in the Swagger UI. When a developer clicks "Try it out", the example request is pre-filled in the input field, so they can test immediately.

---

## 8. Try-It-Out from the Swagger UI

The Swagger UI includes a "Try it out" button on every endpoint. Clicking it:

1. Expands the endpoint with editable input fields
2. Pre-fills example values (if provided)
3. Lets you edit the parameters, headers, and request body
4. Sends the actual HTTP request to your running server
5. Shows the response status, headers, and body

This is a live testing tool built into your documentation. No need for Postman or curl -- frontend developers can test your API directly from the docs page.

### Authentication in Try-It-Out

If your endpoints require authentication, click the "Authorize" button at the top of the Swagger UI. Enter your JWT token or API key, and all subsequent "Try it out" requests will include the authentication header.

Tina4 auto-detects authentication requirements from your route annotations (`@secured`, `@noauth`) and shows the lock icon on endpoints that require auth.

---

## 9. Customizing the Swagger Info Block

Configure the top-level API information in `.env`:

```env
TINA4_SWAGGER_TITLE=My Store API
TINA4_SWAGGER_DESCRIPTION=API for managing products, orders, and users
TINA4_SWAGGER_VERSION=1.0.0
TINA4_SWAGGER_CONTACT_EMAIL=api@mystore.com
TINA4_SWAGGER_LICENSE=MIT
```

This information appears in the header of the Swagger UI and in the OpenAPI spec:

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "My Store API",
    "description": "API for managing products, orders, and users",
    "version": "1.0.0",
    "contact": {
      "email": "api@mystore.com"
    },
    "license": {
      "name": "MIT"
    }
  }
}
```

---

## 10. Generating Client SDKs from the Spec

The OpenAPI spec at `/swagger/json` can be used with code generation tools to create client libraries in any language.

### Using OpenAPI Generator

```bash
# Install the OpenAPI Generator CLI
npm install -g @openapitools/openapi-generator-cli

# Generate a TypeScript client
openapi-generator-cli generate \
  -i http://localhost:7145/swagger/json \
  -g typescript-fetch \
  -o ./frontend/api-client

# Generate a Python client
openapi-generator-cli generate \
  -i http://localhost:7145/swagger/json \
  -g python \
  -o ./python-client
```

This generates typed client code with methods for every endpoint. Your frontend developer gets:

```typescript
// Auto-generated TypeScript client
const api = new ProductsApi();

// Fully typed -- IDE autocompletion works
const product = await api.getProductById({ id: 42 });
console.log(product.name);  // TypeScript knows this is a string

const newProduct = await api.createProduct({
    name: "Widget",
    category: "General",
    price: 9.99,
    inStock: true
});
```

Every time you update your Swagger annotations and regenerate, the client stays in sync with the server.

---

## 11. A Complete Documented API

Here is a full example showing all the annotation features together:

```php
<?php
use Tina4\Route;

/**
 * List all users
 * @description Returns a paginated list of users. Supports filtering by role and searching by name.
 * @tags Users
 * @query int $page Page number (default: 1)
 * @query int $limit Items per page (default: 20)
 * @query string $role Filter by role (admin, user, moderator)
 * @query string $search Search by name or email
 * @response 200 {"users": [{"id": "int", "name": "string", "email": "string", "role": "string"}], "total": "int", "page": "int", "pages": "int"}
 * @example response {"users": [{"id": 1, "name": "Alice", "email": "alice@example.com", "role": "admin"}, {"id": 2, "name": "Bob", "email": "bob@example.com", "role": "user"}], "total": 42, "page": 1, "pages": 3}
 */
Route::get("/api/users", function ($request, $response) {
    $page = (int) ($request->query["page"] ?? 1);
    $limit = (int) ($request->query["limit"] ?? 20);

    return $response->json([
        "users" => [
            ["id" => 1, "name" => "Alice", "email" => "alice@example.com", "role" => "admin"],
            ["id" => 2, "name" => "Bob", "email" => "bob@example.com", "role" => "user"]
        ],
        "total" => 42,
        "page" => $page,
        "pages" => (int) ceil(42 / $limit)
    ]);
});

/**
 * Get user by ID
 * @description Returns full user profile including account creation date
 * @tags Users
 * @param int $id User ID
 * @response 200 {"id": "int", "name": "string", "email": "string", "role": "string", "created_at": "string"}
 * @response 404 {"error": "string"}
 * @example response {"id": 1, "name": "Alice", "email": "alice@example.com", "role": "admin", "created_at": "2026-01-15T10:30:00+00:00"}
 */
Route::get("/api/users/{id:int}", function ($request, $response) {
    $id = $request->params["id"];

    if ($id > 100) {
        return $response->json(["error" => "User not found"], 404);
    }

    return $response->json([
        "id" => $id,
        "name" => "Alice",
        "email" => "alice@example.com",
        "role" => "admin",
        "created_at" => "2026-01-15T10:30:00+00:00"
    ]);
});

/**
 * Create a new user
 * @description Creates a user account. Email must be unique.
 * @tags Users
 * @body {"name": "string", "email": "string", "password": "string", "role": "string"}
 * @response 201 {"id": "int", "name": "string", "email": "string", "role": "string", "created_at": "string"}
 * @response 400 {"errors": ["string"]}
 * @response 409 {"error": "string"}
 * @example request {"name": "Charlie", "email": "charlie@example.com", "password": "securePass123", "role": "user"}
 * @example response {"id": 3, "name": "Charlie", "email": "charlie@example.com", "role": "user", "created_at": "2026-03-22T14:30:00+00:00"}
 */
Route::post("/api/users", function ($request, $response) {
    $body = $request->body;

    $errors = [];
    if (empty($body["name"])) $errors[] = "Name is required";
    if (empty($body["email"])) $errors[] = "Email is required";
    if (empty($body["password"])) $errors[] = "Password is required";

    if (!empty($errors)) {
        return $response->json(["errors" => $errors], 400);
    }

    return $response->json([
        "id" => 3,
        "name" => $body["name"],
        "email" => $body["email"],
        "role" => $body["role"] ?? "user",
        "created_at" => date("c")
    ], 201);
});

/**
 * Delete a user
 * @description Permanently deletes a user account. Requires admin role.
 * @tags Users
 * @param int $id User ID
 * @response 204
 * @response 404 {"error": "string"}
 */
Route::delete("/api/users/{id:int}", function ($request, $response) {
    $id = $request->params["id"];

    if ($id > 100) {
        return $response->json(["error" => "User not found"], 404);
    }

    return $response->json(null, 204);
});
```

Visit `/swagger` and you will see all four endpoints grouped under "Users", each with full parameter documentation, example values, and multiple response codes.

---

## 12. Exercise: Document a Complete User API

Take the User API from the example above and extend it with the following endpoints. Write full Swagger annotations for each one.

### Requirements

Document these additional endpoints (you can use hardcoded data in the handlers):

| Method | Path | Description |
|--------|------|-------------|
| `PUT` | `/api/users/{id}` | Update a user. Body: name, email, role. Response: updated user. |
| `GET` | `/api/users/{id}/orders` | List a user's orders. Query: status filter, pagination. |
| `POST` | `/api/users/{id}/avatar` | Upload user avatar. Body: avatar_url string. |

Each endpoint should have:

1. A summary (first line of doc-block)
2. A `@description`
3. A `@tags` annotation
4. `@param` for path parameters
5. `@query` for query parameters (where applicable)
6. `@body` for request body (where applicable)
7. `@response` for each possible response code
8. `@example` for request and response (where applicable)

### Test by visiting:

```
http://localhost:7145/swagger
```

Verify that all endpoints appear with correct documentation, examples, and response codes.

---

## 13. Solution

Create `src/routes/user-api-documented.php`:

```php
<?php
use Tina4\Route;

/**
 * Update a user
 * @description Updates an existing user's profile information. Only provided fields are updated. Email must remain unique.
 * @tags Users
 * @param int $id User ID
 * @body {"name": "string", "email": "string", "role": "string"}
 * @response 200 {"id": "int", "name": "string", "email": "string", "role": "string", "updated_at": "string"}
 * @response 404 {"error": "string"}
 * @response 409 {"error": "string"}
 * @example request {"name": "Alice Smith", "email": "alice.smith@example.com", "role": "admin"}
 * @example response {"id": 1, "name": "Alice Smith", "email": "alice.smith@example.com", "role": "admin", "updated_at": "2026-03-22T14:30:00+00:00"}
 */
Route::put("/api/users/{id:int}", function ($request, $response) {
    $id = $request->params["id"];
    $body = $request->body;

    if ($id > 100) {
        return $response->json(["error" => "User not found"], 404);
    }

    return $response->json([
        "id" => $id,
        "name" => $body["name"] ?? "Alice",
        "email" => $body["email"] ?? "alice@example.com",
        "role" => $body["role"] ?? "user",
        "updated_at" => date("c")
    ]);
});

/**
 * List user orders
 * @description Returns a paginated list of orders for a specific user. Supports filtering by order status.
 * @tags Users, Orders
 * @param int $id User ID
 * @query string $status Filter by order status (pending, processing, shipped, delivered, cancelled)
 * @query int $page Page number (default: 1)
 * @query int $limit Items per page (default: 20)
 * @response 200 {"orders": [{"id": "int", "product": "string", "quantity": "int", "total": "float", "status": "string", "created_at": "string"}], "total": "int", "page": "int"}
 * @response 404 {"error": "string"}
 * @example response {"orders": [{"id": 101, "product": "Wireless Keyboard", "quantity": 2, "total": 159.98, "status": "shipped", "created_at": "2026-03-20T10:00:00+00:00"}], "total": 5, "page": 1}
 */
Route::get("/api/users/{id:int}/orders", function ($request, $response) {
    $id = $request->params["id"];
    $status = $request->query["status"] ?? null;
    $page = (int) ($request->query["page"] ?? 1);

    if ($id > 100) {
        return $response->json(["error" => "User not found"], 404);
    }

    $orders = [
        ["id" => 101, "product" => "Wireless Keyboard", "quantity" => 2, "total" => 159.98, "status" => "shipped", "created_at" => "2026-03-20T10:00:00+00:00"],
        ["id" => 102, "product" => "USB-C Hub", "quantity" => 1, "total" => 49.99, "status" => "delivered", "created_at" => "2026-03-15T09:00:00+00:00"]
    ];

    if ($status !== null) {
        $orders = array_values(array_filter(
            $orders,
            fn($o) => $o["status"] === $status
        ));
    }

    return $response->json([
        "orders" => $orders,
        "total" => count($orders),
        "page" => $page
    ]);
});

/**
 * Upload user avatar
 * @description Sets or updates the avatar URL for a user. The avatar should be hosted on a CDN or static file server.
 * @tags Users
 * @param int $id User ID
 * @body {"avatar_url": "string"}
 * @response 200 {"id": "int", "avatar_url": "string", "updated_at": "string"}
 * @response 400 {"error": "string"}
 * @response 404 {"error": "string"}
 * @example request {"avatar_url": "https://cdn.example.com/avatars/alice-2026.jpg"}
 * @example response {"id": 1, "avatar_url": "https://cdn.example.com/avatars/alice-2026.jpg", "updated_at": "2026-03-22T14:30:00+00:00"}
 */
Route::post("/api/users/{id:int}/avatar", function ($request, $response) {
    $id = $request->params["id"];
    $body = $request->body;

    if ($id > 100) {
        return $response->json(["error" => "User not found"], 404);
    }

    if (empty($body["avatar_url"])) {
        return $response->json(["error" => "avatar_url is required"], 400);
    }

    return $response->json([
        "id" => $id,
        "avatar_url" => $body["avatar_url"],
        "updated_at" => date("c")
    ]);
});
```

Visit `http://localhost:7145/swagger` and verify:

- The "Users" section now has six endpoints (list, get, create, update, delete, and avatar)
- The "Orders" section shows the "List user orders" endpoint (because it has both `Users` and `Orders` tags)
- Each endpoint has its summary, description, parameters, request body schema, and response codes
- The "Try it out" button works for each endpoint
- Example values are pre-filled when you click "Try it out"

---

## 14. Gotchas

### 1. Annotations Must Be Directly Above the Route

**Problem:** Your Swagger annotations do not appear in the docs.

**Cause:** There is a blank line or other code between the doc-block and the `Route::` call. Tina4 only reads doc-blocks that are immediately above the route definition.

**Fix:** Make sure the `*/` closing of the doc-block is on the line directly before `Route::get(...)` with no blank lines in between.

### 2. Missing @tags Makes Endpoints Hard to Find

**Problem:** All endpoints appear in one giant flat list in the Swagger UI.

**Cause:** You did not add `@tags` to your routes. Without tags, Swagger groups everything under "default".

**Fix:** Add `@tags ResourceName` to every route doc-block. Group related endpoints under the same tag.

### 3. @body Must Be Valid JSON

**Problem:** The Swagger UI shows the body schema as empty or broken.

**Cause:** The JSON in your `@body` annotation is malformed. A trailing comma, missing quotes, or unescaped characters will break the parser.

**Fix:** Validate your `@body` JSON. Every key and string value must be in double quotes. No trailing commas. Use `"string"`, `"int"`, `"float"`, `"bool"` for type placeholders.

### 4. Swagger Shows Routes You Did Not Annotate

**Problem:** Unannotated routes appear in the Swagger UI with minimal documentation.

**Cause:** Tina4 includes all registered routes in the Swagger spec, not just annotated ones. Unannotated routes get a default summary based on the HTTP method and path.

**Fix:** This is by design -- it ensures nothing is hidden. Add annotations to improve the documentation quality. If you want to hide a route from Swagger, add `@hidden` to its doc-block.

### 5. Response Examples Do Not Match Actual Responses

**Problem:** The example response in Swagger shows different fields than the actual API response.

**Cause:** The `@example response` was written once and never updated when the handler changed. Swagger annotations are comments -- they are not validated against the actual code.

**Fix:** Treat annotations as part of the code. When you change a handler's response format, update the annotations at the same time. Consider adding integration tests that compare actual responses to documented schemas.

### 6. Swagger UI Not Available in Production

**Problem:** `/swagger` returns a 404 in production.

**Cause:** By default, Swagger is only available when `TINA4_DEBUG=true`. Production deployments with `TINA4_DEBUG=false` disable the Swagger UI.

**Fix:** If you want Swagger in production (for example, on a staging server), explicitly set `TINA4_SWAGGER=true` in your `.env`. Be aware that exposing your API documentation publicly may reveal implementation details.

### 7. SDK Generation Produces Incorrect Types

**Problem:** The generated TypeScript client has `any` types instead of proper interfaces.

**Cause:** Your `@body` and `@response` annotations use generic strings instead of typed schemas. `"name": "string"` tells the generator the type is a literal string "string", not a TypeScript `string` type.

**Fix:** Use the correct OpenAPI type format in your annotations. For complex schemas, define them with proper type notation: `"name": "string"` (lowercase), `"price": "number"`, `"in_stock": "boolean"`, `"tags": ["string"]` (array of strings).
