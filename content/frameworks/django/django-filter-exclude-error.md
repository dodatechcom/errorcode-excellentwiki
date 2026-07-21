---
title: "[Solution] Django Filter Exclude Error"
description: "filter/exclude wrong."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

filter/exclude wrong.

## Common Causes

Wrong syntax.

## How to Fix

Use correct syntax.

## Example

```python
User.objects.filter(age__gte=18).exclude(role='admin')
```
