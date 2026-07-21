---
title: "[Solution] Django Update Error"
description: "update() not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

update() not working.

## Common Causes

Wrong usage.

## How to Fix

Use on queryset.

## Example

```python
User.objects.filter(active=False).update(active=True)
```
