---
title: "[Solution] Python RuntimeError — dictionary changed size during iteration"
description: "Fix Python RuntimeError: dictionary changed size during iteration. Learn safe patterns for modifying dicts while iterating."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
weight: 704
---

# Python RuntimeError — dictionary changed size during iteration

A `RuntimeError` with the message `dictionary changed size during iteration` is raised when you add or remove keys from a dictionary while iterating over it. Python detects that the dictionary's internal structure has changed during iteration and raises this error to prevent undefined behavior.

## Common Causes

```python
# Cause 1: Adding keys during iteration
data = {"a": 1, "b": 2, "c": 3}
for key in data:
    data["new_key"] = 4  # RuntimeError: dictionary changed size during iteration

# Cause 2: Removing keys during iteration
data = {"a": 1, "b": 2, "c": 3}
for key in data:
    if data[key] == 2:
        del data[key]  # RuntimeError: dictionary changed size during iteration

# Cause 3: Modifying a dict while iterating over its keys()
data = {"a": 1, "b": 2, "c": 3}
for key in data.keys():
    if key == "b":
        data["d"] = 4  # RuntimeError

# Cause 4: Modifying during .items() iteration
data = {"a": 1, "b": 2, "c": 3}
for key, value in data.items():
    if value == 1:
        data["d"] = 4  # RuntimeError

# Cause 5: Modifying dict inside a list comprehension that references it
data = {"a": 1, "b": 2}
result = [data.pop(k) for k in list(data)]  # This actually works (list(data) snapshot)
# But this doesn't:
result = [data.pop(k) for k in data]  # RuntimeError
```

## How to Fix

### Fix 1: Iterate over a copy of the dictionary

```python
# Wrong
data = {"a": 1, "b": 2, "c": 3}
for key in data:
    if data[key] == 2:
        del data[key]  # RuntimeError

# Correct — iterate over a copy
data = {"a": 1, "b": 2, "c": 3}
for key in list(data.keys()):
    if data[key] == 2:
        del data[key]  # Works fine

print(data)  # {'a': 1, 'c': 3}
```

### Fix 2: Collect items to modify, then apply changes

```python
# Wrong
data = {"a": 1, "b": 2, "c": 3}
for key in data:
    data[key] = data[key] * 2  # Works for value changes, not size changes

# Correct — collect modifications first
data = {"a": 1, "b": 2, "c": 3}
keys_to_remove = [k for k, v in data.items() if v == 2]
for key in keys_to_remove:
    del data[key]

print(data)  # {'a': 1, 'c': 3}
```

### Fix 3: Use dictionary comprehension to create a new dict

```python
# Wrong
data = {"a": 1, "b": 2, "c": 3}
for key in data:
    if data[key] % 2 == 0:
        del data[key]  # RuntimeError

# Correct — use dictionary comprehension
data = {"a": 1, "b": 2, "c": 3}
data = {k: v for k, v in data.items() if v % 2 != 0}
print(data)  # {'a': 1, 'c': 3}
```

### Fix 4: Use .copy() pattern for adding during iteration

```python
# Wrong
data = {"a": 1, "b": 2}
for key in data:
    data[f"{key}_copy"] = data[key]  # RuntimeError

# Correct — use .copy()
data = {"a": 1, "b": 2}
for key in list(data.keys()):
    data[f"{key}_copy"] = data[key]

print(data)  # {'a': 1, 'b': 2, 'a_copy': 1, 'b_copy': 2}
```

## Examples

```python
# Real-world: Filtering configuration dict
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True,
    "secret": "abc123",
    "verbose": False,
}

# Wrong — can't delete during iteration
for key in config:
    if not config[key]:
        del config[key]

# Correct — collect keys to remove
keys_to_remove = [k for k, v in config.items() if not v]
for key in keys_to_remove:
    del config[key]

print(config)  # {'host': 'localhost', 'port': 8080, 'debug': True, 'secret': 'abc123'}

# Real-world: Merging dictionaries during iteration
base = {"a": 1, "b": 2}
overrides = {"b": 3, "c": 4}

# Apply overrides
for key, value in overrides.items():
    base[key] = value  # This works — we're changing values, not adding new keys
# But for new keys:
for key, value in overrides.items():
    if key not in base:
        base[key] = value  # This also works — adding one at a time

# Actually, the simplest way:
base.update(overrides)
print(base)  # {'a': 1, 'b': 3, 'c': 4}
```

## Related Errors

- [List changed size during iteration](list-changed-size) — same error for lists.
- [Set changed size during iteration](set-changed-size) — same error for sets.
- [RuntimeError](../runtimeerror) — general runtime errors.
