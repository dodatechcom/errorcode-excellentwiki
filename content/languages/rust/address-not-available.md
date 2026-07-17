---
title: "[Solution] Rust Cannot Assign Requested Address — Address Not Available"
description: "Fix Rust cannot assign requested address error. Learn why binding or connecting to a local address fails and how to resolve address availability issues."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Cannot Assign Requested Address — Address Not Available

An IO error with the message "Cannot assign requested address (os error 99)" occurs when you try to bind or connect to a network address that is not available on the local system.

## Description

This error (code 99, `EADDRNOTAVAIL`) occurs when:

- The IP address doesn't exist on any local network interface.
- You're trying to bind to an interface that isn't configured.
- The local port range is exhausted.
- The address is valid but not assignable to this machine.

Common scenarios:

- **Binding to wrong interface** — using an IP the machine doesn't have.
- **All ephemeral ports used** — too many outgoing connections.
- **Network interface down** — trying to use an interface that's not up.
- **Docker/VM networking** — wrong network context.

## Common Causes

```rust
use std::net::TcpListener;

// Cause 1: Binding to non-existent IP
let listener = TcpListener::bind("192.168.1.100:8080")?; // machine doesn't have this IP

// Cause 2: Binding to interface that's down
let listener = TcpListener::bind("10.0.0.1:8080")?; // interface is down

// Cause 3: Using localhost when not configured
let listener = TcpListener::bind("127.0.0.2:8080")?; // only 127.0.0.1 is available

// Cause 4: Too many outgoing connections
use std::net::TcpStream;
for i in 0..30000 {
    TcpStream::connect("remote-server:80")?; // may exhaust local ports
}
```

## Solutions

### Fix 1: Bind to 0.0.0.0 to listen on all interfaces

```rust
// Wrong — specific IP that doesn't exist
let listener = TcpListener::bind("192.168.1.100:8080")?;

// Correct — listen on all interfaces
let listener = TcpListener::bind("0.0.0.0:8080")?;

// Or bind to localhost
let listener = TcpListener::bind("127.0.0.1:8080")?;
```

### Fix 2: Check available interfaces first

```rust
use std::net::UdpSocket;

fn get_local_ip() -> Option<String> {
    let socket = UdpSocket::bind("0.0.0.0:0").ok()?;
    socket.connect("8.8.8.8:80").ok()?;
    Some(socket.local_addr().ok()?.ip().to_string())
}

fn main() {
    match get_local_ip() {
        Some(ip) => println!("Local IP: {}", ip),
        None => eprintln!("Could not determine local IP"),
    }
}
```

### Fix 3: Use port 0 for automatic port assignment

```rust
use std::net::TcpListener;

// Wrong — specific port might be unavailable
let listener = TcpListener::bind("0.0.0.0:8080")?;

// Correct — let OS assign an available port
let listener = TcpListener::bind("0.0.0.0:0")?;
let port = listener.local_addr()?.port();
println!("Listening on random port: {}", port);
```

### Fix 4: Reduce connection churn to avoid port exhaustion

```rust
use std::net::TcpStream;
use std::time::Duration;

// Wrong — creates too many connections
fn bad_connections() -> std::io::Result<()> {
    for _ in 0..30000 {
        TcpStream::connect("server:80")?;
    }
    Ok(())
}

// Correct — reuse connections
fn good_connections() -> std::io::Result<()> {
    let stream = TcpStream::connect("server:80")?;
    stream.set_read_timeout(Some(Duration::from_secs(30)))?;
    // Reuse the same connection for multiple requests
    Ok(())
}
```

## Examples

```rust
use std::net::TcpListener;

fn main() {
    // This machine doesn't have IP 192.168.1.100
    match TcpListener::bind("192.168.1.100:8080") {
        Ok(_) => println!("Bound successfully"),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

Output:
```
Error: Cannot assign requested address (os error 99)
```

## Related Errors

- [Address in Use]({{< relref "/languages/rust/address-in-use" >}}) — port is already bound by another process.
- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — no one listening on the port.
- [Timed Out]({{< relref "/languages/rust/timed-out" >}}) — connection attempt timed out.
