---
title: "[Solution] Rust Timed Out — Operation Timed Out"
description: "Fix Rust timed out error. Learn why network operations time out and how to configure and handle timeouts properly."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
tags: ["timeout", "timed-out", "network", "connection", "io"]
weight: 5
---

# Timed Out — Operation Timed Out

An IO error with the message "Timed out (os error 110)" occurs when a network operation exceeds its configured timeout duration. The operation was started but didn't complete within the allowed time.

## Description

Timeouts prevent your program from hanging indefinitely when a network operation is slow or unresponsive. Error code 110 (`ETIMEDOUT`) means:

- TCP connection attempt took too long.
- Socket read/write exceeded the timeout.
- Keep-alive probe failed (connection is dead).

Common scenarios:

- **Slow server** — server takes too long to respond.
- **Network congestion** — packets are delayed or lost.
- **DNS resolution** — DNS server is unresponsive.
- **Firewall dropping packets** — SYN packets silently dropped.
- **Dead connection** — server crashed without sending FIN.

## Common Causes

```rust
use std::net::TcpStream;
use std::time::Duration;

// Cause 1: Connection timeout
let stream = TcpStream::connect_timeout(
    &"10.0.0.1:8080".parse()?,
    Duration::from_secs(5),
)?;

// Cause 2: Read timeout
stream.set_read_timeout(Some(Duration::from_secs(3)))?;
let mut buffer = [0; 1024];
stream.read(&mut buffer)?; // may time out

// Cause 3: Write timeout
stream.set_write_timeout(Some(Duration::from_secs(3)))?;
stream.write_all(b"data")?; // may time out

// Cause 4: DNS resolution hangs
use std::net::ToSocketAddrs;
let addrs = "very-slow-dns-server.example.com:80".to_socket_addrs()?;
```

## Solutions

### Fix 1: Configure appropriate timeouts

```rust
use std::net::TcpStream;
use std::time::Duration;

fn connect_with_timeout(addr: &str, timeout_secs: u64) -> std::io::Result<TcpStream> {
    let addr = addr.to_socket_addrs()?.next().unwrap();
    let stream = TcpStream::connect_timeout(
        &addr,
        Duration::from_secs(timeout_secs),
    )?;

    // Also set read/write timeouts
    stream.set_read_timeout(Some(Duration::from_secs(timeout_secs * 2)))?;
    stream.set_write_timeout(Some(Duration::from_secs(timeout_secs)))?;

    Ok(stream)
}

fn main() -> std::io::Result<()> {
    let stream = connect_with_timeout("example.com:80", 10)?;
    println!("Connected to {}", stream.peer_addr()?);
    Ok(())
}
```

### Fix 2: Use async with tokio timeout

```rust
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpStream;
use tokio::time::{timeout, Duration};

#[tokio::main]
async fn main() {
    let addr = "example.com:80";

    match timeout(Duration::from_secs(10), TcpStream::connect(addr)).await {
        Ok(Ok(mut stream)) => {
            match timeout(Duration::from_secs(5), stream.write_all(b"GET / HTTP/1.0\r\n\r\n")).await {
                Ok(Ok(())) => {
                    let mut buffer = vec![0; 4096];
                    match timeout(Duration::from_secs(5), stream.read(&mut buffer)).await {
                        Ok(Ok(n)) => println!("Read {} bytes", n),
                        Ok(Err(e)) => eprintln!("Read error: {}", e),
                        Err(_) => eprintln!("Read timed out"),
                    }
                }
                Ok(Err(e)) => eprintln!("Write error: {}", e),
                Err(_) => eprintln!("Write timed out"),
            }
        }
        Ok(Err(e)) => eprintln!("Connection failed: {}", e),
        Err(_) => eprintln!("Connection timed out"),
    }
}
```

### Fix 3: Implement retry with exponential backoff

```rust
use std::net::TcpStream;
use std::thread;
use std::time::{Duration, Instant};

fn connect_with_backoff(
    addr: &str,
    initial_timeout: Duration,
    max_retries: u32,
) -> std::io::Result<TcpStream> {
    let mut timeout = initial_timeout;

    for attempt in 0..max_retries {
        let start = Instant::now();

        match TcpStream::connect_timeout(
            &addr.to_socket_addrs()?.next().unwrap(),
            timeout,
        ) {
            Ok(stream) => return Ok(stream),
            Err(e) => {
                let elapsed = start.elapsed();
                eprintln!("Attempt {} failed after {:?}: {}", attempt + 1, elapsed, e);
                timeout = (timeout * 2).min(Duration::from_secs(60));
                thread::sleep(Duration::from_millis(100));
            }
        }
    }

    Err(std::io::Error::new(
        std::io::ErrorKind::TimedOut,
        "connection timed out after all retries",
    ))
}
```

### Fix 4: Use reqwest with configurable timeouts

```rust
use reqwest::blocking::Client;
use std::time::Duration;

fn fetch_with_timeout(url: &str) -> Result<String, reqwest::Error> {
    let client = Client::builder()
        .connect_timeout(Duration::from_secs(10))
        .timeout(Duration::from_secs(30))
        .build()?;

    let response = client.get(url).send()?;
    let body = response.text()?;
    Ok(body)
}

fn main() {
    match fetch_with_timeout("https://httpbin.org/delay/5") {
        Ok(body) => println!("Response: {}", body),
        Err(e) => eprintln!("Error: {}", e),
    }
}
```

## Examples

```rust
use std::net::TcpStream;
use std::time::Duration;

fn main() -> std::io::Result<()> {
    let addr = "192.168.1.1:8080".parse()?;
    let stream = TcpStream::connect_timeout(&addr, Duration::from_secs(3))?;
    println!("Connected!");
    Ok(())
}
```

Output (if server is unreachable):
```
Error: Timed out (os error 110)
```

## Related Errors

- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — server actively rejects connection.
- [Connection Reset]({{< relref "/languages/rust/connection-reset" >}}) — connection forcibly closed.
- [Not Connected]({{< relref "/languages/rust/not-connected" >}}) — socket is not connected.
