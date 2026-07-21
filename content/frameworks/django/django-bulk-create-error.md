---
title: "[Solution] Django Bulk Create Error"
description: "bulk_create not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

bulk_create not working.

## Common Causes

Wrong usage.

## How to Fix

Use correctly.

## Example

```python
User.objects.bulk_create([User(name='A'), User(name='B')])
```
