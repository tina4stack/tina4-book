# Chapter 7: Authentication

## 1. Locking the Door

Up to now, every endpoint you have built is public. Anyone with the URL can read, create, update, and delete data. That is fine for a tutorial, but a real application needs to know who is making a request and whether they are allowed to make it.

This chapter covers Tina4's authentication system: JWT tokens, password hashing, middleware-based route protection, CSRF tokens for forms, and session management.

---

## 2. JWT Tokens

Tina4 uses JSON Web Tokens (JWT) for authentication. A JWT is a signed string that contains a payload (like a user ID and role). The server creates the token at login, the client sends it with every request, and the server verifies it without needing to look anything up in a database.

### Generating a Token

```php
<?php
use Tina4\Auth;

$payload = [
    "user_id" => 42,
    "email" => "alice@example.com",
    "role" => "admin"
];

$token = Auth::getToken($payload);
```

`getToken()` signs the payload with a secret key and returns a JWT string like:

```
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjo0MiwiZW1haWwiOiJhbGljZUBleGFtcGxlLmNvbSIsInJvbGUiOiJhZG1pbiIsImlhdCI6MTcxMTExMjYwMCwiZXhwIjoxNzExMTE2MjAwfQ.abc123signature
```

The token has three parts separated by dots: header, payload, and signature. The signature ensures the token has not been tampered with.

### Token Expiry

By default, tokens expire after 1 hour. Configure this in `.env`:

```env
TINA4_JWT_EXPIRY=3600
```

The value is in seconds. Common settings:

| Value | Duration |
|-------|----------|
| `900` | 15 minutes |
| `3600` | 1 hour (default) |
| `86400` | 24 hours |
| `604800` | 7 days |

### Validating a Token

```php
$isValid = Auth::validToken($token);
// Returns true if the token is valid and not expired, false otherwise
```

### Reading the Payload

```php
$payload = Auth::getPayload($token);
```

Returns the original payload array:

```php
[
    "user_id" => 42,
    "email" => "alice@example.com",
    "role" => "admin",
    "iat" => 1711112600,  // issued at (Unix timestamp)
    "exp" => 1711116200   // expires at (Unix timestamp)
]
```

If the token is invalid or expired, `getPayload()` returns `null`.

### The Secret Key

Tina4 uses a secret key to sign and verify tokens. On first run, it automatically generates a random key and stores it in `secrets/jwt.key`. You can also set it explicitly:

```env
TINA4_JWT_SECRET=my-very-long-and-random-secret-key-at-least-32-chars
```

Keep this key secret. If someone gets it, they can forge tokens.

---

## 3. Password Hashing

Never store passwords in plain text. Tina4 provides two functions for secure password handling:

### Hashing a Password

```php
use Tina4\Auth;

$hash = Auth::hashPassword("my-secure-password");
// Returns: "$2y$10$abc123...long-hash-string..."
```

This uses PHP's `password_hash()` with bcrypt under the hood. Each hash includes a random salt, so hashing the same password twice produces different results.

### Checking a Password

```php
$isCorrect = Auth::checkPassword("my-secure-password", $storedHash);
// Returns true if the password matches the hash
```

### Registration Example

```php
<?php
use Tina4\Route;
use Tina4\Auth;
use Tina4\Database;

Route::post("/api/register", function ($request, $response) {
    $body = $request->body;

    // Validate input
    if (empty($body["name"]) || empty($body["email"]) || empty($body["password"])) {
        return $response->json(["error" => "Name, email, and password are required"], 400);
    }

    if (strlen($body["password"]) < 8) {
        return $response->json(["error" => "Password must be at least 8 characters"], 400);
    }

    $db = Database::getConnection();

    // Check if email already exists
    $existing = $db->fetchOne("SELECT id FROM users WHERE email = :email", ["email" => $body["email"]]);
    if ($existing !== null) {
        return $response->json(["error" => "Email already registered"], 409);
    }

    // Hash the password
    $passwordHash = Auth::hashPassword($body["password"]);

    // Create the user
    $db->execute(
        "INSERT INTO users (name, email, password_hash) VALUES (:name, :email, :hash)",
        [
            "name" => $body["name"],
            "email" => $body["email"],
            "hash" => $passwordHash
        ]
    );

    $user = $db->fetchOne("SELECT id, name, email FROM users WHERE id = last_insert_rowid()");

    return $response->json([
        "message" => "Registration successful",
        "user" => $user
    ], 201);
});
```

