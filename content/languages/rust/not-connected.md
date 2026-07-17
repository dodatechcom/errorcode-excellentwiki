---
title: "[Solution] Rust Not Connected — Socket Not Connected Error"
description: "Fix Rust not connected error. Learn why socket operations fail with 'Not connected' and how to ensure sockets are properly connected."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Not Connected — Socket Not Connected Error

An IO error with the message "Not connected (os error 107)" occurs when you try to perform an operation on a socket that is not currently connected. Error code 107 (`ENOTCONN`) means the socket exists but has no established connection.

## Description

TCP sockets must be connected before reading or writing. This error occurs when:

- You try to read/write on a socket before `connect()` succeeds.
- The socket was connected but the connection was closed.
- You're using a socket created with `socket()` but never called `connect()`.
- The socket was created for listening (via `bind`/`listen`) but you try to read data.

Common scenarios:

- **Using unconnected socket** — reading from a socket before connecting.
- **After connection close** — using a socket after the connection drops.
- **Listening socket misuse** — treating a server socket as a client socket.
- **Half-closed connection** — reading after peer has closed their end.

## Common Causes

```rust
use std::net::TcpStream;
use std::io::{Read, Write};

// Cause 1: Using socket before connecting
use std::net::UdpSocket;
let socket = UdpSocket::bind("0.0.0.0:0")?;
let mut buf = [0u8; 1024];
socket.recv(&mut buf)?; // Error: not connected (UDP must connect first for recv)

// Cause 2: Using stream after connection close
let stream = TcpStream::connect("server:8080")?;
drop(stream); // connection closed
let mut buf = [0u8; 1024];
stream.read(&mut buf)?; // Error: not connected

// Cause 3: Reading from a server/listening socket
let listener = std::net::TcpListener::bind("0.0.0.0:8080")?;
// listener is for accepting, not reading

// Cause 4: Using peer_addr on unconnected socket
let socket = TcpStream::connect("server:8080")?;
drop(socket);
socket.peer_addr()?; // Error: not connected
```

## Solutions

### Fix 1: Ensure socket is connected before use

```rust
use std::net::TcpStream;
use std::io::{Read, Write};

// Wrong
let stream = TcpStream::connect("server:8080")?;
drop(stream);
let mut buf = [0u8; 1024];
stream.read(&mut buf)?; // not connected

// Correct — reconnect if needed
fn ensure_connected(addr: &str) -> std::io::Result<TcpStream> {
    TcpStream::connect(addr)
}

let stream = ensure_connected("server:8080")?;
let mut buf = [0u8; 1024];
stream.read(&mut buf)?;
```

### Fix 2: Check connection status before operations

```rust
use std::net::TcpStream;
use std::io;

fn is_connected(stream: &TcpStream) -> bool {
    stream.peer_addr().is_ok()
}

fn main() -> io::Result<()> {
    let stream = TcpStream::connect("server:8080")?;

    if is_connected(&stream) {
        let mut buf = [0u8; 1024];
        stream.read(&mut buf)?;
    } else {
        eprintln!("Socket is not connected");
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
        let mut stream = stream?; // This is a connected socket
        let mut buf = [0u8; 1024];
        let n = stream.read(&mut buf)?;
        stream.write_all(&buf[..n])?;
    }

    Ok(())
}
```

### Fix 4: Use reconnect pattern for resilient connections

```rust
use std::net::TcpStream;
use std::io::{Read, Write};
use std::time::Duration;

struct Connection {
    addr: String,
    stream: Option<TcpStream>,
}

impl Connection {
    fn new(addr: &str) -> Self {
        Connection {
            addr: addr.to_string(),
            stream: None,
        }
    }

    fn ensure_connected(&mut self) -> std::io::Result<&TcpStream> {
        if let Some(ref stream) = self.stream {
            if stream.peer_addr().is_ok() {
                return Ok(stream);
            }
        }
        let stream = TcpStream::connect(&self.addr)?;
        stream.set_read_timeout(Some(Duration::from_secs(30)))?;
        self.stream = Some(stream);
        Ok(self.stream.as_ref().unwrap())
    }

    fn send(&mut self, data: &[u8]) -> std::io::Result<Vec<u8>> {
        let stream = self.ensure_connected()?;
        let mut stream = stream.try_clone()?;
        stream.write_all(data)?;
        let mut response = Vec::new();
        stream.read_to_end(&mut response)?;
        Ok(response)
    }
}
```

## Examples

```rust
use std::net::UdpSocket;
use std::io;

fn main() -> io::Result<()> {
    let socket = UdpSocket::bind("0.0.0.0:0")?;

    // UDP socket must connect before recv
    socket.connect("127.0.0.1:8080")?;

    let mut buf = [0u8; 1024];
    match socket.recv(&mut buf) {
        Ok(n) => println!("Received {} bytes", n),
        Err(e) => eprintln!("Error: {}", e),
    }

    Ok(())
}
```

## Related Errors

- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — server actively rejects connection.
- [Connection Reset]({{< relref "/languages/rust/connection-reset" >}}) — connection forcibly closed by peer.
- [Timed Out]({{< relref "/languages/rust/timed-out" >}}) — connection attempt timed out.
