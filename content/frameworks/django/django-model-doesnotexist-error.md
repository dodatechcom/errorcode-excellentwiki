---
title: "[Solution] Django Model DoesNotExist Error"
description: "DoesNotExist not caught."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

DoesNotExist not caught.

## Common Causes

Not handling.

## How to Fix

Handle exception.

## Example

```python
try:
    user = User.objects.get(pk=1)
except User.DoesNotExist:
    pass
```
