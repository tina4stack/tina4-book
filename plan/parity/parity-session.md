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

| # | Issue | Severity | Status |
|---|-------|----------|--------|
| 1 | ~~Node.js duplicate `clear()`~~ | HIGH | FIXED — removed first, kept metadata-preserving version |
| 2 | ~~Flash API differs~~ | MEDIUM | FIXED — all dual-mode flash() + get_flash/getFlash alias |
| 3 | ~~Ruby `regenerate()` returns nil~~ | MEDIUM | FIXED — returns new session ID |
| 4 | ~~Node.js `save()` private~~ | MEDIUM | FIXED — made public |
| 5 | ~~Node `getId()` naming~~ | LOW | FIXED — renamed to `getSessionId()` |
| 6 | `cookie_header()` only Python/Ruby | LOW | PARKED — nice-to-have |
| 7 | Constructor differs | LOW | BY DESIGN — language idioms |
| 8 | Persistence model differs | LOW | BY DESIGN — lazy vs auto-save |

## Documentation Gaps

| # | Gap |
|---|-----|
| 1 | Only Python CLAUDE.md documents Session API in detail |
| 2 | PHP/Ruby/Node CLAUDE.md have minimal Session docs |
| 3 | Flash API semantic differences not documented anywhere |
| 4 | Backend naming conventions not standardized in docs |
