---
title: "[Solution] Python JSON Error — Serialization and Parsing Issues"
description: "Fix JSON errors by doing X, Y, Z. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 611
---

# Python JSON Error — Serialization and Parsing Issues

JSON errors include decoding malformed input, handling non-serializable types, and managing special float values like NaN and Infinity. These commonly arise in API integrations and data processing pipelines.

## Common Causes

```python
# Cause 1: Trailing comma in JSON (not valid JSON, but common mistake)
import json

json_str = '{"name": "Alice", "age": 30,}'
data = json.loads(json_str)  # JSONDecodeError: Expecting ',' delimiter
```

```python
# Cause 2: Single quotes instead of double quotes
import json

json_str = "{'name': 'Alice', 'age': 30}"
data = json.loads(json_str)  # JSONDecodeError: Expecting property name enclosed in double quotes
```

```python
# Cause 3: NaN and Infinity not handled by default encoder
import json
import math

data = {"value": float('nan'), "limit": float('infinity')}
json_str = json.dumps(data)  # Outputs "NaN" and "Infinity" — not valid JSON!
```

```python
# Cause 4: Non-serializable types (datetime, bytes, custom objects)
import json
from datetime import datetime

data = {
    "timestamp": datetime.now(),  # datetime is not JSON serializable
    "data": b"binary"  # bytes is not JSON serializable
}
json_str = json.dumps(data)  # TypeError: Object of type datetime is not JSON serializable
```

```python
# Cause 5: JSON decoder fails on empty or None input
import json

json_str = ""
data = json.loads(json_str)  # JSONDecodeError: Expecting value: line 1 column 1

json_str = "null"
data = json.loads(json_str)  # Returns None — not always an error, but unexpected
```

## How to Fix

### Fix 1: Use json.loads with Strict Mode Disabled

```python
import json

# Allow single quotes and trailing commas (non-standard but common)
json_str = "{'name': 'Alice', 'age': 30,}"
# Won't work with json.loads — use a preprocessor instead
json_str_clean = json_str.replace("'", '"').rstrip().rstrip(',').rstrip()
data = json.loads(json_str_clean)

# Or use a tolerant parser for non-standard JSON
import ast
data = ast.literal_eval(json_str)  # Handles single quotes but less safe
```

### Fix 2: Handle NaN and Infinity Explicitly

```python
import json
import math

data = {"value": float('nan'), "limit": float('inf')}

# Option 1: Replace NaN/Infinity before serialization
def sanitize_for_json(obj):
    if isinstance(obj, float):
        if math.isnan(obj):
            return None
        if math.isinf(obj):
            return None
    return obj

json_str = json.dumps(data, default=sanitize_for_json)

# Option 2: Use allow_nan=False to raise error on bad floats
json_str = json.dumps(data, allow_nan=False)  # ValueError: Out of range float values
```

### Fix 3: Use a Custom Default Encoder for Non-Serializable Types

```python
import json
from datetime import datetime, date
from decimal import Decimal
import uuid

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, date):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return float(obj)
        if isinstance(obj, uuid.UUID):
            return str(obj)
        if isinstance(obj, bytes):
            return obj.decode('utf-8', errors='replace')
        return super().default(obj)

data = {
    "timestamp": datetime.now(),
    "id": uuid.uuid4(),
    "amount": Decimal("19.99"),
    "raw": b"binary data"
}
json_str = json.dumps(data, cls=CustomEncoder, indent=2)
```

### Fix 4: Use object_hook for Custom Deserialization

```python
import json
from datetime import datetime

def deserialize_obj(dct):
    """Convert ISO date strings back to datetime objects."""
    for key, value in dct.items():
        if isinstance(value, str):
            try:
                dct[key] = datetime.fromisoformat(value)
            except (ValueError, TypeError):
                pass
    return dct

json_str = '{"name": "Alice", "created": "2024-01-15T10:30:00"}'
data = json.loads(json_str, object_hook=deserialize_obj)
print(type(data['created']))  # <class 'datetime.datetime'>
```

### Fix 5: Validate JSON Input Before Parsing

```python
import json

def safe_json_loads(json_str, default=None):
    """Safely parse JSON with fallback value."""
    if not json_str or not isinstance(json_str, str):
        return default

    try:
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}")
        return default

# Usage
data = safe_json_loads("")  # Returns None
data = safe_json_loads("not json")  # Returns None
data = safe_json_loads('{"valid": true}')  # Returns dict
```

## Examples

```python
# Robust JSON API response handler
import json
import requests

def api_request(url, data=None):
    try:
        response = requests.post(url, json=data, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"HTTP error: {e}")
        return None

    try:
        return response.json()
    except json.JSONDecodeError as e:
        print(f"Invalid JSON response: {e}")
        print(f"Raw content: {response.text[:200]}")
        return None

# Stream large JSON files without loading entire file into memory
import ijson  # pip install ijson

def parse_large_json(filepath):
    with open(filepath, 'rb') as f:
        for record in ijson.items(f, 'records.item'):
            yield record
```

## Related Errors

- [Python TypeError](/languages/python/typeerror/) — Type-related errors
- [Python ValueError](/languages/python/valueerror/) — Value errors
- [Python UnicodeDecodeError](/languages/python/unicodedecodeerror/) — Encoding errors
- [Python PicklingError](/languages/python/pickling-error/) — Serialization errors
