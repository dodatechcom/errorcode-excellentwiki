---
title: "[Solution] FastAPI WebSocket Accept Error Code"
description: "Fix FastAPI WebSocket accept errors when connections are rejected with specific close codes or reasons."
frameworks: ["fastapi"]
error-types: ["connection-error"]
severities: ["error"]
---

When accepting WebSocket connections in FastAPI, the server may reject connections with specific close codes.

## Common Causes

- Connection rejected due to missing authentication
- WebSocket protocol version mismatch
- Server at maximum connection capacity
- Subprotocol negotiation failed
- Client sent invalid handshake headers

## How to Fix

### Handle Accept Rejection

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    token = websocket.headers.get("authorization")
    if not token:
        await websocket.close(code=4001, reason="Missing token")
        return
    await websocket.accept()
```

### Limit Connection Capacity

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()
MAX_CONNECTIONS = 100
connection_count = 0

@app.websocket("/ws")
async def limited_ws(websocket: WebSocket):
    global connection_count
    if connection_count >= MAX_CONNECTIONS:
        await websocket.close(code=1013, reason="Server busy")
        return
    await websocket.accept()
    connection_count += 1
    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Echo: {data}")
    except WebSocketDisconnect:
        connection_count -= 1
```

### Common WebSocket Close Codes

```text
1000 - Normal closure
1001 - Going away
1002 - Protocol error
1003 - Unsupported data
1008 - Policy violation
1011 - Server error
1013 - Try again later
4001 - Custom: authentication required
4003 - Custom: forbidden
```

## Examples

The client receives a close frame with the specified code and reason if the connection is rejected.
