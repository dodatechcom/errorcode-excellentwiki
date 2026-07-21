---
title: "[Solution] Django Distinct Error"
description: "distinct() not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

distinct() not working.

## Common Causes

Wrong usage.

## How to Fix

Use on queryset.

## Example

```python
User.objects.values('role').distinct()
```
