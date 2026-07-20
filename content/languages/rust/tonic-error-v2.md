---
title: "[Solution] tonic gRPC Transport Error Fix"
description: "Fix tonic gRPC transport errors. Handle connection failures, channel errors, and transport layer issues."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Tonic Error

Tonic errors occur when using the `tonic` crate for gRPC — connection, transport, and status errors.

## Common Causes

```rust
// Connection refused
let channel = Channel::from_static("http://wrong:50051").connect().await?;

// Invalid protobuf message
let response = client.get_user(request).await?;
```

## How to Fix

1. **Configure channel properly**

```rust
use tonic::transport::Channel;

let channel = Channel::from_static("http://[::1]:50051")
    .connect()
    .await?;
```

2. **Handle gRPC status codes**

```rust
use tonic::Status;

match client.get_user(request).await {
    Ok(response) => println!("{:?}", response.into_inner()),
    Err(Status::NotFound(msg)) => eprintln!("Not found: {}", msg),
    Err(Status::InvalidArgument(msg)) => eprintln!("Invalid: {}", msg),
    Err(status) => eprintln!("RPC error: {}", status),
}
```

3. **Use interceptors for auth**

```rust
use tonic::transport::{Channel, ClientTlsConfig};

let tls = ClientTlsConfig::new()
    .domain_name("example.com");

let channel = Channel::from_static("https://example.com")
    .tls_config(tls)?
    .connect()
    .await?;
```

## Examples

```rust
use tonic::{transport::Server, Request, Response, Status};

pub trait MyService {
    async fn say_hello(&self, req: Request<HelloRequest>)
        -> Result<Response<HelloReply>, Status>;
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr = "[::1]:50051".parse()?;
    println!("Server listening on {}", addr);
    Ok(())
}
```

## Related Errors

- [Tonic Error v2]({{< relref "/languages/rust/tonic-error-v2" >}}) — tonic v2
- [H2 Error]({{< relref "/languages/rust/h2-error" >}}) — HTTP/2
- [Quinn Error]({{< relref "/languages/rust/quinn-error" >}}) — QUIC
