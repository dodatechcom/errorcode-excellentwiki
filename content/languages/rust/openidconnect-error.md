---
title: "[Solution] openidconnect Discovery Error Fix"
description: "Fix OpenID Connect discovery errors. Handle provider metadata, JWKS fetching, and issuer validation."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# OpenID Connect Error

OpenID Connect errors occur when using the `openidconnect` crate — authentication flow failures and token validation issues.

## Common Causes

```rust
// Discovery failed
let issuer = IssuerUrl::new("https://wrong-endpoint".into())?;
let provider_metadata = Discover::discover(issuer).await?;

// Token validation failure
let claims = token_claims.validate(&client, &nonce)?;
```

## How to Fix

1. **Configure the client properly**

```rust
use openidconnect::{
    ClientId, ClientSecret, IssuerUrl, AuthenticationFlow, Scope,
};

let client_id = ClientId::new("client-id".into());
let client_secret = ClientSecret::new("client-secret".into());
let issuer = IssuerUrl::new("https://accounts.google.com".into())?;
```

2. **Handle token exchange**

```rust
let token_response = client
    .exchange_code(AuthorizationCode::new(code))
    .request_async(&http_client)
    .await?;
```

3. **Validate ID tokens**

```rust
let id_token = token_response.id_token().unwrap();
let claims = id_token.claims(&client.id_token_verifier(), &nonce)?;
```

## Examples

```rust
use openidconnect::prelude::*;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let client_id = ClientId::new("my-client-id".into());
    let issuer = IssuerUrl::new("https://accounts.google.com".into())?;

    let client = CoreClient::from_provider_metadata(
        CoreProviderMetadata::discover(issuer)?,
        client_id,
        Some(ClientSecret::new("secret".into())),
        None,
        None,
        None,
    );

    let (auth_url, csrf_token) = client
        .authorize_url(
            AuthenticationFlow::<CoreResponseType>::AuthorizationCode,
            CsrfToken::new_random,
            OpenIdScope::OpenId,
        )
        .url();

    println!("Go to: {}", auth_url);
    Ok(())
}
```

## Related Errors

- [OAuth2 Error]({{< relref "/languages/rust/oauth2-error-rs" >}}) — OAuth2
- [Jsonwebtoken Error]({{< relref "/languages/rust/jsonwebtoken-error-rs" >}}) — JWT
- [WebAuthn RS Error]({{< relref "/languages/rust/webauthn-rs-error" >}}) — WebAuthn
