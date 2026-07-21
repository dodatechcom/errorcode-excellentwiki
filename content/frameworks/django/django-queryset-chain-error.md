---
title: "[Solution] Django QuerySet Chain Error"
description: "QuerySet chain not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

QuerySet chain not working.

## Common Causes

Wrong chaining.

## How to Fix

Chain correctly.

## Example

```python
User.objects.filter(active=True).order_by('name').select_related('profile')
```
