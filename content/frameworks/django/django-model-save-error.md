---
title: "[Solution] Django Model Save Error"
description: "save() failing."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

save() failing.

## Common Causes

Validation error.

## How to Fix

Check validations.

## Example

```python
try: user.save()
except IntegrityError: pass
```
