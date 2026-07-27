# Under Fire: Where Tina4's Opinions Get Contested

A course that teaches best practice through an opinionated framework has to be honest about
where the framework and the industry disagree. If we hide it, the first student to reach a
real job feels lied to. If we teach it, they can defend their choices in an interview.

This document is the audit. Each item states the Tina4 opinion, the criticism a senior
reviewer would raise, the honest verdict, and how the course should handle it.

**Verification key:**
- `SOURCE` means I read the framework code and confirmed the behaviour.
- `DOCS` means it comes from framework documentation and has not been read in source yet.

---

## 1. Zero dependencies versus "never roll your own crypto"

**The opinion.** Tina4 implements JWT, password hashing, the template engine, the SCSS
compiler and the GraphQL parser from scratch on the standard library.

**The criticism.** Module 17 of the syllabus tells students "never write your own crypto."
Tina4 writes its own JWT. A reviewer will spot the contradiction in about four seconds.

**The honest verdict: mostly defensible, and stronger than expected.** `SOURCE`

Reading `tina4_python/auth/__init__.py`:

- The primitives are stdlib, not invented: `hmac`, `hashlib.sha256`, `hashlib.pbkdf2_hmac`.
  Nobody wrote a cipher here.
- Signature comparison uses `hmac.compare_digest`, which is constant-time. That is the
  correct call and plenty of hand-rolled implementations get it wrong.
- `valid_token` never reads the `alg` header. It recomputes the signature with the server's
  own key and compares. That makes it immune to algorithm-confusion and to the
  `"alg": "none"` attack by construction.

That last point is worth teaching loudly. The classic JWT CVEs are protocol bugs, not maths
bugs, and the naive `jwt.decode(token)` call in PyJWT without `algorithms=[...]` was
vulnerable to exactly the attack Tina4 cannot express. The framework is defensible here.

**How the course teaches it.** Module 17 keeps the rule but sharpens it: do not invent
primitives, and do not hand-implement a protocol without knowing its attack list. Then it
shows Tina4's verifier as a worked example of getting the protocol part right.

---

## 2. The `algorithm` parameter does not do what it says

**This is a defect, not an opinion.** `SOURCE`

`Auth.__init__` accepts `algorithm="HS256"` and writes it into the token header:

```python
header = {"alg": self.algorithm, "typ": "JWT"}
```

But `_sign` ignores it:

```python
def _sign(self, message: str) -> str:
    sig = hmac.new(self.secret.encode(), message.encode(), hashlib.sha256).digest()
```

Construct `Auth(secret=s, algorithm="RS256")` and you get a token whose header advertises
RS256 carrying an HMAC-SHA256 signature. Tina4 verifies it fine, because Tina4 also ignores
the header. Any standards-compliant consumer (PyJWT, jose, Auth0, an API gateway) reads
`alg: RS256`, reaches for RSA verification, and rejects the token.

The bug is invisible in a Tina4-to-Tina4 system and breaks the moment a third party is
involved. RFC 7515 says the header describes the signature that is actually there.

**Options:** reject any `algorithm` other than `HS256` at construction, or implement RS256
properly. Rejecting is the smaller change and removes the lie.

Needs a cross-check against PHP, Ruby and Node before anything gets filed.

---

## 3. Only `exp` gets validated

**The gap.** `SOURCE` `valid_token` checks the signature and `exp`. It does not check
`aud`, `iss` or `nbf`.

**The criticism.** RFC 7519 defines those claims for a reason. Two services sharing a
secret means a token minted for service A is accepted by service B. In a microservice
estate that is a privilege-escalation path.

**Verdict: a real gap, though a narrow one.** Most Tina4 deployments are a single
application holding its own secret, where audience validation adds nothing. It matters as
soon as the estate grows, and that is exactly when nobody remembers to check.

Verified across all four: none of them validate `aud` or `iss`, so this is consistent
design rather than a parity break. `nbf` is a different story. Ruby validates it, the other
three ignore it, which means the same token gets two different answers depending on
language. That one is filed as a bug (see `BUGS-FOUND.md`).

**How the course teaches it.** Module 17 covers registered claims as a concept and states
plainly that Tina4 validates `exp` only. A student who needs `aud` learns to check it in
their own middleware.

---

## 4. `get_payload` decodes without verifying

**The opinion.** `SOURCE` The method exists, and its docstring says clearly: "Decode
payload WITHOUT validating signature or expiry."

**The criticism.** A method that returns attacker-controlled claims is a loaded gun in a
codebase where the next developer is in a hurry. The name does not warn anybody.

**Verdict: defensible but poorly named.** The use case is real (reading a `kid` before
picking a key, logging a subject on a rejected token). `get_payload_unverified` would cost
nothing and remove the footgun. PyJWT solved this with an explicit `options={"verify_signature": False}`.

**How the course teaches it.** Module 10 uses it as the worked example of a name that
fails to encode danger.

---

## 5. Secure by default, keyed on HTTP method

**The opinion.** `DOCS` GET routes are public. POST, PUT, PATCH and DELETE require auth
unless opened with `@noauth()`.

