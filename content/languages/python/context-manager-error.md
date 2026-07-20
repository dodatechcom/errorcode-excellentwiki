---
title: "[Solution] Python TypeError — object does not support the context manager protocol"
description: "Fix Python TypeError when using 'with' statement on objects without __enter__/__exit__. Learn context manager protocol and async context managers."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 710
---

# Python TypeError — object does not support the context manager protocol

A `TypeError` with the message `'TYPE' object does not support the context manager protocol` (or `'TYPE' object does not enter the context manager`) is raised when you use the `with` statement on an object that doesn't implement the context manager protocol (`__enter__` and `__exit__` methods). Similarly, `async with` requires `__aenter__` and `__aexit__`.

## Common Causes

```python
# Cause 1: Using 'with' on a plain object
class MyResource:
    def __init__(self, name):
        self.name = name

with MyResource("db") as r:  # TypeError: 'MyResource' does not support the context manager protocol
    print(r.name)

# Cause 2: Using 'async with' without async context manager
class AsyncResource:
    async def __enter__(self):
        return self
    # Missing __aexit__

# Cause 3: Using 'with' on a function return value
def get_connection():
    return Connection()

with get_connection() as conn:  # TypeError if Connection lacks __enter__/__exit__
    conn.execute("SELECT 1")

# Cause 4: Using 'with' on a file opened with wrong mode
import io
f = io.StringIO("hello")
# StringIO supports context manager, but some custom file-like objects don't

# Cause 5: Using 'with' on a generator
def my_gen():
    yield 1
    yield 2

with my_gen() as g:  # TypeError: 'generator' does not support the context manager protocol
    pass
```

## How to Fix

### Fix 1: Implement __enter__ and __exit__ methods

```python
# Wrong — no context manager protocol
class DatabaseConnection:
    def __init__(self, host):
        self.host = host
        self.conn = None

    def connect(self):
        self.conn = create_connection(self.host)

    def close(self):
        if self.conn:
            self.conn.close()

# Correct — implement context manager
class DatabaseConnection:
    def __init__(self, host):
        self.host = host
        self.conn = None

    def __enter__(self):
        self.conn = create_connection(self.host)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.close()
        return False  # Don't suppress exceptions

with DatabaseConnection("localhost") as db:
    db.conn.execute("SELECT 1")
```

### Fix 2: Use contextlib.contextmanager for simple cases

```python
from contextlib import contextmanager

@contextmanager
def database_connection(host):
    conn = create_connection(host)
    try:
        yield conn
    finally:
        conn.close()

with database_connection("localhost") as conn:
    conn.execute("SELECT 1")
```

### Fix 3: Use async context manager for async operations

```python
# Wrong — missing __aenter__/__aexit__
class AsyncDB:
    def __init__(self, host):
        self.host = host

# Correct — implement async context manager
class AsyncDB:
    def __init__(self, host):
        self.host = host

    async def __aenter__(self):
        self.conn = await async_connect(self.host)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.conn.close()
        return False

async def main():
    async with AsyncDB("localhost") as db:
        await db.conn.execute("SELECT 1")
```

### Fix 4: Use contextlib.asynccontextmanager

```python
import asyncio
from contextlib import asynccontextmanager

@asynccontextmanager
async def async_database(host):
    conn = await async_connect(host)
    try:
        yield conn
    finally:
        await conn.close()

async def main():
    async with async_database("localhost") as conn:
        await conn.execute("SELECT 1")
```

## Examples

```python
# Real-world: File handling with context manager
class TempFile:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "w")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        import os
        os.remove(self.filename)
        return False

with TempFile("temp.txt") as f:
    f.write("Hello, World!")
# File is automatically closed and deleted

# Real-world: Database transaction management
from contextlib import contextmanager

@contextmanager
def transaction(conn):
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise

# Usage
with transaction(db_connection) as conn:
    conn.execute("INSERT INTO users VALUES (1, 'Alice')")
    conn.execute("UPDATE accounts SET balance = 1000")
# Automatically commits on success, rolls back on exception
```

## Related Errors

- [TypeError](../typeerror) — general type mismatch errors.
- [AttributeError](../attributeerror) — object has no attribute.
- [Generator close](generator-close) — generator cleanup issues.
