---
title: "[Solution] native-tls Handshake Error Fix"
description: "Fix native-tls handshake errors. Handle certificate validation, SNI, and protocol configuration."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Native TLS Error

Native TLS errors occur when using the `native-tls` crate — certificate verification, handshake failures, and protocol issues.

## Common Causes

```rust
// Certificate not trusted
let connector = TlsConnector::new()?;
let stream = TcpStream::connect("example.com:443")?;
let mut tls = connector.connect("example.com", stream)?; // Untrusted cert

// Wrong hostname
connector.connect("wrong-hostname", stream)?; // hostname mismatch
```

## How to Fix

1. **Configure connector properly**

```rust
use native_tls::{TlsConnector, TlsConnectorBuilder};

let connector = TlsConnector::builder()
    .danger_accept_invalid_certs(false) // Keep true for production
    .build()?;
```

2. **Handle certificate errors**

```rust
use native_tls::TlsConnector;

match TlsConnector::new()?.connect("example.com", stream) {
    Ok(tls) => println!("Connected securely"),
    Err(e) => eprintln!("TLS error: {}", e),
}
```

3. **Use identity for client certs**

```rust
use native_tls::{Identity, TlsConnector};
use std::fs;

let cert = fs::read("client.p12")?;
let identity = Identity::from_pkcs12(&cert, "password")?;
let connector = TlsConnector::builder()
    .identity(identity)
    .build()?;
```

## Examples

```rust
use native_tls::TlsConnector;
use std::net::TcpStream;
use std::io::{Read, Write};

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let connector = TlsConnector::new()?;
    let stream = TcpStream::connect("example.com:443")?;
    let mut tls = connector.connect("example.com", stream)?;

    tls.write_all(b"GET / HTTP/1.1
Host: example.com

")?;
    let mut buf = [0u8; 1024];
    let n = tls.read(&mut buf)?;
    println!("{}", String::from_utf8_lossy(&buf[..n]));
    Ok(())
}
```

## Related Errors

- [OpenSSL Error]({{< relref "/languages/rust/openssl-error-rs" >}}) — OpenSSL
- [Rustls Error]({{< relref "/languages/rust/rustls-error" >}}) — Rustls
- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — network
