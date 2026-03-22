# Chapter 3: Request & Response

## 1. The Two Objects You Always Get

Every route handler in Tina4 receives two arguments: `request` and `response`. The request tells you what the client sent. The response is how you send something back. Together they are the entire HTTP conversation.

```ruby
Tina4::Router.get("/echo") do |request, response|
  response.json({
    method: request.method,
    path: request.path,
    your_ip: request.ip
  })
end
```

```bash
curl http://localhost:7147/echo
```

```json
{"method":"GET","path":"/echo","your_ip":"127.0.0.1"}
```

That is the pattern for every route: inspect the request, build the response, return it.

---

## 2. The Request Object

The `request` object gives you access to everything the client sent. Here is the complete list of properties.

### method

The HTTP method as an uppercase string: `"GET"`, `"POST"`, `"PUT"`, `"PATCH"`, or `"DELETE"`.

```ruby
request.method # "GET"
```

### path

The URL path without query parameters:

```ruby
# Request to /api/users?page=2
request.path # "/api/users"
```

### params

Path parameters from the URL pattern (see Chapter 2):

```ruby
# Route: /users/{id}/posts/{post_id}
# Request: /users/5/posts/42
request.params["id"]      # "5" (or 5 if typed as {id:int})
request.params["post_id"] # "42"
```

### query

Query string parameters as a hash:

```ruby
# Request: /search?q=keyboard&page=2&sort=price
request.query["q"]    # "keyboard"
request.query["page"] # "2"
request.query["sort"] # "price"
```

### body

The parsed request body. For JSON requests, this is a hash. For form submissions, it contains the form fields:

```ruby
# POST with {"name": "Widget", "price": 9.99}
request.body["name"]  # "Widget"
request.body["price"] # 9.99
```

### headers

Request headers as a hash. Header names are normalized to their original casing:

```ruby
request.headers["Content-Type"]  # "application/json"
request.headers["Authorization"] # "Bearer eyJhbGci..."
request.headers["X-Custom"]      # "my-value"
```

### ip

The client's IP address:

```ruby
request.ip # "127.0.0.1"
```

Tina4 respects `X-Forwarded-For` and `X-Real-IP` headers when behind a reverse proxy.

### cookies

Cookies sent by the client:

```ruby
request.cookies["session_id"]  # "abc123"
request.cookies["preferences"] # "dark-mode"
```

### files

Uploaded files (covered in detail in section 7):

```ruby
request.files["avatar"] # File object with name, type, size, tmp_path
```

### Inspecting the Full Request

Here is a route that dumps everything:

```ruby
Tina4::Router.post("/debug/request") do |request, response|
  response.json({
    method: request.method,
    path: request.path,
    params: request.params,
    query: request.query,
    body: request.body,
    headers: request.headers,
    ip: request.ip,
    cookies: request.cookies
  })
end
```

```bash
curl -X POST "http://localhost:7147/debug/request?page=1" \
  -H "Content-Type: application/json" \
  -H "X-Custom: hello" \
  -d '{"name": "test"}'
```

```json
{
  "method": "POST",
  "path": "/debug/request",
  "params": {},
  "query": {"page": "1"},
  "body": {"name": "test"},
  "headers": {
    "Content-Type": "application/json",
    "X-Custom": "hello",
    "Host": "localhost:7147",
    "User-Agent": "curl/8.4.0",
    "Accept": "*/*",
    "Content-Length": "16"
  },
  "ip": "127.0.0.1",
  "cookies": {}
}
```

---

## 3. The Response Object

The `response` object is your toolkit for sending data back to the client. Every method on it returns the response, so you can chain calls together.

### json -- JSON Response

The most common response for APIs. Pass any hash or value and it becomes JSON:

```ruby
response.json({ name: "Alice", age: 30 })
```

```json
{"name":"Alice","age":30}
```

Pass a status code as the second argument:

```ruby
response.json({ id: 7, name: "Widget" }, 201)
```

This returns `201 Created` with the JSON body.

### html -- Raw HTML Response

Return an HTML string directly:

```ruby
response.html("<h1>Hello</h1><p>This is HTML.</p>")
```

Sets `Content-Type: text/html; charset=utf-8` automatically.

