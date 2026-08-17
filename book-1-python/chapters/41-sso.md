# Chapter 41: OpenID Connect SSO

Tina4 uses one provider-neutral OpenID Connect flow. Configure an issuer; the framework discovers its endpoints, runs Authorization Code with PKCE, verifies the result through introspection, and stores the normalized identity in the existing Tina4 Session.

```ini
TINA4_SSO_ISSUER=https://identity.example.com/realms/my-app
TINA4_SSO_CLIENT_ID=my-app
TINA4_SSO_CLIENT_SECRET=replace-me
TINA4_SSO_REDIRECT_URI=https://app.example.com/auth/callback
TINA4_SSO_SCOPES=["openid", "profile", "email"]
TINA4_SSO_VERIFY=introspection
TINA4_SSO_POST_LOGOUT_REDIRECT_URI=https://app.example.com/
```

SSO is off unless the required values are present. When configured, `tina4 serve` mounts `GET /auth/login`, `GET /auth/callback`, and `POST /auth/logout`. A collision with an application route fails startup.

Use the normal secured-route mechanism. The normalized identity appears in `request.user`; provider tokens remain in reserved Session data and never appear in `session.all()` or `request.user`.

```python
from tina4_python import get, Sso

@get("/account")
async def account(request, response):
    return response.json(request.user)

sso = Sso.from_issuer()
identity = sso.identity(request.session)
```

The runtime does not name providers. For Keycloak, use the realm issuer. For Microsoft Entra ID, use the tenant-specific v2 issuer. Register the Tina4 callback URI and use `TINA4_SSO_CLAIM_MAP` only when roles or groups use different claim names.

Production issuer and callback URLs require HTTPS; HTTP is loopback-only. Introspection is the supported verification mode in 3.13.104 and requires a client secret. Selecting `jwks` fails during configuration until an application cryptography capability is available.
