---
title: "[Solution] Python TimeoutError — Operation Timed Out Fix"
description: "Fix Python TimeoutError when socket or async operations exceed their time limit. Configure timeouts, use retry logic, and handle timeout scenarios."
languages: ["python"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["timeouterror", "timeout", "socket", "async", "network"]
weight: 5
---

# TimeoutError — Operation Timed Out Fix

A `TimeoutError` is raised when a socket operation or other I/O operation exceeds its configured timeout period. It's a subclass of `OSError`. This is different from `asyncio.TimeoutError`, which is used in async contexts.

## Description

`TimeoutError` occurs when you set a timeout on a socket or other blocking operation and the operation doesn't complete within the specified time. The timeout is set using `socket.settimeout()` or passed as a parameter to functions like `socket.create_connection()`.

Note: In Python 3.3+, `socket.timeout` is an alias for `TimeoutError`. In async contexts, `asyncio.TimeoutError` is a separate exception raised by `asyncio.wait_for()`.

Common scenarios:

- **Socket connection timeout** — server takes too long to respond.
- **Socket read timeout** — data doesn't arrive within time limit.
- **Socket write timeout** — send buffer is full and write blocks.
- **DNS resolution timeout** — hostname lookup takes too long.
- **HTTP request timeout** — server doesn't respond in time.

## Common Causes

```python
import socket

# Cause 1: Connection timeout
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1.0)  # 1 second timeout
sock.connect(("192.168.1.999", 80))  # TimeoutError: connection too slow

# Cause 2: Read timeout
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("example.com", 80))
sock.settimeout(1.0)
data = sock.recv(1024)  # TimeoutError if no data in 1 second

# Cause 3: Write timeout
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(1.0)
sock.connect(("example.com", 80))
sock.send(b"x" * 10**8)  # TimeoutError if send buffer full

# Cause 4: Using socket.create_connection with timeout
sock = socket.create_connection(("example.com", 80), timeout=2.0)
# TimeoutError if connection takes more than 2 seconds

# Cause 5: HTTP request timeout
import requests
response = requests.get("http://slow-server.com", timeout=1.0)  # TimeoutError
```

## Solutions

### Fix 1: Set appropriate timeouts

```python
import socket

# Wrong — no timeout, may hang forever
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("example.com", 80))
data = sock.recv(4096)

# Correct — set reasonable timeout
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10.0)  # 10 seconds
try:
    sock.connect(("example.com", 80))
    data = sock.recv(4096)
except socket.timeout:
    print("Operation timed out")
```

### Fix 2: Handle TimeoutError with retry logic

```python
import socket
import time

# Wrong — single attempt
sock = socket.create_connection(("example.com", 80), timeout=5)

# Correct — retry with backoff
def connect_with_retry(host, port, timeout=5, max_retries=3):
    for attempt in range(max_retries):
        try:
            return socket.create_connection((host, port), timeout=timeout)
        except socket.timeout:
            wait = 2 ** attempt
            print(f"Attempt {attempt + 1} timed out, retrying in {wait}s...")
            time.sleep(wait)
    raise socket.timeout(f"Failed to connect to {host}:{port}")

sock = connect_with_retry("example.com", 80)
```

### Fix 3: Use requests with timeout for HTTP

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Wrong — no timeout
response = requests.get("http://api.example.com/data")

# Correct — timeout with retry
session = requests.Session()
retry = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retry)
session.mount("http://", adapter)
session.mount("https://", adapter)

try:
    response = session.get("http://api.example.com/data", timeout=(3.05, 30))
    data = response.json()
except requests.Timeout:
    print("Request timed out")
```

### Fix 4: Use asyncio for async timeouts

```python
import asyncio

# Wrong — no timeout in async context
async def fetch_data():
    reader, writer = await asyncio.open_connection("example.com", 80)
    data = await reader.read(1024)  # May hang

# Correct — use asyncio.wait_for
async def fetch_data():
    try:
        reader, writer = await asyncio.wait_for(
            asyncio.open_connection("example.com", 80),
            timeout=10.0
        )
        data = await reader.read(1024)
        return data
    except asyncio.TimeoutError:
        print("Async operation timed out")
        return None
```

### Fix 5: Use non-blocking I/O with select for timeout control

```python
import socket
import select

# Wrong — blocking with fixed timeout
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(5.0)
sock.connect(("example.com", 80))

# Correct — use select for flexible timeout
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("example.com", 80))
ready, _, _ = select.select([sock], [], [], 5.0)
if ready:
    data = sock.recv(1024)
else:
    print("Read timed out")
```

## Related Errors

- [BlockingIOError](../blockingioerror) — non-blocking I/O would block.
- [ConnectionError](../connectionerror) — network connection failed.
- [OSError](../oserror) — generic OS-level error.
