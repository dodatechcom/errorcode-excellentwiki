---
title: "[Solution] Python ConnectionRefusedError — Connection Refused Fix"
description: "Fix Python ConnectionRefusedError when a connection is refused by the server. Check server status, port, firewall, and use retry logic."
languages: ["python"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["connectionrefusederror", "connection", "network", "server", "port"]
weight: 5
---

# ConnectionRefusedError — Connection Refused Fix

A `ConnectionRefusedError` is raised when a connection attempt is actively refused by the server. It's a subclass of `ConnectionError`, which is a subclass of `OSError`. This typically means the server is not running or not listening on the specified port.

## Description

When you try to connect to a host and port where no service is listening, the operating system's TCP/IP stack responds with a "connection refused" (RST packet). Python raises `ConnectionRefusedError` to indicate this. Unlike a timeout (which means the host is unreachable), a refused connection means the host is reachable but the port is closed.

Common scenarios:

- **Server not running** — connecting to a port where no process is listening.
- **Wrong port** — server is running on a different port than expected.
- **Server crashed** — server was running but has since terminated.
- **Firewall blocking** — firewall drops SYN packets without sending RST.
- **Backlog full** — server's listen backlog is full and new connections are refused.

## Common Causes

```python
import requests

# Cause 1: Server not running
response = requests.get("http://localhost:8080/api")  # ConnectionRefusedError

# Cause 2: Wrong port number
response = requests.get("http://localhost:3000/api")  # Server runs on 5000

# Cause 3: Server crashed during operation
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 5000))
# Server crashes...
sock.send(b"data")  # May get ConnectionRefusedError

# Cause 4: Server backlog full
import socket
import threading

def slow_handler(conn):
    import time
    time.sleep(10)
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen(1)  # Only 1 pending connection
# New connections get ConnectionRefusedError
```

## Solutions

### Fix 1: Verify the server is running before connecting

```python
import requests

# Wrong — assumes server is up
response = requests.get("http://localhost:8080/api")

# Correct — check if server is reachable
import socket

def is_server_up(host, port, timeout=2):
    try:
        sock = socket.create_connection((host, port), timeout=timeout)
        sock.close()
        return True
    except (ConnectionRefusedError, socket.timeout, OSError):
        return False

if is_server_up("localhost", 8080):
    response = requests.get("http://localhost:8080/api")
else:
    print("Server is not running")
```

### Fix 2: Handle ConnectionRefusedError with retry logic

```python
import requests
import time

# Wrong — single attempt fails
response = requests.get("http://localhost:8080/api")

# Correct — retry with exponential backoff
def fetch_with_retry(url, max_retries=5):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=5)
            return response
        except requests.ConnectionError as e:
            if "Connection refused" in str(e):
                wait = 2 ** attempt
                print(f"Attempt {attempt + 1} refused, retrying in {wait}s...")
                time.sleep(wait)
            else:
                raise
    raise ConnectionError(f"Server at {url} is not available")

data = fetch_with_retry("http://localhost:8080/api")
```

### Fix 3: Use try/except for graceful handling

```python
import requests

# Wrong — crashes on refused connection
response = requests.get("http://localhost:8080/api")
data = response.json()

# Correct — handle gracefully
try:
    response = requests.get("http://localhost:8080/api", timeout=5)
    data = response.json()
except requests.ConnectionError:
    print("Cannot connect to server — is it running?")
    data = None
except requests.Timeout:
    print("Connection timed out")
    data = None
```

### Fix 4: Check port and firewall settings

```python
import subprocess
import socket

# Check if port is in use
def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    sock.close()
    return result == 0

# Check multiple ports
for port in [80, 443, 8080, 5000]:
    if check_port("localhost", port):
        print(f"Port {port}: OPEN")
    else:
        print(f"Port {port}: CLOSED (ConnectionRefusedError if you connect)")
```

### Fix 5: Ensure server has sufficient backlog

```python
import socket

# Wrong — small backlog may refuse connections
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen(1)  # Only 1 pending connection

# Correct — larger backlog for high-traffic servers
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 5000))
server.listen(128)  # Allow 128 pending connections
```

## Related Errors

- [TimeoutError](../timeouterror) — connection timed out.
- [ConnectionResetError](../connectionreseterror) — connection reset by remote end.
- [ConnectionError](../connectionerror) — base class for connection errors.
