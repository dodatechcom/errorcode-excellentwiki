---
title: "Solved Python WebSocket Client Error — How to Fix"
date: 2026-03-12T09:40:22+00:00
description: "Learn how to resolve Python WebSocket connection, handshake, and data transfer errors with websockets library."
categories: ["python"]
keywords: ["python websocket", "websocket error", "websockets library", "websocket connection", "websocket handshake"]
error-types: ["runtime-error"]
severities: ["error"]
languages: ["python"]
weight: 5
comments: true
---

## Why It Happens

WebSocket errors in Python arise when the client cannot establish or maintain a persistent connection to a server. These include handshake failures, connection drops, and protocol violations during data exchange.

Common causes include:
- Server rejecting WebSocket upgrade request
- TLS/SSL certificate verification failures
- Sending data after connection closure
- Exceeding maximum message size limits
- Incorrect subprotocol negotiation

## Common Error Messages

```python
import asyncio
import websockets

async def connect():
    try:
        async with websockets.connect("ws://localhost:8765") as ws:
            pass
    except websockets.exceptions.ConnectionClosedError as e:
        print(f"Connection closed: {e}")
    except OSError as e:
        print(f"Connection failed: {e}")

asyncio.run(connect())
```

```python
# Handshake failure
try:
    ws = await websockets.connect("ws://example.com:8080/ws")
except websockets.exceptions.InvalidStatusCode as e:
    print(f"Handshake failed: status {e.status_code}")
```

```python
# Invalid URI
try:
    ws = await websockets.connect("http://example.com/ws")
except ValueError as e:
    print(f"Invalid URI: {e}")
```

## How to Fix It

### 1. Implement Reconnection with Exponential Backoff

Handle connection drops gracefully with automatic reconnection.

```python
import asyncio
import websockets
import json

class ReconnectingWebSocket:
    def __init__(self, uri, max_retries=10):
        self.uri = uri
        self.max_retries = max_retries
        self.ws = None
        self._reconnect_delay = 1
    
    async def connect(self):
        for attempt in range(self.max_retries):
            try:
                self.ws = await websockets.connect(
                    self.uri,
                    ping_interval=20,
                    ping_timeout=10,
                    close_timeout=5
                )
                self._reconnect_delay = 1
                print(f"Connected to {self.uri}")
                return self.ws
            except (OSError, websockets.exceptions.ConnectionClosed) as e:
                wait = min(self._reconnect_delay * 2, 60)
                print(f"Attempt {attempt+1} failed: {e}, retrying in {wait}s")
                await asyncio.sleep(wait)
                self._reconnect_delay = wait
        raise ConnectionError("Max retries exceeded")
    
    async def send_with_retry(self, data, max_retries=3):
        for attempt in range(max_retries):
            try:
                if self.ws is None or self.ws.closed:
                    await self.connect()
                await self.ws.send(json.dumps(data))
                return True
            except websockets.exceptions.ConnectionClosed:
                await self.connect()
        return False
    
    async def close(self):
        if self.ws and not self.ws.closed:
            await self.ws.close()

async def main():
    client = ReconnectingWebSocket("ws://localhost:8765")
    ws = await client.connect()
    
    async for message in ws:
        data = json.loads(message)
        print(f"Received: {data}")
        await client.send_with_retry({"echo": data})

asyncio.run(main())
```

### 2. Handle Message Size Limits

Configure appropriate message size limits for your use case.

```python
import asyncio
import websockets

MAX_MSG_SIZE = 10 * 1024 * 1024  # 10MB

async def handler(websocket):
    async for message in websocket:
        if isinstance(message, bytes):
            print(f"Binary message: {len(message)} bytes")
        else:
            if len(message) > MAX_MSG_SIZE:
                await websocket.close(1009, "Message too large")
                return
            print(f"Text message: {message}")

async def client():
    async with websockets.connect(
        "ws://localhost:8765",
        max_size=MAX_MSG_SIZE,
        max_queue=32
    ) as ws:
        await ws.send("Hello")
        response = await ws.recv()
        print(f"Server: {response}")

asyncio.run(client())
```

### 3. Implement Secure WebSocket Connections

Configure TLS and authentication for production use.

```python
import asyncio
import websockets
import ssl
import json

def create_ssl_context():
    ssl_ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ssl_ctx.load_verify_locations("/path/to/ca.crt")
    ssl_ctx.check_hostname = True
    ssl_ctx.verify_mode = ssl.CERT_REQUIRED
    return ssl_ctx

class SecureWebSocketClient:
    def __init__(self, uri, token=None):
        self.uri = uri
        self.token = token
        self.ssl_ctx = create_ssl_context() if uri.startswith("wss") else None
    
    async def connect(self):
        extra_headers = {}
        if self.token:
            extra_headers["Authorization"] = f"Bearer {self.token}"
        
        self.ws = await websockets.connect(
            self.uri,
            ssl=self.ssl_ctx,
            additional_headers=extra_headers,
            ping_interval=30,
            ping_timeout=10
        )
        return self.ws
    
    async def send_auth(self, credentials):
        await self.ws.send(json.dumps({
            "type": "auth",
            "token": credentials["token"]
        }))
        response = json.loads(await self.ws.recv())
        return response.get("status") == "ok"

async def main():
    client = SecureWebSocketClient(
        "wss://secure-server.example.com/ws",
        token="my-api-token"
    )
    ws = await client.connect()
    
    if await client.send_auth({"token": "my-api-token"}):
        await ws.send(json.dumps({"action": "subscribe", "channel": "updates"}))
        async for msg in ws:
            print(json.loads(msg))

asyncio.run(main())
```

## Common Scenarios

### Scenario 1: Real-Time Chat Application

Managing multiple chat room connections:

```python
import asyncio
import websockets
import json
from collections import defaultdict

class ChatClient:
    def __init__(self, uri):
        self.uri = uri
        self.rooms = {}
        self.ws = None
    
    async def connect(self):
        self.ws = await websockets.connect(self.uri)
        return self
    
    async def join_room(self, room_id, on_message):
        self.rooms[room_id] = on_message
        await self.ws.send(json.dumps({
            "type": "join",
            "room": room_id
        }))
    
    async def send_message(self, room_id, text):
        await self.ws.send(json.dumps({
            "type": "message",
            "room": room_id,
            "text": text
        }))
    
    async def listen(self):
        async for msg in self.ws:
            data = json.loads(msg)
            room = data.get("room")
            if room in self.rooms:
                await self.rooms[room](data)

async def on_chat_message(data):
    print(f"[{data['user']}]: {data['text']}")

async def main():
    client = await ChatClient("ws://localhost:8765").connect()
    await client.join_room("general", on_chat_message)
    await client.listen()

asyncio.run(main())
```

## Prevent It

- Always handle `ConnectionClosed` exceptions and implement reconnection logic
- Use `ping_interval` and `ping_timeout` to detect dead connections early
- Set appropriate `max_size` limits for incoming messages
- Use WSS (WebSocket Secure) for production deployments
- Handle both text and binary messages appropriately in your protocol