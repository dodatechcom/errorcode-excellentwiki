---
title: "[Solution] Django NoReverseMatch Error"
description: "Cannot reverse pattern."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Cannot reverse pattern.

## Common Causes

Wrong arguments.

## How to Fix

Check parameters.

## Example

```python
reverse('user-detail', args=[u.pk])
```
