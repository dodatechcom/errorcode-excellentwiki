---
title: "[Solution] Django Order By Error"
description: "order_by not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

order_by not working.

## Common Causes

Wrong field.

## How to Fix

Use correct field.

## Example

```python
User.objects.order_by('-created_at', 'name')
```
