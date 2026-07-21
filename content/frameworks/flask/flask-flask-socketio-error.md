---
title: "[Solution] Flask Flask-SocketIO Error"
description: "SocketIO not connecting."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

SocketIO not connecting.

## Common Causes

Wrong event.

## How to Fix

Define events.

## Example

```python
from flask_socketio import SocketIO, emit
sio = SocketIO(app)
@sio.on('msg')
def h(d): emit('resp', {'d': 'ok'})
```
