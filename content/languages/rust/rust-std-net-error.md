---
title: "[Solution] Rust Std Net Error — How to Fix"
description: "Fix standard library networking errors. Resolve TCP/UDP connection, binding, and address issues."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
comments: true
---

# Std Net Error

Std net errors occur when using `std::net` for networking — DNS resolution failures, connection refused, address already in use, and broken pipe.

## Common Causes

```rust
use std::net::{TcpListener, TcpStream, UdpSocket};

// Address already in use
let listener = TcpListener::bind("127.0.0.1:8080").unwrap();
let _listener2 = TcpListener::bind("127.0.0.1:8080").unwrap(); // ERROR: addr in use

// Connection refused
let stream = TcpStream::connect("127.0.0.1:9999").unwrap(); // ERROR: refused

// DNS resolution failure
let stream = TcpStream::connect("nonexistent.invalid:80").unwrap(); // ERROR

// UDP socket bound to wrong address
let socket = UdpSocket::bind("127.0.0.1:8080").unwrap();
socket.connect("192.168.1.1:8080").unwrap(); // May fail if unreachable
```

## How to Fix

1. **Use `set_nonblocking` for async-like behavior**

```rust
use std::net::TcpListener;

fn start_server() -> std::io::Result<()> {
    let listener = TcpListener::bind("127.0.0.1:0")?; // Bind to any port
    println!("Listening on {}", listener.local_addr()?);

    listener.set_nonblocking(true)?;

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => println!("Connection from {}", stream.peer_addr()?),
            Err(ref e) if e.kind() == std::io::ErrorKind::WouldBlock => {
                // No connection yet, do other work
                std::thread::sleep(std::time::Duration::from_millis(10));
            }
            Err(e) => eprintln!("Error: {}", e),
        }
    }
    Ok(())
}
```

2. **Use socket options for reuse and timeouts**

```rust
use std::net::TcpListener;
use std::time::Duration;

fn start_server() -> std::io::Result<()> {
    let listener = TcpListener::bind("127.0.0.1:8080")?;
    listener.set_nonblocking(false)?;

    for stream in listener.incoming() {
        match stream {
            Ok(stream) => {
                stream.set_read_timeout(Some(Duration::from_secs(30)))?;
                stream.set_write_timeout(Some(Duration::from_secs(10)))?;
                // Handle connection
            }
            Err(e) => eprintln!("Accept error: {}", e),
        }
    }
    Ok(())
}
```

3. **Handle DNS resolution errors**

```rust
use std::net::ToSocketAddrs;

fn resolve(host: &str, port: u16) -> std::io::Result<std::net::SocketAddr> {
    let addrs = format!("{}:{}", host, port).to_socket_addrs()?;
    addrs.first()
        .copied()
        .ok_or_else(|| std::io::Error::new(std::io::ErrorKind::Other, "No addresses found"))
}
```

## Examples

```rust
use std::net::{TcpListener, TcpStream};
use std::io::{Read, Write};

fn main() -> std::io::Result<()> {
    // Server
    let listener = TcpListener::bind("127.0.0.1:0")?;
    let addr = listener.local_addr()?;
    println!("Server at {}", addr);

    // Client (in same thread for demo)
    let mut client = TcpStream::connect(addr)?;
    client.write_all(b"Hello, server!")?;

    let mut server = listener.incoming().next().unwrap()?;
    let mut buf = [0u8; 1024];
    let n = server.read(&mut buf)?;
    println!("Server received: {}", String::from_utf8_lossy(&buf[..n]));

    Ok(())
}
```

## Related Errors

- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — connection refused
- [Timed Out]({{< relref "/languages/rust/timed-out" >}}) — operation timed out
- [Address In Use]({{< relref "/languages/rust/address-in-use" >}}) — port occupied
