---
title: "[Solution] Actix CORS Error -- How to Fix"
description: "Fix Actix CORS errors. Resolve cross-origin request blocked, missing headers, and preflight issues."
frameworks: ["actix"]
error-types: ["security-error"]
severities: ["error"]
weight: 5
comments: true
---

An Actix CORS error occurs when the browser blocks cross-origin requests due to missing or incorrect CORS headers.

## Why It Happens

CORS errors happen because the server doesn't send proper Access-Control-Allow-Origin headers or doesn't handle preflight OPTIONS requests.

## Common Error Messages

```
CORS error: No Access-Control-Allow-Origin
```

```
Blocked by CORS policy
```

```
Response to preflight request doesn't pass
```

```
Origin is not allowed
```

## How to Fix It

### 1. Enable CORS

Use actix-cors for CORS handling.

```rust
use actix_cors::Cors;

App::new()
    .wrap(
        Cors::default()
            .allowed_origin("http://localhost:3000")
            .allowed_methods(vec!["GET", "POST", "PUT", "DELETE"])
            .allowed_headers(vec![http::header::CONTENT_TYPE, http::header::AUTHORIZATION])
    )
```

### 2. Allow All Origins (Dev)

Use permissive CORS for development.

```rust
App::new().wrap(Cors::permissive())
```

### 3. Restrict Origins

Use specific origins for production.

```rust
App::new()
    .wrap(
        Cors::default()
            .allowed_origin("https://myapp.com")
    )
```

### 4. Set Credentials

Allow credentials in requests.

```rust
App::new()
    .wrap(
        Cors::default()
            .supports_credentials()
            .allowed_origin("https://myapp.com")
    )
```

## Common Scenarios

**Scenario 1: Browser console shows CORS error.**
Check Access-Control-Allow-Origin header.

**Scenario 2: Preflight request fails.**
Ensure OPTIONS requests are handled.

## Prevent It

1. **Always configure CORS explicitly.**


2. **Use allowlists for production origins.**


3. **Handle preflight OPTIONS requests.**