```bash
curl -X POST http://localhost:7145/api/register \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com", "password": "securePass123"}'
```

```json
{
  "message": "Registration successful",
  "user": {"id": 1, "name": "Alice", "email": "alice@example.com"}
}
```

---

## 4. The Login Flow

Here is the complete login flow: the client sends credentials, the server validates them, and returns a JWT token.

```php
<?php
use Tina4\Route;
use Tina4\Auth;
use Tina4\Database;

/**
 * @noauth
 */
Route::post("/api/login", function ($request, $response) {
    $body = $request->body;

    if (empty($body["email"]) || empty($body["password"])) {
        return $response->json(["error" => "Email and password are required"], 400);
    }

    $db = Database::getConnection();

    // Find the user
    $user = $db->fetchOne(
        "SELECT id, name, email, password_hash FROM users WHERE email = :email",
        ["email" => $body["email"]]
    );

    if ($user === null) {
        return $response->json(["error" => "Invalid email or password"], 401);
    }

    // Check the password
    if (!Auth::checkPassword($body["password"], $user["password_hash"])) {
        return $response->json(["error" => "Invalid email or password"], 401);
    }

    // Generate a token
    $token = Auth::getToken([
        "user_id" => $user["id"],
        "email" => $user["email"],
        "name" => $user["name"]
    ]);

    return $response->json([
        "message" => "Login successful",
        "token" => $token,
        "user" => [
            "id" => $user["id"],
            "name" => $user["name"],
            "email" => $user["email"]
        ]
    ]);
});
```

Notice the `@noauth` annotation. The login endpoint must be public -- you cannot require a token to get a token.

```bash
curl -X POST http://localhost:7145/api/login \
  -H "Content-Type: application/json" \
  -d '{"email": "alice@example.com", "password": "securePass123"}'
```

```json
{
  "message": "Login successful",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com"
  }
}
```

The client stores this token (in localStorage, a cookie, or memory) and sends it with subsequent requests.

---

## 5. Using Tokens in Requests

The client sends the token in the `Authorization` header with the `Bearer` prefix:

```bash
curl http://localhost:7145/api/profile \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

---

## 6. Protecting Routes

### Auth Middleware

Create a reusable auth middleware:

```php
<?php
use Tina4\Auth;

function authMiddleware($request, $response, $next) {
    $authHeader = $request->headers["Authorization"] ?? "";

    if (empty($authHeader) || !str_starts_with($authHeader, "Bearer ")) {
        return $response->json(["error" => "Authorization header required"], 401);
    }

    $token = substr($authHeader, 7); // Remove "Bearer " prefix

    if (!Auth::validToken($token)) {
        return $response->json(["error" => "Invalid or expired token"], 401);
    }

    $payload = Auth::getPayload($token);
    $request->user = $payload; // Attach user data to the request

    return $next($request, $response);
}
```

### Applying Middleware to Routes

```php
<?php
use Tina4\Route;

Route::get("/api/profile", function ($request, $response) {
    return $response->json([
        "user_id" => $request->user["user_id"],
        "email" => $request->user["email"],
        "name" => $request->user["name"]
    ]);
}, "authMiddleware");
```

```bash
# Without token -- 401
curl http://localhost:7145/api/profile
```

```json
{"error":"Authorization header required"}
```

```bash
# With valid token -- 200
curl http://localhost:7145/api/profile \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
```

```json
{
  "user_id": 1,
  "email": "alice@example.com",
  "name": "Alice"
}
```

### Applying Middleware to a Group

```php
Route::group("/api/admin", function () {

    Route::get("/stats", function ($request, $response) {
        return $response->json(["active_users" => 42]);
    });

    Route::get("/logs", function ($request, $response) {
        return $response->json(["logs" => []]);
    });

}, "authMiddleware");
```

Every route in the group requires a valid token.

---

## 7. @noauth and @secured Decorators

As introduced in Chapter 2, these decorators control authentication at the route level.

### @noauth -- Skip Authentication

Use `@noauth` for public endpoints that should bypass any global or group-level auth:

```php
/**
 * @noauth
 */
