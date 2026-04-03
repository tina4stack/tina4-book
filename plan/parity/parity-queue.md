# Parity Audit: Queue

> **Generated:** 2026-04-03 | **Updated:** 2026-04-03 | **Version:** v3.10.67

## Status: FULL PARITY (100%) — audit corrected

All 4 frameworks have identical Queue APIs and backends. The initial audit was wrong.

---

## Core Methods — ALL PRESENT IN ALL 4

| Method | Python | PHP | Ruby | Node.js | Parity |
|--------|--------|-----|------|---------|--------|
| `push(data)` | YES | YES | YES | YES | OK |
| `pop()` | YES | YES | YES | YES | OK |
| `consume(topic, id?, poll_interval?)` | YES (generator) | YES (generator) | YES (enum/block) | YES (async generator) | OK |
| `size(status?)` | YES | YES | YES | YES | OK |
| `purge(status?)` | YES | YES | YES | YES | OK |
| `retry_failed()` / `retryFailed()` | YES | YES | YES | YES | OK |
| `dead_letters()` / `deadLetters()` | YES | YES | YES | YES | OK |
| Job: `complete()`, `fail()`, `reject()`, `retry()` | YES | YES | YES | YES | OK |

## Backends — ALL 4 IN ALL 4

| Backend | Python | PHP | Ruby | Node.js |
|---------|--------|-----|------|---------|
| File/SQLite | YES | YES (sqlite) | YES (lite) | YES (file) |
| RabbitMQ | YES | YES | YES | YES |
| Kafka | YES | YES | YES | YES |
| MongoDB | YES | YES | YES | YES |

## consume() with poll_interval — FIXED this session

All 4 frameworks now support `consume(topic, poll_interval)`:
- `poll_interval > 0`: long-running generator, sleeps when empty (default 1.0s / 1000ms)
- `poll_interval = 0`: single-pass drain (old behavior, for tests)

## Issues — ALL RESOLVED

| # | Original Issue | Status |
|---|---------------|--------|
| 1 | ~~PHP uses enqueue/dequeue~~ | **AUDIT ERROR** — PHP has push/pop |
| 2 | ~~PHP lacks unified Queue~~ | **AUDIT ERROR** — PHP has full Queue class |
| 3 | ~~Consume pattern differs~~ | FIXED — all use generator with poll_interval |
| 4 | ~~Node missing backends~~ | **AUDIT ERROR** — Node has RabbitMQ/Kafka/MongoDB |
| 5 | No peek()/remove(id) | PARKED — not needed |
