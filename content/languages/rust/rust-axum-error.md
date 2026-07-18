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

## Why It Happens

- Handler function signatures do not match expected extractor types
- Routes are defined with conflicting HTTP method and path combinations
- State is not properly shared across handlers
- Middleware is applied in the wrong order or with incorrect bounds

## Common Error Messages

- `the trait bound Handler<_, _> is not satisfied`
- `cannot extract from a handler function`
- `no method named route found for struct Router`
- `state is not a Send + Sync type`

## How to Fix It

### Fix 1: Match handler signatures to extractors

```rust
use axum::{extract::Path, routing::get, Router};

async fn get_user(Path(id): Path<u32>) -> String {
    format!("User {}", id)
}

#[tokio::main]
async fn main() {
    let app = Router::new().route("/users/:id", get(get_user));
    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
```

### Fix 2: Share state with Arc

```rust
use axum::{extract::State, routing::get, Router};
use std::sync::Arc;

struct AppState { db: String }

async fn handler(State(state): State<Arc<AppState>>) -> String {
    state.db.clone()
}

let state = Arc::new(AppState { db: "test".into() });
let app = Router::new().route("/", get(handler)).with_state(state);
```

### Fix 3: Use proper error handling with IntoResponse

```rust
use axum::http::StatusCode;
use axum::response::{IntoResponse, Response};

enum AppError { NotFound, Internal }

impl IntoResponse for AppError {
    fn into_response(self) -> Response {
        match self {
            AppError::NotFound => StatusCode::NOT_FOUND.into_response(),
            AppError::Internal => StatusCode::INTERNAL_SERVER_ERROR.into_response(),
        }
    }
}
```

## Common Scenarios

1. Building a REST API with path parameters
2. Adding authentication middleware to Axum routes
3. Handling JSON request bodies with proper error responses

## Prevent It

- Always return types that implement `IntoResponse` from handlers
- Use Axum 0.7+ with `tokio::net::TcpListener` instead of `axum::Server`
- Share state via `Arc` or Axum's built-in `State` extractor
