---
title: "[Solution] axum-extra Typed Header Error Fix"
description: "Fix axum-extra typed header errors. Handle header extraction, parsing, and response headers."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Axum Extra Error

Axum extra errors occur when using `axum-extra` crate features — typed header issues, cookie extraction failures, and form/query parsing errors.

## Common Causes

```rust
use axum_extra::typed_header::{TypedHeader, headers};

// Missing required header
async fn handler(TypedHeader(auth): TypedHeader<headers::Authorization<String>>) -> String {
    format!("Auth: {}", auth.0) // Fails if Authorization header missing
}

// Cookie extraction failure
use axum_extra::extract::CookieJar;
async fn handler(jar: CookieJar) -> String {
    let session = jar.get("session").unwrap(); // No session cookie
    format!("Session: {}", session.value())
}
```

## How to Fix

1. **Handle missing headers gracefully**

```rust
use axum_extra::typed_header::{TypedHeader, headers};
use axum::http::StatusCode;

async fn handler(
    TypedHeader(auth): Result<TypedHeader<headers::Authorization<String>>, axum_extra::typed_header::TypedHeaderRejection>,
) -> Result<String, StatusCode> {
    match auth {
        Ok(TypedHeader(auth)) => Ok(format!("Auth: {}", auth.0)),
        Err(_) => Err(StatusCode::UNAUTHORIZED),
    }
}
```

2. **Use CookieJar with proper defaults**

```rust
use axum_extra::extract::CookieJar;

async fn handler(jar: CookieJar) -> String {
    let session = jar.get("session")
        .map(|c| c.value().to_string())
        .unwrap_or_else(|| "no session".into());
    format!("Session: {}", session)
}
```

3. **Use proper query extraction**

```rust
use axum::extract::Query;
use serde::Deserialize;

#[derive(Deserialize)]
struct Params { page: Option<u32>, limit: Option<u32> }

async fn handler(Query(params): Query<Params>) -> String {
    format!("Page: {}, Limit: {}", params.page.unwrap_or(1), params.limit.unwrap_or(20))
}
```

## Examples

```rust
use axum_extra::extract::{CookieJar, Cookie};
use axum::{routing::get, Router, http::StatusCode};

async fn login(jar: CookieJar) -> CookieJar {
    jar.add(Cookie::new("session", "abc123"))
}

async fn dashboard(jar: CookieJar) -> Result<String, StatusCode> {
    jar.get("session")
        .map(|c| format!("Welcome! Session: {}", c.value()))
        .ok_or(StatusCode::UNAUTHORIZED)
}

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/login", get(login))
        .route("/dashboard", get(dashboard));
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
```

## Related Errors

- [Axum Error]({{< relref "/languages/rust/rust-axum-error" >}}) — Axum core
- [Hyper Error]({{< relref "/languages/rust/hyper-error" >}}) — HTTP layer
- [Serde Error]({{< relref "/languages/rust/rust-serde-error-rs" >}}) — deserialization