Route::get("/api/public/health", function ($request, $response) {
    return $response->json(["status" => "ok"]);
});

/**
 * @noauth
 */
Route::post("/api/login", function ($request, $response) {
    // Login logic
});

/**
 * @noauth
 */
Route::post("/api/register", function ($request, $response) {
    // Registration logic
});
```

### @secured -- Require Authentication for GET Routes

By default, POST, PUT, PATCH, and DELETE routes are considered secured. GET routes are public. Use `@secured` to explicitly protect a GET route:

```php
/**
 * @secured
 */
Route::get("/api/me", function ($request, $response) {
    // This GET route requires authentication
    return $response->json($request->user);
});
```

### Role-Based Authorization

Combine auth middleware with role checks:

```php
<?php
use Tina4\Auth;

function requireRole($role) {
    return function ($request, $response, $next) use ($role) {
        // First check authentication
        $authHeader = $request->headers["Authorization"] ?? "";
        if (empty($authHeader) || !str_starts_with($authHeader, "Bearer ")) {
            return $response->json(["error" => "Authorization required"], 401);
        }

        $token = substr($authHeader, 7);
        if (!Auth::validToken($token)) {
            return $response->json(["error" => "Invalid or expired token"], 401);
        }

        $payload = Auth::getPayload($token);

        // Check role
        if (($payload["role"] ?? "") !== $role) {
            return $response->json(["error" => "Forbidden. Required role: " . $role], 403);
        }

        $request->user = $payload;
        return $next($request, $response);
    };
}
```

Note that `requireRole()` returns a closure. To use it as middleware, you need to register the returned function:

```php
$adminOnly = requireRole("admin");

Route::delete("/api/users/{id:int}", function ($request, $response) {
    // Only admins can delete users
    return $response->json(["deleted" => true]);
}, $adminOnly);
```

---

## 8. CSRF Protection

For traditional form-based applications (not SPAs), Tina4 provides CSRF protection with form tokens.

### Generating a Token

In your template, include the CSRF token in every form:

```html
<form method="POST" action="/profile/update">
    {{ form_token() }}

    <div class="form-group">
        <label for="name">Name</label>
        <input type="text" name="name" id="name" value="{{ user.name }}">
    </div>

    <button type="submit">Update Profile</button>
</form>
```

`{{ form_token() }}` renders a hidden input field:

```html
<input type="hidden" name="_token" value="abc123randomtoken456">
```

### Validating the Token

In your route handler, check the token:

```php
<?php
use Tina4\Route;
use Tina4\Auth;

Route::post("/profile/update", function ($request, $response) {
    // Validate CSRF token
    if (!Auth::validateFormToken($request->body["_token"] ?? "")) {
        return $response->json(["error" => "Invalid form token. Please refresh and try again."], 403);
    }

    // Process the form...
    return $response->redirect("/profile");
});
```

The CSRF token is tied to the user's session and expires after a single use. This prevents cross-site request forgery attacks where a malicious site tricks the user's browser into submitting a form.

### When to Use CSRF Tokens

Use CSRF tokens for:
- HTML forms submitted by browsers
- Any POST/PUT/DELETE from server-rendered pages

You do not need CSRF tokens for:
- API endpoints that use JWT (the Bearer token already proves the request is intentional)
- Single-page applications that use `fetch()` with custom headers (the `Authorization` header cannot be set by cross-origin forms)

---

## 9. Sessions

Tina4 supports server-side sessions for storing per-user state between requests. Sessions work alongside JWT tokens -- use JWTs for API authentication and sessions for stateful web pages.

### Session Configuration

Set the session backend in `.env`:

```env
# File-based sessions (default)
TINA4_SESSION_DRIVER=file

# Redis
TINA4_SESSION_DRIVER=redis
TINA4_SESSION_HOST=localhost
TINA4_SESSION_PORT=6379

# MongoDB
TINA4_SESSION_DRIVER=mongodb
TINA4_SESSION_HOST=localhost
TINA4_SESSION_PORT=27017

