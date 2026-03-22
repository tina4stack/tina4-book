# Chapter 9: Sessions & Cookies

## 1. State in a Stateless World

Your e-commerce site needs a shopping cart that persists across page loads, remembers the user's language preference, and flashes success or error messages after form submissions. HTTP is stateless -- every request is independent, with no memory of what came before. Sessions and cookies solve this by giving the server a way to remember who is making requests and what they have been doing.

In Chapter 7 you saw a brief introduction to sessions for authentication. This chapter goes deeper: session backends, flash messages, cookies, remember-me tokens, and security configuration.

---

## 2. How Sessions Work

When a user visits your site for the first time, Tina4 generates a unique session ID (a long random string), stores it in a cookie on the user's browser, and creates a server-side storage entry keyed by that ID. On every subsequent request, the browser sends the cookie, Tina4 looks up the session data, and makes it available via `$request->session`.

The flow looks like this:

1. Browser sends first request (no session cookie)
2. Tina4 generates session ID: `abc123def456`
3. Tina4 sets cookie: `tina4_session=abc123def456`
4. Tina4 creates empty session storage for `abc123def456`
5. Browser sends second request with cookie `tina4_session=abc123def456`
6. Tina4 loads session data for `abc123def456`
7. Your route handler reads and writes `$request->session`
8. At the end of the request, Tina4 saves the updated session data

The session data is stored server-side. The browser only has the session ID -- it never sees the actual data.

---

## 3. File Sessions (Default)

Out of the box, Tina4 stores sessions in files. No configuration needed.

```php
<?php
use Tina4\Route;

Route::get("/visit-counter", function ($request, $response) {
    $count = ($request->session["visit_count"] ?? 0) + 1;
    $request->session["visit_count"] = $count;

    return $response->json([
        "visit_count" => $count,
        "message" => "You have visited this page " . $count . " time" . ($count === 1 ? "" : "s")
    ]);
});
```

```bash
curl http://localhost:7145/visit-counter -c cookies.txt -b cookies.txt
```

```json
{"visit_count":1,"message":"You have visited this page 1 time"}
```

```bash
curl http://localhost:7145/visit-counter -c cookies.txt -b cookies.txt
```

```json
{"visit_count":2,"message":"You have visited this page 2 times"}
```

```bash
curl http://localhost:7145/visit-counter -c cookies.txt -b cookies.txt
```

```json
{"visit_count":3,"message":"You have visited this page 3 times"}
```

The `-c cookies.txt` flag tells curl to save cookies to a file, and `-b cookies.txt` tells it to send them back. This simulates how a browser works.

Session files are stored in your system's temporary directory by default. You can change this:

```env
TINA4_SESSION_PATH=/path/to/session/files
```

File sessions work perfectly for single-server deployments. They are the simplest option and require no additional software.

---

## 4. Redis Sessions

For production deployments with multiple servers (behind a load balancer), you need a shared session store. Redis is the most common choice.

```env
TINA4_SESSION_HANDLER=redis
TINA4_SESSION_HOST=localhost
TINA4_SESSION_PORT=6379
TINA4_SESSION_PASSWORD=your-redis-password
```

That is the only change. Your code stays exactly the same. `$request->session` works identically whether sessions are stored in files, Redis, MongoDB, or Valkey. The storage backend is invisible to your route handlers.

### Why Redis?

- Sessions are shared across all server instances
- Sub-millisecond reads and writes
- Built-in key expiry (session cleanup happens automatically)
- No disk I/O

### Redis with a Prefix

If you share a Redis instance with other applications, add a prefix to avoid key collisions:

```env
TINA4_SESSION_HANDLER=redis
TINA4_SESSION_HOST=localhost
TINA4_SESSION_PORT=6379
TINA4_SESSION_PREFIX=myapp:sess:
```

---

## 5. MongoDB Sessions

If your stack already uses MongoDB, you can store sessions there:

```env
TINA4_SESSION_HANDLER=mongodb
TINA4_SESSION_HOST=localhost
TINA4_SESSION_PORT=27017
TINA4_SESSION_DATABASE=myapp
TINA4_SESSION_COLLECTION=sessions
```

MongoDB sessions support TTL indexes, so expired sessions are cleaned up automatically by MongoDB itself.

---

## 6. Valkey Sessions

Valkey is the open-source fork of Redis. If you use Valkey, the configuration is almost identical:

