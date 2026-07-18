---
title: "[Solution] Flask SocketIO Connection Error — How to Fix"
description: "Fix Flask SocketIO connection errors. Resolve WebSocket connection failures and event handling issues."
frameworks: ["flask"]
error-types: ["connection-error"]
severities: ["error"]
weight: 5
comments: true
---

A Flask SocketIO connection error occurs when the WebSocket or long-polling connection between the client and server fails to establish or is dropped unexpectedly. This affects real-time features like chat, notifications, and live updates.

## Why It Happens

Flask-SocketIO relies on eventlet or gevent for asynchronous handling. Errors occur when the wrong async server is used, when CORS is not configured for WebSocket connections, when the connection upgrade fails, when event handlers raise exceptions, or when load balancers strip WebSocket headers.

## Common Error Messages

```
ConnectionRefusedError: Connection refused
```

```
socketio.exceptions.ConnectionError: SocketIO connection failed
```

```
EngineIOError: Bad handshake method: GET
```

```
websocket.exceptions.InvalidStatusCode: Server rejected WebSocket upgrade
```

## How to Fix It

### 1. Use the Correct Async Server

Install and configure eventlet or gevent:

```python
# Install with async support
# pip install flask-socketio[eventlet]
# or: pip install flask-socketio[gevent]

# app.py
from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    emit('response', {'data': 'Connected'})

@socketio.on('message')
def handle_message(data):
    emit('response', {'data': f'Received: {data}'}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
```

### 2. Configure CORS for SocketIO

Allow WebSocket connections from your frontend:

```python
socketio = SocketIO(
    app,
    cors_allowed_origins=[
        "http://localhost:3000",
        "https://example.com",
    ],
    async_mode='eventlet',
    logger=True,
    engineio_logger=True,
)

# Or allow all origins in development
socketio = SocketIO(app, cors_allowed_origins="*", async_mode='eventlet')
```

### 3. Handle Connection Events Properly

Implement robust event handlers:

```python
from flask_socketio import SocketIO, emit, join_room, leave_room

socketio = SocketIO(app, async_mode='eventlet')

@socketio.on('connect')
def handle_connect(auth=None):
    if auth and auth.get('token') != valid_token:
        return False  # Reject connection
    print(f'Client connected: {request.sid}')

@socketio.on('disconnect')
def handle_disconnect():
    print(f'Client disconnected: {request.sid}')

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    emit('status', {'msg': f'Joined room {room}'}, room=room)

@socketio.on('leave')
def handle_leave(data):
    room = data['room']
    leave_room(room)
    emit('status', {'msg': f'Left room {room}'}, room=room)

@socketio.on_error_default
def error_handler(e):
    print(f'SocketIO error: {e}')
```

### 4. Run with the Correct Server

Use socketio.run instead of app.run:

```python
if __name__ == '__main__':
    # Correct: use socketio.run()
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

    # Wrong: Flask's built-in server doesn't support WebSockets
    # app.run(host='0.0.0.0', port=5000)
```

For production with Nginx, configure WebSocket proxying:

```nginx
location /socket.io/ {
    proxy_pass http://127.0.0.1:5000;
    proxy_http_version 1.1;
    proxy_set_header Upgrade $http_upgrade;
    proxy_set_header Connection "Upgrade";
    proxy_set_header Host $host;
}
```

## Common Scenarios

**Scenario 1: Connection works with polling but not WebSocket.**
Check that Nginx or the load balancer forwards the `Upgrade` and `Connection` headers. Without these, the WebSocket handshake fails.

**Scenario 2: Events not received by other clients.**
Ensure `broadcast=True` is set on `emit()` calls that should reach all connected clients, or use `room=` for targeted delivery.

**Scenario 3: Connection drops intermittently.**
Increase the ping timeout and interval:

```python
socketio = SocketIO(
    app,
    ping_timeout=60,
    ping_interval=25,
    async_mode='eventlet',
)
```

## Prevent It

1. **Always use `socketio.run()` in development.** Flask's default server does not support WebSockets.

2. **Use eventlet or gevent consistently.** Mixing async modes causes unpredictable behavior.

3. **Test with actual WebSocket connections.** Browser developer tools and `wscat` are useful for debugging.
