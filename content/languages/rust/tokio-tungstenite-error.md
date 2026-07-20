---
title: "[Solution] tokio-tungstenite WebSocket Error Fix"
description: "Fix tokio-tungstenite async WebSocket errors. Handle async connection, message handling, and reconnection."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Tokio Tungstenite Error

Tokio tungstenite errors occur when using `tokio-tungstenite` for WebSocket — connection and protocol errors.

## Common Causes

```rust
// Connection failure
let (ws_stream, _) = connect_async("ws://localhost:9999").await?;

// Sending on closed connection
sink.send(Message::Text("hello".into())).await?;
```

## How to Fix

1. **Handle connection errors**

```rust
use tokio_tungstenite::connect_async;

match connect_async("ws://echo.websocket.org").await {
    Ok((ws, _)) => println!("Connected"),
    Err(e) => eprintln!("Connection failed: {}", e),
}
```

2. **Check connection state**

```rust
use futures::{SinkExt, StreamExt};

let (mut write, mut read) = ws_stream.split();

// Send messages
write.send(Message::Text("hello".into())).await?;

// Read messages
while let Some(msg) = read.next().await {
    match msg {
        Ok(Message::Text(text)) => println!("Received: {}", text),
        Ok(Message::Close(_)) => break,
        Err(e) => eprintln!("Error: {}", e),
        _ => {}
    }
}
```

3. **Handle ping/pong**

```rust
use tokio_tungstenite::tungstenite::Message;

match msg {
    Ok(Message::Ping(data)) => {
        write.send(Message::Pong(data)).await?;
    }
    _ => {}
}
```

## Examples

```rust
use futures::{SinkExt, StreamExt};
use tokio_tungstenite::{connect_async, tungstenite::Message};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let (mut ws, _) = connect_async("ws://echo.websocket.org").await?;

    ws.send(Message::Text("Hello WebSocket!".into())).await?;

    if let Some(Ok(msg)) = ws.next().await {
        println!("Response: {}", msg);
    }
    Ok(())
}
```

## Related Errors

- [H2 Error]({{< relref "/languages/rust/h2-error" >}}) — HTTP/2
- [Quinn Error]({{< relref "/languages/rust/quinn-error" >}}) — QUIC
- [Tokio Error]({{< relref "/languages/rust/tokio-error" >}}) — tokio runtime
