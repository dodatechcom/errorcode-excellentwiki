---
title: "[Solution] Django Values List Error"
description: "values_list wrong."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

values_list wrong.

## Common Causes

Wrong usage.

## How to Fix

Use correctly.

## Example

```python
User.objects.values_list('name', flat=True)
```