### text -- Plain Text Response

Return plain text:

```ruby
response.text("Just a plain string.")
```

Sets `Content-Type: text/plain; charset=utf-8`.

### render -- Template Response

Render a Frond template with data (covered in depth in Chapter 4):

```ruby
response.render("products.html", {
  products: products,
  title: "Our Products"
})
```

Tina4 looks for the template in `src/templates/`, renders it with the provided data, and returns the HTML.

### redirect -- Redirect Response

Send the client to a different URL:

```ruby
response.redirect("/login")
```

This sends a `302 Found` redirect by default. Pass a different status code for permanent redirects:

```ruby
response.redirect("/new-location", 301)
```

### file -- File Download Response

Send a file to the client for download:

```ruby
response.file("/path/to/report.pdf")
```

This sets the appropriate `Content-Type` based on the file extension and adds a `Content-Disposition` header so the browser downloads the file rather than displaying it.

You can set a custom filename:

```ruby
response.file("/path/to/report.pdf", "monthly-report-march-2026.pdf")
```

---

## 4. Status Codes

Every response method accepts a status code. Here are the most common ones you will use:

| Code | Meaning | When to Use |
|------|---------|-------------|
| `200` | OK | Default. Successful GET, PUT, PATCH. |
| `201` | Created | Successful POST that created a resource. |
| `204` | No Content | Successful DELETE. No body needed. |
| `301` | Moved Permanently | URL has permanently changed. |
| `302` | Found | Temporary redirect. |
| `400` | Bad Request | Invalid input from the client. |
| `401` | Unauthorized | Missing or invalid authentication. |
| `403` | Forbidden | Authenticated but not allowed. |
| `404` | Not Found | Resource does not exist. |
| `409` | Conflict | Duplicate or conflicting data. |
| `422` | Unprocessable Entity | Valid JSON but fails business rules. |
| `500` | Internal Server Error | Something went wrong on the server. |

You can also set the status explicitly with the `status` method and chain it:

```ruby
response.status(201).json({ id: 7, created: true })
```

This is equivalent to `response.json({ id: 7, created: true }, 201)` but some developers find the chained form more readable.

---

## 5. Custom Headers

Set response headers with the `header` method:

```ruby
Tina4::Router.get("/api/data") do |request, response|
  response
    .header("X-Request-Id", SecureRandom.hex(8))
    .header("X-Rate-Limit-Remaining", "57")
    .header("Cache-Control", "no-cache")
    .json({ data: [1, 2, 3] })
end
```

```bash
curl -v http://localhost:7147/api/data 2>&1 | grep "< X-"
```

```
< X-Request-Id: 65f3a7b8c1234567
< X-Rate-Limit-Remaining: 57
```

Headers are case-insensitive in HTTP, but it is conventional to use `Title-Case` for custom headers and prefix them with `X-`.

### CORS Headers

Tina4 handles CORS automatically based on the `CORS_ORIGINS` setting in `.env`. The default `*` allows all origins. For production, restrict it:

```env
CORS_ORIGINS=https://myapp.com,https://admin.myapp.com
```

You rarely need to set CORS headers manually, but you can if needed:

```ruby
response
  .header("Access-Control-Allow-Origin", "https://myapp.com")
  .header("Access-Control-Allow-Methods", "GET, POST, PUT, DELETE")
  .header("Access-Control-Allow-Headers", "Content-Type, Authorization")
  .json({ data: "value" })
```

---

## 6. Cookies

Set cookies on the response:

```ruby
Tina4::Router.post("/login") do |request, response|
  # After validating credentials...
  response
    .cookie("session_id", "abc123xyz", {
      http_only: true,
      secure: true,
      same_site: "Strict",
      max_age: 3600,       # 1 hour in seconds
      path: "/"
    })
    .json({ message: "Logged in" })
end
```

Cookie options:

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `http_only` | bool | `false` | Cannot be accessed by JavaScript |
| `secure` | bool | `false` | Only sent over HTTPS |
| `same_site` | string | `"Lax"` | `"Strict"`, `"Lax"`, or `"None"` |
| `max_age` | int | session | Lifetime in seconds |
| `path` | string | `"/"` | URL path scope |
| `domain` | string | current | Domain scope |

