---
title: "[Solution] Rust Address Already in Use — Address in Use Error"
description: "Fix Rust address already in use error. Learn why binding to a port fails with 'Address already in use' and how to handle port conflicts."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Address Already in Use — Address in Use Error

An IO error with the message "Address already in use (os error 98)" occurs when you try to bind a TCP or UDP socket to a port that is already in use by another process or socket.

## Description

Only one process can bind to a specific IP:port combination at a time (unless `SO_REUSEADDR` or `SO_REUSEPORT` is set). When you try to bind to a port that's already taken, the OS returns error code 98 (`EADDRINUSE`). This is common when:

- Restarting a server without properly closing the old socket.
- Running multiple instances of the same server.
- The old socket is in `TIME_WAIT` state after closing.

Common scenarios:

- **Server restart** — previous instance didn't shut down cleanly.
- **Multiple instances** — running two copies of the same server.
- **TIME_WAIT state** — port is "occupied" after connection closes.
- **Wrong user** — another user's process is using the port.

## Common Causes

```rust
use std::net::TcpListener;

// Cause 1: Server already running
let listener = TcpListener::bind("0.0.0.0:8080")?; // port 8080 taken

// Cause 2: Previous instance didn't shut down
// Server was killed, port is in TIME_WAIT
let listener = TcpListener::bind("0.0.0.0:8080")?;

// Cause 3: Multiple instances
let listener1 = TcpListener::bind("0.0.0.0:8080")?;
let listener2 = TcpListener::bind("0.0.0.0:8080")?; // fails

// Cause 4: Another application using the port
let listener = TcpListener::bind("0.0.0.0:80")?; // nginx might be on 80
```

## Solutions

### Fix 1: Use SO_REUSEADDR to allow port reuse

```rust
use std::net::TcpListener;
use socket2::{Domain, Protocol, Socket, Type};
use std::net::SocketAddr;

fn bind_with_reuse(addr: &str) -> std::io::Result<TcpListener> {
    let addr: SocketAddr = addr.parse()?;
    let socket = Socket::new(Domain::IPV4, Type::STREAM, Some(Protocol::TCP))?;
    socket.set_reuse_address(true)?;
    socket.set_nonblocking(true)?;
    socket.bind(&addr.into())?;
    socket.listen(128)?;
    Ok(TcpListener::from(socket))
}

fn main() -> std::io::Result<()> {
    let listener = bind_with_reuse("0.0.0.0:8080")?;
    println!("Listening on {}", listener.local_addr()?);
    Ok(())
}
```

### Fix 2: Use a different port

```rust
use std::net::TcpListener;

fn find_available_port(start: u16) -> Option<u16> {
    for port in start..65535 {
        let addr = format!("0.0.0.0:{}", port);
        if TcpListener::bind(&addr).is_ok() {
            return Some(port);
        }
    }
    None
}

fn main() {
    match find_available_port(8080) {
        Some(port) => println!("Available port: {}", port),
        None => eprintln!("No available ports found"),
    }
}
```

### Fix 3: Wait for TIME_WAIT to expire

```rust
use std::net::TcpListener;
use std::thread;
use std::time::Duration;

fn bind_with_retry(addr: &str, max_retries: u32) -> std::io::Result<TcpListener> {
    for attempt in 0..max_retries {
        match TcpListener::bind(addr) {
            Ok(listener) => return Ok(listener),
            Err(e) => {
                eprintln!("Attempt {}: {}", attempt + 1, e);
                thread::sleep(Duration::from_secs(1));
            }
        }
    }
    Err(std::io::Error::new(
        std::io::ErrorKind::AddrInUse,
        "port still in use after retries",
    ))
}
```

### Fix 4: Kill the old process using the port

```rust
use std::process::Command;

fn kill_process_on_port(port: u16) -> std::io::Result<()> {
    let output = Command::new("lsof")
        .args(&["-ti", &format!(":{}", port)])
        .output()?;

    let pids = String::from_utf8_lossy(&output.stdout);
    for pid in pids.lines() {
        if !pid.is_empty() {
            Command::new("kill")
                .args(&["-9", pid])
                .output()?;
            println!("Killed process {} on port {}", pid, port);
        }
    }
    Ok(())
}

fn main() -> std::io::Result<()> {
    kill_process_on_port(8080)?;
    let listener = std::net::TcpListener::bind("0.0.0.0:8080")?;
    println!("Listening on {}", listener.local_addr()?);
    Ok(())
}
```

## Examples

```rust
use std::net::TcpListener;

fn main() {
    let _listener1 = TcpListener::bind("0.0.0.0:8080").unwrap();
    let _listener2 = TcpListener::bind("0.0.0.0:8080").unwrap(); // fails
}
```

Output:
```
thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: Os { code: 98, kind: AddrInUse, message: "Address already in use" }'
```

## Related Errors

- [Address Not Available]({{< relref "/languages/rust/address-not-available" >}}) — cannot assign requested address.
- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — no one listening on the port.
- [Broken Pipe]({{< relref "/languages/rust/broken-pipe" >}}) — write to closed pipe.
