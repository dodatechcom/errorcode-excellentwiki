---
title: "[Solution] h2 HTTP/2 Error Fix"
description: "Fix h2 HTTP/2 errors. Handle connection preface, stream management, and flow control."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# H2 Error

H2 errors occur when using the `h2` crate for HTTP/2 protocol handling — connection errors, stream errors, and frame parsing issues.

## Common Causes

```rust
// Connection error
let client = h2::Client::connect("http://localhost:3000").await?;

// Stream error — sending on closed stream
let stream = client.ready().await?.send_request(request, false)?;

// Invalid frame
```

## How to Fix

1. **Handle connection errors**

```rust
use h2::client;

let tcp = tokio::net::TcpStream::connect("localhost:3000").await?;
let (client, h2_conn) = client::handshake(tcp).await?;
```

2. **Check stream state before sending**

```rust
let (response, body) = sender.send_request(request, end_of_stream)?;
```

## Examples

```rust
use h2::server;
use tokio::net::TcpListener;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let listener = TcpListener::bind("127.0.0.1:3000").await?;

    loop {
        let (socket, _) = listener.accept().await?;
        tokio::spawn(async move {
            let mut h2 = server::handshake(socket).await.unwrap();
            while let Some((req, mut send)) = h2.accept().await.unwrap() {
                let body = send.send_response(
                    http::Response::builder().body(()).unwrap(), false
                ).unwrap();
                // Handle request
            }
        });
    }
}
```

## Related Errors

- [Hyper Error]({{< relref "/languages/rust/hyper-error" >}}) — HTTP/1.1
- [HTTP Body Util Error]({{< relref "/languages/rust/http-body-util-error" >}}) — body handling
- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — network errors