Read cookies from the request:

```ruby
Tina4::Router.get("/profile") do |request, response|
  session_id = request.cookies["session_id"]

  if session_id.nil?
    return response.json({ error: "Not logged in" }, 401)
  end

  response.json({ session: session_id })
end
```

Delete a cookie by setting its `max_age` to `0`:

```ruby
response
  .cookie("session_id", "", { max_age: 0, path: "/" })
  .json({ message: "Logged out" })
```

---

## 7. File Uploads

Uploaded files are available via `request.files`. Each file is an object with properties for the file's metadata and a temporary path.

### Handling a Single File Upload

```ruby
Tina4::Router.post("/api/upload") do |request, response|
  if request.files["image"].nil?
    return response.json({ error: "No file uploaded" }, 400)
  end

  file = request.files["image"]

  response.json({
    name: file.name,        # "photo.jpg"
    type: file.type,        # "image/jpeg"
    size: file.size,        # 245760 (bytes)
    tmp_path: file.tmp_path # Temporary file location
  })
end
```

Test with curl:

```bash
curl -X POST http://localhost:7147/api/upload \
  -F "image=@/path/to/photo.jpg"
```

```json
{
  "name": "photo.jpg",
  "type": "image/jpeg",
  "size": 245760,
  "tmp_path": "/tmp/tina4_upload_abc123"
}
```

### Saving the Uploaded File

The uploaded file is stored in a temporary location. Move it to a permanent location:

```ruby
Tina4::Router.post("/api/upload") do |request, response|
  if request.files["image"].nil?
    return response.json({ error: "No file uploaded" }, 400)
  end

  file = request.files["image"]

  # Validate file type
  allowed_types = ["image/jpeg", "image/png", "image/gif", "image/webp"]
  unless allowed_types.include?(file.type)
    return response.json({ error: "Invalid file type. Allowed: JPEG, PNG, GIF, WebP" }, 400)
  end

  # Validate file size (max 5MB)
  max_size = 5 * 1024 * 1024
  if file.size > max_size
    return response.json({ error: "File too large. Maximum size: 5MB" }, 400)
  end

  # Generate a unique filename
  extension = File.extname(file.name)
  filename = "img_#{SecureRandom.hex(8)}#{extension}"
  upload_dir = File.join(__dir__, "../../public/uploads")
  destination = File.join(upload_dir, filename)

  # Ensure the uploads directory exists
  FileUtils.mkdir_p(upload_dir) unless Dir.exist?(upload_dir)

  # Move the file
  FileUtils.mv(file.tmp_path, destination)

  response.json({
    message: "File uploaded successfully",
    filename: filename,
    url: "/uploads/#{filename}",
    size: file.size
  }, 201)
end
```

```bash
curl -X POST http://localhost:7147/api/upload \
  -F "image=@/path/to/photo.jpg"
```

```json
{
  "message": "File uploaded successfully",
  "filename": "img_a1b2c3d4e5f6a7b8.jpg",
  "url": "/uploads/img_a1b2c3d4e5f6a7b8.jpg",
  "size": 245760
}
```

The uploaded file is now available at `http://localhost:7147/uploads/img_a1b2c3d4e5f6a7b8.jpg`.

### Handling Multiple Files

When the HTML form uses `multiple` or you have multiple file inputs:

```ruby
Tina4::Router.post("/api/upload-many") do |request, response|
  results = []

  request.files.each do |key, file|
    extension = File.extname(file.name)
    filename = "file_#{SecureRandom.hex(8)}#{extension}"
    upload_dir = File.join(__dir__, "../../public/uploads")
    destination = File.join(upload_dir, filename)

    FileUtils.mkdir_p(upload_dir) unless Dir.exist?(upload_dir)
    FileUtils.mv(file.tmp_path, destination)

    results << {
      original_name: file.name,
      saved_as: filename,
      url: "/uploads/#{filename}"
    }
  end

  response.json({ uploaded: results, count: results.length }, 201)
end
```

---

## 8. File Downloads

Send files to the client using `response.file`:

