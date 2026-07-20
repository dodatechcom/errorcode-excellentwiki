---
title: "[Solution] Python 3.11 tomllib Error — TOMLDecodeError, Parsing, Type Conversion"
description: "Fix Python 3.11 tomllib errors including TOMLDecodeError, parsing syntax errors, type conversion issues, and nested table problems."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 509
---

# Python 3.11 tomllib Error — TOMLDecodeError, Parsing, Type Conversion

Python 3.11 added `tomllib` to the standard library for reading TOML files. `TOMLDecodeError` occurs when TOML syntax is invalid, types don't match expectations, or nested structures have issues. Writing TOML is not supported - use `tomli_w` for that.

## Common Causes

```python
# Cause 1: Invalid TOML syntax
import tomllib
data = tomllib.loads("""
[server
host = "localhost"
""")  # TOMLDecodeError: missing closing bracket

# Cause 2: Duplicate keys
data = tomllib.loads("""
key = "first"
key = "second"
""")  # TOMLDecodeError: duplicate key

# Cause 3: Missing quotes around strings
data = tomllib.loads('name = hello')  # TOMLDecodeError

# Cause 4: Invalid inline table syntax
data = tomllib.loads('config = {key = value}')  # TOMLDecodeError

# Cause 5: Bad date/time format
data = tomllib.loads('date = 2024-13-01')  # TOMLDecodeError: invalid month
```

## How to Fix

### Fix 1: Validate TOML syntax before parsing

```python
import tomllib

# Wrong - no error handling
with open("config.toml", "rb") as f:
    data = tomllib.load(f)  # Raises TOMLDecodeError on bad syntax

# Correct - handle parse errors
try:
    with open("config.toml", "rb") as f:
        data = tomllib.load(f)
except tomllib.TOMLDecodeError as e:
    print(f"TOML syntax error at line {e.lineno}, column {e.colno}: {e.msg}")
```

### Fix 2: Fix duplicate keys

```python
# Wrong - duplicate keys in TOML
toml_str = """
[server]
host = "localhost"
port = 8080

[server]
host = "0.0.0.0"
"""

# Correct - use dotted keys or nested tables
toml_str = """
[server]
host = "localhost"
port = 8080

[server.backup]
host = "0.0.0.0"
"""
data = tomllib.loads(toml_str)
```

### Fix 3: Fix string quoting

```python
# Wrong - unquoted string value
bad_toml = 'name = hello'

# Correct - quote all string values
good_toml = 'name = "hello"'

# For strings with special characters, use quotes
good_toml = 'path = "C:\\Users\\test"'
good_toml = 'message = "Hello \"world\""'
```

### Fix 4: Fix inline table syntax

```python
# Wrong - missing quotes in inline table
bad_toml = 'config = {key = value}'

# Correct - proper inline table syntax
good_toml = 'config = {key = "value"}'

# Multi-line inline tables (TOML 1.0)
good_toml = """
config = {
    key = "value",
    number = 42
}
"""
data = tomllib.loads(good_toml)
```

### Fix 5: Validate date/time formats

```python
# Wrong - invalid date
bad_toml = 'date = 2024-13-01'  # Month 13 doesn't exist

# Correct - valid RFC 3339 date/time
good_toml = 'date = 2024-01-15'
good_toml = 'datetime = 2024-01-15T10:30:00Z'
good_toml = 'time = 10:30:00'
data = tomllib.loads(good_toml)
```

## Examples

```python
# Reading a pyproject.toml
import tomllib

with open("pyproject.toml", "rb") as f:
    config = tomllib.load(f)

name = config["project"]["name"]
version = config["project"]["version"]
deps = config["project"]["dependencies"]

# Safe config loading with defaults
def load_config(path, defaults=None):
    try:
        with open(path, "rb") as f:
            return tomllib.load(f)
    except FileNotFoundError:
        return defaults or {}
    except tomllib.TOMLDecodeError as e:
        raise ValueError(f"Invalid TOML in {path}: {e}") from e

config = load_config("config.toml", defaults={"server": {"port": 8080}})

# Nested table access
toml_str = """
[database]
host = "localhost"
port = 5432

[database.credentials]
user = "admin"
password = "secret"
"""
data = tomllib.loads(toml_str)
db_host = data["database"]["host"]
db_user = data["database"]["credentials"]["user"]
```

## Related Errors

- [jsondecodeerror](../jsondecodeerror) — JSON parsing errors
- [python311-deprecation](../python311-deprecation) — Python 3.11 changes
- [ValueError](../valueerror) — Invalid values in parsed data
- [FileNotFoundError](../filenotfounderror) — Missing TOML files
