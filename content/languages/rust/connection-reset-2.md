---
title: "[Solution] Rust Connection Reset — Peer Reset Connection"
description: "Fix Rust connection reset error. Learn why connections are reset by the peer and how to implement retry logic and keepalive."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Connection Reset — Peer Reset Connection

An IO error with the message "Connection reset by peer (os error 104)" occurs when the remote end of an established TCP connection sends a RST packet, forcibly closing it.

## Description

A connection reset means a connection _was_ established but was then abruptly terminated. The peer (server or client) sent a TCP RST instead of a graceful FIN. Error code 104 (`ECONNRESET`).

Common scenarios:

- **Server crashes** — process dies mid-connection.
- **Server restarts** — service restarts dropping existing connections.
- **Firewall timeout** — idle connection killed by firewall.
- **Load balancer** — proxy closes idle backend connections.

## Common Causes

```rust
use std::io::{Read, Write};
use std::net::TcpStream;

// Cause 1: Server crashes during transfer
let mut stream = TcpStream::connect("server:8080")?;
stream.write_all(b"request")?;
let mut buf = [0u8; 1024];
let n = stream.read(&mut buf)?; // may get connection reset

// Cause 2: Server closes abruptly
let mut stream = TcpStream::connect("server:8080")?;
// Server sends RST after receiving data

// Cause 3: Firewall kills idle connection
std::thread::sleep(std::time::Duration::from_secs(300));
let n = stream.read(&mut buf)?; // reset

// Cause 4: Half-closed connection
let mut stream = TcpStream::connect("server:8080")?;
stream.shutdown(std::net::Shutdown::Write)?;
let n = stream.read(&mut buf)?; // may reset
```

## Solutions

### Fix 1: Retry with reconnect

```rust
use std::io::{Read, Write};
use std::net::TcpStream;
use std::time::Duration;

fn send_retry(addr: &str, data: &[u8], retries: u32) -> std::io::Result<Vec<u8>> {
    for attempt in 0..retries {
        match TcpStream::connect(addr) {
            Ok(mut stream) => {
                stream.set_read_timeout(Some(Duration::from_secs(10)))?;
                if stream.write_all(data).is_err() { continue; }
                let mut buf = Vec::new();
                match stream.read_to_end(&mut buf) {
                    Ok(_) => return Ok(buf),
                    Err(e) if e.kind() == std::io::ErrorKind::ConnectionReset => continue,
                    Err(e) => return Err(e),
                }
            }
            Err(_) => {
                std::thread::sleep(Duration::from_millis(100 * (attempt as u64 + 1)));
            }
        }
    }
    Err(std::io::Error::new(std::io::ErrorKind::Other, "retries exhausted"))
}
```

### Fix 2: Handle partial reads

```rust
use std::io::{Read, Write};
use std::net::TcpStream;

fn read_all(stream: &mut TcpStream) -> std::io::Result<Vec<u8>> {
    let mut buf = Vec::new();
    let mut chunk = [0u8; 4096];
    loop {
        match stream.read(&mut chunk) {
            Ok(0) => break,
            Ok(n) => buf.extend_from_slice(&chunk[..n]),
            Err(e) if e.kind() == std::io::ErrorKind::ConnectionReset => {
                eprintln!("Connection reset, returning partial data");
                break;
            }
            Err(e) => return Err(e),
        }
    }
    Ok(buf)
}
```

### Fix 3: Use TCP keepalive

```rust
use std::net::TcpStream;
use std::time::Duration;

fn connect_keepalive(addr: &str) -> std::io::Result<TcpStream> {
    let stream = TcpStream::connect(addr)?;
    stream.set_read_timeout(Some(Duration::from_secs(60)))?;
    // Keepalive detects dead connections
    // (platform-specific socket2 setup needed for full control)
    Ok(stream)
}
```

### Fix 4: Use reqwest with retry

```rust
use reqwest::blocking::Client;
use std::time::Duration;

fn fetch_retry(url: &str, retries: u32) -> Result<String, reqwest::Error> {
    let client = Client::builder()
        .timeout(Duration::from_secs(30))
        .build()?;
    let mut last_err = None;
    for attempt in 0..retries {
        match client.get(url).send() {
            Ok(resp) => return resp.text(),
            Err(e) => {
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
    let mut buf = [0u8; 1024];
    let n = stream.read(&mut buf)?;
    println!("Read {} bytes", n);
    Ok(())
}
```

Output (if server crashes):
```
Error: Connection reset by peer (os error 104)
```

## Related Errors

- [Connection Refused]({{< relref "/languages/rust/connection-refused-2" >}}) — server not listening.
- [Timed Out]({{< relref "/languages/rust/timed-out-2" >}}) — connection timed out.
- [Not Connected]({{< relref "/languages/rust/not-connected-2" >}}) — socket not connected.
