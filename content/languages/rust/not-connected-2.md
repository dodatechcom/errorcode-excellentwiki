---
title: "[Solution] Rust Not Connected — Socket Not Connected Error"
description: "Fix Rust not connected error. Learn why socket operations fail with 'Not connected' and how to ensure sockets are properly connected."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Not Connected — Socket Not Connected Error

An IO error with the message "Not connected (os error 107)" occurs when you try to read or write on a socket that has no established connection.

## Description

TCP sockets must be connected before data transfer. Error code 107 (`ENOTCONN`) means the socket exists but isn't connected. This can happen with UDP sockets that haven't called `connect()`, or TCP sockets used after the connection dropped.

Common scenarios:

- **UDP recv without connect** — UDP must connect before `recv`.
- **Using closed stream** — reading from a dropped TcpStream.
- **Listening socket misuse** — treating a server socket as client.
- **Half-closed connection** — reading after peer closed their end.

## Common Causes

```rust
use std::net::UdpSocket;
use std::io::{Read, Write};

// Cause 1: UDP recv without connect
let socket = UdpSocket::bind("0.0.0.0:0")?;
let mut buf = [0u8; 1024];
socket.recv(&mut buf)?; // Error: not connected

// Cause 2: Using closed stream
let stream = std::net::TcpStream::connect("server:8080")?;
drop(stream);
let mut buf = [0u8; 1024];
// stream.read(&mut buf)?; // Error: not connected (can't use after drop)

// Cause 3: Listening socket misuse
let listener = std::net::TcpListener::bind("0.0.0.0:8080")?;
// listener is for accepting, not reading

// Cause 4: peer_addr on unconnected socket
let socket = std::net::TcpStream::connect("server:8080")?;
drop(socket);
// socket.peer_addr()?; // Error
```

## Solutions

### Fix 1: Ensure connection before use

```rust
use std::net::TcpStream;
use std::io::{Read, Write};

fn ensure_connected(addr: &str) -> std::io::Result<TcpStream> {
    TcpStream::connect(addr)
}

let stream = ensure_connected("server:8080")?;
let mut buf = [0u8; 1024];
stream.read(&mut buf)?;
```

### Fix 2: Check connection status

```rust
use std::net::TcpStream;

fn is_connected(stream: &TcpStream) -> bool {
    stream.peer_addr().is_ok()
}

fn main() -> std::io::Result<()> {
    let stream = TcpStream::connect("server:8080")?;
    if is_connected(&stream) {
        println!("Connected to {}", stream.peer_addr()?);
    }
    Ok(())
}
```

### Fix 3: Use accept() for server sockets

```rust
use std::net::TcpListener;
use std::io::{Read, Write};

fn main() -> std::io::Result<()> {
    let listener = TcpListener::bind("0.0.0.0:8080")?;
    for stream in listener.incoming() {
        let mut stream = stream?; // connected socket
        let mut buf = [0u8; 1024];
        let n = stream.read(&mut buf)?;
        stream.write_all(&buf[..n])?;
    }
    Ok(())
}
```

### Fix 4: Connect UDP before recv

```rust
use std::net::UdpSocket;

fn main() -> std::io::Result<()> {
    let socket = UdpSocket::bind("0.0.0.0:0")?;
    socket.connect("127.0.0.1:8080")?; // must connect first
    let mut buf = [0u8; 1024];
    match socket.recv(&mut buf) {
        Ok(n) => println!("Received {} bytes", n),
        Err(e) => eprintln!("Error: {}", e),
    }
    Ok(())
}
```

## Examples

```rust
use std::net::UdpSocket;

fn main() -> std::io::Result<()> {
    let socket = UdpSocket::bind("0.0.0.0:0")?;
    let mut buf = [0u8; 1024];
    socket.recv(&mut buf)?;
    Ok(())
}
```

Output:
```
Error: Not connected (os error 107)
```

## Related Errors

- [Connection Refused]({{< relref "/languages/rust/connection-refused-2" >}}) — server actively rejects.
- [Connection Reset]({{< relref "/languages/rust/connection-reset-2" >}}) — connection forcibly closed.
- [Timed Out]({{< relref "/languages/rust/timed-out-2" >}}) — connection timed out.
