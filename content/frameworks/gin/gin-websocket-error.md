---
title: "[Solution] Gin WebSocket Error — How to Fix"
description: "Fix Gin WebSocket errors. Resolve WebSocket connection, upgrade, and message handling issues."
frameworks: ["gin"]
error-types: ["websocket-error"]
severities: ["error"]
weight: 5
comments: true
---

A Gin WebSocket error occurs when WebSocket connections fail to establish or maintain properly.

## Why It Happens

WebSocket errors happen due to failed HTTP upgrades, incorrect Origin headers, connection drops, or message handling issues.

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

### 1. Use gorilla/websocket

Set up WebSocket with proper upgrader.

```go
import "github.com/gorilla/websocket"

var upgrader = websocket.Upgrader{
    CheckOrigin: func(r *http.Request) bool {
        return true
    },
}

func wsHandler(c *gin.Context) {
    conn, err := upgrader.Upgrade(c.Writer, c.Request, nil)
    if err != nil {
        log.Printf("upgrade error: %v", err)
        return
    }
    defer conn.Close()
}
```

### 2. Handle Connection Errors

Check for WebSocket errors.

```go
for {
    messageType, message, err := conn.ReadMessage()
    if err != nil {
        if websocket.IsCloseError(err, websocket.CloseNormalClosure, websocket.CloseGoingAway) {
            log.Println("client disconnected")
        } else {
            log.Printf("read error: %v", err)
        }
        break
    }
    // Process message
}
```

### 3. Use Ping/Pong for Keep-Alive

Detect dead connections.

```go
conn.SetPongHandler(func(string) error {
    conn.SetReadDeadline(time.Now().Add(60 * time.Second))
    return nil
})

go func() {
    ticker := time.NewTicker(30 * time.Second)
    defer ticker.Stop()
    for range ticker.C {
        if err := conn.WriteMessage(websocket.PingMessage, nil); err != nil {
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
Check Origin header in upgrader.

**Scenario 2: Messages not received.**
Check read deadline and ping/pong.

## Prevent It

1. **Always handle connection close.**


2. **Use ping/pong for keep-alive.**


3. **Set read/write deadlines.**


