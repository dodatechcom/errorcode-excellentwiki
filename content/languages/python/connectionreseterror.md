---
title: "[Solution] Python ConnectionResetError — Connection Reset Fix"
description: "Fix Python ConnectionResetError when a connection is reset by the remote host. Handle reset errors, use keepalive, and implement retry logic."
languages: ["python"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# ConnectionResetError — Connection Reset Fix

A `ConnectionResetError` is raised when a connection is reset by the remote host (the other end sends a TCP RST packet). It's a subclass of `ConnectionError`, which is a subclass of `OSError`.

## Description

When the remote end of a connection actively resets it — typically by calling `close()` on its socket or by the process crashing — Python raises `ConnectionResetError` on the local side. This differs from `ConnectionAbortedError` (where the local host initiates the abort) and `BrokenPipeError` (which occurs during write operations).

Common scenarios:

- **Server crashes during request** — server process dies while client is connected.
- **Remote host closes connection** — server calls `close()` while client is reading.
- **Firewall kills connection** — firewall sends RST to terminate the connection.
- **Load balancer drops connection** — balancer closes idle connections abruptly.
- **Peer process terminates** — remote process is killed with SIGKILL.

## Common Causes

```python
import socket

# Cause 1: Server crashes during communication
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("localhost", 5000))
sock.send(b"data")
# Server crashes here...
response = sock.recv(1024)  # ConnectionResetError

# Cause 2: Remote end closes while we're reading
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("example.com", 80))
sock.send(b"GET / HTTP/1.0\r\n\r\n")
# Server closes connection after sending response
data = sock.recv(4096)  # May get ConnectionResetError on next recv

# Cause 3: Connection idle too long, server drops it
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("example.com", 80))
time.sleep(300)  # Connection may be reset by server
sock.send(b"GET / HTTP/1.0\r\n\r\n")  # ConnectionResetError

# Cause 4: Remote host reboots
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("192.168.1.100", 80))
# Remote host reboots...
sock.send(b"data")  # ConnectionResetError
```

## Solutions

### Fix 1: Handle ConnectionResetError with try/except

```python
import socket

# Wrong — no error handling
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("example.com", 80))
sock.send(b"data")
response = sock.recv(4096)

# Correct — handle reset gracefully
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("example.com", 80))
try:
    sock.send(b"data")
    response = sock.recv(4096)
except ConnectionResetError:
    print("Connection was reset by remote host")
    response = b""
finally:
    sock.close()
```

### Fix 2: Use TCP keepalive to detect dead connections

```python
import socket

# Wrong — no keepalive, connection may go stale
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("example.com", 80))
# Long idle period...

# Correct — enable TCP keepalive
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
# Optional: configure keepalive parameters
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 60)    # Start after 60s
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 10)   # Interval 10s
sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 6)      # 6 probes
sock.connect(("example.com", 80))
```

### Fix 3: Implement retry with reconnection

```python
import socket
import time

# Wrong — single attempt
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("example.com", 80))
sock.send(b"data")
response = sock.recv(4096)

# Correct — retry on reset
def reliable_send(host, port, data, max_retries=3):
    for attempt in range(max_retries):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(10.0)
            sock.connect((host, port))
            sock.send(data)
            response = sock.recv(4096)
            sock.close()
            return response
        except ConnectionResetError:
            print(f"Attempt {attempt + 1} failed, connection reset")
            time.sleep(2 ** attempt)
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(2 ** attempt)
    raise ConnectionResetError("All retries failed")
```

### Fix 4: Use requests library with retry adapters

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Wrong — no retry logic
response = requests.get("http://api.example.com/data")

# Correct — use retry adapter
session = requests.Session()
retry = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retry)
session.mount("http://", adapter)
session.mount("https://", adapter)

try:
    response = session.get("http://api.example.com/data", timeout=10)
    data = response.json()
except requests.ConnectionError:
    print("Connection failed after retries")
```

## Related Errors

- [ConnectionAbortedError](../connectionabortederror) — connection aborted by local host.
- [BrokenPipeError](../brokenpipeerror) — broken pipe during write.
- [ConnectionError](../connectionerror) — base class for connection errors.
