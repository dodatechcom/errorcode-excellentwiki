---
title: "[Solution] Rust Axum Error — How to Fix"
description: "Fix Axum web framework errors. Resolve routing issues, handler type mismatches, extractors, and middleware configuration problems."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Axum Error

Axum errors arise from incorrect handler signatures, extractor conflicts, routing misconfigurations, or state sharing issues in the Axum web framework.

## Common Causes

```rust
use axum::{extract::Path, routing::get, Router};

// Handler returns type that doesn't implement IntoResponse
async fn get_user(Path(id): Path<u32>) -> i32 { id }

// Double body consumption
async fn handler(
    axum::extract::String(body): axum::extract::String,
    axum::extract::RawBody(bytes): axum::extract::RawBody,
) -> String { format!("{} {:?}", body, bytes) }

// State type not Clone + Send + Sync
struct AppState { data: std::cell::RefCell<String> } // RefCell !Sync
```

## How to Fix

1. **Ensure handler return types implement `IntoResponse`**

```rust
use axum::{routing::get, Router, Json, http::StatusCode};
use serde_json::{json, Value};

async fn get_user() -> (StatusCode, Json<Value>) {
    (StatusCode::OK, Json(json!({"id": 1, "name": "Alice"})))
}

#[tokio::main]
async fn main() {
    let app = Router::new().route("/users", get(get_user));
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
```

2. **Share state via `Arc` or Axum's `State` extractor**

```rust
use axum::{extract::State, routing::get, Router};
use std::sync::Arc;

struct AppState { db_url: String }

async fn handler(State(state): State<Arc<AppState>>) -> String {
    format!("Connecting to {}", state.db_url)
}

#[tokio::main]
async fn main() {
    let state = Arc::new(AppState { db_url: "postgres://localhost/mydb".into() });
    let app = Router::new().route("/", get(handler)).with_state(state);
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
```

3. **Implement `IntoResponse` for custom error types**

```rust
use axum::http::StatusCode;
use axum::response::{IntoResponse, Response};
use axum::Json;
use serde_json::json;

enum AppError { NotFound, Unauthorized, Internal(String) }

impl IntoResponse for AppError {
    fn into_response(self) -> Response {
        let (status, msg) = match self {
            AppError::NotFound => (StatusCode::NOT_FOUND, "Not found".to_string()),
            AppError::Unauthorized => (StatusCode::UNAUTHORIZED, "Unauthorized".to_string()),
            AppError::Internal(e) => (StatusCode::INTERNAL_SERVER_ERROR, e),
        };
        (status, Json(json!({"error": msg}))).into_response()
    }
}
```

## Examples

```rust
use axum::{extract::{Path, Query, State}, routing::get, Json, Router};
use serde::Deserialize;
use std::sync::Arc;

#[derive(Deserialize)]
struct ListParams { page: Option<u32>, limit: Option<u32> }

struct AppState { db: String }

async fn get_user(
    State(state): State<Arc<AppState>>,
    Path(id): Path<u64>,
) -> Result<Json<serde_json::Value>, StatusCode> {
    println!("DB: {}", state.db);
    Ok(Json(serde_json::json!({"id": id})))
}

async fn list_users(Query(params): Query<ListParams>) -> Json<serde_json::Value> {
    Json(serde_json::json!({"page": params.page.unwrap_or(1), "limit": params.limit.unwrap_or(20)}))
}

#[tokio::main]
async fn main() {
    let state = Arc::new(AppState { db: "sqlite://db.sqlite".into() });
    let app = Router::new()
        .route("/users/:id", get(get_user))
        .route("/users", get(list_users))
        .with_state(state);
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
```

## Related Errors

- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — server not running
- [Tokio Runtime Error]({{< relref "/languages/rust/rust-tokio-runtime-error" >}}) — async runtime issues
- [Hyper Error]({{< relref "/languages/rust/hyper-error" >}}) — HTTP layer errors
