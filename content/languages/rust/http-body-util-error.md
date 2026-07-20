---
title: "[Solution] http-body-util Body Error Fix"
description: "Fix http-body-util body errors. Handle body framing, size limits, and streaming."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# HTTP Body Util Error

HTTP body util errors occur when using the `http-body-util` crate for HTTP body manipulation — empty bodies, size limits, and framing issues.

## Common Causes

```rust
// Empty body when content expected
let body = Empty::new().map_err(|never| match never {});

// Missing body size hint
let body = Full::new(Bytes::from("data"));
```

## How to Fix

1. **Collect body data properly**

```rust
use http_body_util::{BodyExt, Full, Empty};
use bytes::Bytes;

let body = Full::new(Bytes::from("Hello, Body!"));
let collected = body.collect().await?;
let data = collected.to_bytes();
```

2. **Limit body size**

```rust
let limited = body.limit(1024 * 1024); // 1MB max
match limited.collect().await {
    Ok(data) => println!("Got {} bytes", data.to_bytes().len()),
    Err(e) => eprintln!("Body too large: {}", e),
}
```

3. **Handle empty bodies**

```rust
use http_body_util::{BodyExt, Full, Empty};
use bytes::Bytes;

let empty: Empty<Bytes> = Empty::new();
let data = empty.collect().await?.to_bytes();
```

## Examples

```rust
use http_body_util::{BodyExt, Full, Empty};
use bytes::Bytes;

#[tokio::main]
async fn main() {
    let body = Full::new(Bytes::from("Hello, World!"));
    let data = body.collect().await.unwrap().to_bytes();
    println!("Body: {}", String::from_utf8_lossy(&data));
}
```

## Related Errors

- [Hyper Error]({{< relref "/languages/rust/hyper-error" >}}) — HTTP layer
- [H2 Error]({{< relref "/languages/rust/h2-error" >}}) — HTTP/2
- [Tower Error]({{< relref "/languages/rust/tower-error" >}}) — middleware
