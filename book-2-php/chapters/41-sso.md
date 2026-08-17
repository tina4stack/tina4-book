# Chapter 41: OpenID Connect SSO

Tina4 uses one provider-neutral OpenID Connect flow. Configure an issuer; the framework discovers its endpoints, runs Authorization Code with PKCE, verifies the result through introspection, and stores the normalized identity in the existing Tina4 Session.

```ini
TINA4_SSO_ISSUER=https://identity.example.com/realms/my-app
TINA4_SSO_CLIENT_ID=my-app
TINA4_SSO_CLIENT_SECRET=replace-me
TINA4_SSO_REDIRECT_URI=https://app.example.com/auth/callback
TINA4_SSO_SCOPES=["openid", "profile", "email"]
TINA4_SSO_VERIFY=introspection
```

When configured, `tina4 serve` mounts `GET /auth/login`, `GET /auth/callback`, and `POST /auth/logout`. Route collisions fail startup. Use the existing secured-route mechanism; the normalized identity is available as `$request->user`.

```php
use Tina4\Sso;

$sso = Sso::fromIssuer();
$identity = $sso->identity($request->session);
```

Provider tokens remain in reserved Session data and never appear in `Session::all()`. The runtime does not name providers. Keycloak and Microsoft Entra ID examples are configuration recipes, not provider-specific adapters.

Production issuer and callback URLs require HTTPS; HTTP is loopback-only. Introspection is the supported verification mode in 3.13.104 and requires a client secret. `jwks` fails during configuration until an application cryptography capability is available.
