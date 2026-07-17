---
title: "[Solution] Rust Address Already in Use — Port Binding Conflict"
description: "Fix Rust address already in use error. Learn why port binding fails and how to use SO_REUSEADDR, retry, or kill old processes."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Address Already in Use — Port Binding Conflict

An IO error with the message "Address already in use (os error 98)" occurs when you try to bind a socket to a port that's already taken.

## Description

Only one process can bind to a specific IP:port at a time (without `SO_REUSEADDR`/`SO_REUSEPORT`). Error code 98 (`EADDRINUSE`) means another process or socket is using that port. The port may be actively in use or in `TIME_WAIT` state after a recent connection close.

Common scenarios:

- **Server restart** — previous instance didn't shut down cleanly.
- **Multiple instances** — two copies of the same server.
- **TIME_WAIT** — port in lingering state after close.
- **Other application** — nginx on port 80, etc.

## Common Causes

```rust
use std::net::TcpListener;

// Cause 1: Server already running
let listener = TcpListener::bind("0.0.0.0:8080")?; // port taken

// Cause 2: Previous instance still in TIME_WAIT
let listener = TcpListener::bind("0.0.0.0:8080")?;

// Cause 3: Two instances
let l1 = TcpListener::bind("0.0.0.0:8080")?;
let l2 = TcpListener::bind("0.0.0.0:8080")?; // fails

// Cause 4: Another application
let listener = TcpListener::bind("0.0.0.0:80")?; // nginx might be on 80
```

## Solutions

### Fix 1: Use SO_REUSEADDR

```rust
use std::net::TcpListener;
use socket2::{Domain, Protocol, Socket, Type};
use std::net::SocketAddr;

fn bind_reuse(addr: &str) -> std::io::Result<TcpListener> {
    let addr: SocketAddr = addr.parse()?;
    let socket = Socket::new(Domain::IPV4, Type::STREAM, Some(Protocol::TCP))?;
    socket.set_reuse_address(true)?;
    socket.set_nonblocking(true)?;
    socket.bind(&addr.into())?;
    socket.listen(128)?;
    Ok(TcpListener::from(socket))
}
```

### Fix 2: Find an available port

```rust
use std::net::TcpListener;

fn find_port(start: u16) -> Option<u16> {
    for port in start..65535 {
        if TcpListener::bind(format!("0.0.0.0:{}", port)).is_ok() {
            return Some(port);
        }
    }
    None
}

fn main() {
    match find_port(8080) {
        Some(port) => println!("Available: {}", port),
        None => eprintln!("No ports available"),
    }
}
```

### Fix 3: Retry with delay

```rust
use std::net::TcpListener;
use std::thread;
use std::time::Duration;

fn bind_retry(addr: &str, retries: u32) -> std::io::Result<TcpListener> {
    for attempt in 0..retries {
        match TcpListener::bind(addr) {
            Ok(l) => return Ok(l),
            Err(_) => thread::sleep(Duration::from_secs(1)),
        }
    }
    Err(std::io::Error::new(std::io::ErrorKind::AddrInUse, "port in use"))
}
```

### Fix 4: Kill the old process

```rust
use std::process::Command;

fn kill_on_port(port: u16) -> std::io::Result<()> {
    let output = Command::new("lsof")
        .args(&["-ti", &format!(":{}", port)])
        .output()?;
    for pid in String::from_utf8_lossy(&output.stdout).lines() {
        if !pid.is_empty() {
            Command::new("kill").args(&["-9", pid]).output()?;
            println!("Killed PID {}", pid);
        }
    }
    Ok(())
}
```

## Examples

```rust
use std::net::TcpListener;

fn main() {
    let _l1 = TcpListener::bind("0.0.0.0:8080").unwrap();
    let _l2 = TcpListener::bind("0.0.0.0:8080").unwrap();
}
```

Output:
```
thread 'main' panicked at 'called `Result::unwrap()` on an `Err` value: Os { code: 98, kind: AddrInUse, message: "Address already in use" }'
```

## Related Errors

- [Address Not Available]({{< relref "/languages/rust/address-not-available-2" >}}) — cannot assign requested address.
- [Connection Refused]({{< relref "/languages/rust/connection-refused-2" >}}) — no one listening on port.
- [Broken Pipe]({{< relref "/languages/rust/broken-pipe-2" >}}) — write to closed pipe.
