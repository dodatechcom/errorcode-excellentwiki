---
title: "[Solution] Flask-SocketIO Emit Error 2"
description: "Fix Flask-SocketIO emit errors when broadcasting events to multiple clients fails or is slow."
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
---

When emitting to many clients simultaneously, Flask-SocketIO may experience performance issues or partial delivery failures.

## Common Causes

- Broadcasting to thousands of clients causes delays
- Client disconnections during broadcast
- Event payload too large for WebSocket frames
- Async mode not properly configured for high load
- Memory usage grows with connection count

## How to Fix

### Optimize Broadcasting

```python
from flask_socketio import SocketIO, emit

socketio = SocketIO(app, async_mode="eventlet")

@socketio.on("update")
def handle_update(data):
    # Emit only to affected clients, not all
    emit("update", data, room=data.get("room"))
```

### Use Rooms for Targeted Broadcasting

```python
@socketio.on("join_room")
def handle_join(data):
    room = data["room"]
    join_room(room)
    emit("status", {"msg": "Joined"}, room=room)

@socketio.on("send")
def handle_send(data):
    room = data["room"]
    emit("message", data, room=room)
```

### Compress Large Payloads

```python
import json
import zlib

@socketio.on("large_data")
def handle_large_data(data):
    compressed = zlib.compress(json.dumps(data).encode())
    emit("compressed_data", {"data": compressed})
```

## Examples

```python
from flask_socketio import SocketIO, emit

socketio = SocketIO(app)

# Bug -- emitting to all clients for every update
@socketio.on("user_update")
def handle_user_update(data):
    emit("update", data, broadcast=True)  # Slow for many clients

# Fix -- emit to specific room
@socketio.on("user_update_fixed")
def handle_user_update_fixed(data):
    room = data.get("room", "general")
    emit("update", data, room=room)
```
