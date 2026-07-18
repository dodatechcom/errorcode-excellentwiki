---
title: "[Solution] Fiber WebSocket Error — How to Fix"
description: "Fix Fiber WebSocket errors. Resolve WebSocket connection, upgrade, and message handling issues."
frameworks: ["fiber"]
error-types: ["websocket-error"]
severities: ["error"]
weight: 5
comments: true
---

A Fiber WebSocket error occurs when WebSocket connections fail to establish or maintain properly.

## Why It Happens

WebSocket errors happen due to failed HTTP upgrades, connection drops, or message handling issues.

## Common Error Messages

```
websocket: invalid handshake
```

```
connection reset by peer
```

```
websocket: close 1006
```

```
unexpected EOF
```

## How to Fix It

### 1. Use WebSocket Handler

Set up WebSocket properly.

```go
import "github.com/gofiber/websocket/v2"

app.Get("/ws", websocket.New(func(c *websocket.Conn) {
    for {
        messageType, msg, err := c.ReadMessage()
        if err != nil {
            log.Printf("read error: %v", err)
            break
        }
        if err := c.WriteMessage(messageType, msg); err != nil {
            break
        }
    }
}))
```

### 2. Handle Connection Errors

Check for WebSocket errors.

```go
for {
    _, msg, err := c.ReadMessage()
    if err != nil {
        if websocket.IsCloseError(err, websocket.CloseNormalClosure, websocket.CloseGoingAway) {
            log.Println("client disconnected")
        } else {
            log.Printf("error: %v", err)
        }
        break
    }
}
```

### 3. Use Ping/Pong for Keep-Alive

Detect dead connections.

```go
c.SetPongHandler(func(appData string) error {
    c.SetReadDeadline(time.Now().Add(60 * time.Second))
    return nil
})

go func() {
    ticker := time.NewTicker(30 * time.Second)
    defer ticker.Stop()
    for range ticker.C {
        if err := c.WriteMessage(websocket.PingMessage, nil); err != nil {
            return
        }
    }
}()
```

### 4. Broadcast to Multiple Clients

Manage multiple connections.

```go
type Hub struct {
    clients    map[*websocket.Conn]bool
    broadcast  chan []byte
    register   chan *websocket.Conn
    unregister chan *websocket.Conn
}
```

## Common Scenarios

**Scenario 1: Connection fails to upgrade.**
Check Origin header.

**Scenario 2: Messages not received.**
Check read deadline.

## Prevent It

1. **Always handle connection close.**


2. **Use ping/pong for keep-alive.**


3. **Set read/write deadlines.**


