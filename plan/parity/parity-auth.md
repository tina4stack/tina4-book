# Parity Audit: Auth

> **Generated:** 2026-04-03 | **Version:** v3.10.67

## Status: MODERATE PARITY (80%) — Several critical issues

---

## Token Creation

### `get_token()` / `getToken()`

| Framework | Signature | expires_in unit | secret source |
|-----------|-----------|----------------|---------------|
| Python | `get_token(payload, expires_in=None)` | **MINUTES** | Instance or env `SECRET` |
| PHP | `getToken(payload, secret, expiresIn=3600)` | seconds | Required param |
| Ruby | `get_token(payload, expires_in: 3600)` | seconds | env `SECRET` |
| Node.js | `getToken(payload, secret, expiresIn=3600)` | seconds | Required param |

- [ ] **CRITICAL ISSUE:** Python uses **minutes**, others use **seconds**
- [ ] **PARITY ISSUE:** PHP/Node require explicit `secret` param; Python/Ruby read from env
- [ ] **Documented?** CLAUDE.md: yes but Python doesn't flag the minutes unit

## Token Validation

### `valid_token()` / `validToken()`

| Framework | Signature | Return |
|-----------|-----------|--------|
| Python | `valid_token(token)` | `dict \| None` |
| PHP | `validToken(token, secret, algorithm='HS256')` | `?array` |
| Ruby | `valid_token(token)` | `hash \| nil` |
| Node.js | `validToken(token, secret, algorithm='HS256')` | `Record \| null` |

- [ ] **PARITY ISSUE:** PHP/Node require explicit `secret` param; Python/Ruby don't
- [ ] **Documented?** All CLAUDE.md: partially

## Get Payload (no verification)

### `get_payload()` / `getPayload()`

| Framework | Signature | Return |
|-----------|-----------|--------|
| Python | `get_payload(token)` | `dict \| None` |
| PHP | `getPayload(token)` | `?array` |
| Ruby | `get_payload(token)` | `hash \| nil` |
| Node.js | `getPayload(token)` | `Record \| null` |

- [ ] **PARITY: OK** — all decode without verification, same signature
- [ ] **Documented?** All CLAUDE.md: yes

## Password Hashing

### `hash_password()` / `hashPassword()`

| Framework | Algorithm | Default iterations | Hash format |
|-----------|-----------|-------------------|-------------|
| Python | PBKDF2-SHA256 | **260000** | `pbkdf2_sha256$iterations$salt$hash` |
| PHP | PBKDF2-SHA256 | 100000 | `pbkdf2_sha256$iterations$salt$hash` |
| Ruby | **bcrypt** | ~12 cost factor | bcrypt format |
| Node.js | PBKDF2-SHA256 | 100000 | `pbkdf2_sha256:iterations:salt:hash` |

- [ ] **CRITICAL ISSUE:** Ruby uses **bcrypt**, not PBKDF2 — hashes NOT cross-framework portable
- [ ] **CRITICAL ISSUE:** Node.js delimiter is `:` not `$` — hashes NOT portable to Python/PHP
- [ ] **PARITY ISSUE:** Python iterations (260000) differ from PHP/Node (100000)
- [ ] **Documented?** Ruby mentions bcrypt. Others don't flag incompatibility.

## Check Password

### `check_password()` / `checkPassword()`

| Framework | Signature | Notes |
|-----------|-----------|-------|
| Python | `check_password(password, hashed)` | PBKDF2 |
| PHP | `checkPassword(password, hash)` | PBKDF2 |
| Ruby | `check_password(password, hash)` | bcrypt |
| Node.js | `checkPassword(password, hash)` | PBKDF2 |

- [ ] **CRITICAL ISSUE:** Ruby hashes can't be verified by Python/PHP/Node and vice versa
- [ ] **Documented?** Not flagged as incompatible

## API Key Validation

### `validate_api_key()` / `validateApiKey()`

| Framework | Timing-safe? |
|-----------|-------------|
| Python | YES (`hmac.compare_digest`) |
| PHP | YES (`hash_equals`) |
| Ruby | **NO** (uses plain `==`) |
| Node.js | YES (`timingSafeEqual`) |

- [ ] **SECURITY ISSUE:** Ruby's API key validation is NOT timing-safe
- [ ] **Documented?** Not flagged

## Authenticate Request

### `authenticate_request()` / `authenticateRequest()`

| Framework | API key fallback? | Basic auth? |
|-----------|------------------|-------------|
| Python | YES | YES |
| PHP | NO | NO |
| Ruby | YES | NO |
| Node.js | NO | NO |

- [ ] **PARITY ISSUE:** Python/Ruby fall back to API key if Bearer fails; PHP/Node don't
- [ ] **Documented?** Not flagged

## Algorithm Support

| Framework | HS256 | RS256 | Auto-select |
|-----------|-------|-------|-------------|
| Python | YES (stdlib) | NO | N/A |
| PHP | YES (stdlib) | YES (OpenSSL) | NO |
| Ruby | YES (stdlib) | YES (jwt gem) | YES (auto based on env) |
| Node.js | YES (stdlib) | YES (stdlib) | NO |

- [ ] **PARITY ISSUE:** Python doesn't support RS256
- [ ] **Documented?** CLAUDE.md: partially

## Issues to Fix (Priority Order)

| # | Issue | Severity | Frameworks |
|---|-------|----------|------------|
| 1 | **Ruby uses bcrypt, others PBKDF2** — hashes not portable | CRITICAL | Ruby |
| 2 | **Node.js PBKDF2 delimiter `:` not `$`** — hashes not portable | CRITICAL | Node.js |
| 3 | **Python expires_in is minutes, others seconds** | CRITICAL | Python |
| 4 | **Ruby API key validation not timing-safe** | HIGH | Ruby |
| 5 | **PHP/Node require explicit secret param** — Python/Ruby read env | MEDIUM | PHP, Node.js |
| 6 | **Python iterations 260000 vs PHP/Node 100000** | MEDIUM | All |
| 7 | **Python doesn't support RS256** | MEDIUM | Python |
| 8 | **PHP/Node missing API key fallback in authenticateRequest** | LOW | PHP, Node.js |

## Documentation Gaps

| # | Gap |
|---|-----|
| 1 | Python CLAUDE.md doesn't flag minutes vs seconds for expires_in |
| 2 | Cross-framework hash incompatibility not documented anywhere |
| 3 | PHP CLAUDE.md missing refreshToken, authenticateRequest, validateApiKey |
| 4 | Node.js CLAUDE.md has no Auth method stubs at all |
| 5 | Ruby bcrypt vs PBKDF2 difference not flagged as parity issue |