```env
TINA4_SESSION_HANDLER=valkey
TINA4_SESSION_HOST=localhost
TINA4_SESSION_PORT=6379
```

Valkey is wire-compatible with Redis, so the same client library works for both.

---

## 7. Reading and Writing Session Data

Session data is a simple key-value store. You read and write it through `$request->session`:

```php
<?php
use Tina4\Route;

// Write to session
Route::post("/api/preferences", function ($request, $response) {
    $body = $request->body;

    $request->session["language"] = $body["language"] ?? "en";
    $request->session["theme"] = $body["theme"] ?? "light";
    $request->session["items_per_page"] = (int) ($body["items_per_page"] ?? 20);

    return $response->json([
        "message" => "Preferences saved",
        "preferences" => [
            "language" => $request->session["language"],
            "theme" => $request->session["theme"],
            "items_per_page" => $request->session["items_per_page"]
        ]
    ]);
});

// Read from session
Route::get("/api/preferences", function ($request, $response) {
    return $response->json([
        "language" => $request->session["language"] ?? "en",
        "theme" => $request->session["theme"] ?? "light",
        "items_per_page" => $request->session["items_per_page"] ?? 20
    ]);
});

// Delete a specific key
Route::delete("/api/preferences/{key}", function ($request, $response) {
    $key = $request->params["key"];
    unset($request->session[$key]);

    return $response->json(["message" => "Preference '" . $key . "' removed"]);
});

// Clear all session data
Route::post("/api/session/clear", function ($request, $response) {
    $request->session = [];

    return $response->json(["message" => "Session cleared"]);
});
```

```bash
curl -X POST http://localhost:7145/api/preferences \
  -H "Content-Type: application/json" \
  -d '{"language": "es", "theme": "dark", "items_per_page": 50}' \
  -c cookies.txt -b cookies.txt
```

```json
{
  "message": "Preferences saved",
  "preferences": {
    "language": "es",
    "theme": "dark",
    "items_per_page": 50
  }
}
```

```bash
curl http://localhost:7145/api/preferences -b cookies.txt
```

```json
{"language":"es","theme":"dark","items_per_page":50}
```

### Storing Complex Data

Sessions can hold arrays and nested structures:

```php
Route::post("/api/cart/add", function ($request, $response) {
    $body = $request->body;

    if (!isset($request->session["cart"])) {
        $request->session["cart"] = [];
    }

    $cart = $request->session["cart"];

    $cart[] = [
        "product_id" => (int) $body["product_id"],
        "name" => $body["name"],
        "price" => (float) $body["price"],
        "quantity" => (int) ($body["quantity"] ?? 1),
        "added_at" => date("c")
    ];

    $request->session["cart"] = $cart;

    $total = array_sum(array_map(
        fn($item) => $item["price"] * $item["quantity"],
        $cart
    ));

    return $response->json([
        "message" => "Added to cart",
        "cart_items" => count($cart),
        "cart_total" => $total
    ]);
});
```

---

## 8. Flash Messages

Flash messages are session data that exists for exactly one request. You set a flash message before redirecting, and it is available on the very next request. After that next request reads it, it is gone.

This is the standard pattern for form submissions: submit the form, redirect to a success page, show a "Profile updated" message that disappears on refresh.

### Setting a Flash Message

```php
<?php
use Tina4\Route;

Route::post("/profile/update", function ($request, $response) {
    $body = $request->body;

    // Update the profile (database logic here)

    // Set a flash message
    $request->session["_flash"] = [
        "type" => "success",
        "message" => "Profile updated successfully"
    ];

    return $response->redirect("/profile");
});
```

### Reading and Clearing Flash Messages

```php
Route::get("/profile", function ($request, $response) {
    // Read the flash message
    $flash = $request->session["_flash"] ?? null;

    // Clear it immediately so it does not show again
    unset($request->session["_flash"]);

    return $response->render("profile.html", [
        "user" => ["name" => "Alice", "email" => "alice@example.com"],
        "flash" => $flash
    ]);
});
```

### Using Flash Messages in Templates

```html
{% extends "base.html" %}

{% block content %}
    {% if flash %}
        <div class="alert alert-{{ flash.type }}">
            {{ flash.message }}
        </div>
    {% endif %}

    <h1>Profile</h1>
    <p>Name: {{ user.name }}</p>
    <p>Email: {{ user.email }}</p>
{% endblock %}
```