# Valkey
TINA4_SESSION_DRIVER=valkey
TINA4_SESSION_HOST=localhost
TINA4_SESSION_PORT=6379
```

File-based sessions work out of the box with no additional dependencies. Use Redis or Valkey for production deployments with multiple servers, so sessions are shared across instances.

### Using Sessions

Access session data via `$request->session`:

```php
<?php
use Tina4\Route;

Route::post("/login-form", function ($request, $response) {
    // After validating credentials...
    $request->session["user_id"] = 42;
    $request->session["user_name"] = "Alice";
    $request->session["logged_in"] = true;

    return $response->redirect("/dashboard");
});

Route::get("/dashboard", function ($request, $response) {
    if (empty($request->session["logged_in"])) {
        return $response->redirect("/login");
    }

    return $response->render("dashboard.html", [
        "user_name" => $request->session["user_name"]
    ]);
});

Route::post("/logout", function ($request, $response) {
    // Clear all session data
    $request->session = [];

    return $response->redirect("/login");
});
```

### Session Options

```env
TINA4_SESSION_LIFETIME=3600       # Session lifetime in seconds (default: 3600)
TINA4_SESSION_NAME=tina4_session  # Cookie name for the session ID
```

---

## 10. Exercise: Build Login, Register, and Profile

Build a complete authentication system with registration, login, profile viewing, and password changing.

### Requirements

1. Create a `users` table migration with: `id`, `name`, `email` (unique), `password_hash`, `role` (default "user"), `created_at`

2. Build these endpoints:

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST` | `/api/register` | @noauth | Create an account. Validate name, email, password (min 8 chars). |
| `POST` | `/api/login` | @noauth | Login. Return JWT token. |
| `GET` | `/api/profile` | secured | Get current user's profile from token. |
| `PUT` | `/api/profile` | secured | Update name and email. |
| `PUT` | `/api/profile/password` | secured | Change password. Require current password. |

3. Create auth middleware that extracts the user from the JWT and attaches it to `$request->user`.

### Test with:

```bash
# Register
curl -X POST http://localhost:7145/api/register \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice", "email": "alice@example.com", "password": "securePass123"}'

# Login
curl -X POST http://localhost:7145/api/login \
  -H "Content-Type: application/json" \
  -d '{"email": "alice@example.com", "password": "securePass123"}'

# Save the token from login response, then:

# Get profile
curl http://localhost:7145/api/profile \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"

# Update profile
curl -X PUT http://localhost:7145/api/profile \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice Smith"}'

# Change password
curl -X PUT http://localhost:7145/api/profile/password \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{"current_password": "securePass123", "new_password": "evenMoreSecure456"}'

# Try with no token (should fail)
curl http://localhost:7145/api/profile
```

---

## 11. Solution

### Migration

Create `src/migrations/20260322160000_create_auth_users_table.sql`:

```sql
-- UP
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'user',
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);

-- DOWN
DROP TABLE IF EXISTS users;
```

```bash
tina4 migrate
```

### Middleware

Create `src/routes/middleware.php`:

```php
<?php
use Tina4\Auth;

function authMiddleware($request, $response, $next) {
    $authHeader = $request->headers["Authorization"] ?? "";

    if (empty($authHeader) || !str_starts_with($authHeader, "Bearer ")) {
        return $response->json(["error" => "Authorization required. Send: Authorization: Bearer <token>"], 401);
    }

    $token = substr($authHeader, 7);

    if (!Auth::validToken($token)) {
        return $response->json(["error" => "Invalid or expired token. Please login again."], 401);
    }

    $payload = Auth::getPayload($token);
    $request->user = $payload;

    return $next($request, $response);
}
```

### Routes

Create `src/routes/auth.php`:

