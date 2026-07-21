---
title: "[Solution] Django QuerySet Empty Error"
description: "QuerySet unexpectedly empty."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

QuerySet unexpectedly empty.

## Common Causes

Wrong filter.

## How to Fix

Check filters.

## Example

```python
users = User.objects.all()
if not users.exists(): print('No users')
```