The alert div appears on the first load after the form submission. If the user refreshes, the flash message is gone because it was cleared when it was first read.

### Multiple Flash Messages

You can flash multiple messages by using an array:

```php
$request->session["_flash"] = [
    ["type" => "success", "message" => "Email updated"],
    ["type" => "warning", "message" => "Please verify your new email address"]
];
```

```html
{% if flash %}
    {% for msg in flash %}
        <div class="alert alert-{{ msg.type }}">
            {{ msg.message }}
        </div>
    {% endfor %}
{% endif %}
```

---

## 9. Setting and Reading Cookies

Cookies are small pieces of data stored in the browser. Unlike sessions, the data is stored client-side. Use cookies for non-sensitive preferences that should persist even after the session expires.

### Setting a Cookie

```php
<?php
use Tina4\Route;

Route::post("/api/set-language", function ($request, $response) {
    $language = $request->body["language"] ?? "en";

    $response->setCookie("language", $language, [
        "expires" => time() + (365 * 24 * 60 * 60),  // 1 year
        "path" => "/",
        "httpOnly" => false,  // Allow JavaScript to read it
        "secure" => false,    // Set to true in production (HTTPS only)
        "sameSite" => "Lax"
    ]);

    return $response->json(["message" => "Language set to " . $language]);
});
```

### Reading a Cookie

```php
Route::get("/api/get-language", function ($request, $response) {
    $language = $request->cookies["language"] ?? "en";

    return $response->json(["language" => $language]);
});
```

```bash
curl -X POST http://localhost:7145/api/set-language \
  -H "Content-Type: application/json" \
  -d '{"language": "fr"}' \
  -c cookies.txt

curl http://localhost:7145/api/get-language -b cookies.txt
```

```json
{"language":"fr"}
```

### Deleting a Cookie

To delete a cookie, set it with an expiry date in the past:

```php
Route::post("/api/clear-language", function ($request, $response) {
    $response->setCookie("language", "", [
        "expires" => time() - 3600,
        "path" => "/"
    ]);

    return $response->json(["message" => "Language cookie cleared"]);
});
```

### When to Use Cookies vs Sessions

| Use Cookies For | Use Sessions For |
|-----------------|------------------|
| Language preference | Shopping cart contents |
| Theme preference (light/dark) | User authentication state |
| "Remember this device" flag | Flash messages |
| Analytics tracking consent | Form wizard progress |
| Non-sensitive, long-lived data | Sensitive, short-lived data |

---

## 10. Remember Me Functionality

The "remember me" pattern uses a long-lived cookie to re-authenticate users after their session expires.

```php
<?php
use Tina4\Route;
use Tina4\Auth;
use Tina4\Database;

/**
 * @noauth
 */
Route::post("/login", function ($request, $response) {
    $body = $request->body;
    $db = Database::getConnection();

    // Validate credentials
    $user = $db->fetchOne(
        "SELECT id, name, email, password_hash FROM users WHERE email = :email",
        ["email" => $body["email"]]
    );

    if ($user === null || !Auth::checkPassword($body["password"], $user["password_hash"])) {
        return $response->json(["error" => "Invalid email or password"], 401);
    }

    // Set session
    $request->session["user_id"] = $user["id"];
    $request->session["user_name"] = $user["name"];

    // Handle "remember me"
    if (!empty($body["remember_me"])) {
        $rememberToken = bin2hex(random_bytes(32));

        // Store hashed token in database
        $db->execute(
            "UPDATE users SET remember_token = :token WHERE id = :id",
            ["token" => hash("sha256", $rememberToken), "id" => $user["id"]]
        );

        // Set long-lived cookie with the unhashed token
        $response->setCookie("remember_me", $rememberToken, [
            "expires" => time() + (30 * 24 * 60 * 60),  // 30 days
            "path" => "/",
            "httpOnly" => true,
            "secure" => true,
            "sameSite" => "Lax"
        ]);
    }

    return $response->json([
        "message" => "Login successful",
        "user" => ["id" => $user["id"], "name" => $user["name"]]
    ]);
});
```

The "remember me" middleware that checks the cookie:

