---
title: "[Solution] Python shelve Module Error — Persistent Dictionary Failures"
description: "Fix Python shelve module errors including shelve.error, key errors, pickle protocol issues, and open/close problems. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 248
---

# Python shelve Module Error — Persistent Dictionary Failures

The `shelve` module provides persistent dictionary-like storage using `dbm` and `pickle`. Errors occur due to pickle protocol limitations, improper file handling, key access issues, or database corruption.

## Common Causes

```python
# Cause 1: Pickling objects that cannot be serialized
import shelve

class MyData:
    def __init__(self):
        self.lambda_fn = lambda x: x + 1  # Lambdas cannot be pickled

with shelve.open("mydb") as db:
    db["data"] = MyData()  # shelve.error: cannot pickle 'function'

# Cause 2: Accessing non-existent keys
import shelve

with shelve.open("mydb") as db:
    value = db["nonexistent_key"]  # KeyError: 'nonexistent_key'

# Cause 3: Database corruption from improper close
import shelve

db = shelve.open("mydb")
db["key"] = "value"
# Forgetting to close — data may not be flushed
del db  # Not guaranteed to close properly

# Cause 4: Writing non-picklable types
import shelve

with shelve.open("mydb") as db:
    db["lambda"] = lambda: None  # Cannot pickle function
    db["generator"] = (x for x in range(10))  # Cannot pickle generator

# Cause 5: Concurrent access from multiple processes
import shelve

# Two processes writing to the same shelve file
db1 = shelve.open("shared_db")
db2 = shelve.open("shared_db")  # May cause corruption
```

## How to Fix

### Fix 1: Use writeback mode for mutable objects

```python
import shelve

# With writeback=True, changes to mutable objects are saved
with shelve.open("mydb", writeback=True) as db:
    if "items" not in db:
        db["items"] = []
    db["items"].append("new_item")  # Automatically saved on close

# Without writeback, you must reassign
with shelve.open("mydb") as db:
    items = db.get("items", [])
    items.append("another_item")
    db["items"] = items  # Must reassign to save
```

### Fix 2: Handle key errors safely

```python
import shelve

def safe_get(db, key, default=None):
    try:
        return db[key]
    except KeyError:
        return default

with shelve.open("mydb") as db:
    value = safe_get(db, "nonexistent", "default_value")

# Or use the dict-like .get() method
with shelve.open("mydb") as db:
    value = db.get("nonexistent_key", "default_value")
    exists = "key" in db
```

### Fix 3: Ensure proper close with context manager

```python
import shelve

# Always use context manager
with shelve.open("mydb") as db:
    db["key1"] = "value1"
    db["key2"] = [1, 2, 3]
    db["key3"] = {"nested": "dict"}
# Automatically closed and flushed

# Manual close (less preferred)
db = shelve.open("mydb")
try:
    db["key"] = "value"
finally:
    db.close()
```

### Fix 4: Pickle custom objects correctly

```python
import shelve
import pickle

class MyData:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __repr__(self):
        return f"MyData(name={self.name!r}, value={self.value!r})"

    def __getstate__(self):
        # Control what gets pickled
        return {"name": self.name, "value": self.value}

    def __setstate__(self, state):
        # Control how unpickled
        self.name = state["name"]
        self.value = state["value"]

with shelve.open("mydb") as db:
    db["data"] = MyData("test", 42)

with shelve.open("mydb") as db:
    print(db["data"])  # MyData(name='test', value=42)
```

### Fix 5: Use flags for read-only and create modes

```python
import shelve

# Read-only mode — prevents corruption from concurrent writes
with shelve.open("mydb", flag="r") as db:
    value = db.get("key", "default")

# Create new database, fail if exists
try:
    with shelve.open("mydb", flag="n") as db:
        db["key"] = "value"
except dbm.error:
    print("Database already exists")

# Open existing, create if needed (default)
with shelve.open("mydb", flag="c") as db:
    db.setdefault("key", "value")
```

## Examples

```python
# Real-world: Configuration storage
import shelve
import os

class ConfigManager:
    def __init__(self, config_path="app_config"):
        self.config_path = config_path

    def get(self, key, default=None):
        with shelve.open(self.config_path) as db:
            return db.get(key, default)

    def set(self, key, value):
        with shelve.open(self.config_path, writeback=True) as db:
            db[key] = value

    def delete(self, key):
        with shelve.open(self.config_path) as db:
            if key in db:
                del db[key]

    def list_keys(self):
        with shelve.open(self.config_path) as db:
            return list(db.keys())

config = ConfigManager()
config.set("theme", "dark")
config.set("language", "en")
print(config.get("theme"))  # dark

# Real-world: Simple cache with TTL
import shelve
import time

class ShelfCache:
    def __init__(self, path="cache_db", ttl=3600):
        self.path = path
        self.ttl = ttl

    def get(self, key):
        with shelve.open(self.path) as db:
            if key in db:
                value, timestamp = db[key]
                if time.time() - timestamp < self.ttl:
                    return value
            return None

    def set(self, key, value):
        with shelve.open(self.path) as db:
            db[key] = (value, time.time())

    def clear(self):
        with shelve.open(self.path) as db:
            for key in list(db.keys()):
                del db[key]
```

## Related Errors

- [PickleError](/languages/python/typeerror/) — objects that cannot be pickled
- [KeyError](/languages/python/keyerror/) — dictionary key not found
- [FileNotFoundError](/languages/python/filenotfounderror/) — database file missing