**The criticism.** This is a genuinely good default and it teaches a dangerous
generalisation. Broken access control is OWASP A01, the top item on the list, and the most
common form of it is a readable endpoint exposing data the caller should not see.
`GET /api/users/42/medical-history` is a GET. It is not safe to be public.

Method-based defaults protect against unauthorised **writes**. They do nothing about
unauthorised **reads**, and a student who internalises "GET is public" ships a data breach.

**Verdict: the default is right, the lesson it accidentally teaches is wrong.**

**How the course teaches it.** Module 17 makes this an explicit correction: the framework
defends writes, you defend reads. `@secured()` on any GET touching user data. This is
probably the single most important safety correction in the whole course.

---

## 6. Decorator order carries security meaning - WITHDRAWN

I raised this and then checked it. The criticism does not survive the source. `SOURCE`

```python
# tina4_python/core/router.py:765-772
fn._secured = True
if hasattr(fn, "_route_ref"):
    fn._route_ref._route["auth_required"] = True
if hasattr(fn, "_ws_route_ref"):
    fn._ws_route_ref["auth_required"] = True
```

`@secured()` and `@noauth()` each hold a back-reference to the registered route and flip
the auth flag whichever order the decorators are applied in, for HTTP and websocket routes
alike. The documented ordering is a style convention, not a correctness requirement. A
misordered decorator does not silently disable auth.

**Verdict: no fragility.** The framework handles both orders on purpose.

**How the course teaches it.** Module 26 can still use it, but as the opposite lesson: a
convention that looks load-bearing and is not, because somebody did the work to make order
irrelevant. Good design is often invisible.

---

## 7. Active Record couples the domain to the schema

Already handled in syllabus module 14. Standard trade, Django and Rails made the same one,
and Data Mapper is the answer when the domain outgrows the table. No change needed.

---

## 8. Convention and auto-discovery hide behaviour

**The criticism.** Dropping a file in `src/routes` and having it register itself is
wonderful until something does not register and there is no stack trace to read.

**Verdict: a fair trade, honestly made.** Tina4 writes `.broken` sentinel files on
auto-discovery failure and surfaces them on the dev dashboard, which is more than most
convention-driven frameworks do. `SOURCE`

**How the course teaches it.** Module 7 already covers it. Add the `.broken` mechanism as
the worked example of making magic debuggable.

---

## 9. Auto-migrate on startup

**The criticism.** Industry practice is unambiguous: schema changes in production are a
deliberate, gated step, never a side effect of a process starting. Two instances booting
at once race each other.

**Verdict: correct in development, hazardous in production.** Already flagged in syllabus
module 15. Module 33 covers expand and contract properly.

---

## 10. Inline `@tests()` decorators in shipped source

**The criticism.** `DOCS` Test assertions living on production functions means test code
ships to production. It grows the deployed surface and puts assertions in a place where a
reviewer does not expect them.

**Verdict: unusual, and the counter-argument is decent.** Tests next to the code they
describe get maintained. Tests in a distant folder rot. Doctest has made the same bet in
Python for twenty years.

**How the course teaches it.** Module 23 presents it as a genuine trade rather than a
mistake, alongside doctest, and lets the student argue it in the Judge dimension.

---

## 11. Four-language parity constrains idiomatic design

**The criticism.** One API across Python, PHP, Ruby and Node means each language gets bent
toward the shared shape. A Python reviewer expects ASGI and Starlette conventions. A PHP
reviewer expects PSR-7 and PSR-15 middleware. `return response(data)` is a Tina4 idiom, not
a Python one.

**Verdict: the most legitimate architectural criticism on this list.** It is a deliberate
trade with a real cost, and it is the one a senior hire will push hardest on.

**How the course teaches it.** Module 27 uses it as the flagship case study in
architectural trade-offs. The student has to argue both sides for marks. A course that
teaches judgement should be willing to put its own foundation on the stand.

---

## 12. AutoCrud from a raw SQL string

**The criticism.** `DOCS` `CRUD.to_crud(request, {"sql": "SELECT id, name FROM users"})`
generates a full admin surface with create, update and delete routes from a query string.
Convenient, and a mass-assignment surface if the generated writes accept whatever fields
arrive.

**Verdict: needs verification before I say anything stronger.** Worth reading the generated
write path to see what it does with unexpected fields.

**How the course teaches it.** Module 16 covers mass assignment as a concept regardless.

---

## Summary

Two items need action outside the course:

1. **The `algorithm` parameter defect (item 2).** Real, verified in source, breaks external
   interop. Needs a cross-language check.
2. **Silent versus loud failure on misordered `@secured()` (item 6).** Needs investigation.

Two items are course corrections that matter more than any chapter:

3. **"GET is public" is not "GET is safe" (item 5).**
4. **Four-language parity as an argued trade, not a slogan (item 11).**

Everything else is a defensible opinion that the course should teach as an opinion, with
the counter-argument attached. That is the whole pedagogical bet: a student who can argue
against the framework they learned on is a student who can think.
