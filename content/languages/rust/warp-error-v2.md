---
title: "[Solution] warp Filter Rejection Error Fix"
description: "Fix warp filter rejection errors. Handle filter combinators, rejections, and custom error responses."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# warp Filter Rejection Error

Fix warp filter rejection errors. Handle filter combinators, rejections, and custom error responses.

## What This Error Means

warp filter rejections occur when a request does not match any filter. The server returns a 404 or custom rejection:

```
warp::reject::not_found()
Rejection(UnknownRoute)
```

## Common Causes

```rust
// Cause 1: Route path does not match
let route = warp::path("users").and(warp::get());

// Cause 2: Missing required query parameter
// Cause 3: Wrong HTTP method (GET vs POST)
// Cause 4: Request body does not match expected type
// Cause 5: Header filter mismatch
```

## How to Fix

### Fix 1: Use recover to handle rejections

```rust
use warp::Rejection;
use warp::reply;

async fn handle_rejection(err: Rejection) -> Result<impl warp::Reply, std::convert::Infallible> {
    if err.is_not_found() {
        Ok(reply::with_status(
            "Not Found",
            reply::StatusCode::NOT_FOUND,
        ))
    } else if let Some(e) = err.find::<CustomError>() {
        Ok(reply::with_status(
            e.0.clone(),
            reply::StatusCode::BAD_REQUEST,
        ))
    } else {
        Ok(reply::with_status(
            "Internal Server Error",
            reply::StatusCode::INTERNAL_SERVER_ERROR,
        ))
    }
}
```

### Fix 2: Use optional filters for non-required parameters

```rust
use warp::query;

#[derive(serde::Deserialize)]
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
    .and(query::<Search>())
    .and_then(search_handler);
```

### Fix 3: Combine filters with or for multiple routes

```rust
let api = warp::path("api")
    .and(
        warp::path("users")
            .and(warp::get())
            .map(|| "list users")
        .or(
            warp::path("users")
                .and(warp::post())
                .map(|| "create user")
        )
    );

let routes = api.recover(handle_rejection);
```

## Examples

```rust
use warp::Filter;
use std::convert::Infallible;

#[derive(serde::Deserialize)]
struct CreateUser {
    name: String,
}

async fn create_user(body: CreateUser) -> Result<impl warp::Reply, Infallible> {
    Ok(warp::reply::with_status(
        format!("Created user: {}", body.name),
        warp::http::StatusCode::CREATED,
    ))
}

#[tokio::main]
async fn main() {
    let create = warp::path("users")
        .and(warp::post())
        .and(warp::body::json())
        .and_then(create_user);

    let routes = create.recover(handle_rejection);

    warp::serve(routes).run(([127, 0, 0, 1], 3030)).await;
}
```

## Related Errors

- [Warp Error]({{< relref "/languages/rust/warp-error" >}}) — warp error
- [IO Error]({{< relref "/languages/rust/io-error" >}}) — I/O error
- [JSON Parse]({{< relref "/languages/rust/json-parse" >}}) — JSON parse error
