# Parity Audit: Template / Frond Engine

> **Generated:** 2026-04-03 | **Version:** v3.10.67

## Status: MODERATE PARITY (75%) — Ruby and Node.js lag behind

Python and PHP have full Frond APIs. Ruby and Node.js are missing several developer-facing methods.

---

## Core Methods

| Method | Python | PHP | Ruby | Node.js | Parity |
|--------|--------|-----|------|---------|--------|
| `render(template, data)` | YES | YES | YES | YES (async) | OK (sync vs async) |
| `render_string(source, data)` | YES | YES | NO | NO | MISSING |
| `add_filter(name, fn)` | YES | YES | NO | NO | MISSING |
| `add_global(name, value)` | YES | YES | YES | NO | PARTIAL |
| `add_test(name, fn)` | YES | YES | NO | NO | MISSING |
| `clear_cache()` | YES | YES | NO | NO | MISSING |
| `sandbox(filters, tags, vars)` | YES | YES | NO | NO | MISSING |
| `unsandbox()` | YES | YES | NO | NO | MISSING |

## Response Integration

| Framework | Method | Sync/Async |
|-----------|--------|------------|
| Python | `response.render(template, data)` | Sync |
| PHP | `response.template(template, data)` (alias: `render`) | Sync |
| Ruby | `response.render(template, data)` | Sync |
| Node.js | `response.render(template, data)` | **Async (Promise)** |

- [ ] **PARITY ISSUE:** Node.js render is async, others are sync

## Built-in Filters

- [ ] **PARITY: OK** — all 4 have 40+ identical filters (upper, lower, capitalize, trim, length, escape, etc.)

## Issues to Fix

| # | Issue | Severity | Frameworks |
|---|-------|----------|------------|
| 1 | **Ruby missing** `render_string`, `add_filter`, `add_test`, `clear_cache`, `sandbox` | HIGH | Ruby |
| 2 | **Node.js missing** `render_string`, `add_filter`, `add_global`, `add_test`, `clear_cache`, `sandbox` | HIGH | Node.js |
| 3 | **Node.js render is async** — Python/PHP/Ruby are sync | MEDIUM | Node.js |
| 4 | **Constructor style differs** — Python/PHP: `Frond(template_dir)`. Ruby: module-level. Node: separate package | LOW | Ruby, Node.js |

## Documentation Gaps

| # | Gap |
|---|-----|
| 1 | Ruby CLAUDE.md only documents `Template.render()` and `add_global()` |
| 2 | Node.js CLAUDE.md only documents `response.render()` — no Frond class API |
| 3 | `render_string()` not documented for Ruby/Node (because it doesn't exist) |
| 4 | Sandbox feature not documented for Ruby/Node (because it doesn't exist) |
