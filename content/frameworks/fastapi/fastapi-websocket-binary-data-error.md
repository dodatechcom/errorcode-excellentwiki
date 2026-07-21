---
title: "[Solution] FastAPI WebSocket Binary Data Error"
description: "Fix FastAPI WebSocket binary data errors when sending or receiving binary frames fails or is corrupted."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

When sending binary data over a WebSocket in FastAPI, errors occur if the data is not properly encoded or if text methods are used for binary payloads.

## Common Causes

- Using `send_text()` to send binary data (bytes)
- Binary data not encoded as UTF-8 when using text frames
- WebSocket connection closed before binary frame is sent
- Large binary frames exceed WebSocket buffer limits
- Mixed text and binary frames confuse the client parser

## How to Fix

### Use Correct Send Methods

```python
from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_bytes()
        await websocket.send_bytes(data)  # Echo binary data
```

### Send JSON Data Properly

```python
@app.websocket("/ws/json")
async def ws_json(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        await websocket.send_json({"echo": data})
```

## Examples

```python
# Bug -- sending bytes with send_text
async def broken_send(websocket: WebSocket):
    await websocket.accept()
    data = b"\x00\x01\x02"
    await websocket.send_text(data)  # Fails -- expects str

# Fix -- use send_bytes for binary data
async def correct_send(websocket: WebSocket):
    await websocket.accept()
    data = b"\x00\x01\x02"
    await websocket.send_bytes(data)
```

Use `send_bytes()` for binary data and `send_text()` for string data.
