---
title: "[Solution] FastAPI WebSocket State Reset Error"
description: "Fix FastAPI WebSocket state reset errors when websocket connection state is lost between handler invocations."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

When using `websocket.state` to store per-connection data, the state may be lost if the connection handler is restructured incorrectly.

## Common Causes

- State set in one handler but accessed in a different handler
- Connection state shared between unrelated websocket connections
- State modified concurrently by multiple async tasks
- State attribute accessed before it is set
- Connection reconnection loses previous state

## How to Fix

### Store State on the WebSocket Object

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_handler(websocket: WebSocket):
    await websocket.accept()
    websocket.state.user_id = None
    try:
        while True:
            data = await websocket.receive_json()
            if data.get("type") == "auth":
                websocket.state.user_id = data["user_id"]
                await websocket.send_json({"status": "authenticated"})
            elif data.get("type") == "message":
                if websocket.state.user_id:
                    await websocket.send_json({
                        "from": websocket.state.user_id,
                        "text": data["text"],
                    })
    except Exception:
        pass
```

### Use a Connection Manager

```python
class Manager:
    def __init__(self):
        self.connections: dict[str, dict] = {}

    def set_state(self, ws_id: str, key: str, value):
        if ws_id not in self.connections:
            self.connections[ws_id] = {}
        self.connections[ws_id][key] = value

    def get_state(self, ws_id: str, key: str):
        return self.connections.get(ws_id, {}).get(key)

manager = Manager()
```

## Examples

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

# Bug -- state not initialized before use
@app.websocket("/ws/broken")
async def broken_ws(websocket: WebSocket):
    await websocket.accept()
    user_id = websocket.state.user_id  # AttributeError

# Fix -- initialize state first
@app.websocket("/ws/fixed")
async def fixed_ws(websocket: WebSocket):
    await websocket.accept()
    websocket.state.user_id = None  # Initialize
    data = await websocket.receive_json()
    websocket.state.user_id = data.get("user_id")
```
