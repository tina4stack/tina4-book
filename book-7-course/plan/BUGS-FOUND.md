# Bugs Found While Grounding the Course

Found while auditing `Auth` across all four frameworks for course module 17. No fixes
applied in this session, by instruction. Each report below is written to be filed as-is.

All four implementations were read in source: `tina4_python/auth/__init__.py`,
`tina4-php/Tina4/Auth.php`, `tina4-ruby/lib/tina4/auth.rb`,
`tina4-nodejs/packages/core/src/auth.ts`.

## Filed

| Bug | Issue |
|-----|-------|
| 1. JWT header advertises an algorithm the signature does not use | [tina4-python#105](https://github.com/tina4stack/tina4-python/issues/105) |
| 2. `TINA4_JWT_ALGORITHM` ignored by Python | [tina4-python#106](https://github.com/tina4stack/tina4-python/issues/106) |
| 3. `nbf` validated in Ruby only (master decision) | [tina4-python#107](https://github.com/tina4stack/tina4-python/issues/107) |
| 3. `nbf` port | [tina4-php#187](https://github.com/tina4stack/tina4-php/issues/187) |
| 3. `nbf` port | [tina4-nodejs#39](https://github.com/tina4stack/tina4-nodejs/issues/39) |

Ruby needs no issue for bug 3. It is the framework that gets it right.

Not filed: the `aud`/`iss` enhancement (consistent across all four, so a design gap rather
than a defect) and the `get_payload` naming hazard (breaking change, belongs in a v4
discussion). Both are described at the end of this document.

---

## BUG 1 (Python) - JWT header advertises an algorithm the signature does not use

**Repo:** tina4stack/tina4-python
**Severity:** high (breaks interop with every standards-compliant JWT consumer)
**Affects:** 3.13.89, and every version carrying the current `Auth` implementation

### What happens

`Auth.__init__` accepts an `algorithm` argument and writes it straight into the token
header:

```python
# tina4_python/auth/__init__.py:202
def __init__(self, secret: str = None, algorithm: str = "HS256", ...):
    self.algorithm = algorithm

# tina4_python/auth/__init__.py:240
header = {"alg": self.algorithm, "typ": "JWT"}
```

`_sign` ignores it and always uses HMAC-SHA256:

```python
# tina4_python/auth/__init__.py:316
def _sign(self, message: str) -> str:
    sig = hmac.new(self.secret.encode(), message.encode(), hashlib.sha256).digest()
    return _b64url_encode(sig)
```

### Reproduction

```python
from tina4_python.auth import Auth
import base64, json

token = Auth(secret="test-secret", algorithm="RS256").get_token({"user_id": 1})
header = json.loads(base64.urlsafe_b64decode(token.split(".")[0] + "=="))
print(header)   # {'alg': 'RS256', 'typ': 'JWT'}   <- claims RSA
                # the signature is HMAC-SHA256
```

### Why it matters

The token is self-consistent inside Tina4, because `valid_token` also ignores the header
and recomputes with `_sign`. It breaks the moment anything else reads the token. PyJWT,
python-jose, Auth0, an API gateway, or a partner service will read `alg: RS256`, attempt
RSA verification against an HMAC signature, and reject or error.

RFC 7515 section 4.1.1 requires the `alg` header to describe the signature actually
present. This violates that.

The failure is silent and only appears at an integration boundary, which is the worst place
to discover it.

### Cross-language comparison

Python is the only one that does this.

| Framework | Behaviour with an unsupported/other algorithm |
|-----------|-----------------------------------------------|
| Python | Silently signs HMAC-SHA256, header lies |
| PHP | `sign()` branches HS256/RS256, both implemented correctly (`Auth.php:494-503`) |
| Ruby | Header hardcoded `HS256` and decode asserts `header["alg"] == "HS256"` (`auth.rb:116,134`), separate RS256 path |
| Node | `sign()` throws `Unsupported algorithm: ${algorithm}` (`auth.ts:263`) |

Node given the same input throws. Python lies. Same API, opposite behaviour.

### Suggested fix

Smallest correct change: reject anything other than `HS256` in `__init__`, matching Node's
throw. Larger change: implement RS256 to reach parity with PHP and Node (see BUG 2, which
this would also resolve).

### Worth noting in defence of the current code

`valid_token` never reads the `alg` header when verifying. That makes Python immune to
algorithm-confusion and to the `"alg": "none"` attack by construction, which is a stronger
posture than a naive `jwt.decode()` call. The bug is the advertising, not the verification.

---

## BUG 2 (Python) - `TINA4_JWT_ALGORITHM` is ignored

**Repo:** tina4stack/tina4-python
**Severity:** medium (parity break against the CLI's own source of truth)

### What happens

`TINA4_JWT_ALGORITHM` is a documented environment variable registered in the CLI's
`known_vars`:

```rust
// tina4/src/env_config.rs:84
("TINA4_JWT_ALGORITHM", "HS256", "JWT signing algorithm", "Auth"),
```

`tina4/src/env_migrate.rs:30` even migrates the legacy `JWT_ALGORITHM` name onto it.

PHP reads it (`Auth.php:196, 237`). Node reads it (`auth.ts:176, 213`). Python never
references it anywhere in the codebase.

### Reproduction

Set `TINA4_JWT_ALGORITHM=RS256` in `.env`. PHP and Node sign with RS256. Python signs with
HMAC-SHA256 and says nothing.

### Why it matters

A team running a mixed estate, or migrating a service from PHP to Python, gets a silent
downgrade from asymmetric to symmetric signing. The env var appears to work because nothing
errors.

This also breaks the env-uniformity contract where the CLI's `known_vars` is the source of
truth for what a variable does in every framework.

### Suggested fix

Either implement RS256 in Python (full parity), or read the variable and raise on any value
Python cannot honour. Silence is the one option that should be off the table.

---

## BUG 3 (all four) - `nbf` is validated in Ruby only

**Repos:** tina4stack/tina4-python, tina4-php, tina4-nodejs (Ruby is the correct one)
**Severity:** medium (cross-framework inconsistency in a security check)

### What happens

Ruby issues and validates the `nbf` (not before) claim:

```ruby
# lib/tina4/auth.rb:149
return nil if payload["nbf"] && now < payload["nbf"]
# lib/tina4/auth.rb:163
"nbf" => now
```

Python, PHP and Node validate the signature and `exp` only. None of them look at `nbf`.

### Why it matters

A token carrying a future `nbf` is rejected by Ruby and accepted by the other three. The
same token, the same secret, four frameworks, two answers. Any estate mixing languages gets
inconsistent authentication behaviour, and a token intended to become valid later is live
immediately on three of the four.

`nbf` is a registered claim in RFC 7519 section 4.1.5. A verifier that ignores a claim it
was given is not doing what the caller expected.

### Suggested fix

Python is master, so decide there first: either validate `nbf` in all four, or drop issuing
it in Ruby. Validating in all four is the correct call, since Ruby already issues it and
tokens in the wild may carry it.

---

## Not a bug (enhancement) - no `aud` or `iss` validation anywhere

Verified across all four: none validate `aud` or `iss`. This is consistent, so it is a
design gap rather than a parity break.

It matters when several services share a secret, because a token minted for service A is
then accepted by service B. Most Tina4 deployments are a single application holding its own
secret, where this adds nothing.

Worth an enhancement issue rather than a bug report. Optional `audience` and `issuer`
parameters on `valid_token`, off by default, would close it without breaking anybody.

---

## Retraction - decorator order is NOT a security fragility

I raised this in `UNDER-FIRE.md` item 6 and it is wrong. Checked in source:

```python
# tina4_python/core/router.py:765-772
fn._secured = True
if hasattr(fn, "_route_ref"):
    fn._route_ref._route["auth_required"] = True
if hasattr(fn, "_ws_route_ref"):
    fn._ws_route_ref["auth_required"] = True
```

`@secured()` and `@noauth()` both carry a back-reference to the registered route and flip
the flag whichever order the decorators are applied in, for HTTP and websocket routes
alike. The documented ordering is a style convention, not a correctness requirement.

Nothing to file. `UNDER-FIRE.md` has been corrected.

---

## Minor DX suggestion - `get_payload` name does not warn

`get_payload` decodes claims without verifying the signature. The docstring says so
clearly, the name does not. `get_payload_unverified` would carry the warning to every call
site. PyJWT solved the same problem with an explicit `options={"verify_signature": False}`.

Naming change is breaking, so it belongs in a v4 discussion rather than a bug report.
