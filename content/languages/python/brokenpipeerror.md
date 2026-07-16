---
title: "[Solution] Python BrokenPipeError — Broken Pipe Fix"
description: "Fix Python BrokenPipeError when writing to a pipe or socket that the other end has closed. Handle SIGPIPE, use try/except, and check connection state."
languages: ["python"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["brokenpipeerror", "pipe", "socket", "network", "signal"]
weight: 5
---

# BrokenPipeError — Broken Pipe Fix

A `BrokenPipeError` is raised when you try to write to a pipe, socket, or stream whose reading end has been closed. It's a subclass of `ConnectionError` (which is a subclass of `OSError`). On Unix systems, this often manifests as `SIGPIPE`.

## Description

When one end of a pipe or socket closes the connection and the other end continues writing, the operating system sends a `SIGPIPE` signal. Python raises `BrokenPipeError` on Unix systems when this occurs. On Windows, the behavior is similar but without the `SIGPIPE` signal.

Common scenarios:

- **Client disconnects mid-response** — web server writes to a client that closed the browser.
- **Piped commands fail** — `head` closes its stdin, causing `grep` to get `BrokenPipeError`.
- **Socket peer closes connection** — writing to a socket after the remote end called `close()`.
- **Subprocess closes stdin** — parent writes to a subprocess that has already exited.

## Common Causes

```python
import socket

# Cause 1: Writing to a closed socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("example.com", 80))
sock.close()
sock.send(b"data")  # BrokenPipeError

# Cause 2: Piped command closes stdin
import subprocess
p = subprocess.Popen(["grep", "pattern"], stdin=subprocess.PIPE)
p.stdin.write(b"some data\n")
p.stdin.close()  # BrokenPipeError if grep exits early

# Cause 3: Client disconnects from server
server_sock, addr = server.accept()
data = server_sock.recv(1024)
client_sock.close()  # Client disconnects
server_sock.send(b"response")  # BrokenPipeError

# Cause 4: Writing to a closed pipe
import os
r, w = os.pipe()
os.close(r)  # Close read end
os.write(w, b"data")  # BrokenPipeError
```

## Solutions

### Fix 1: Handle BrokenPipeError with try/except

```python
import socket

# Wrong — assumes connection stays open
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("example.com", 80))
sock.send(b"GET / HTTP/1.0\r\n\r\n")
response = sock.recv(4096)

# Correct — handle broken pipe
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("example.com", 80))
try:
    sock.send(b"GET / HTTP/1.0\r\n\r\n")
    response = sock.recv(4096)
except BrokenPipeError:
    print("Connection was closed by the remote end")
finally:
    sock.close()
```

### Fix 2: Ignore SIGPIPE on Unix systems

```python
import signal
import socket

# Wrong — SIGPIPE kills the process on some systems
signal.signal(signal.SIGPIPE, signal.SIG_DFL)

# Correct — ignore SIGPIPE so Python raises BrokenPipeError instead
signal.signal(signal.SIGPIPE, signal.SIG_IGN)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect(("example.com", 80))
    sock.send(b"data")
except BrokenPipeError:
    print("Pipe broken, handled gracefully")
```

### Fix 3: Check socket state before writing

```python
import socket
import select

# Wrong — blindly writes to socket
sock.send(b"data")

# Correct — check if socket is still writable
ready, _, _ = select.select([], [sock], [], 1.0)
if ready:
    try:
        sock.send(b"data")
    except BrokenPipeError:
        print("Connection broken")
```

### Fix 4: Handle BrokenPipeError in web servers

```python
from http.server import HTTPServer, BaseHTTPRequestHandler

# Wrong — crashes when client disconnects
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, World!")  # BrokenPipeError if client leaves

# Correct — handle BrokenPipeError
class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, World!")
        except BrokenPipeError:
            pass  # Client disconnected, ignore

server = HTTPServer(("localhost", 8080), Handler)
server.serve_forever()
```

### Fix 5: Use context managers for pipe safety

```python
import subprocess
import sys

# Wrong — pipe may break
p = subprocess.Popen(["head", "-5"], stdin=subprocess.PIPE)
p.stdin.write(b"line1\nline2\n")
p.stdin.close()

# Correct — handle BrokenPipeError in piped commands
try:
    p = subprocess.Popen(["head", "-5"], stdin=subprocess.PIPE)
    p.stdin.write(b"line1\nline2\n")
    p.stdin.close()
except BrokenPipeError:
    # Reset SIGPIPE to default behavior
    import signal
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
```

## Related Errors

- [ConnectionResetError](../connectionreseterror) — connection reset by remote end.
- [ConnectionAbortedError](../connectionabortederror) — connection aborted by local host.
- [ConnectionError](../connectionerror) — base class for connection errors.
