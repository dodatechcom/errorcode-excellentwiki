---
title: "[Solution] Python TypeError — Not JSON Serializable"
description: "Fix Python TypeError: not JSON serializable when encoding objects to JSON. Learn which types are JSON-serializable and how to handle custom objects."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["json", "encode", "serializable", "typeerror"]
weight: 5
---

# TypeError — Not JSON Serializable

A `TypeError` with the message "Object of type X is not JSON serializable" is raised when `json.dumps()` or `json.dump()` encounters an object that cannot be converted to JSON format. Standard JSON only supports strings, numbers, booleans, None, lists, and dicts.

## Description

JSON has a limited set of data types. Python objects like `datetime`, `set`, `bytes`, `tuple`, custom classes, and `numpy` arrays are not directly serializable. You need to provide a custom encoder or convert these objects to JSON-compatible types before serialization.

Common patterns:

- **Serializing datetime** — `json.dumps(datetime.now())`.
- **Serializing sets** — `json.dumps({1, 2, 3})`.
- **Serializing bytes** — `json.dumps(b"hello")`.
- **Serializing custom objects** — `json.dumps(MyClass())`.
- **Serializing tuples** — `json.dumps((1, 2, 3))` — tuples serialize as arrays, but may cause issues in some contexts.

## Common Causes

```python
import json
from datetime import datetime

# Cause 1: Serializing datetime
data = {"time": datetime.now()}
json.dumps(data)  # TypeError: Object of type datetime is not JSON serializable

# Cause 2: Serializing a set
data = {"numbers": {1, 2, 3}}
json.dumps(data)  # TypeError: Object of type set is not JSON serializable

# Cause 3: Serializing bytes
data = {"data": b"hello"}
json.dumps(data)  # TypeError: Object of type bytes is not JSON serializable

# Cause 4: Serializing custom objects
class MyClass:
    def __init__(self, value):
        self.value = value

data = {"obj": MyClass(42)}
json.dumps(data)  # TypeError: Object of type MyClass is not JSON serializable
```

## Solutions

### Fix 1: Use a custom JSON encoder

```python
import json
from datetime import datetime

# Wrong
json.dumps({"time": datetime.now()})  # TypeError

# Correct — custom encoder
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, set):
            return list(obj)
        if isinstance(obj, bytes):
            return obj.decode("utf-8")
        return super().default(obj)

data = {"time": datetime.now(), "numbers": {1, 2, 3}}
json.dumps(data, cls=CustomEncoder)
```

### Fix 2: Convert objects before serialization

```python
import json
from datetime import datetime

# Wrong
data = {"time": datetime.now()}
json.dumps(data)  # TypeError

# Correct — convert before serialization
data = {"time": datetime.now().isoformat()}
json.dumps(data)  # Works
```

### Fix 3: Use default parameter in json.dumps

```python
import json
from datetime import datetime

def json_default(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, set):
        return list(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

data = {"time": datetime.now()}
json.dumps(data, default=json_default)
```

### Fix 4: Handle numpy arrays and pandas DataFrames

```python
import json
import numpy as np

# Wrong
data = {"array": np.array([1, 2, 3])}
json.dumps(data)  # TypeError

# Correct — convert to list
data = {"array": np.array([1, 2, 3]).tolist()}
json.dumps(data)

# Or use a custom encoder
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        return super().default(obj)

data = {"array": np.array([1, 2, 3])}
json.dumps(data, cls=NumpyEncoder)
```

## Related Errors

- [JSON decode](json-decode) — parsing invalid JSON.
- [TypeError](../typeerror) — general type mismatch errors.
- [Pickling error](pickling-error) — serializing objects with pickle.
