---
title: "[Solution] Flask-SocketIO Connection Error"
description: "Fix Flask-SocketIO connection errors when WebSocket or long-polling connections fail to establish."
frameworks: ["flask"]
error-types: ["connection-error"]
severities: ["error"]
---

SocketIO connection errors occur when the client cannot establish a connection to the server due to configuration or network issues.

## Common Causes

- SocketIO server not running with proper async mode
- CORS not configured for cross-origin connections
- Nginx not configured to proxy WebSocket connections
- Connection timeout too short
- Maximum connections limit reached

## How to Fix

### Configure SocketIO Server

```python
from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    async_mode="eventlet",
    ping_timeout=60,
    ping_interval=25,
)
```

### Configure Nginx for WebSocket

```nginx
location /socket.io {
    proxy_pass http://127.0.0.1:5000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "Upgrade";
    proxy_set_header Host $host;
}
```

### Handle Connection Events

```python
@socketio.on("connect")
def handle_connect():
    print("Client connected")
    emit("connected", {"status": "ok"})

@socketio.on("disconnect")
def handle_disconnect():
    print("Client disconnected")
```

## Examples

```python
from flask_socketio import SocketIO

app = Flask(__name__)

# Bug -- using default sync mode
socketio = SocketIO(app)  # May not support WebSocket

# Fix -- use eventlet or gevent
socketio = SocketIO(app, async_mode="eventlet")
socketio.run(app)
```
