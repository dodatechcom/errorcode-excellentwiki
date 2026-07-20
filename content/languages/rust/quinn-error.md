---
title: "[Solution] quinn QUIC Error Fix"
description: "Fix quinn QUIC protocol errors. Handle connection establishment, streams, and congestion control."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Quinn Error

Quinn errors occur when using the `quinn` crate for QUIC — connection and stream errors.

## Common Causes

```rust
// Connection refused
let endpoint = Endpoint::client("0.0.0.0:0".parse()?)?;
let conn = endpoint.connect(addr, "localhost")?.await?;

// TLS certificate errors
// Self-signed certs not accepted by default
```

## How to Fix

1. **Configure the endpoint properly**

```rust
use quinn::Endpoint;

let mut endpoint = Endpoint::client("0.0.0.0:0".parse()?)?;
```

2. **Handle self-signed certificates for testing**

```rust
use quinn::crypto::rustls::QuicClientConfig;
use rustls::ClientConfig;

let mut roots = rustls::RootCertStore::empty();
roots.add(cert)?;
let mut config = ClientConfig::builder()
    .with_root_certificates(roots)
    .with_no_client_auth();
```

3. **Use accept() properly**

```rust
while let Some(conn) = endpoint.accept().await {
    tokio::spawn(async move {
        if let Ok(conn) = conn.await {
            // handle connection
        }
    });
}
```

## Examples

```rust
use quinn::{Endpoint, ServerConfig};
use std::net::SocketAddr;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let addr: SocketAddr = "127.0.0.1:4433".parse()?;
    let endpoint = Endpoint::client("0.0.0.0:0".parse()?)?;
    let conn = endpoint.connect(addr, "localhost")?.await?;
    let mut stream = conn.open_bi().await?.0;
    stream.write_all(b"hello").await?;
    Ok(())
}
```

## Related Errors

- [Rustls Error]({{< relref "/languages/rust/rustls-error" >}}) — TLS layer
- [Ring Error]({{< relref "/languages/rust/ring-error" >}}) — crypto
- [Tokio Error]({{< relref "/languages/rust/tokio-error" >}}) — async runtime
