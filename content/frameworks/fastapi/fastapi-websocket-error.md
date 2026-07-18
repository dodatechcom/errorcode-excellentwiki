---
title: "[Solution] FastAPI WebSocket Error — How to Fix"
description: "Fix FastAPI WebSocket errors. Resolve connection failures, handshake issues, and protocol errors."
frameworks: ["fastapi"]
error-types: ["websocket-error"]
severities: ["error"]
weight: 5
comments: true
---

A FastAPI WebSocket error occurs when WebSocket connections fail to establish, maintain, or close properly.

## Why It Happens

WebSocket errors happen due to incorrect upgrade headers, authentication failures, timeout issues, or protocol mismatches.

## Common Error Messages

```
WebSocketDisconnect: connection closed
```

```
ValueError: Not a valid websocket scope
```

```
WebSocketException: could not accept websocket
```

```
StarletteWebSocketException: WebSocket connection failed
```

## How to Fix It

### 1. Implement WebSocket Endpoint

Create a proper WebSocket endpoint.

```python
from fastapi import WebSocket, WebSocketDisconnect

class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for conn in self.active_connections:
            await conn.send_text(message)

manager = ConnectionManager()

@app.websocket('/ws/{client_id}')
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f'{client_id}: {data}')
    except WebSocketDisconnect:
        manager.disconnect(websocket)
```

### 2. Authenticate WebSocket Connections

Add auth to WebSocket endpoints.

```python
@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket, token: str = Query(...)):
    user = await verify_token(token)
    if not user:
        await websocket.close(code=1008)
        return
    await websocket.accept()
```

### 3. Handle Connection Lifecycle

Implement proper connect/disconnect.

```python
@app.websocket('/ws/{room_id}')
async def websocket_endpoint(websocket: WebSocket, room_id: str):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            await process_message(room_id, data)
    except WebSocketDisconnect:
        await handle_disconnect(room_id)
```

### 4. Add Error Handling

Handle WebSocket errors gracefully.

```python
@app.websocket('/ws')
async def websocket_endpoint(websocket: WebSocket):
    try:
        await websocket.accept()
        while True:
            data = await websocket.receive_text()
            await process(data)
    except WebSocketDisconnect:
        pass
    except Exception:
        await websocket.close(code=1011)
```

## Common Scenarios

**Scenario 1: Connection immediately closes.**
Check authentication and upgrade headers.

**Scenario 2: Messages not received.**
Verify protocol and message format.

**Scenario 3: Connection drops under load.**
Implement reconnection logic.

## Prevent It

1. **Use connection pooling.**
Limit concurrent connections.

2. **Add heartbeat messages.**
Send periodic pings.

3. **Test with WebSocket clients.**
Use `websocat` for testing.

