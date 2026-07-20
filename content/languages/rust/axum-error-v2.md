---
title: "[Solution] axum Routing/Handler Error Fix"
description: "Fix axum routing and handler errors. Handle missing route parameters, state extraction, and middleware failures."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Axum Error

Axum errors occur when using the Axum web framework — handler signature mismatches, extractor conflicts, and state sharing issues.

## Common Causes

```rust
use axum::{extract::Path, routing::get, Router};

// Handler returns non-IntoResponse type
async fn get_user(Path(id): Path<u32>) -> i32 { id }

// State not Clone + Send + Sync
struct AppState { data: std::cell::RefCell<String> } // RefCell !Sync
```

## How to Fix

1. **Return types implementing IntoResponse**

```rust
use axum::{routing::get, Router, Json, http::StatusCode};

async fn get_user() -> (StatusCode, Json<serde_json::Value>) {
    (StatusCode::OK, Json(serde_json::json!({"id": 1})))
}
```

2. **Share state with Arc**

```rust
use axum::{extract::State, routing::get, Router};
use std::sync::Arc;

struct AppState { db: String }

async fn handler(State(state): State<Arc<AppState>>) -> String {
    format!("DB: {}", state.db)
}
```

3. **Implement IntoResponse for errors**

```rust
use axum::http::StatusCode;
use axum::response::{IntoResponse, Response};

enum AppError { NotFound }

impl IntoResponse for AppError {
    fn into_response(self) -> Response {
        StatusCode::NOT_FOUND.into_response()
    }
}
```

## Examples

```rust
use axum::{extract::{Path, State}, routing::get, Json, Router};
use std::sync::Arc;

struct AppState { db: String }

async fn get_user(
    State(state): State<Arc<AppState>>,
    Path(id): Path<u64>,
) -> Result<Json<serde_json::Value>, StatusCode> {
    Ok(Json(serde_json::json!({"id": id, "db": state.db})))
}

#[tokio::main]
async fn main() {
    let state = Arc::new(AppState { db: "sqlite://db.sqlite".into() });
    let app = Router::new().route("/users/:id", get(get_user)).with_state(state);
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
```

## Related Errors

- [Hyper Error]({{< relref "/languages/rust/hyper-error" >}}) — HTTP layer
- [Tokio Runtime Error]({{< relref "/languages/rust/rust-tokio-runtime-error" >}}) — async runtime
- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — server not running
