---
title: "[Solution] Django QuerySet Error Django"
description: "QuerySet not evaluating."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

QuerySet not evaluating.

## Common Causes

Not evaluating.

## How to Fix

Evaluate queryset.

## Example

```python
users = list(User.objects.all())  # force evaluation
```
