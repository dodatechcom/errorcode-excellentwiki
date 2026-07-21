---
title: "[Solution] FastAPI WebSocket Concurrent Error"
description: "Fix FastAPI WebSocket concurrency errors when multiple websocket connections cause race conditions or data corruption."
frameworks: ["fastapi"]
error-types: ["concurrency-error"]
severities: ["error"]
---

When multiple WebSocket connections share state in FastAPI, concurrent access to shared resources causes race conditions.

## Common Causes

- Shared dictionary mutated by multiple async websocket handlers
- Database writes from multiple concurrent websocket connections
- Broadcast function modifies connection list while iterating
- Lock not used when updating shared state
- Event loop starvation from long-running operations

## How to Fix

### Use Thread-Safe Connection Manager

```python
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, WebSocket] = {}
        self._lock = asyncio.Lock()

    async def connect(self, websocket: WebSocket, client_id: str):
        await websocket.accept()
        async with self._lock:
            self.active_connections[client_id] = websocket

    async def disconnect(self, client_id: str):
        async with self._lock:
            self.active_connections.pop(client_id, None)

    async def broadcast(self, message: str):
        async with self._lock:
            connections = list(self.active_connections.values())
        for conn in connections:
            try:
                await conn.send_text(message)
            except Exception:
                pass

manager = ConnectionManager()

@app.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: str):
    await manager.connect(websocket, client_id)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"{client_id}: {data}")
    except WebSocketDisconnect:
        await manager.disconnect(client_id)
```

### Use Asyncio Queue for Message Passing

```python
message_queue = asyncio.Queue()

async def producer():
    await message_queue.put({"type": "update", "data": "new data"})

async def consumer():
    msg = await message_queue.get()
    return msg
```

## Examples

```python
import asyncio
from fastapi import FastAPI, WebSocket

app = FastAPI()

shared_state = {}  # Bug -- not thread-safe

@app.websocket("/ws/{user_id}")
async def unsafe_ws(websocket: WebSocket, user_id: str):
    await websocket.accept()
    shared_state[user_id] = {"online": True}  # Race condition
    await asyncio.sleep(10)
    del shared_state[user_id]

# Fix -- use asyncio.Lock
state_lock = asyncio.Lock()

@app.websocket("/ws/safe/{user_id}")
async def safe_ws(websocket: WebSocket, user_id: str):
    await websocket.accept()
    async with state_lock:
        shared_state[user_id] = {"online": True}
    await asyncio.sleep(10)
    async with state_lock:
        shared_state.pop(user_id, None)
```
