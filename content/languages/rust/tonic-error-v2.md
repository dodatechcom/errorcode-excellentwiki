---
title: "[Solution] tonic gRPC Transport Error Fix"
description: "Fix tonic gRPC transport errors. Handle connection failures, channel errors, and transport layer issues."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# tonic gRPC Transport Error

Fix tonic gRPC transport errors. Handle connection failures, channel errors, and transport layer issues.

## What This Error Means

tonic transport errors occur when the gRPC client or server cannot establish or maintain a connection:

```
tonic::transport::Error(Transport, connect error: os error 111)
Status { code: Unavailable, message: "connection refused" }
```

## Common Causes

```rust
// Cause 1: Server not running or wrong address
let client = MyServiceClient::connect("http://localhost:50051").await?;

// Cause 2: TLS mismatch (client expects TLS, server uses plaintext)
// Cause 3: DNS resolution failure
// Cause 4: Connection timeout under load
// Cause 5: Max concurrent streams exceeded
```

## How to Fix

### Fix 1: Configure channel options

```rust
use tonic::transport::Channel;

let channel = Channel::from_static("http://[::1]:50051")
    .connect_timeout(std::time::Duration::from_secs(5))
    .keep_alive(std::time::Duration::from_secs(30), "ping".parse().unwrap())
    .max_concurrent_streams(100)
    .connect()
    .await?;

let mut client = MyServiceClient::new(channel);
```

### Fix 2: Add reconnection logic

```rust
use tonic::transport::Channel;
use std::time::Duration;

async fn connect_with_retry(endpoint: &str) -> Result<Channel, tonic::transport::Error> {
    let mut delay = Duration::from_secs(1);

    for attempt in 0..5 {
        match Channel::from_shared(endpoint.to_string())?.connect().await {
            Ok(channel) => return Ok(channel),
            Err(e) => {
                eprintln!("Connection attempt {} failed: {}", attempt + 1, e);
                tokio::time::sleep(delay).await;
                delay = (delay * 2).min(Duration::from_secs(30));
            }
        }
    }

    Err(tonic::transport::Error::new("Failed to connect after 5 attempts"))
}
```

### Fix 3: Use appropriate transport (TLS vs plaintext)

```rust
use tonic::transport::{Channel, ClientTlsConfig};

// Plaintext connection
let channel = Channel::from_static("http://localhost:50051")
    .connect()
    .await?;

// TLS connection
let tls_config = ClientTlsConfig::new()
    .domain_name("example.com")
    .ca_certificate(tonic::transport::Certificate::from_pem(ca_pem));

let channel = Channel::from_static("https://example.com:50051")
    .tls_config(tls_config)?
    .connect()
    .await?;
```

## Examples

```rust
use tonic::{Request, Status, Response};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let channel = tonic::transport::Channel::from_static("http://[::1]:50051")
        .connect()
        .await?;

    let mut client = GreeterClient::new(channel);

    let request = Request::new(HelloRequest {
        name: "World".into(),
    });

    let response = client.say_hello(request).await?;
    println!("Response: {:?}", response.into_inner());

    Ok(())
}
```

## Related Errors

- [H2 Error]({{< relref "/languages/rust/h2-error" >}}) — HTTP/2 error
- [Hyper Error]({{< relref "/languages/rust/hyper-error" >}}) — hyper error
- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — connection refused
