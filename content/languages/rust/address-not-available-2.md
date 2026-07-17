---
title: "[Solution] Rust Cannot Assign Requested Address — Address Not Available"
description: "Fix Rust cannot assign requested address error. Learn why binding or connecting to a local address fails and how to resolve it."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Cannot Assign Requested Address — Address Not Available

An IO error with the message "Cannot assign requested address (os error 99)" occurs when you try to bind or connect to a network address that doesn't exist on the local system.

## Description

Error code 99 (`EADDRNOTAVAIL`) means the IP address isn't configured on any local interface, or the local port range is exhausted. This is common in containers, VMs, or when creating many outbound connections.

Common scenarios:

- **Binding to wrong interface** — IP doesn't exist on this machine.
- **Ephemeral port exhaustion** — too many outgoing connections.
- **Network interface down** — trying to use an interface that's not up.
- **Docker/VM networking** — wrong network context.

## Common Causes

```rust
use std::net::TcpListener;

// Cause 1: Non-existent IP
let listener = TcpListener::bind("192.168.1.100:8080")?;

// Cause 2: Interface is down
let listener = TcpListener::bind("10.0.0.1:8080")?;

// Cause 3: Wrong loopback address
let listener = TcpListener::bind("127.0.0.2:8080")?;

// Cause 4: Port exhaustion
use std::net::TcpStream;
for _ in 0..30000 {
    TcpStream::connect("remote:80")?;
}
```

## Solutions

### Fix 1: Bind to 0.0.0.0

```rust
// Wrong — specific IP that doesn't exist
let listener = std::net::TcpListener::bind("192.168.1.100:8080")?;

// Correct — all interfaces
let listener = std::net::TcpListener::bind("0.0.0.0:8080")?;

// Or localhost
let listener = std::net::TcpListener::bind("127.0.0.1:8080")?;
```

### Fix 2: Detect local IP

```rust
use std::net::UdpSocket;

fn local_ip() -> Option<String> {
    let sock = UdpSocket::bind("0.0.0.0:0").ok()?;
    sock.connect("8.8.8.8:80").ok()?;
    Some(sock.local_addr().ok()?.ip().to_string())
}

fn main() {
    match local_ip() {
        Some(ip) => println!("Local IP: {}", ip),
        None => eprintln!("Could not determine local IP"),
    }
}
```

### Fix 3: Use port 0 for auto-assignment

```rust
use std::net::TcpListener;

let listener = TcpListener::bind("0.0.0.0:0")?;
let port = listener.local_addr()?.port();
println!("Listening on random port: {}", port);
```

### Fix 4: Reuse connections to avoid port exhaustion

```rust
use std::net::TcpStream;
use std::time::Duration;

fn reuse_connection() -> std::io::Result<()> {
    let stream = TcpStream::connect("server:80")?;
    stream.set_read_timeout(Some(Duration::from_secs(30)))?;
    // Reuse this connection instead of creating many
    Ok(())
}
```

## Examples

```rust
use std::net::TcpListener;

fn main() {
    match TcpListener::bind("192.168.1.100:8080") {
        Ok(_) => println!("Bound!"),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

Output:
```
Error: Cannot assign requested address (os error 99)
```

## Related Errors

- [Address in Use]({{< relref "/languages/rust/address-in-use-2" >}}) — port already bound.
- [Connection Refused]({{< relref "/languages/rust/connection-refused-2" >}}) — no listener on port.
- [Timed Out]({{< relref "/languages/rust/timed-out-2" >}}) — connection timed out.
