---
title: "[Solution] Django Login Required Error"
description: "Not redirecting."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

Not redirecting.

## Common Causes

LOGIN_URL not set.

## How to Fix

Set URL.

## Example

```python
LOGIN_URL = '/login/'
```
