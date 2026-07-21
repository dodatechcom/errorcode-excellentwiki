---
title: "[Solution] Django QuerySet Values List Dict Error"
description: "values_list not returning tuples."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

values_list not returning tuples.

## Common Causes

Wrong usage.

## How to Fix

Use correctly.

## Example

```python
User.objects.values_list('name', 'email')
```
