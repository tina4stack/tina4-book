# Parity Audit: Template / Frond Engine

> **Generated:** 2026-04-03 | **Updated:** 2026-04-09 | **Version:** v3.10.89

## Status: FULL PARITY (100%) — audit corrected

All 4 frameworks have the complete Frond API. The initial audit checked Ruby's `Template` wrapper (limited) instead of the underlying `Frond` class (full API). Node.js has `@tina4/frond` package with all methods.

---

## Core Methods

| Method | Python | PHP | Ruby | Node.js | Parity |
|--------|--------|-----|------|---------|--------|
| `render(template, data)` | YES | YES | YES | YES (async) | OK |
| `render_string(source, data)` | YES | YES | YES | YES | OK |
| `add_filter(name, fn)` | YES | YES | YES | YES | OK |
| `add_global(name, value)` | YES | YES | YES | YES | OK |
| `add_test(name, fn)` | YES | YES | YES | YES | OK |
| `clear_cache()` | YES | YES | YES | YES | OK |
| `sandbox(filters, tags, vars)` | YES | YES | YES | YES | OK |
| `unsandbox()` | YES | YES | YES | YES | OK |

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

## Dump Helper (v3.10.89+)

All 4 frameworks expose `dump` as **both a filter and a callable global function**. Both forms delegate to a single `render_dump` helper per framework so they produce identical output.

| Framework | Filter | Function | Shared helper |
|-----------|--------|----------|---------------|
| Python | `{{ x\|dump }}` | `{{ dump(x) }}` | `_render_dump()` |
| PHP | `{{ x\|dump }}` | `{{ dump($x) }}` | `Frond::renderDump()` |
| Ruby | `{{ x\|dump }}` | `{{ dump(x) }}` | `Tina4::Frond.render_dump` |
| Node.js | `{{ x\|dump }}` | `{{ dump(x) }}` | `renderDump()` |

**Production gating.** All 4 implementations check `TINA4_DEBUG=true` at call time. In production (env var unset or `false`) both filter and function return an empty string — prevents accidental leaks of internal state, object shapes, and sensitive values through rendered HTML.

**Output format.** Language-native inspection wrapped in `<pre>` and HTML-escaped:
- Python: `repr(v)` — prints `{...}` for cycles
- PHP: `var_dump($v)` — prints `*RECURSION*` for cycles
- Ruby: `v.inspect` — prints `{...}` for cycles
- Node.js: `inspectValue(v)` — custom inspector with `[Circular]`, BigInt, Map/Set, Error, Date support

- [x] **PARITY: OK** — all 4 implementations cross-tested and released in v3.10.89

## Issues to Fix

| # | Issue | Severity | Status |
|---|-------|----------|--------|
| 1 | ~~Ruby missing methods~~ | HIGH | **AUDIT ERROR** — `Tina4::Frond` class has all methods |
| 2 | ~~Node.js missing methods~~ | HIGH | **AUDIT ERROR** — `@tina4/frond` package has all methods |
| 3 | Node.js render async | MEDIUM | BY DESIGN — Node is async |
| 4 | Constructor style differs | LOW | BY DESIGN — all accept template_dir |

## Documentation Gaps

| # | Gap |
|---|-----|
| 1 | Ruby CLAUDE.md only documents `Template.render()` and `add_global()` |
| 2 | Node.js CLAUDE.md only documents `response.render()` — no Frond class API |
| 3 | `render_string()` not documented for Ruby/Node (because it doesn't exist) |
| 4 | Sandbox feature not documented for Ruby/Node (because it doesn't exist) |
