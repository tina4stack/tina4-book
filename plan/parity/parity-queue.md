# Parity Audit: Queue

> **Generated:** 2026-04-03 | **Version:** v3.10.67

## Status: MODERATE PARITY (75%)

---

## Core Methods

| Method | Python | PHP | Ruby | Node.js | Parity |
|--------|--------|-----|------|---------|--------|
| `push(job)` | YES | `enqueue()` | YES | YES | NAMING |
| `pop()` | YES | `dequeue()` | YES | YES | NAMING |
| `consume(handler)` | YES (generator) | N/A (raw backend) | YES (block) | `process()` (callback) | INCONSISTENT |
| `size()` | YES | YES | YES | YES | OK |
| `purge()` | YES | N/A | YES | `clear()` | NAMING |
| `retry_failed()` | YES | N/A | YES | `retryFailed()` | OK (casing) |
| `dead_letters()` | YES | N/A | YES | `deadLetters()` | OK (casing) |
| `peek()` | NO | NO | NO | NO | ALL MISSING |
| `remove(id)` | NO | NO | NO | NO | ALL MISSING |

## Issues to Fix

| # | Issue | Severity | Frameworks |
|---|-------|----------|------------|
| 1 | **PHP uses `enqueue`/`dequeue`** not `push`/`pop` | MEDIUM | PHP |
| 2 | **PHP lacks unified Queue wrapper** — uses raw backend interfaces | MEDIUM | PHP |
| 3 | **Consume pattern differs** — Python/Ruby generators, Node callback, PHP N/A | MEDIUM | All |
| 4 | **Node.js missing RabbitMQ/Kafka/MongoDB backends** — only file | HIGH | Node.js |
| 5 | **No `peek()` or `remove(id)` anywhere** | LOW | All |

## Documentation Gaps

| # | Gap |
|---|-----|
| 1 | PHP queue method naming inconsistency not flagged |
| 2 | Backend availability per framework not compared |
