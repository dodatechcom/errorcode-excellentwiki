---
title: "[Solution] Python ResourceWarning — Resource Leak Fix"
description: "Fix Python ResourceWarning when resources are not properly cleaned up. Use context managers, close files/connections, and handle resource lifecycle."
languages: ["python"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# ResourceWarning — Resource Leak Fix

A `ResourceWarning` is raised when a resource (like a file, socket, or database connection) is not properly cleaned up. It's a subclass of `Warning` and is ignored by default. It helps detect resource leaks that could cause problems in long-running applications.

## Description

`ResourceWarning` is emitted when Python's garbage collector detects that a resource was never explicitly closed. This includes unclosed files, sockets, database connections, and other resources that require cleanup. These warnings are hidden by default but are invaluable for finding resource leaks.

Common scenarios:

- **Unclosed files** — opening files without `with` statement or `.close()`.
- **Unclosed sockets** — creating sockets without closing them.
- **Database connections** — connections not returned to pool.
- **Database cursors** — cursors left open after queries.
- **Thread resources** — threads not properly joined.

## Common Causes

```python
# Cause 1: File not closed
def read_file():
    f = open("data.txt")
    content = f.read()
    return content  # ResourceWarning: file not closed

# Cause 2: Socket not closed
import socket
def create_connection():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("example.com", 80))
    return sock  # ResourceWarning: socket not closed

# Cause 3: Database connection not closed
import sqlite3
def query_db():
    conn = sqlite3.connect("mydb.db")
    cursor = conn.execute("SELECT * FROM users")
    return cursor.fetchall()  # ResourceWarning: connection not closed

# Cause 4: Generator not fully consumed
def read_lines():
    f = open("data.txt")
    for line in f:
        yield line
    f.close()

# Usage that leaks
lines = read_lines()
first_line = next(lines)  # Only reads first line, f never closed

# Cause 5: Exception prevents close
def process():
    f = open("data.txt")
    data = f.read()
    raise ValueError("Processing error")  # f never closed
```

## Solutions

### Fix 1: Use context managers (with statement)

```python
# Wrong — file not closed on error
def read_file():
    f = open("data.txt")
    content = f.read()
    return content

# Correct — context manager ensures cleanup
def read_file():
    with open("data.txt") as f:
        content = f.read()
    return content
```

### Fix 2: Use try/finally for guaranteed cleanup

```python
# Wrong — may not close on exception
def process():
    f = open("data.txt")
    data = f.read()
    process_data(data)

# Correct — finally ensures cleanup
def process():
    f = None
    try:
        f = open("data.txt")
        data = f.read()
        process_data(data)
    finally:
        if f:
            f.close()
```

### Fix 3: Close database connections properly

```python
import sqlite3

# Wrong — connection not closed
def query_db():
    conn = sqlite3.connect("mydb.db")
    result = conn.execute("SELECT * FROM users").fetchall()
    return result

# Correct — close connection
def query_db():
    conn = sqlite3.connect("mydb.db")
    try:
        result = conn.execute("SELECT * FROM users").fetchall()
        return result
    finally:
        conn.close()

# Or use context manager
def query_db():
    with sqlite3.connect("mydb.db") as conn:
        result = conn.execute("SELECT * FROM users").fetchall()
        return result
```

### Fix 4: Close sockets with context manager

```python
import socket

# Wrong — socket not closed
def communicate():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("example.com", 80))
    sock.send(b"data")
    return sock.recv(1024)

# Correct — use context manager
def communicate():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(("example.com", 80))
        sock.send(b"data")
        return sock.recv(1024)
```

### Fix 5: Show ResourceWarnings for debugging

```python
import warnings

# Wrong — ResourceWarning hidden by default
def process():
    f = open("data.txt")
    data = f.read()
    return data

# Correct — enable ResourceWarning
warnings.filterwarnings("always", category=ResourceWarning)

def process():
    f = open("data.txt")
    data = f.read()
    return data  # ResourceWarning now visible
```

### Fix 6: Handle generators that open resources

```python
# Wrong — generator may not close file
def read_lines():
    f = open("data.txt")
    for line in f:
        yield line

# Correct — use contextmanager or explicit cleanup
from contextlib import contextmanager

@contextmanager
def open_file(filename):
    f = open(filename)
    try:
        yield f
    finally:
        f.close()

def read_lines():
    with open_file("data.txt") as f:
        for line in f:
            yield line
```

## Related Errors

- [Warning](../warning) — base class for all warnings.
- [DeprecationWarning](../deprecationwarning) — deprecated feature usage.
- [ResourceWarning](../resourcewarning) — resource leak detected.
- [PermissionError](../permissionerror) — insufficient permissions.