```php
<?php
use Tina4\Route;
use Tina4\Auth;
use Tina4\Database;

/**
 * @noauth
 */
Route::post("/api/register", function ($request, $response) {
    $body = $request->body;

    // Validate input
    $errors = [];
    if (empty($body["name"])) {
        $errors[] = "Name is required";
    }
    if (empty($body["email"])) {
        $errors[] = "Email is required";
    }
    if (empty($body["password"])) {
        $errors[] = "Password is required";
    } elseif (strlen($body["password"]) < 8) {
        $errors[] = "Password must be at least 8 characters";
    }

    if (!empty($errors)) {
        return $response->json(["errors" => $errors], 400);
    }

    $db = Database::getConnection();

    // Check for existing email
    $existing = $db->fetchOne("SELECT id FROM users WHERE email = :email", ["email" => $body["email"]]);
    if ($existing !== null) {
        return $response->json(["error" => "Email already registered"], 409);
    }

    // Create user
    $hash = Auth::hashPassword($body["password"]);

    $db->execute(
        "INSERT INTO users (name, email, password_hash) VALUES (:name, :email, :hash)",
        [
            "name" => $body["name"],
            "email" => $body["email"],
            "hash" => $hash
        ]
    );

    $user = $db->fetchOne("SELECT id, name, email, role, created_at FROM users WHERE id = last_insert_rowid()");

    return $response->json([
        "message" => "Registration successful",
        "user" => $user
    ], 201);
});

/**
 * @noauth
 */
Route::post("/api/login", function ($request, $response) {
    $body = $request->body;

    if (empty($body["email"]) || empty($body["password"])) {
        return $response->json(["error" => "Email and password are required"], 400);
    }

    $db = Database::getConnection();

    $user = $db->fetchOne(
        "SELECT id, name, email, password_hash, role FROM users WHERE email = :email",
        ["email" => $body["email"]]
    );

    if ($user === null || !Auth::checkPassword($body["password"], $user["password_hash"])) {
        return $response->json(["error" => "Invalid email or password"], 401);
    }

    $token = Auth::getToken([
        "user_id" => $user["id"],
        "email" => $user["email"],
        "name" => $user["name"],
        "role" => $user["role"]
    ]);

    return $response->json([
        "message" => "Login successful",
        "token" => $token,
        "user" => [
            "id" => $user["id"],
            "name" => $user["name"],
            "email" => $user["email"],
            "role" => $user["role"]
        ]
    ]);
});

// Get current user profile
Route::get("/api/profile", function ($request, $response) {
    $db = Database::getConnection();

    $user = $db->fetchOne(
        "SELECT id, name, email, role, created_at FROM users WHERE id = :id",
        ["id" => $request->user["user_id"]]
    );

    if ($user === null) {
        return $response->json(["error" => "User not found"], 404);
    }

    return $response->json($user);
}, "authMiddleware");

// Update profile
Route::put("/api/profile", function ($request, $response) {
    $db = Database::getConnection();
    $body = $request->body;
    $userId = $request->user["user_id"];

    // Check for email uniqueness if email is being changed
    if (!empty($body["email"])) {
        $existing = $db->fetchOne(
            "SELECT id FROM users WHERE email = :email AND id != :id",
            ["email" => $body["email"], "id" => $userId]
        );
        if ($existing !== null) {
            return $response->json(["error" => "Email already in use by another account"], 409);
        }
    }

    $current = $db->fetchOne("SELECT * FROM users WHERE id = :id", ["id" => $userId]);

    $db->execute(
        "UPDATE users SET name = :name, email = :email WHERE id = :id",
        [
            "name" => $body["name"] ?? $current["name"],
            "email" => $body["email"] ?? $current["email"],
            "id" => $userId
        ]
    );

    $updated = $db->fetchOne(
        "SELECT id, name, email, role, created_at FROM users WHERE id = :id",
        ["id" => $userId]
    );

    return $response->json([
        "message" => "Profile updated",
        "user" => $updated
    ]);
}, "authMiddleware");

// Change password
Route::put("/api/profile/password", function ($request, $response) {
    $db = Database::getConnection();
    $body = $request->body;
    $userId = $request->user["user_id"];

    if (empty($body["current_password"]) || empty($body["new_password"])) {
        return $response->json(["error" => "Current password and new password are required"], 400);
    }

    if (strlen($body["new_password"]) < 8) {
        return $response->json(["error" => "New password must be at least 8 characters"], 400);
    }

    $user = $db->fetchOne("SELECT password_hash FROM users WHERE id = :id", ["id" => $userId]);

    if (!Auth::checkPassword($body["current_password"], $user["password_hash"])) {
        return $response->json(["error" => "Current password is incorrect"], 401);
    }

    $newHash = Auth::hashPassword($body["new_password"]);

    $db->execute(
        "UPDATE users SET password_hash = :hash WHERE id = :id",
        ["hash" => $newHash, "id" => $userId]
    );

    return $response->json(["message" => "Password changed successfully"]);
}, "authMiddleware");
```

