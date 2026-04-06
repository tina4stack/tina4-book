# Parity Audit: SSE (Server-Sent Events) / Streaming Responses

> **Generated:** 2026-04-06 | **Version:** v3.10.69+

## Status: FULL PARITY (100%)

---

## `response.stream()` — Streaming Response Method

| # | Feature | Python | PHP | Ruby | Node.js |
|---|---------|--------|-----|------|---------|
| 1 | `response.stream(generator)` method exists | Yes | Yes | Yes | Yes |
| 2 | Default content type `text/event-stream` | Yes | Yes | Yes | Yes |
| 3 | Sets `Cache-Control: no-cache` | Yes | Yes | Yes | Yes |
| 4 | Sets `Connection: keep-alive` | Yes | Yes | Yes | Yes |
| 5 | Sets `X-Accel-Buffering: no` (nginx proxy support) | Yes | Yes | Yes | Yes |
| 6 | Custom content type override | Yes | Yes | Yes | Yes |
| 7 | Fluent return (returns self/response) | Yes | Yes | Yes | Yes |
| 8 | Default status 200 | Yes | Yes | Yes | Yes |
| 9 | Preserves existing headers/cookies | Yes | Yes | Yes | Yes |
| 10 | Chunks flushed immediately (real-time) | Yes | Yes | Yes | Yes |
| 11 | Client disconnect detection | N/A (ASGI) | Yes (`connection_aborted()`) | N/A (Rack) | N/A (Node) |

---

## Method Signatures

| Framework | Signature | Generator Type |
|-----------|-----------|---------------|
| Python | `response.stream(source, content_type="text/event-stream")` | `async generator` or sync iterable |
| PHP | `$response->stream(callable $source, string $contentType = "text/event-stream")` | `callable` returning a Generator (`yield`) |
| Ruby | `response.stream(content_type: "text/event-stream") { \|out\| out << chunk }` | Block with yielder |
| Node.js | `res.stream(asyncIterable, contentType?)` | `AsyncIterable<string \| Buffer>` |

---

## Server/Runtime Support

| Framework | Built-in Server | Production Server | Notes |
|-----------|----------------|-------------------|-------|
| Python | Yes (asyncio ASGI) | Yes (uvicorn) | Built-in server modified to flush `more_body` chunks immediately |
| PHP | Yes (built-in) | Yes (Apache/nginx) | Uses `ob_flush()` + `flush()`, `set_time_limit(0)` |
| Ruby | Yes (WEBrick/Puma) | Yes (Puma) | Returns Rack `Enumerator` body — server iterates and flushes |
| Node.js | Yes (node:http) | Yes (cluster) | Native `ServerResponse.write()` — chunked by default |

---

## Tests

| Framework | Test File | Test Count | Status |
|-----------|-----------|------------|--------|
| Python | `tests/test_sse.py` | 13 | All pass |
| PHP | `tests/SSETest.php` | 10 (14 assertions) | All pass |
| Ruby | `spec/sse_spec.rb` | 13 | All pass |
| Node.js | `test/sse.test.ts` | 24 | All pass |

**Total: 60 tests across all frameworks.**

---

## Issues

None. Full parity achieved on initial implementation.
