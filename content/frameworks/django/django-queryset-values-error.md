---
title: "[Solution] Django QuerySet Values Error"
description: "values() not returning dict."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

values() not returning dict.

## Common Causes

Wrong usage.

## How to Fix

Use correctly.

## Example

```python
User.objects.values('name', 'email')
```
