# Parity Audit: Session

> **Generated:** 2026-04-03 | **Version:** v3.10.67

## Status: MODERATE PARITY (85%)

Core CRUD methods (get/set/delete/has/all/clear/destroy) are consistent. Flash, regenerate, save visibility, and constructor patterns differ.

---

## Backends Supported

| Backend | Python | PHP | Ruby | Node.js |
|---------|--------|-----|------|---------|
| File | YES | YES | YES | YES |
| Redis | YES | YES | YES | YES (raw TCP + npm) |
| Valkey | YES | YES | YES | YES |
| MongoDB | YES | YES | YES | YES |
| Database | YES | YES | YES | YES |

- [ ] **PARITY: OK** — all 5 backends across all 4 frameworks

## Core Methods

| Method | Python | PHP | Ruby | Node.js | Parity |
|--------|--------|-----|------|---------|--------|
| `get(key, default)` | YES | YES | YES | YES | OK |
| `set(key, value)` | YES | YES | YES | YES | OK |
| `delete(key)` | YES | YES | YES | YES | OK |
| `has(key)` | YES | YES | YES (`has?`) | YES | OK |
| `all()` | YES | YES | YES | YES | OK |
| `clear()` | YES | YES | YES | YES (duplicate bug) | BUG |
| `destroy()` | YES | YES | YES | YES | OK |
| `start(sessionId?)` | YES | YES | constructor | YES | INCONSISTENT |

- [ ] **Documented?** Python CLAUDE.md: yes. Others: minimal.

## Issues to Fix

| # | Issue | Severity | Frameworks |
|---|-------|----------|------------|
| 1 | **Node.js has duplicate `clear()` method** (two definitions) | HIGH | Node.js |
| 2 | **Flash API differs** — Python/Ruby: dual-mode `flash(key, value?)`. PHP/Node: separate `flash()` + `getFlash()` | MEDIUM | All |
| 3 | **`regenerate()` return** — Ruby returns `nil`, others return new session ID string | MEDIUM | Ruby |
| 4 | **`save()` visibility** — Node.js makes it private, others expose it | MEDIUM | Node.js |
| 5 | **Session ID access** — Python: `session.session_id` property. PHP: `getSessionId()`. Ruby: `session.id`. Node: `getId()` | LOW | All |
| 6 | **`cookie_header()` helper** — only Python/Ruby have it | LOW | PHP, Node.js |
| 7 | **Constructor differs** — Python takes handler instance, PHP/Node take backend string, Ruby takes env | LOW | All |
| 8 | **Persistence model** — Python/Ruby use dirty flag (lazy save). PHP/Node auto-save on every set/delete | LOW | All |

## Documentation Gaps

| # | Gap |
|---|-----|
| 1 | Only Python CLAUDE.md documents Session API in detail |
| 2 | PHP/Ruby/Node CLAUDE.md have minimal Session docs |
| 3 | Flash API semantic differences not documented anywhere |
| 4 | Backend naming conventions not standardized in docs |
