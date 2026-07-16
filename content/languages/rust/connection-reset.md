---
title: "[Solution] Rust Connection Reset — Connection Reset by Peer"
description: "Fix Rust connection reset error. Learn why connections are reset by the peer and how to handle this network error."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["connection", "reset", "network", "tcp", "peer", "io"]
weight: 5
---

# Connection Reset — Connection Reset by Peer

An IO error with the message "Connection reset by peer (os error 104)" occurs when the remote side of a TCP connection sends a RST packet, abruptly closing the connection.

## Description

A connection reset happens when:

- The server process crashes or is killed.
- The server's OS closes the connection abruptly.
- A firewall or load balancer drops the connection.
- Network issues cause the connection to become invalid.

Unlike "connection refused" (which means the server isn't listening), "connection reset" means a connection was established but then forcibly closed. The error code is 104 (`ECONNRESET`).

Common scenarios:

- **Server crashes** — server process dies while connected.
- **Server restarts** — service restarts, dropping existing connections.
- **Firewall timeout** — idle connection killed by firewall.
- **Load balancer timeout** — proxy closes idle backend connections.
- **Network interruption** — brief network outage resets the connection.

## Common Causes

```rust
use std::io::{Read, Write};
use std::net::TcpStream;

// Cause 1: Server crashes during data transfer
let mut stream = TcpStream::connect("server:8080")?;
stream.write_all(b"request")?;
let mut buffer = [0; 1024];
let n = stream.read(&mut buffer)?; // may get connection reset

// Cause 2: Server closes connection abruptly
let mut stream = TcpStream::connect("server:8080")?;
// Server sends RST after receiving data

// Cause 3: Firewall timeout
let mut stream = TcpStream::connect("server:8080")?;
// Wait too long, firewall kills the connection
std::thread::sleep(std::time::Duration::from_secs(300));
let n = stream.read(&mut buffer)?; // connection reset

// Cause 4: Half-closed connection
let mut stream = TcpStream::connect("server:8080")?;
stream.shutdown(std::net::Shutdown::Write)?; // half-close
let n = stream.read(&mut buffer)?; // may get reset
```

## Solutions

### Fix 1: Implement connection retry with reconnect

```rust
use std::io::{Read, Write};
use std::net::TcpStream;
use std::time::Duration;

fn send_with_retry(addr: &str, data: &[u8], max_retries: u32) -> std::io::Result<Vec<u8>> {
    let mut last_err = None;

    for attempt in 0..max_retries {
        match TcpStream::connect(addr) {
            Ok(mut stream) => {
                stream.set_read_timeout(Some(Duration::from_secs(10)))?;
                stream.set_write_timeout(Some(Duration::from_secs(10)))?;

                if stream.write_all(data).is_err() {
                    last_err = std::io::Error::last_os_error().into();
                    continue;
                }

                let mut buffer = Vec::new();
                match stream.read_to_end(&mut buffer) {
                    Ok(_) => return Ok(buffer),
                    Err(e) => {
                        eprintln!("Read failed on attempt {}: {}", attempt + 1, e);
                        last_err = Some(e);
                    }
                }
            }
            Err(e) => {
                eprintln!("Connect failed on attempt {}: {}", attempt + 1, e);
                last_err = Some(e);
            }
        }

        std::thread::sleep(Duration::from_millis(100 * (attempt as u64 + 1)));
    }

    Err(last_err.unwrap_or_else(|| {
        std::io::Error::new(std::io::ErrorKind::Other, "all retries failed")
    }))
}
```

### Fix 2: Use TCP keepalive to detect dead connections

```rust
use std::net::TcpStream;
use std::time::Duration;

fn connect_with_keepalive(addr: &str) -> std::io::Result<TcpStream> {
    let stream = TcpStream::connect(addr)?;

    // Enable TCP keepalive
    let keepalive = socket2::Keepalive::new()
        .with_time(Duration::from_secs(60))
        .with_interval(Duration::from_secs(10));

    let socket = socket2::Socket::from(stream);
    socket.set_keepalive(true)?;
    socket.set_tcp_keepalive(&keepalive)?;

    Ok(TcpStream::from(socket))
}
```

### Fix 3: Handle partial reads gracefully

```rust
use std::io::{Read, Write};
use std::net::TcpStream;

fn read_all(stream: &mut TcpStream) -> std::io::Result<Vec<u8>> {
    let mut buffer = Vec::new();
    let mut chunk = [0; 4096];

    loop {
        match stream.read(&mut chunk) {
            Ok(0) => break, // connection closed gracefully
            Ok(n) => buffer.extend_from_slice(&chunk[..n]),
            Err(e) if e.kind() == std::io::ErrorKind::ConnectionReset => {
                eprintln!("Connection reset, returning partial data");
                break;
            }
            Err(e) => return Err(e),
        }
    }

    Ok(buffer)
}
```

### Fix 4: Use higher-level libraries that handle reconnection

```rust
use reqwest::blocking::Client;
use std::time::Duration;

fn fetch_with_retry(url: &str, max_retries: u32) -> Result<String, reqwest::Error> {
    let client = Client::builder()
        .timeout(Duration::from_secs(30))
        .build()?;

    let mut last_err = None;

    for attempt in 0..max_retries {
        match client.get(url).send() {
            Ok(response) => {
                return response.text();
            }
            Err(e) => {
                eprintln!("Attempt {} failed: {}", attempt + 1, e);
                last_err = Some(e);
                std::thread::sleep(Duration::from_millis(500 * (attempt as u64 + 1)));
            }
        }
    }

    Err(last_err.unwrap())
}
```

## Examples

```rust
use std::io::{Read, Write};
use std::net::TcpStream;

fn main() -> std::io::Result<()> {
    let mut stream = TcpStream::connect("localhost:8080")?;
    stream.write_all(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")?;

    let mut buffer = [0; 1024];
    let n = stream.read(&mut buffer)?;
    println!("Read {} bytes", n);
    Ok(())
}
```

Output (if server crashes):
```
Error: Connection reset by peer (os error 104)
```

## Related Errors

- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — server not listening on port.
- [Timed Out]({{< relref "/languages/rust/timed-out" >}}) — connection timed out.
- [Not Connected]({{< relref "/languages/rust/not-connected" >}}) — socket is not connected.
