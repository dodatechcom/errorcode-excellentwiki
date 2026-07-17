---
title: "[Solution] Python KeyError — Dictionary Key Not Found Fix"
description: "Fix Python KeyError when accessing dictionary keys. Use .get(), dict.setdefault(), or check membership before accessing keys."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 30
---

# KeyError — Dictionary Key Not Found Fix

A `KeyError` is raised when you try to access a dictionary key that does not exist. This happens with bracket notation `dict[key]` — the key is simply absent from the dictionary.

## Description

Unlike `TypeError` or `ValueError`, `KeyError` is specific to mapping types (dict, defaultdict, OrderedDict, etc.). It only fires with bracket notation; `.get()` never raises it.

Common scenarios:

- **Typo in key name** — `data["useername"]` instead of `data["username"]`.
- **Key only exists conditionally** — the key is set inside an `if` branch that didn't execute.
- **Nested dict access** — `data["level1"]["level2"]` where `level2` doesn't exist inside `level1`.
- **Key deleted between check and access** — race condition in concurrent code.

## Common Causes

```python
# Cause 1: Typo in key name
config = {"database": "postgres", "port": 5432}
db = config["databse"]  # KeyError: 'databse'

# Cause 2: Key set conditionally
data = {}
if some_condition:
    data["result"] = compute()
print(data["result"])  # KeyError if condition was False

# Cause 3: Nested key missing
users = {"alice": {"age": 30}}
print(users["alice"]["email"])  # KeyError: 'email'

# Cause 4: Using pop() without a default on a missing key
data = {"a": 1}
value = data.pop("b")  # KeyError: 'b'
```

## Solutions

### Fix 1: Use .get() with a default value

```python
# Wrong
config = {"database": "postgres", "port": 5432}
db = config["databse"]

# Correct
db = config.get("databse", "sqlite")  # Returns "sqlite" if key missing
```

### Fix 2: Check membership with 'in' before accessing

```python
# Wrong
data = {"name": "Alice"}
print(data["age"])

# Correct
if "age" in data:
    print(data["age"])
else:
    print("Age not available")
```

### Fix 3: Use try/except for expected missing keys

```python
# Wrong
raw_config = {}
host = raw_config["host"]

# Correct
try:
    host = raw_config["host"]
except KeyError:
    host = "localhost"
    print("Host not configured, using default")
```

### Fix 4: Use defaultdict for automatic key creation

```python
from collections import defaultdict

# Wrong — requires manual initialization
word_counts = {}
for word in ["apple", "banana", "apple"]:
    word_counts[word] += 1  # KeyError on first access

# Correct — defaultdict creates default values automatically
word_counts = defaultdict(int)
for word in ["apple", "banana", "apple"]:
    word_counts[word] += 1
print(dict(word_counts))  # {'apple': 2, 'banana': 1}
```

### Fix 5: Safely access nested dictionaries

```python
# Wrong
users = {"alice": {"age": 30}}
email = users["alice"]["email"]

# Correct — chain .get() calls
email = users.get("alice", {}).get("email", "unknown")

# Alternative using a helper function
def safe_get(d, *keys, default=None):
    for key in keys:
        if isinstance(d, dict):
            d = d.get(key, default)
        else:
            return default
    return d

email = safe_get(users, "alice", "email", default="unknown")
```

### Fix 6: Use setdefault for one-time key initialization

```python
# Wrong
groups = {}
for name, team in [("Alice", "red"), ("Bob", "blue"), ("Carol", "red")]:
    groups[team].append(name)  # KeyError on first append per team

# Correct
groups = {}
for name, team in [("Alice", "red"), ("Bob", "blue"), ("Carol", "red")]:
    groups.setdefault(team, []).append(name)
print(groups)  # {'red': ['Alice', 'Carol'], 'blue': ['Bob']}
```

## Related Errors

- [IndexError](../indexerror) — index out of range for lists/sequences.
- [TypeError](../typeerror) — wrong type passed to a function.
- [AttributeError](../attributeerror) — attribute not found on an object.
