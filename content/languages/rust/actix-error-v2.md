---
title: "[Solution] actix-web Handler Panic Error Fix"
description: "Fix actix-web handler panic errors. Handle panics during request processing and state management."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# actix-web Handler Error

Actix-web handler errors occur when request processing fails due to incorrect handler signatures, extractor mismatches, or middleware misconfiguration.

## Common Causes

```rust
use actix_web::{web, App, HttpServer, HttpResponse};

// Handler returns wrong type
async fn handler() -> i32 { 42 } // i32 doesn't implement Responder

// Double body extraction
async fn bad(
    web::Json(body): web::Json<serde_json::Value>,
    web::Payload(payload): web::Payload,
) -> String { format!("{:?}", body) }
```

## How to Fix

1. **Return types that implement `Responder`**

```rust
use actix_web::{HttpResponse, Responder};

async fn handler() -> impl Responder {
    HttpResponse::Ok().json(serde_json::json!({"status": "ok"}))
}
```

2. **Use `web::Data` for shared state**

```rust
use actix_web::{web, App, HttpServer};
use std::sync::Mutex;

struct AppState { count: Mutex<i32> }

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    let data = web::Data::new(AppState { count: Mutex::new(0) });
    HttpServer::new(move || {
        App::new().app_data(data.clone()).route("/", web::get().to(index))
    }).bind("127.0.0.1:8080")?.run().await
}

async fn index(data: web::Data<AppState>) -> String {
    let mut count = data.count.lock().unwrap();
    *count += 1;
    format!("Count: {}", *count)
}
```

3. **Implement `ResponseError` for custom errors**

```rust
use actix_web::{HttpResponse, ResponseError};
use std::fmt;

#[derive(Debug)]
enum AppError { NotFound, DbError(String) }

impl fmt::Display for AppError {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            AppError::NotFound => write!(f, "Not found"),
            AppError::DbError(e) => write!(f, "DB: {}", e),
        }
    }
}

impl ResponseError for AppError {}
```

## Examples

```rust
use actix_web::{web, App, HttpServer, HttpResponse};
use serde::Deserialize;

#[derive(Deserialize)]
struct CreateItem { name: String }

async fn create_item(web::Json(item): web::Json<CreateItem>) -> HttpResponse {
    HttpResponse::Created().json(serde_json::json!({"id": 1, "name": item.name}))
}

#[actix_web::main]
async fn main() -> std::io::Result<()> {
    HttpServer::new(|| {
        App::new().route("/items", web::post().to(create_item))
    }).bind("127.0.0.1:8080")?.run().await
}
```

## Related Errors

- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — server binding fails
- [Timed Out]({{< relref "/languages/rust/timed-out" >}}) — request timeout
- [IO Error]({{< relref "/languages/rust/io-error" >}}) — I/O failure
