---
title: "[Solution] FastAPI WebSocket Subprotocol Error"
description: "Fix FastAPI WebSocket subprotocol negotiation errors when client and server fail to agree on a protocol."
frameworks: ["fastapi"]
error-types: ["connection-error"]
severities: ["error"]
---

When a WebSocket client specifies subprotocols like `graphql-ws` or `vite-hmr`, the server must accept or reject them during the handshake.

## Common Causes

- Server does not check the requested subprotocols during accept
- Client sends unsupported subprotocol name
- Multiple subprotocols sent but server does not iterate through them
- Missing `Sec-WebSocket-Protocol` header handling
- GraphQL or HMR connections fail due to subprotocol mismatch

## How to Fix

### Handle Subprotocol Negotiation

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    subprotocol = websocket.headers.get("sec-websocket-protocol")
    if subprotocol == "graphql-ws":
        await websocket.accept(subprotocols=["graphql-ws"])
    else:
        await websocket.accept()
```

## Examples

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def broken_ws(websocket: WebSocket):
    await websocket.accept()  # Does not negotiate subprotocol
```

The client sends `Sec-WebSocket-Protocol: graphql-ws` in the upgrade request. The server must pass this back:

```python
await websocket.accept(subprotocols=["graphql-ws"])
```