```ruby
Tina4::Router.get("/api/reports/{filename}") do |request, response|
  filename = request.params["filename"]
  filepath = File.join(__dir__, "../../data/reports", filename)

  unless File.exist?(filepath)
    return response.json({ error: "Report not found" }, 404)
  end

  response.file(filepath)
end
```

The browser will download the file. Tina4 automatically detects the MIME type from the file extension and sets the appropriate headers.

To force a specific download filename:

```ruby
response.file(filepath, "Q1-2026-Sales-Report.pdf")
```

---

## 9. Content Negotiation

Sometimes the same endpoint should return different formats based on what the client asks for. Check the `Accept` header:

```ruby
Tina4::Router.get("/api/products/{id:int}") do |request, response|
  id = request.params["id"]
  product = {
    id: id,
    name: "Wireless Keyboard",
    price: 79.99
  }

  accept = request.headers["Accept"] || "application/json"

  if accept.include?("text/html")
    response.render("product-detail.html", { product: product })
  elsif accept.include?("text/plain")
    text = "Product ##{id}: #{product[:name]} - $#{product[:price]}"
    response.text(text)
  else
    # Default to JSON
    response.json(product)
  end
end
```

```bash
# JSON (default)
curl http://localhost:7147/api/products/1
```

```json
{"id":1,"name":"Wireless Keyboard","price":79.99}
```

```bash
# Plain text
curl http://localhost:7147/api/products/1 -H "Accept: text/plain"
```

```
Product #1: Wireless Keyboard - $79.99
```

```bash
# HTML (would render the template)
curl http://localhost:7147/api/products/1 -H "Accept: text/html"
```

```html
<!DOCTYPE html>
<html>...rendered template...</html>
```

---

## 10. Exercise: Build an Image Upload API

Build an API that handles image uploads and serves them back. Create two endpoints:

### Requirements

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/images` | Upload an image. Validate type and size. Return the image URL. |
| `GET` | `/api/images/{filename}` | Return the uploaded image file. Return 404 if not found. |

Rules:

1. Only accept JPEG, PNG, and WebP files
2. Maximum file size: 2MB
3. Save files to `src/public/uploads/` with a unique filename
4. Return the original filename, the saved filename, file size in KB, and the URL
5. The GET endpoint should serve the file directly (not JSON)

### Test with:

```bash
# Upload
curl -X POST http://localhost:7147/api/images \
  -F "image=@/path/to/photo.jpg"

# Download
curl http://localhost:7147/api/images/img_a1b2c3d4e5f6a7b8.jpg --output downloaded.jpg
```

---

## 11. Solution

Create `src/routes/images.rb`:

```ruby
require "securerandom"
require "fileutils"

Tina4::Router.post("/api/images") do |request, response|
  # Check if a file was uploaded
  if request.files["image"].nil?
    return response.json({ error: "No image file provided. Use field name 'image'." }, 400)
  end

  file = request.files["image"]

  # Validate file type
  allowed_types = ["image/jpeg", "image/png", "image/webp"]
  unless allowed_types.include?(file.type)
    return response.json({
      error: "Invalid file type",
      received: file.type,
      allowed: allowed_types
    }, 400)
  end

  # Validate file size (max 2MB)
  max_size = 2 * 1024 * 1024
  if file.size > max_size
    return response.json({
      error: "File too large",
      size_bytes: file.size,
      max_bytes: max_size
    }, 400)
  end

  # Generate unique filename preserving extension
  extension = File.extname(file.name).downcase
  saved_name = "img_#{SecureRandom.hex(8)}#{extension}"
  upload_dir = File.join(__dir__, "../../public/uploads")
  destination = File.join(upload_dir, saved_name)

  # Create uploads directory if it does not exist
  FileUtils.mkdir_p(upload_dir) unless Dir.exist?(upload_dir)

  # Move the uploaded file
  FileUtils.mv(file.tmp_path, destination)

  response.json({
    message: "Image uploaded successfully",
    original_name: file.name,
    saved_name: saved_name,
    size_kb: (file.size / 1024.0).round(1),
    type: file.type,
    url: "/uploads/#{saved_name}"
  }, 201)
end

