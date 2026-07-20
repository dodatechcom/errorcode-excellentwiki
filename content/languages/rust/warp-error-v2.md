---
title: "[Solution] warp Filter Rejection Error Fix"
description: "Fix warp filter rejection errors. Handle filter combinators, rejections, and custom error responses."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# warp Filter Rejection Error

The `warp` crate uses a rejection-based error model where unmatched filters produce `Rejection` values. When a request doesn't match any route, warp returns a 404 by default. Rejections carry typed error information that you can intercept with `.recover()` to produce custom error responses. This is distinct from handler-level errors — rejections mean the filter itself couldn't process the request.

## Common Causes

```rust
use warp::Filter;

// 1. Route path doesn't match the request URL
let route = warp::path("users").and(warp::get());
// GET /posts → rejection (no matching route)

// 2. Missing required query parameter
let search = warp::query::<SearchParams>();
// /search without ?q=... → rejection if q is required

// 3. Wrong HTTP method
let post_only = warp::path("items").and(warp::post());
// GET /items → MethodNotAllowed rejection

// 4. Body type mismatch
let json_route = warp::body::json::<MyStruct>();
// POST with form data instead of JSON → rejection
```

## How to Fix

1. **Use recover to handle rejections with typed responses**

```rust
use warp::{Filter, Rejection, Reply};
use std::convert::Infallible;

#[derive(Debug)]
struct AppError(String);
impl warp::reject::Reject for AppError {}

async fn handle_rejection(err: Rejection) -> Result<impl Reply, Infallible> {
    let (status, body) = if err.is_not_found() {
        (warp::http::StatusCode::NOT_FOUND, "Route not found".to_string())
    } else if let Some(e) = err.find::<AppError>() {
        (warp::http::StatusCode::BAD_REQUEST, e.0.clone())
    } else if let Some(_) = err.find::<warp::reject::MethodNotAllowed>() {
        (warp::http::StatusCode::METHOD_NOT_ALLOWED, "Wrong method".to_string())
    } else if let Some(e) = err.find::<warp::reject::InvalidQuery>() {
        (warp::http::StatusCode::BAD_REQUEST, format!("Bad query: {}", e))
    } else {
        (warp::http::StatusCode::INTERNAL_SERVER_ERROR, "Unknown error".to_string())
    };

    Ok(warp::reply::with_status(body, status))
}
```

2. **Use optional filters for non-required parameters**

```rust
use warp::Filter;
use serde::Deserialize;

#[derive(Deserialize)]
struct Search {
    q: String,
    page: Option<u32>,
}

async fn search_handler(params: Search) -> Result<String, warp::Rejection> {
    let page = params.page.unwrap_or(1);
    Ok(format!("Searching '{}' page {}", params.q, page))
}

let route = warp::path("search")
    .and(warp::get())
    .and(warp::query::<Search>())
    .and_then(search_handler);
```

3. **Combine filters with or for multiple routes**

```rust
use warp::Filter;

let api = warp::path("api").and(
    warp::path("users")
        .and(warp::get())
        .map(|| "list users")
    .or(
        warp::path("users")
            .and(warp::post())
            .map(|| "create user")
    )
    .or(
        warp::path("items")
            .and(warp::get())
            .map(|| "list items")
    )
);

let routes = api.recover(handle_rejection);
```

4. **Provide fallback routes for unmatched paths**

```rust
use warp::Filter;

let api = warp::path("api")
    .and(warp::path("v1").and(warp::get()).map(|| "v1 endpoint"))
    .or(warp::any().map(|| warp::reply::with_status(
        "Not found",
        warp::http::StatusCode::NOT_FOUND,
    )));

warp::serve(api).run(([127, 0, 0, 1], 3030)).await;
```

## Examples

```rust
use warp::Filter;
use serde::{Deserialize, Serialize};
use std::convert::Infallible;

#[derive(Debug, Deserialize, Serialize]
struct CreateUser { name: String }

#[derive(Debug, Deserialize)]
struct Pagination { page: Option<u32>, limit: Option<u32> }

async fn handle_rejection(err: warp::Rejection) -> Result<impl warp::Reply, Infallible> {
    let code = if err.is_not_found() {
        warp::http::StatusCode::NOT_FOUND
    } else {
        warp::http::StatusCode::INTERNAL_SERVER_ERROR
    };
    Ok(warp::reply::with_status(format!("Error: {}", err), code))
}

#[tokio::main]
async fn main() {
    let create = warp::path("users")
        .and(warp::post())
        .and(warp::body::json())
        .and_then(|body: CreateUser| async move {
            Ok::<_, warp::Rejection>(warp::reply::json(
                &serde_json::json!({"id": 1, "name": body.name})
            ))
        });

    let list = warp::path("users")
        .and(warp::get())
        .and(warp::query::<Pagination>())
        .map(|p: Pagination| {
            warp::reply::json(&serde_json::json!({"page": p.page.unwrap_or(1)}))
        });

    let routes = create.or(list).recover(handle_rejection);
    warp::serve(routes).run(([127, 0, 0, 1], 3030)).await;
}
```

## Related Errors

- [Warp Error]({{< relref "/languages/rust/warp-error" >}}) — warp filters
- [Axum Error]({{< relref "/languages/rust/axum-error" >}}) — Axum framework
- [Hyper Error]({{< relref "/languages/rust/hyper-error" >}}) — HTTP layer