```php
<?php
use Tina4\Database;

function rememberMeMiddleware($request, $response, $next) {
    // Already logged in via session? Continue.
    if (!empty($request->session["user_id"])) {
        return $next($request, $response);
    }

    // Check for remember_me cookie
    $rememberToken = $request->cookies["remember_me"] ?? "";

    if (empty($rememberToken)) {
        return $next($request, $response);
    }

    $db = Database::getConnection();
    $hashedToken = hash("sha256", $rememberToken);

    $user = $db->fetchOne(
        "SELECT id, name, email FROM users WHERE remember_token = :token",
        ["token" => $hashedToken]
    );

    if ($user !== null) {
        // Restore session from cookie
        $request->session["user_id"] = $user["id"];
        $request->session["user_name"] = $user["name"];
    }

    return $next($request, $response);
}
```

The flow:

1. User logs in with "remember me" checked
2. Server stores a hashed token in the database and sets an unhashed token in a cookie
3. Session expires (user closes browser or session lifetime ends)
4. User returns -- session is empty, but the `remember_me` cookie is still there
5. Middleware finds the cookie, looks up the hashed token in the database, restores the session
6. User is logged in again without entering credentials

We store the hash in the database and the raw token in the cookie. If the database is breached, the attacker gets hashes, not tokens. They cannot forge the cookie.

---

## 11. Session Security

### Configuration Options

```env
TINA4_SESSION_LIFETIME=3600       # Session expires after 1 hour of inactivity
TINA4_SESSION_NAME=tina4_session  # Cookie name for the session ID
TINA4_SESSION_SECURE=true         # Only send cookie over HTTPS
TINA4_SESSION_HTTPONLY=true       # JavaScript cannot access the cookie
TINA4_SESSION_SAMESITE=Lax        # CSRF protection
```

### httpOnly

When `TINA4_SESSION_HTTPONLY=true` (the default), the session cookie cannot be read by JavaScript. This prevents XSS attacks from stealing the session ID. There is almost never a reason to set this to `false`.

### secure

When `TINA4_SESSION_SECURE=true`, the session cookie is only sent over HTTPS connections. Set this to `true` in production. During development with `http://localhost`, set it to `false` or your browser will not send the cookie.

### sameSite

The `sameSite` attribute controls whether the browser sends the cookie with cross-site requests:

| Value | Behavior |
|-------|----------|
| `Strict` | Cookie is never sent with cross-site requests. Safest, but breaks some legitimate flows (e.g., clicking a link from an email). |
| `Lax` | Cookie is sent with top-level navigations (clicking links) but not with cross-site API calls. Good default. |
| `None` | Cookie is always sent. Requires `secure=true`. Only use if you need cross-site cookie access. |

### Session Regeneration

After a user logs in, regenerate the session ID to prevent session fixation attacks:

```php
Route::post("/login", function ($request, $response) {
    // Validate credentials...

    // Regenerate session ID (keeps the data, changes the ID)
    $request->sessionRegenerate();

    $request->session["user_id"] = $user["id"];

    return $response->redirect("/dashboard");
});
```

Session fixation is an attack where an attacker sets a known session ID on the victim's browser before the victim logs in. After login, the attacker uses the same session ID to access the victim's account. Regenerating the session ID after login invalidates the attacker's known ID.

---

## 12. Exercise: Build a Shopping Cart with Session Storage

Build a shopping cart that stores items in the session. No database needed -- the cart lives entirely in session data.

### Requirements

Create these endpoints:

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/cart/add` | Add an item to the cart. Body: `{"product_id": 1, "name": "Widget", "price": 9.99, "quantity": 2}` |
| `GET` | `/api/cart` | View the cart. Show items, quantities, item subtotals, and cart total. |
| `PUT` | `/api/cart/{product_id:int}` | Update quantity. Body: `{"quantity": 3}`. Remove item if quantity is 0. |
| `DELETE` | `/api/cart/{product_id:int}` | Remove an item from the cart. |
| `DELETE` | `/api/cart` | Clear the entire cart. |

### Business Rules

1. If adding a product that already exists in the cart, increment the quantity instead of adding a duplicate
2. Cart total should be calculated dynamically
3. Return the full cart state after every operation

### Test with:

```bash
# Add first item
curl -X POST http://localhost:7145/api/cart/add \
  -H "Content-Type: application/json" \
  -d '{"product_id": 1, "name": "Wireless Keyboard", "price": 79.99, "quantity": 1}' \
  -c cookies.txt -b cookies.txt

