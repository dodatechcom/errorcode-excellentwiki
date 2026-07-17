---
title: "[Solution] Rust Timed Out — Operation Timed Out"
description: "Fix Rust timed out error. Learn why network operations time out and how to configure timeouts, retry, and use async patterns."
languages: ["rust"]
error_types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Timed Out — Operation Timed Out

An IO error with the message "Timed out (os error 110)" occurs when a network operation exceeds its configured timeout duration.

## Description

Timeouts prevent your program from hanging when a network operation is slow or unresponsive. Error code 110 (`ETIMEDOUT`) means the TCP connection, read, or write didn't complete within the allowed time.

Common scenarios:

- **Slow server** — response takes too long.
- **Network congestion** — packets delayed or dropped.
- **Firewall dropping SYN** — connection attempt never completes.
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
let mut buf = [0u8; 1024];
stream.read(&mut buf)?;

// Cause 3: Write timeout
stream.set_write_timeout(Some(Duration::from_secs(3)))?;
stream.write_all(b"data")?;

// Cause 4: DNS hangs
use std::net::ToSocketAddrs;
let addrs = "very-slow-dns.example.com:80".to_socket_addrs()?;
```

## Solutions

### Fix 1: Configure appropriate timeouts

```rust
use std::net::TcpStream;
use std::time::Duration;

fn connect_with_timeout(addr: &str, secs: u64) -> std::io::Result<TcpStream> {
    let addr = addr.to_socket_addrs()?.next().unwrap();
    let stream = TcpStream::connect_timeout(&addr, Duration::from_secs(secs))?;
    stream.set_read_timeout(Some(Duration::from_secs(secs * 2)))?;
    stream.set_write_timeout(Some(Duration::from_secs(secs)))?;
    Ok(stream)
}
```

### Fix 2: Use tokio timeout

```rust
use tokio::io::{AsyncReadExt, AsyncWriteExt};
use tokio::net::TcpStream;
use tokio::time::{timeout, Duration};

#[tokio::main]
async fn main() {
    match timeout(Duration::from_secs(10), TcpStream::connect("example.com:80")).await {
        Ok(Ok(mut stream)) => {
            let mut buf = vec![0u8; 4096];
            match timeout(Duration::from_secs(5), stream.read(&mut buf)).await {
                Ok(Ok(n)) => println!("Read {} bytes", n),
                Ok(Err(e)) => eprintln!("Read error: {}", e),
                Err(_) => eprintln!("Read timed out"),
            }
        }
        Ok(Err(e)) => eprintln!("Connect failed: {}", e),
        Err(_) => eprintln!("Connect timed out"),
    }
}
```

### Fix 3: Retry with backoff

```rust
use std::net::TcpStream;
use std::thread;
use std::time::{Duration, Instant};

fn connect_backoff(addr: &str, timeout: Duration, retries: u32) -> std::io::Result<TcpStream> {
    let mut timeout = timeout;
    for attempt in 0..retries {
        let start = Instant::now();
        match TcpStream::connect_timeout(
            &addr.to_socket_addrs()?.next().unwrap(),
            timeout,
        ) {
            Ok(s) => return Ok(s),
            Err(e) => {
                eprintln!("Attempt {} ({:?}): {}", attempt + 1, start.elapsed(), e);
                timeout = (timeout * 2).min(Duration::from_secs(60));
                thread::sleep(Duration::from_millis(100));
            }
        }
    }
    Err(std::io::Error::new(std::io::ErrorKind::TimedOut, "all retries failed"))
}
```

### Fix 4: Use reqwest with timeout

```rust
use reqwest::blocking::Client;
use std::time::Duration;

fn fetch(url: &str) -> Result<String, reqwest::Error> {
    let client = Client::builder()
        .connect_timeout(Duration::from_secs(10))
        .timeout(Duration::from_secs(30))
        .build()?;
    let body = client.get(url).send()?.text()?;
    Ok(body)
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

Output:
```
Error: Timed out (os error 110)
```

## Related Errors

- [Connection Refused]({{< relref "/languages/rust/connection-refused-2" >}}) — server actively rejects.
- [Connection Reset]({{< relref "/languages/rust/connection-reset-2" >}}) — connection forcibly closed.
- [Not Connected]({{< relref "/languages/rust/not-connected-2" >}}) — socket not connected.
