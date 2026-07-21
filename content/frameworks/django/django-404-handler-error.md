---
title: "[Solution] Django 404 Handler Error"
description: "Custom 404 not working."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Custom 404 not working.

## Common Causes

Not configured.

## How to Fix

Configure handler.

## Example

```python
handler404 = 'myapp.views.custom_404'
```