Tina4::Router.get("/api/images/{filename}") do |request, response|
  filename = request.params["filename"]

  # Prevent directory traversal
  if filename.include?("..") || filename.include?("/")
    return response.json({ error: "Invalid filename" }, 400)
  end

  filepath = File.join(__dir__, "../../public/uploads", filename)

  unless File.exist?(filepath)
    return response.json({ error: "Image not found", filename: filename }, 404)
  end

  response.file(filepath)
end
```

**Expected output for upload:**

```json
{
  "message": "Image uploaded successfully",
  "original_name": "photo.jpg",
  "saved_name": "img_a1b2c3d4e5f6a7b8.jpg",
  "size_kb": 240.0,
  "type": "image/jpeg",
  "url": "/uploads/img_a1b2c3d4e5f6a7b8.jpg"
}
```

(Status: `201 Created`)

**Expected output for invalid type:**

```json
{
  "error": "Invalid file type",
  "received": "application/pdf",
  "allowed": ["image/jpeg", "image/png", "image/webp"]
}
```

(Status: `400 Bad Request`)

**Expected output for file too large:**

```json
{
  "error": "File too large",
  "size_bytes": 5242880,
  "max_bytes": 2097152
}
```

(Status: `400 Bad Request`)

**The GET endpoint** returns the raw image file with the correct `Content-Type` header. The browser displays the image directly, and curl with `--output` saves it to disk.

---

## 12. Gotchas

### 1. Forgetting the response method

**Problem:** Your handler runs (you can see log output) but the browser shows an empty response or a 500 error.

**Cause:** You did not call `response.json`, `response.html`, or another response method. Ruby returns the last expression in a block, but if the last expression is not a response, Tina4 cannot send it to the client.

**Fix:** Always end your handler with a response method call: `response.json(...)`, `response.html(...)`, or `response.render(...)`.

### 2. Body Is Nil for JSON Requests

**Problem:** `request.body` is `nil` or empty even though you are sending JSON.

**Cause:** You forgot the `Content-Type: application/json` header in your request. Without it, Tina4 does not know to parse the body as JSON.

**Fix:** Always include `-H "Content-Type: application/json"` when sending JSON with curl. In frontend JavaScript, `fetch()` with `JSON.stringify()` requires `headers: {"Content-Type": "application/json"}`.

### 3. Content-Type Mismatch

**Problem:** You call `response.json` but the client receives HTML, or you call `response.html` but the client gets plain text.

**Cause:** A middleware or error handler is overwriting the response. Or you are using `puts` instead of a response method.

**Fix:** Make sure your handler uses `response.json(...)`, `response.html(...)`, or another response method. Do not use `puts` -- it bypasses the response object entirely.

### 4. File Uploads Return Empty

**Problem:** `request.files` is empty even though you are uploading a file.

**Cause:** The form is not using `enctype="multipart/form-data"`, or the curl command is using `-d` instead of `-F`.

**Fix:** For HTML forms, use `<form enctype="multipart/form-data">`. For curl, use `-F "field=@file.jpg"` (with `@`), not `-d`.

### 5. Redirect Loops

**Problem:** The browser shows "too many redirects" or hangs.

**Cause:** You have a route that redirects to another route, which redirects back to the first one. For example, `/login` redirects to `/dashboard`, and `/dashboard` redirects to `/login` because the user is not authenticated.

**Fix:** Check your redirect logic carefully. Use the browser's network inspector to trace the redirect chain. Make sure your auth check does not redirect authenticated users away from pages they should access.

### 6. Cookie Not Set

**Problem:** You called `response.cookie(...)` but the browser does not show the cookie.

**Cause:** If `secure` is `true`, the cookie is only sent over HTTPS. During local development with `http://localhost`, the cookie is silently dropped.

**Fix:** Set `secure: false` during development, or use `secure: ENV["TINA4_DEBUG"] != "true"` to auto-switch based on environment.

### 7. Large Request Body Rejected

**Problem:** POST requests with large bodies return a 413 error.

**Cause:** The request body exceeds the configured maximum size.

**Fix:** Increase `TINA4_MAX_BODY_SIZE` in `.env`. The default is `10mb`. For file upload endpoints, you may need `50mb` or more:

```env
TINA4_MAX_BODY_SIZE=50mb
```
