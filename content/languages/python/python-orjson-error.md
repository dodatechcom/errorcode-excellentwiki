---
title: "[Solution] Python orjson Serialization Error — How to Fix"
description: "Fix Python orjson serialization errors. Resolve type conversion failures, NaN handling issues, and encoding problems."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python orjson Serialization Error

A `orjson.JSONEncodeError` or `TypeError` occurs when orjson fails to serialize a Python object because it does not support the type, encounters NaN values, or receives non-UTF-8 encoded strings.

## Why It Happens

orjson is a fast JSON serializer that supports a subset of Python types. Errors arise when you attempt to serialize types not in its supported set (like custom classes without converters), when float NaN or Infinity values appear, or when bytes contain non-UTF-8 characters.

## Common Error Messages

- `TypeError: Type is not JSON serializable: datetime.datetime`
- `ValueError: Out of range float values are not JSON compliant`
- `TypeError: 'bytes' object cannot be interpreted as an integer`
- `orjson.JSONEncodeError: Expected str, got dict`

## How to Fix It

### Fix 1: Handle unsupported types with custom encoders

```python
import orjson
from datetime import datetime

# Wrong — datetime not serializable by default
# orjson.dumps({"ts": datetime.now()})  # TypeError

# Correct — use default function for custom types
def default_handler(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} is not JSON serializable")

data = {"timestamp": datetime.now(), "name": "test"}
result = orjson.dumps(data, default=default_handler)
print(result.decode())

# Use orjson.OPT_SERIALIZE_NUMPY for numpy types
import numpy as np
result = orjson.dumps(
    {"value": np.int64(42)},
    option=orjson.OPT_SERIALIZE_NUMPY,
)
```

### Fix 2: Handle NaN and Infinity values

```python
import orjson
import math

# Wrong — NaN not allowed by default
# orjson.dumps({"value": float("nan")})  # ValueError

# Correct — use option to allow non-finite floats
data = {"value": float("nan"), "other": float("inf")}
result = orjson.dumps(data, option=orjson.OPT_ALLOW_NAN)
print(result.decode())

# Or filter out NaN before serialization
clean_data = {k: v for k, v in data.items() if not (isinstance(v, float) and math.isnan(v))}
result = orjson.dumps(clean_data)
```

### Fix 3: Fix bytes and encoding issues

```python
import orjson

# Wrong — bytes not directly serializable
# orjson.dumps({"data": b"binary"})  # TypeError

# Correct — decode bytes to string first
data = {"raw": b"hello world"}
clean = {k: v.decode("utf-8") if isinstance(v, bytes) else v for k, v in data.items()}
result = orjson.dumps(clean)
print(result.decode())

# Handle mixed bytes/str
def clean_for_json(obj):
    if isinstance(obj, bytes):
        return obj.decode("utf-8", errors="replace")
    if isinstance(obj, dict):
        return {k: clean_for_json(v) for k, v in obj.items()}
    if isinstance(obj, list):
        return [clean_for_json(i) for i in obj]
    return obj

result = orjson.dumps(clean_for_json(data))
```

### Fix 4: Optimize serialization with options

```python
import orjson

# Wrong — default options may not suit your use case
# result = orjson.dumps(data)

# Correct — configure options for your needs
data = {"users": [{"name": "Alice", "active": True}, {"name": "Bob", "active": False}]}

# Compact output, sorted keys
result = orjson.dumps(
    data,
    option=orjson.OPT_SORT_KEYS | orjson.OPT_INDENT_2,
)

# Handle numpy arrays
import numpy as np
data_np = {"values": np.array([1, 2, 3])}
result = orjson.dumps(data_np, option=orjson.OPT_SERIALIZE_NUMPY)

# Non-ASCII strings
data_unicode = {"name": "日本語テスト"}
result = orjson.dumps(data_unicode)
print(result.decode())
```

## Common Scenarios

- **Custom objects** — Dataclasses and Pydantic models require explicit serialization hooks or `default` function.
- **NaN in float columns** — DataFrame columns with NaN values fail to serialize without `OPT_ALLOW_NAN`.
- **Binary data** — Bytes objects from database BLOBs or network responses need decoding before JSON serialization.

## Prevent It

- Always define a `default` handler when serializing objects with custom types.
- Use `orjson.dumps(data, option=orjson.OPT_SERIALIZE_NUMPY)` when working with NumPy arrays.
- Test serialization with representative data including edge cases like None, empty strings, and NaN.

## Related Errors

- [TypeError](/languages/python/typeerror/) — type not supported
- [ValueError](/languages/python/valueerror/) — out of range float value
- [UnicodeDecodeError](/languages/python/unicodedecodeerror/) — encoding failure
