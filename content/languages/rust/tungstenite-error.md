---
title: "[Solution] tungstenite WebSocket Error Fix"
description: "Fix tungstenite WebSocket errors. Handle handshake, framing, and protocol negotiation."
languages: ["rust"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# tungstenite WebSocket Error

The `tungstenite` crate provides a lightweight, synchronous WebSocket implementation for Rust. Errors occur during the WebSocket handshake (HTTP upgrade negotiation), during message framing/serialization, or when the peer closes the connection unexpectedly. These errors surface as `tungstenite::Error` variants like `ConnectionClosed`, `AlreadyClosed`, `Capacity`, `Utf8`, and `Tls`.

## Common Causes

```rust
use tungstenite::{connect, Message};
use std::net::TcpStream;

// 1. Connecting to a non-WebSocket endpoint or wrong port
let (mut socket, _response) =
    connect("ws://localhost:9999").expect("Failed to connect");
// Fails with Error::Io if nothing is listening

// 2. Sending after the connection has been closed
let (mut socket, _) = connect("ws://echo.websocket.org").expect("connect");
drop(socket); // or the peer sent a Close frame
socket.write_message(Message::Text("hello".into()));
// Fails with Error::AlreadyClosed

// 3. Payload too large for the default buffer
let huge = vec![0u8; 64 * 1024 * 1024]; // 64 MB
socket.write_message(Message::Binary(huge));
// Fails with Error::Capacity if the message exceeds MaxFrameSize

// 4. Receiving non-UTF-8 text
// Peer sends invalid UTF-8 in a Text frame → Error::Utf8
```

## How to Fix

1. **Handle connection errors with proper error matching**

```rust
use tungstenite::{connect, Error};

match connect("ws://localhost:9001") {
    Ok((socket, response)) => {
        println!("Connected: {}", response.status());
    }
    Err(Error::Io(e)) => eprintln!("Connection failed: {}", e),
    Err(Error::Tls(e)) => eprintln!("TLS error: {}", e),
    Err(e) => eprintln!("Other error: {}", e),
}
```

2. **Increase the max frame size before connecting**

```rust
use tungstenite::protocol::WebSocketConfig;
use tungstenite::connect;

let config = WebSocketConfig {
    max_send_queue: Some(1 << 20), // 1 MB send queue
    max_frame_size: Some(16 << 20), // 16 MB max frame
    max_message_size: Some(32 << 20),
    ..Default::default()
};

let (mut socket, _) = connect("ws://localhost:9001")?;
socket.set_config(config);
```

3. **Gracefully handle close frames and check connection state**

```rust
use tungstenite::{Message, protocol::frame::CloseFrame};

loop {
    match socket.read_message() {
        Ok(Message::Text(text)) => println!("Text: {}", text),
        Ok(Message::Binary(data)) => println!("Binary: {} bytes", data.len()),
        Ok(Message::Close(_)) => {
            println!("Server initiated close");
            break;
        }
        Ok(Message::Ping(data)) => {
            socket.write_message(Message::Pong(data))?;
        }
        Err(tungstenite::Error::ConnectionClosed) => break,
        Err(tungstenite::Error::AlreadyClosed) => break,
        Err(e) => eprintln!("Read error: {}", e),
        _ => {}
    }
}
```

4. **Use tungstenite with tokio via tokio-tungstenite for async contexts**

```rust
// For async applications, use tokio-tungstenite instead
// tokio-tungstenite wraps tungstenite with async I/O
use tokio_tungstenite::connect_async;

let (ws_stream, _) = connect_async("ws://localhost:9001").await?;
// ws_stream implements Stream + Sink for async message handling
```

## Examples

```rust
use tungstenite::{connect, Message};
use tungstenite::protocol::WebSocketConfig;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = WebSocketConfig {
        max_frame_size: Some(8 * 1024 * 1024),
        ..Default::default()
    };

    let (mut socket, response) = connect("ws://echo.websocket.org")?;
    println!("Connected with status: {}", response.status());

    socket.write_message(Message::Text("Hello, WebSocket!".into()))?;

    let msg = socket.read_message()?;
    match msg {
        Message::Text(text) => println!("Echo: {}", text),
        Message::Close(_) => println!("Connection closed by server"),
        _ => {}
    }

    // Send a close frame to cleanly shut down
    socket.close(None)?;
    Ok(())
}
```

## Related Errors

- [H2 Error]({{< relref "/languages/rust/h2-error" >}}) — HTTP/2 framing
- [Hyper Error]({{< relref "/languages/rust/hyper-error" >}}) — HTTP layer
- [Connection Refused]({{< relref "/languages/rust/connection-refused" >}}) — network errors
