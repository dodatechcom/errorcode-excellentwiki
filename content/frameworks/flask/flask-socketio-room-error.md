---
title: "[Solution] Flask SocketIO Room Error"
description: "Room not joining."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Room not joining.

## Common Causes

Wrong room name.

## How to Fix

Join first.

## Example

```python
from flask_socketio import join_room, emit
@sio.on('join')
def h(d):
    join_room(d['room'])
    emit('status', room=d['room'])
```
