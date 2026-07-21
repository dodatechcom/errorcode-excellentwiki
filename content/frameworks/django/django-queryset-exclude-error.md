---
title: "[Solution] Django QuerySet Exclude Error"
description: "Exclude not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Exclude not working.

## Common Causes

Wrong syntax.

## How to Fix

Use exclude.

## Example

```python
User.objects.exclude(is_active=False)
```