**Expected output for register:**

```json
{
  "message": "Registration successful",
  "user": {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "role": "user",
    "created_at": "2026-03-22 16:00:00"
  }
}
```

(Status: `201 Created`)

**Expected output for login:**

```json
{
  "message": "Login successful",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": 1,
    "name": "Alice",
    "email": "alice@example.com",
    "role": "user"
  }
}
```

**Expected output for profile without token:**

```json
{"error":"Authorization required. Send: Authorization: Bearer <token>"}
```

(Status: `401 Unauthorized`)

**Expected output for profile with token:**

```json
{
  "id": 1,
  "name": "Alice",
  "email": "alice@example.com",
  "role": "user",
  "created_at": "2026-03-22 16:00:00"
}
```

**Expected output for password change with wrong current password:**

```json
{"error":"Current password is incorrect"}
```

(Status: `401 Unauthorized`)

**Expected output for successful password change:**

```json
{"message":"Password changed successfully"}
```

---

## 12. Gotchas

### 1. Token Expiry Confusion

**Problem:** Tokens that worked yesterday now return 401.

**Cause:** The default token lifetime is 1 hour. After that, the token is invalid even if the signature is correct.

**Fix:** Issue a new token at login. If your application needs long-lived sessions, use refresh tokens: a short-lived access token (15 minutes) paired with a long-lived refresh token (7 days) that can be used to get a new access token without re-entering credentials.

### 2. Secret Key Management

**Problem:** Tokens generated on one server are invalid on another, or tokens stop working after a deployment.

**Cause:** Each server generated its own random `secrets/jwt.key` file. Or the key file was deleted/regenerated during deployment.

**Fix:** Set `TINA4_JWT_SECRET` in `.env` explicitly and use the same value across all servers. Store it in your deployment secrets manager (not in version control). If the key changes, all existing tokens become invalid and users must log in again.

### 3. CORS with Authentication

**Problem:** Frontend requests with the `Authorization` header fail with a CORS error, even though `CORS_ORIGINS=*` is set.

**Cause:** When the browser sends an `Authorization` header, it first sends a preflight `OPTIONS` request. The server must respond to the OPTIONS request with the correct CORS headers, including `Access-Control-Allow-Headers: Authorization`.

**Fix:** Tina4 handles preflight requests automatically. Make sure `CORS_ORIGINS` is set correctly. If it is still failing, check that you are not overriding CORS headers in middleware.

### 4. Storing Tokens in localStorage

**Problem:** Your token is stolen via an XSS attack because it was stored in `localStorage`.

**Cause:** Any JavaScript on the page can read `localStorage`, including injected scripts from an XSS vulnerability.

**Fix:** Store tokens in `httpOnly` cookies when possible -- they cannot be accessed by JavaScript. For SPAs that must use `localStorage`, implement strict Content Security Policy headers and sanitize all user input.

### 5. Forgetting @noauth on Login

**Problem:** Your login endpoint returns 401 -- you cannot log in because the endpoint requires authentication.

**Cause:** If you have global auth middleware, the login endpoint needs the `@noauth` annotation to bypass it.

**Fix:** Add `@noauth` to your login and register routes. Without it, users cannot authenticate because authentication is required to authenticate -- a catch-22.

### 6. Password Hash Column Too Short

**Problem:** Registration fails with a database error about the password hash being too long.

**Cause:** bcrypt hashes are 60 characters long. If your `password_hash` column is defined as `VARCHAR(50)`, it gets truncated.

**Fix:** Use `TEXT` for the password hash column, or at minimum `VARCHAR(255)`. Never constrain the hash length.

### 7. Token in URL Query Parameters

**Problem:** Tokens in URLs like `/api/profile?token=eyJ...` leak through browser history, server logs, and the Referer header.

**Cause:** Query parameters are visible in many places where headers are not.

**Fix:** Always send tokens in the `Authorization` header, never in the URL. The only exception is WebSocket connections, where the initial HTTP upgrade request cannot carry custom headers -- use a short-lived token for that case.
