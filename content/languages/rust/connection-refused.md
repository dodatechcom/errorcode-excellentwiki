---
title: "[Solution] Rust Connection Refused — Network Connection Error"
description: "Fix Rust connection refused error. Learn why TCP connections are refused and how to handle network connection failures."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["connection", "refused", "network", "tcp", "socket", "io"]
weight: 5
---

# Connection Refused — Network Connection Error

An IO error with the message "Connection refused (os error 111)" occurs when a TCP connection attempt is actively rejected by the target server. The server's OS sent a RST packet instead of completing the handshake.

## Description

When you try to connect to a TCP port and the server:

- Is not listening on that port.
- Has a firewall blocking the connection.
- Has a backlog queue that is full.
- Has `net.ipv4.tcp_abort_on_overflow` enabled.

The OS returns error code 111 (`ECONNREFUSED`), which Rust wraps as `io::Error`. This differs from "connection timed out" (error 110), which means the server didn't respond at all.

Common scenarios:

- **Server not running** — connecting to a port where no service is listening.
- **Wrong port** — service is on port 8080 but you're connecting to 80.
- **Firewall blocking** — firewall actively rejects connections.
- **Server crashed** — service was running but has stopped.
- **Wrong address** — connecting to the wrong host.

## Common Causes

```rust
use std::net::TcpStream;

// Cause 1: Server not running
let stream = TcpStream::connect("localhost:8080")?;

// Cause 2: Wrong port
let stream = TcpStream::connect("localhost:80")?; // service is on 8080

// Cause 3: Connecting to wrong host
let stream = TcpStream::connect("wrong-hostname:8080")?;

// Cause 4: Firewall blocking
let stream = TcpStream::connect("remote-server:3306")?;

// Cause 5: Service crashed between check and connect
// (TOCTOU race condition)
```

## Solutions

### Fix 1: Retry with exponential backoff

```rust
use std::net::TcpStream;
use std::thread;
use std::time::Duration;

fn connect_with_retry(addr: &str, max_retries: u32) -> std::io::Result<TcpStream> {
    let mut delay = Duration::from_millis(100);

    for attempt in 0..max_retries {
        match TcpStream::connect(addr) {
            Ok(stream) => {
                println!("Connected on attempt {}", attempt + 1);
                return Ok(stream);
            }
            Err(e) => {
                eprintln!("Attempt {} failed: {}", attempt + 1, e);
                if attempt < max_retries - 1 {
                    thread::sleep(delay);
                    delay = (delay * 2).min(Duration::from_secs(30));
                }
            }
        }
    }

    Err(std::io::Error::new(
        std::io::ErrorKind::ConnectionRefused,
        format!("Failed to connect after {} retries", max_retries),
    ))
}

fn main() -> std::io::Result<()> {
    let stream = connect_with_retry("localhost:8080", 5)?;
    println!("Connected!");
    Ok(())
}
```

### Fix 2: Validate address before connecting

```rust
use std::net::TcpStream;
use std::time::Duration;

fn try_connect(addr: &str) -> bool {
    TcpStream::connect(addr)
        .map(|stream| {
            stream.set_read_timeout(Some(Duration::from_secs(5))).ok();
            true
        })
        .unwrap_or(false)
}

fn main() {
    let addresses = vec![
        "localhost:8080",
        "localhost:3000",
        "localhost:5000",
    ];

    for addr in addresses {
        if try_connect(addr) {
            println!("Found service at {}", addr);
            break;
        } else {
            println!("No service at {}", addr);
        }
    }
}
```

### Fix 3: Use async with timeout for non-blocking connection

```rust
use tokio::net::TcpStream;
use tokio::time::{timeout, Duration};

#[tokio::main]
async fn main() {
    let addr = "localhost:8080";

    match timeout(Duration::from_secs(5), TcpStream::connect(addr)).await {
        Ok(Ok(_stream)) => {
            println!("Connected to {}", addr);
        }
        Ok(Err(e)) => {
            eprintln!("Connection failed: {}", e);
        }
        Err(_) => {
            eprintln!("Connection timed out after 5 seconds");
        }
    }
}
```

### Fix 4: Check if server is running before connecting

```rust
use std::process::Command;

fn is_port_in_use(port: u16) -> bool {
    Command::new("ss")
        .args(&["-tlnp", &format!("port:{}", port)])
        .output()
        .map(|output| {
            let stdout = String::from_utf8_lossy(&output.stdout);
            stdout.contains(&port.to_string())
        })
        .unwrap_or(false)
}

fn main() {
    let port = 8080;
    if is_port_in_use(port) {
        println!("Port {} is in use, attempting connection...", port);
    } else {
        println!("Port {} is not in use", port);
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

- [Timed Out]({{< relref "/languages/rust/timed-out" >}}) — connection attempt timed out.
- [Connection Reset]({{< relref "/languages/rust/connection-reset" >}}) — connection was reset by peer.
- [Not Connected]({{< relref "/languages/rust/not-connected" >}}) — socket is not connected.
