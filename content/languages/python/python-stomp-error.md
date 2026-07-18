---
title: "Solved Python STOMP Error — How to Fix"
date: 2026-03-12T09:30:15+00:00
description: "Learn how to resolve Python STOMP protocol errors with ActiveMQ and message broker connection issues."
categories: ["python"]
keywords: ["python stomp", "stomp error", "activemq python", "stomp protocol", "stomp connection error"]
error-types: ["runtime-error"]
severities: ["error"]
languages: ["python"]
weight: 5
comments: true
---

## Why It Happens

STOMP (Simple Text Oriented Messaging Protocol) errors occur when Python clients using `stomp.py` fail to connect, authenticate, or properly subscribe to message brokers like ActiveMQ or RabbitMQ. Protocol version mismatches and authentication failures are the most common culprits.

Common causes include:
- Protocol version mismatch between client and broker
- Invalid login credentials or missing authentication headers
- Frame size exceeding broker limits
- Subscription ID conflicts
- Sending frames on a disconnected transport

## Common Error Messages

```python
import stomp
import time

conn = stomp.Connection12([("nonexistent", 61613)])
try:
    conn.connect(wait=True)
except Exception as e:
    print(e)
# ConnectFailedException: Failed to connect
```

```python
# Protocol version mismatch
conn = stomp.Connection10([("localhost", 61613)])
conn.connect("user", "pass", wait=True)
# Sometimes silently fails or returns unexpected frames
```

```python
# Not connected error
conn = stomp.Connection11([("localhost", 61613)])
try:
    conn.send(destination="/queue/test", body="hello")
except Exception as e:
    print(type(e).__name__)
# NoConnectionEstablishedError
```

## How to Fix It

### 1. Use the Correct Protocol Version

Match your STOMP protocol version with the broker configuration.

```python
import stomp
import ssl

class MyListener(stomp.ConnectionListener):
    def on_error(self, frame):
        print(f"ERROR: {frame.headers.get('message', 'Unknown error')}")
        print(f"Detail: {frame.body}")
    
    def on_connected(self, frame):
        print(f"Connected: {frame.headers}")
    
    def on_disconnected(self):
        print("Disconnected, attempting reconnect...")
        # Implement reconnection logic here

# ActiveMQ 5.x typically uses STOMP 1.1 or 1.2
conn = stomp.Connection12(
    host_and_ports=[("localhost", 61613)],
    heart_beat=(10000, 10000),
    keepalive=True
)
conn.set_listener("my_listener", MyListener())
conn.connect("admin", "admin", wait=True)
```

### 2. Implement Heartbeat and Reconnection

Keep connections alive with heartbeats and auto-reconnect.

```python
import stomp
import time
import threading

class ReconnectingSTOMP:
    def __init__(self, hosts, login, passcode):
        self.hosts = hosts
        self.login = login
        self.passcode = passcode
        self.conn = None
        self._reconnect_delay = 5
        self._max_delay = 300
        self._running = True
        self.connect()
    
    def connect(self):
        self.conn = stomp.Connection12(
            self.hosts,
            heart_beat=(10000, 10000),
            keepalive=True
        )
        self.conn.set_listener("reconnect", self)
        self.conn.connect(self.login, self.passcode, wait=True)
    
    def on_disconnected(self):
        if self._running:
            print(f"Reconnecting in {self._reconnect_delay}s...")
            time.sleep(self._reconnect_delay)
            try:
                self.connect()
                self._reconnect_delay = min(self._reconnect_delay * 2, self._max_delay)
            except Exception as e:
                print(f"Reconnect failed: {e}")
    
    def on_connected(self, frame):
        self._reconnect_delay = 5
        print("Connected successfully")
        # Re-subscribe after reconnect
        self.conn.subscribe(
            destination="/queue/myqueue",
            id="sub-1",
            ack="auto"
        )
    
    def send(self, destination, body):
        if not self.conn.is_connected():
            raise ConnectionError("Not connected to broker")
        self.conn.send(destination=destination, body=body)
    
    def shutdown(self):
        self._running = False
        if self.conn and self.conn.is_connected():
            self.conn.disconnect()

client = ReconnectingSTOMP(
    hosts=[("localhost", 61613)],
    login="admin",
    passcode="admin"
)
client.send("/queue/test", "Hello World")
```

### 3. Handle Frame Size Limits

Respect broker frame size limits for large messages.

```python
import stomp
import json
import base64

MAX_FRAME_SIZE = 100 * 1024  # 100KB safety margin

def send_large_message(conn, destination, data):
    payload = json.dumps(data)
    
    if len(payload.encode()) <= MAX_FRAME_SIZE:
        conn.send(destination=destination, body=payload)
        return
    
    # Compress or chunk large messages
    compressed = base64.b64encode(payload.encode()).decode()
    
    conn.send(
        destination=destination,
        body=compressed,
        headers={
            "content-type": "application/base64",
            "original-size": str(len(payload))
        }
    )

conn = stomp.Connection12([("localhost", 61613)])
conn.connect("admin", "admin", wait=True)
send_large_message(conn, "/queue/big", {"data": "x" * 200000})
```

## Common Scenarios

### Scenario 1: Request-Reply Pattern

Implementing synchronous messaging over STOMP:

```python
import stomp
import uuid
import threading

class RequestReplyClient:
    def __init__(self, host, port):
        self.conn = stomp.Connection12([(host, port)])
        self.reply_queue = f"/queue/reply-{uuid.uuid4()}"
        self.responses = {}
        self.events = {}
        self.conn.set_listener("listener", self)
        self.conn.connect("admin", "admin", wait=True)
        self.conn.subscribe(
            destination=self.reply_queue,
            id="reply-sub",
            ack="auto"
        )
    
    def on_message(self, frame):
        corr_id = frame.headers.get("correlation-id")
        if corr_id in self.events:
            self.responses[corr_id] = frame.body
            self.events[corr_id].set()
    
    def request(self, destination, body, timeout=30):
        corr_id = str(uuid.uuid4())
        event = threading.Event()
        self.events[corr_id] = event
        
        self.conn.send(
            destination=destination,
            body=body,
            headers={
                "reply-to": self.reply_queue,
                "correlation-id": corr_id
            }
        )
        
        if event.wait(timeout):
            return self.responses.pop(corr_id)
        raise TimeoutError("Request timed out")
```

## Prevent It

- Always match STOMP protocol version with broker configuration
- Implement heartbeat (at least every 30 seconds) to detect dead connections
- Use connection listeners for error and disconnect events
- Set `keepalive=True` on the connection for TCP-level keepalive
- Handle `on_disconnected` callbacks to implement reconnection logic