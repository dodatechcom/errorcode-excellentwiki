---
title: "[Solution] Rust Connection Refused — TCP Connection Rejected"
description: "Fix Rust connection refused error. Learn why TCP connections are rejected and how to retry, validate addresses, and handle gracefully."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["connection", "refused", "network", "tcp", "socket", "retry"]
weight: 5
---

# Connection Refused — TCP Connection Rejected

An IO error with the message "Connection refused (os error 111)" occurs when a TCP connection attempt is actively rejected by the target — the server is not listening on that port.

## Description

When you try to connect to a TCP port and no process is listening, the OS sends a RST packet back. This results in error code 111 (`ECONNREFUSED`). This differs from "timed out" (no response at all) and "connection reset" (connection was established then dropped).

Common scenarios:

- **Server not running** — connecting to a port with no listener.
- **Wrong port** — service is on 8080 but you connected to 80.
- **Firewall actively rejecting** — firewall sends RST instead of dropping.
- **Server crashed** — service stopped between check and connect.

## Common Causes

```rust
use std::net::TcpStream;

// Cause 1: Server not running
let stream = TcpStream::connect("localhost:8080")?;

// Cause 2: Wrong port
let stream = TcpStream::connect("localhost:80")?; // service is on 8080

// Cause 3: Wrong hostname
let stream = TcpStream::connect("wrong-host:8080")?;

// Cause 4: Firewall blocking
let stream = TcpStream::connect("remote:3306")?;

// Cause 5: Service crashed between check and connect
```

## Solutions

### Fix 1: Retry with exponential backoff

```rust
use std::net::TcpStream;
use std::thread;
use std::time::Duration;

fn connect_retry(addr: &str, retries: u32) -> std::io::Result<TcpStream> {
    let mut delay = Duration::from_millis(100);
    for attempt in 0..retries {
        match TcpStream::connect(addr) {
            Ok(stream) => return Ok(stream),
            Err(e) => {
                eprintln!("Attempt {}: {}", attempt + 1, e);
                thread::sleep(delay);
                delay = (delay * 2).min(Duration::from_secs(30));
            }
        }
    }
    Err(std::io::Error::new(
        std::io::ErrorKind::ConnectionRefused,
        "all retries failed",
    ))
}
```

### Fix 2: Validate address before connecting

```rust
use std::net::TcpStream;
use std::time::Duration;

fn is_reachable(addr: &str) -> bool {
    TcpStream::connect(addr)
        .map(|s| s.set_read_timeout(Some(Duration::from_secs(1))).is_ok())
        .unwrap_or(false)
}

fn main() {
    let addrs = ["localhost:8080", "localhost:3000", "localhost:5000"];
    for addr in addrs {
        if is_reachable(addr) {
            println!("Found service at {}", addr);
            break;
        }
    }
}
```

### Fix 3: Use tokio with timeout

```rust
use tokio::net::TcpStream;
use tokio::time::{timeout, Duration};

#[tokio::main]
async fn main() {
    match timeout(Duration::from_secs(5), TcpStream::connect("localhost:8080")).await {
        Ok(Ok(_)) => println!("Connected!"),
        Ok(Err(e)) => eprintln!("Failed: {}", e),
        Err(_) => eprintln!("Timed out"),
    }
}
```

### Fix 4: Check if port is in use first

```rust
use std::process::Command;

fn is_port_in_use(port: u16) -> bool {
    Command::new("ss")
        .args(&["-tlnp", &format!("port:{}", port)])
        .output()
        .map(|o| String::from_utf8_lossy(&o.stdout).contains(&port.to_string()))
        .unwrap_or(false)
}

fn main() {
    let port = 8080;
    if is_port_in_use(port) {
        println!("Port {} is in use", port);
    } else {
        println!("Port {} is free", port);
    }
}
```

## Examples

```rust
use std::net::TcpStream;

fn main() {
    match TcpStream::connect("localhost:9999") {
        Ok(_) => println!("Connected!"),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

Output:
```
Error: Connection refused (os error 111)
```

## Related Errors

- [Timed Out]({{< relref "/languages/rust/timed-out-2" >}}) — connection attempt timed out.
- [Connection Reset]({{< relref "/languages/rust/connection-reset-2" >}}) — connection reset by peer.
- [Not Connected]({{< relref "/languages/rust/not-connected-2" >}}) — socket not connected.
