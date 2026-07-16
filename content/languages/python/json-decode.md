---
title: "[Solution] Python json.JSONDecodeError — Invalid JSON"
description: "Fix Python json.JSONDecodeError when parsing invalid JSON. Learn common JSON parsing errors and how to handle them properly."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["json", "decode", "jsondecodeerror", "parse"]
weight: 5
---

# json.JSONDecodeError — Invalid JSON

A `json.JSONDecodeError` is raised when `json.loads()` or `json.load()` receives a string that is not valid JSON. This includes syntax errors like trailing commas, single quotes, unquoted keys, or malformed data.

## Description

JSON has strict syntax rules. Unlike Python dictionaries, JSON requires double quotes for strings, does not allow trailing commas, and does not support comments. `json.JSONDecodeError` inherits from `ValueError` and includes the line number and position of the error.

Common patterns:

- **Trailing commas** — `{"key": "value",}` (invalid in JSON).
- **Single quotes** — `{'key': 'value'}` (Python dict syntax, not JSON).
- **Unquoted keys** — `{key: "value"}`.
- **Comments in JSON** — `// comment` or `/* comment */`.
- **Empty string or None** — `json.loads("")` or `json.loads(None)`.

## Common Causes

```python
import json

# Cause 1: Trailing comma
json.loads('{"key": "value",}')  # JSONDecodeError

# Cause 2: Single quotes
json.loads("{'key': 'value'}")  # JSONDecodeError

# Cause 3: Unquoted keys
json.loads('{key: "value"}')  # JSONDecodeError

# Cause 4: Python dict syntax
data = {"key": "value"}
json_string = str(data)  # "{'key': 'value'}" — single quotes!
json.loads(json_string)  # JSONDecodeError

# Cause 5: Empty string
json.loads("")  # JSONDecodeError
```

## Solutions

### Fix 1: Use proper JSON syntax

```python
import json

# Wrong — trailing comma
json.loads('{"key": "value",}')

# Correct — no trailing comma
json.loads('{"key": "value"}')
```

### Fix 2: Use json.dumps() to create valid JSON strings

```python
import json

# Wrong — using str() on a dict
data = {"key": "value"}
json_string = str(data)  # "{'key': 'value'}" — invalid JSON

# Correct — use json.dumps()
json_string = json.dumps(data)  # '{"key": "value"}' — valid JSON
```

### Fix 3: Handle encoding issues

```python
import json

# Wrong — unescaped characters
json.loads('{"path": "C:\new\file"}')  # JSONDecodeError

# Correct — escape backslashes
json.loads('{"path": "C:\\new\\file"}')

# Or use raw strings
json.loads(r'{"path": "C:\new\file"}')
```

### Fix 4: Validate JSON before parsing

```python
import json

def safe_parse(json_string):
    try:
        return json.loads(json_string), True
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        return None, False

data, valid = safe_parse('{"key": "value"}')
if valid:
    print(data)
```

### Fix 5: Use json.loads with strict=False for more lenient parsing

```python
import json

# Default strict parsing
json.loads('{"key": "value"}')  # Works

# More lenient (allows control characters)
json.loads('{"key": "value"}', strict=False)
```

## Related Errors

- [JSON encode](json-encode) — serializing objects to JSON.
- [ValueError](../valueerror) — general value errors.
- [TypeError](../typeerror) — general type errors.
