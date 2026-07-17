---
title: "[Solution] axum Routing/Handler Error Fix"
description: "Fix axum routing and handler errors. Handle missing route parameters, state extraction, and middleware failures."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["axum", "web", "framework", "routing", "handler"]
weight: 5
---

# axum Routing/Handler Error

Fix axum routing and handler errors. Handle missing route parameters, state extraction, and middleware failures.

## What This Error Means

When using axum as a web framework, handler errors typically occur when:

- A route handler fails to extract a request part (path, query, headers)
- Shared state is not properly injected or is the wrong type
- A middleware or layer panics or returns an unexpected error
- The router is misconfigured with duplicate or overlapping routes

The error message may look like:

```
thread 'main' panicked at 'Failed to extract `State<AppState>`: ...
```

## Common Causes

```rust
// Cause 1: Missing shared state in the router
async fn handler(State(state): State<AppState>) -> String { ... }
// Router was built without .with_state(state)

// Cause 2: Wrong extractor order or conflicting extractors
async fn handler(Form(form): Form<MyForm>, Json(json): Json<MyJson>) -> String { ... }
// Cannot consume both Form and Json from the same request body

// Cause 3: Path parameter type mismatch
async fn handler(Path(id): Path<u32>) -> String { ... }
// Route pattern uses a non-numeric segment
```

## How to Fix

### Fix 1: Ensure state is provided to the router

```rust
use axum::{routing::get, Router};
use std::sync::Arc;

#[derive(Clone)]
struct AppState {
    db: Arc<Database>,
}

let state = AppState { db: Arc::new(Database::connect()) };

let app = Router::new()
    .route("/users", get(list_users))
    .with_state(state);
```

### Fix 2: Use the correct extractor combination

```rust
use axum::extract::{Form, Json};

// Use Option for body extractors that conflict
async fn handler(
    form: Option<Form<MyForm>>,
    json: Option<Json<MyJson>>,
) -> String {
    if let Some(json) = json {
        format!("JSON: {:?}", json)
    } else if let Some(form) = form {
        format!("Form: {:?}", form)
    } else {
        "No body".to_string()
    }
}
```

### Fix 3: Use IntoResponse for custom error handling

```rust
use axum::http::StatusCode;
use axum::response::{IntoResponse, Response};

async fn handler() -> Result<String, (StatusCode, String)> {
    Err((
        StatusCode::NOT_FOUND,
        "Resource not found".to_string(),
    ))
}
```

## Examples

```rust
use axum::{
    extract::{Path, State},
    routing::get,
    Router,
};

async fn get_user(
    State(state): State<AppState>,
    Path(user_id): Path<u64>,
) -> Result<String, StatusCode> {
    state.db.get_user(user_id)
        .map_err(|_| StatusCode::NOT_FOUND)
}

#[tokio::main]
async fn main() {
    let app = Router::new()
        .route("/users/{id}", get(get_user))
        .with_state(AppState::new());

    let listener = tokio::net::TcpListener::bind("0.0.0.0:3000").await.unwrap();
    axum::serve(listener, app).await.unwrap();
}
```

## Related Errors

- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — connection refused
- [IO Error]({{< relref "/languages/rust/io-error" >}}) — I/O error
- [JSON Parse]({{< relref "/languages/rust/json-parse" >}}) — JSON parsing error
