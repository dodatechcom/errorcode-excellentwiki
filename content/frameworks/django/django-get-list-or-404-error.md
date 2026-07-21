---
title: "[Solution] Django get_list_or_404 Error"
description: "get_list_or_404 not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

get_list_or_404 not working.

## Common Causes

Wrong usage.

## How to Fix

Use correctly.

## Example

```python
from django.shortcuts import get_list_or_404
users = get_list_or_404(User, active=True)
```
