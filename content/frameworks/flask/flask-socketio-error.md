---
title: "Flask-SocketIO Error"
description: "Flask-SocketIO raises errors related to WebSocket connection, event handling, and room management"
frameworks: ["flask"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["socketio", "websocket", "realtime", "events", "flask"]
weight: 5
---

## What This Error Means

Flask-SocketIO errors occur when WebSocket connections fail, event handlers encounter exceptions, or room/namespace management has issues. These errors can appear during connection establishment, event emission, or client disconnection.

## Common Causes

- Socket.IO version mismatch between client and server
- WebSocket transport not supported by server
- Event handler throws an exception
- Namespace not properly registered
- Client disconnected during event emission

## How to Fix

Set up Flask-SocketIO properly:

```python
from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on('connect')
def handle_connect():
    emit('response', {'data': 'Connected'})

@socketio.on('message')
def handle_message(msg):
    emit('response', {'data': f'Received: {msg}'})

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')
```

Use consistent Socket.IO versions:

```python
# Server: python-socketio >= 5.0
# Client: socket.io-client >= 4.0

socketio = SocketIO(app, async_mode='eventlet', cors_allowed_origins="*")
```

Handle event errors gracefully:

```python
@socketio.on('error')
def handle_error(error):
    print(f'Socket error: {error}')
    emit('error_response', {'error': str(error)})

@socketio.on('my_event')
def handle_my_event(data):
    try:
        result = process_data(data)
        emit('result', {'data': result})
    except Exception as e:
        emit('error_response', {'error': str(e)})
```

Manage rooms properly:

```python
@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    emit('status', {'msg': f'{username} has entered the room.'}, room=room)
```

## Examples

```python
@socketio.on('send_message')
def send_message(data):
    emit('new_message', data, broadcast=True)
```

```text
ConnectionRefusedError: [Errno 111] Connection refused
```

## Related Errors

- [Configuration error]({{< relref "/frameworks/flask/config-error" >}})
- [CORS error]({{< relref "/frameworks/flask/flask-cors-error" >}})
