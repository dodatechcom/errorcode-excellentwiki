---
title: "[Solution] Python JSONDecodeError: Expecting Value — Invalid JSON Fix"
description: "Fix Python JSONDecodeError: Expecting value. Handle empty responses, trailing commas, single quotes, and encoding issues when parsing JSON."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 5
---

# JSONDecodeError: Expecting Value

A `json.JSONDecodeError: Expecting value: line 1 column 1 (char 0)` is raised when `json.loads()` receives a string that does not contain valid JSON. The most common cause is receiving an empty response, HTML error page, or non-JSON data when expecting JSON.

## Description

JSON has strict syntax requirements. `json.JSONDecodeError` inherits from `ValueError` and includes the line number and character position where parsing failed. The error message `Expecting value` specifically means the parser expected a JSON value (string, number, object, array, `true`, `false`, or `null`) but found something else.

Common variants:

- `Expecting value: line 1 column 1 (char 0)` — empty string or HTML response
- `Expecting property name enclosed in double quotes` — single quotes or unquoted keys
- `Expecting value: line N column M` — syntax error at specific position

## Common Causes

```python
import json

# Cause 1: Empty string from API
response_text = ""
data = json.loads(response_text)  # JSONDecodeError: Expecting value

# Cause 2: HTML error page instead of JSON
response_text = "<html><body>403 Forbidden</body></html>"
data = json.loads(response_text)  # JSONDecodeError

# Cause 3: Single quotes (Python dict syntax, not JSON)
data = json.loads("{'key': 'value'}")  # JSONDecodeError

# Cause 4: Trailing commas
data = json.loads('{"key": "value",}')  # JSONDecodeError

# Cause 5: BOM (Byte Order Mark) at start
data = json.loads('\ufeff{"key": "value"}')  # JSONDecodeError

# Cause 6: Python dict converted with str() instead of json.dumps()
data = json.loads(str({"key": "value"}))  # JSONDecodeError (single quotes)
```

## How to Fix

### Fix 1: Validate the response before parsing

```python
import requests
import json

# Wrong
response = requests.get("https://api.example.com/data")
data = response.json()  # May throw JSONDecodeError

# Correct
response = requests.get("https://api.example.com/data")
if response.status_code == 200:
    try:
        data = response.json()
    except json.JSONDecodeError:
        print(f"Invalid JSON response: {response.text[:200]}")
else:
    print(f"HTTP error: {response.status_code}")
```

### Fix 2: Handle empty strings

```python
import json

# Wrong
data = json.loads("")  # JSONDecodeError

# Correct
text = ""
if text.strip():
    data = json.loads(text)
else:
    data = None
    print("Empty JSON response")
```

### Fix 3: Fix Python dict to JSON conversion

```python
import json

# Wrong — str() produces single quotes
data = {"key": "value"}
json_str = str(data)  # "{'key': 'value'}"
json.loads(json_str)  # JSONDecodeError

# Correct — json.dumps() produces valid JSON
json_str = json.dumps(data)  # '{"key": "value"}'
json.loads(json_str)
```

### Fix 4: Strip BOM and whitespace

```python
import json

# Wrong
text = '\ufeff{"key": "value"}'
data = json.loads(text)  # JSONDecodeError

# Correct
text = '\ufeff{"key": "value"}'
text = text.encode().decode('utf-8-sig')  # Strips BOM
data = json.loads(text.strip())
```

### Fix 5: Use a safe parsing helper

```python
import json

def safe_json_loads(text, default=None):
    try:
        return json.loads(text) if text.strip() else default
    except json.JSONDecodeError as e:
        print(f"JSON parse error at line {e.lineno}, col {e.colno}: {e.msg}")
        return default

# Usage
data = safe_json_loads('{"key": "value"}')  # Returns dict
data = safe_json_loads("")  # Returns None
data = safe_json_loads("not json", default={})  # Returns {}
```

## Examples

This error commonly occurs when:

- An API returns an HTML login page instead of JSON data
- The request was rate-limited and returned an HTML error page
- A proxy server intercepted the request and returned its own response
- The response body is empty (e.g., DELETE request with no body)

## Related Errors

- [ValueError](valueerror) — invalid value passed to a function
- [TypeError](typeerror) — wrong type used in an operation
- [UnicodeDecodeError](unicodedecodeerror) — encoding issue in the response text
