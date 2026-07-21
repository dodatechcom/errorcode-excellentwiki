---
title: "[Solution] Django Admin Site URL Error"
description: "Admin URL not accessible."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Admin URL not accessible.

## Common Causes

Wrong URL.

## How to Fix

Check urls.

## Example

```python
path('admin/', admin.site.urls)
```