# Add second item
curl -X POST http://localhost:7145/api/cart/add \
  -H "Content-Type: application/json" \
  -d '{"product_id": 2, "name": "USB-C Hub", "price": 49.99, "quantity": 2}' \
  -c cookies.txt -b cookies.txt

# Add more of item 1 (should increment, not duplicate)
curl -X POST http://localhost:7145/api/cart/add \
  -H "Content-Type: application/json" \
  -d '{"product_id": 1, "name": "Wireless Keyboard", "price": 79.99, "quantity": 1}' \
  -c cookies.txt -b cookies.txt

# View cart
curl http://localhost:7145/api/cart -b cookies.txt

# Update quantity
curl -X PUT http://localhost:7145/api/cart/2 \
  -H "Content-Type: application/json" \
  -d '{"quantity": 5}' \
  -c cookies.txt -b cookies.txt

# Remove an item
curl -X DELETE http://localhost:7145/api/cart/1 -b cookies.txt -c cookies.txt

# Clear cart
curl -X DELETE http://localhost:7145/api/cart -b cookies.txt -c cookies.txt
```

---

## 13. Solution

Create `src/routes/cart.php`:

```php
<?php
use Tina4\Route;

function getCart($session) {
    return $session["cart"] ?? [];
}

function cartResponse($cart) {
    $total = 0;
    $itemCount = 0;
    $items = [];

    foreach ($cart as $item) {
        $subtotal = $item["price"] * $item["quantity"];
        $total += $subtotal;
        $itemCount += $item["quantity"];
        $items[] = array_merge($item, ["subtotal" => $subtotal]);
    }

    return [
        "items" => $items,
        "item_count" => $itemCount,
        "unique_items" => count($cart),
        "total" => round($total, 2)
    ];
}

// Add item to cart
Route::post("/api/cart/add", function ($request, $response) {
    $body = $request->body;

    if (empty($body["product_id"]) || empty($body["name"]) || !isset($body["price"])) {
        return $response->json(["error" => "product_id, name, and price are required"], 400);
    }

    $cart = getCart($request->session);
    $productId = (int) $body["product_id"];
    $quantity = (int) ($body["quantity"] ?? 1);
    $found = false;

    // Check if product already in cart
    foreach ($cart as $index => $item) {
        if ($item["product_id"] === $productId) {
            $cart[$index]["quantity"] += $quantity;
            $found = true;
            break;
        }
    }

    // Add new item if not found
    if (!$found) {
        $cart[] = [
            "product_id" => $productId,
            "name" => $body["name"],
            "price" => (float) $body["price"],
            "quantity" => $quantity
        ];
    }

    $request->session["cart"] = $cart;

    return $response->json(cartResponse($cart));
});

// View cart
Route::get("/api/cart", function ($request, $response) {
    $cart = getCart($request->session);
    return $response->json(cartResponse($cart));
});

// Update quantity
Route::put("/api/cart/{product_id:int}", function ($request, $response) {
    $productId = $request->params["product_id"];
    $quantity = (int) ($request->body["quantity"] ?? 0);
    $cart = getCart($request->session);
    $found = false;

    foreach ($cart as $index => $item) {
        if ($item["product_id"] === $productId) {
            if ($quantity <= 0) {
                array_splice($cart, $index, 1);
            } else {
                $cart[$index]["quantity"] = $quantity;
            }
            $found = true;
            break;
        }
    }

    if (!$found) {
        return $response->json(["error" => "Product not in cart"], 404);
    }

    $request->session["cart"] = $cart;

    return $response->json(cartResponse($cart));
});

// Remove item
Route::delete("/api/cart/{product_id:int}", function ($request, $response) {
    $productId = $request->params["product_id"];
    $cart = getCart($request->session);
    $found = false;

    foreach ($cart as $index => $item) {
        if ($item["product_id"] === $productId) {
            array_splice($cart, $index, 1);
            $found = true;
            break;
        }
    }

    if (!$found) {
        return $response->json(["error" => "Product not in cart"], 404);
    }

    $request->session["cart"] = $cart;

    return $response->json(cartResponse($cart));
});

