---
title: "[Solution] Flask Flask CORS Origin Error"
description: "CORS preflight failing."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

CORS preflight failing.

## Common Causes

Origin not allowed.

## How to Fix

Add origins.

## Example

```python
CORS(app, origins=['http://localhost:3000'])
```
