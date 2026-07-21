---
title: "[Solution] FastAPI WebSocket Origin Check Error"
description: "Fix FastAPI WebSocket origin check errors when WebSocket connections are rejected by origin validation."
frameworks: ["fastapi"]
error-types: ["connection-error"]
severities: ["error"]
---

When WebSocket connections include an `Origin` header, the server may reject connections from unauthorized origins.

## Common Causes

- Nginx or reverse proxy filters WebSocket connections by origin
- Custom middleware rejects connections without matching origin
- Origin header includes port number that differs from expected
- Browser sends origin as `http://` while server expects `wss://`
- CORS middleware interferes with WebSocket upgrade handshake

## How to Fix

### Validate WebSocket Origin Manually

```python
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

ALLOWED_ORIGINS = {"https://myapp.com", "http://localhost:3000"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    origin = websocket.headers.get("origin", "")
    if origin not in ALLOWED_ORIGINS:
        await websocket.close(code=4003)
        return
    await websocket.accept()
```

### Configure Nginx for WebSocket Origins

```nginx
location /ws {
    proxy_pass http://backend;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "upgrade";
    proxy_set_header Origin $http_origin;
}
```

## Examples

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

# No origin check -- accepts any connection
@app.websocket("/ws/open")
async def open_ws(websocket: WebSocket):
    await websocket.accept()

# Origin check -- validates the connecting origin
@app.websocket("/ws/secure")
async def secure_ws(websocket: WebSocket):
    origin = websocket.headers.get("origin")
    if origin != "https://trusted.com":
        await websocket.close(code=4003)
        return
    await websocket.accept()
```