// Clear cart
Route::delete("/api/cart", function ($request, $response) {
    $request->session["cart"] = [];

    return $response->json(cartResponse([]));
});
```

**Expected output after adding two items and then adding more of item 1:**

```bash
curl http://localhost:7145/api/cart -b cookies.txt
```

```json
{
  "items": [
    {
      "product_id": 1,
      "name": "Wireless Keyboard",
      "price": 79.99,
      "quantity": 2,
      "subtotal": 159.98
    },
    {
      "product_id": 2,
      "name": "USB-C Hub",
      "price": 49.99,
      "quantity": 2,
      "subtotal": 99.98
    }
  ],
  "item_count": 4,
  "unique_items": 2,
  "total": 259.96
}
```

Notice that the Wireless Keyboard has `quantity: 2` (1 + 1 from the second add), not two separate entries.

**Expected output after updating quantity of item 2 to 5:**

```json
{
  "items": [
    {
      "product_id": 1,
      "name": "Wireless Keyboard",
      "price": 79.99,
      "quantity": 2,
      "subtotal": 159.98
    },
    {
      "product_id": 2,
      "name": "USB-C Hub",
      "price": 49.99,
      "quantity": 5,
      "subtotal": 249.95
    }
  ],
  "item_count": 7,
  "unique_items": 2,
  "total": 409.93
}
```

**Expected output after clearing the cart:**

```json
{
  "items": [],
  "item_count": 0,
  "unique_items": 0,
  "total": 0
}
```

---

## 14. Gotchas

### 1. Sessions Do Not Work with curl Without Cookie Flags

**Problem:** Each curl request sees an empty session, as if it is a new user.

**Cause:** curl does not automatically save or send cookies. Without the `-c` and `-b` flags, every request starts a new session.

**Fix:** Use `-c cookies.txt -b cookies.txt` with curl. The `-c` flag saves cookies to a file after the response, and `-b` sends cookies from that file with the request. Browsers handle this automatically.

### 2. Session Data Disappears After Server Restart

**Problem:** All session data is gone after restarting the dev server.

**Cause:** If you are using file sessions and the session files are stored in the system temp directory, a server restart might clear them (depending on your OS and PHP configuration). Or, if the session ID cookie has expired, the browser sends a new request without the cookie.

**Fix:** Set `TINA4_SESSION_PATH` to a persistent directory outside the temp folder. For production, use Redis or Valkey which persist data independently of the web server.

### 3. Session Cookie Not Sent Over HTTP in Production

**Problem:** Sessions work locally but not in production. The browser does not send the session cookie.

**Cause:** `TINA4_SESSION_SECURE=true` means the cookie is only sent over HTTPS. If your production server is behind a reverse proxy that terminates SSL, the app sees HTTP and the cookie is not set.

**Fix:** Ensure your reverse proxy sets the `X-Forwarded-Proto: https` header, and that Tina4 trusts proxy headers. Or make sure `TINA4_SESSION_SECURE` is only `true` when the connection is genuinely HTTPS end-to-end.

### 4. Flash Messages Show Twice

**Problem:** The flash message appears, then appears again on the next page load.

**Cause:** You read the flash message but did not clear it from the session. It persists until explicitly removed.

**Fix:** Always clear the flash message immediately after reading it: `unset($request->session["_flash"])`. The flash pattern requires manual cleanup -- read it, use it, delete it, all in the same request.

### 5. Large Session Data Causes Slow Requests

**Problem:** Pages load slowly and performance degrades over time.

**Cause:** You are storing large amounts of data in the session (entire database result sets, uploaded file contents, large arrays). Session data is serialized and deserialized on every request.

**Fix:** Keep session data small. Store IDs and references, not entire objects. If a cart has 50 items, store `[{"product_id": 1, "quantity": 2}, ...]` rather than full product objects with descriptions, images, and metadata.

### 6. Remember Me Token Not Invalidated on Password Change

**Problem:** After a user changes their password, their "remember me" cookies on other devices still work.

**Cause:** The remember-me token in the database was not cleared when the password changed.

**Fix:** Clear the `remember_token` column whenever the password is updated: `$db->execute("UPDATE users SET remember_token = NULL WHERE id = :id", ["id" => $userId])`. This forces all other devices to log in again with the new password.

### 7. Session Fixation

**Problem:** An attacker can hijack a user's session by setting a known session ID before the user logs in.

**Cause:** The session ID is not regenerated after login. The attacker knows the session ID (because they set it), and after the user logs in, the attacker's session ID now has an authenticated session.

**Fix:** Call `$request->sessionRegenerate()` after successful login. This creates a new session ID, copies the data, and invalidates the old ID. The attacker's known ID becomes useless.
