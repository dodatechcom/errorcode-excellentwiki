---
title: "[Solution] Actix WebSocket Error — How to Fix"
description: "Fix Actix WebSocket errors. Resolve WebSocket connection, upgrade, and message handling issues."
frameworks: ["actix"]
error-types: ["websocket-error"]
severities: ["error"]
weight: 5
comments: true
---

An Actix WebSocket error occurs when WebSocket connections fail to establish or maintain properly.

## Why It Happens

WebSocket errors happen due to failed HTTP upgrades, incorrect protocol handling, or message deserialization issues.

## Common Error Messages

```
WebSocket connection error
```

```
upgrade error
```

```
failed to read frame
```

```
connection reset by peer
```

## How to Fix It

### 1. Use WebSocket Handler

Set up WebSocket properly.

```rust
use actix_web::{web, HttpRequest, HttpResponse};
use actix_ws::Message;

async fn ws_handler(req: HttpRequest, body: web::Payload) -> Result<HttpResponse, actix_web::Error> {
    let (response, mut session, mut msg_stream) = actix_ws::handle(&req, body)?;
    actix_rt::spawn(async move {
        while let Some(Ok(msg)) = msg_stream.recv().await {
            match msg {
                Message::Text(text) => {
                    session.text(text).await.unwrap();
                }
                Message::Ping(bytes) => {
                    session.pong(&bytes).await.unwrap();
                }
                _ => break,
            }
        }
    });
    Ok(response)
}
```

### 2. Handle Connection Errors

Check for WebSocket errors.

```rust
while let Some(Ok(msg)) = msg_stream.recv().await {
    match msg {
        Message::Text(text) => println!("Received: {}", text),
        Message::Binary(bin) => println!("Binary: {} bytes", bin.len()),
        Message::Ping(bytes) => session.pong(&bytes).await?,
        Message::Close(reason) => {
            session.close(reason).await?;
            break;
        }
        _ => {}
    }
}
```

### 3. Use Ping/Pong for Keep-Alive

Detect dead connections.

```rust
let heartbeat = actix_rt::spawn(async move {
    let mut interval = time::interval(Duration::from_secs(30));
    loop {
        interval.tick().await;
        if session.ping(b"").await.is_err() {
            break;
        }
    }
});
```

### 4. Broadcast to Multiple Clients

Manage multiple connections.

```rust
use std::sync::Arc;
use tokio::sync::broadcast;

let (tx, _) = broadcast::channel::<String>(100);
```

## Common Scenarios

**Scenario 1: Connection fails to upgrade.**
Check WebSocket handler registration.

**Scenario 2: Messages not received.**
Check message handling loop.

## Prevent It

1. **Always handle connection close.**


2. **Use ping/pong for keep-alive.**


3. **Set appropriate timeouts.**


