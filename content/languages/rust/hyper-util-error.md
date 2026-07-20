---
title: "[Solution] hyper-util Connection Error Fix"
description: "Fix hyper-util connection errors. Handle HTTP/1.1 and HTTP/2 connections, pooling, and keep-alive."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Hyper Error

Hyper errors occur when using the `hyper` crate for HTTP — connection errors, request/response parsing failures, and body handling issues.

## Common Causes

```rust
// Connection refused
let client = Client::new();
let resp = client.get("http://localhost:9999".parse()?).await?;

// Body already consumed
let body = resp.into_body();
let data = body.try_into_bytes()?;
// body.try_into_bytes()?; // ERROR: already consumed
```

## How to Fix

1. **Handle connection errors with retries**

```rust
use hyper::{Client, Uri};
use http_body_util::BodyExt;

let client = Client::new();
let uri: Uri = "http://httpbin.org/get".parse()?;
let resp = client.get(uri).await?;
let body = resp.into_body().collect().await?.to_bytes();
```

2. **Use proper body handling**

```rust
let body = resp.into_body();
let data = body.collect().await?.to_bytes();
println!("{}", String::from_utf8_lossy(&data));
```

3. **Use hyper-util for easier setup**

```rust
use hyper_util::rt::TokioIo;
use tokio::net::TcpStream;

let stream = TcpStream::connect("127.0.0.1:3000").await?;
let io = TokioIo::new(stream);
```

## Examples

```rust
use hyper::{Client, Server};
use hyper::service::{make_service_fn, service_fn};
use http_body_util::Full;
use bytes::Bytes;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = ([127, 0, 0, 1], 3000).into();
    let service = make_service_fn(|_| async {
        Ok::<_, hyper::Error>(service_fn(|_req| async {
            Ok::<_, hyper::Error>(
                http::Response::new(Full::new(Bytes::from("Hello, Hyper!")))
            )
        }))
    });
    Server::bind(&addr).serve(service).await?;
    Ok(())
}
```

## Related Errors

- [Axum Error]({{< relref "/languages/rust/rust-axum-error" >}}) — Axum framework
- [Warp Error]({{< relref "/languages/rust/rust-warp-error" >}}) — Warp framework
- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — network errors
