---
title: "[Solution] Actix JWT Error — How to Fix"
description: "Fix Actix JWT authentication errors. Resolve token parsing, validation, and expiration issues."
frameworks: ["actix"]
error-types: ["auth-error"]
severities: ["error"]
weight: 5
comments: true
---

An Actix JWT error occurs when JSON Web Token authentication fails due to invalid, expired, or malformed tokens.

## Why It Happens

JWT errors happen due to incorrect signing, token expiration, missing claims, or secret key mismatches.

## Common Error Messages

```
token is expired
```

```
invalid token
```

```
signature verification failed
```

```
invalid algorithm
```

## How to Fix It

### 1. Parse JWT Correctly

Use proper JWT decoding.

```rust
use jsonwebtoken::{decode, DecodingKey, Validation, EncodingKey, encode, Header};

#[derive(Serialize, Deserialize)]
struct Claims {
    sub: String,
    exp: usize,
}

fn validate_token(token: &str) -> Result<Claims, jsonwebtoken::errors::Error> {
    decode::<Claims>(
        token,
        &DecodingKey::from_secret("secret".as_ref()),
        &Validation::default(),
    ).map(|data| data.claims)
}
```

### 2. Set Token Expiration

Add proper expiration.

```rust
fn generate_token(user_id: &str) -> Result<String, jsonwebtoken::errors::Error> {
    let claims = Claims {
        sub: user_id.to_string(),
        exp: chrono::Utc::now().checked_add_signed(chrono::Duration::hours(24)).unwrap().timestamp() as usize,
    };
    encode(&Header::default(), &claims, &EncodingKey::from_secret("secret".as_ref()))
}
```

### 3. Use Auth Middleware

Apply JWT middleware to routes.

```rust
fn auth_middleware(req: &HttpRequest) -> Result<Claims, HttpResponse> {
    let token = req.headers().get("Authorization")
        .and_then(|v| v.to_str().ok())
        .and_then(|v| v.strip_prefix("Bearer "));
    match token {
        Some(t) => validate_token(t).map_err(|_| HttpResponse::Unauthorized().finish()),
        None => Err(HttpResponse::Unauthorized().finish()),
    }
}
```

### 4. Refresh Expired Tokens

Implement refresh flow.

```rust
async fn refresh(token: web::Json<RefreshRequest>) -> HttpResponse {
    match validate_token(&token.refresh_token) {
        Ok(claims) => {
            let new_token = generate_token(&claims.sub).unwrap();
            HttpResponse::Ok().json(serde_json::json!({"token": new_token}))
        }
        Err(_) => HttpResponse::Unauthorized().finish(),
    }
}
```

## Common Scenarios

**Scenario 1: Token expired error.**
Implement token refresh flow.

**Scenario 2: Invalid signature error.**
Check secret key matches.

## Prevent It

1. **Use short-lived access tokens.**


2. **Store secrets securely.**


3. **Validate tokens on every request.**


