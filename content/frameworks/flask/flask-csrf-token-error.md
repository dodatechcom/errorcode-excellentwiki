---
title: "[Solution] Flask CSRF Token Error"
description: "CSRF missing."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

CSRF missing.

## Common Causes

Not initialized.

## How to Fix

Initialize CSRFProtect.

## Example

```python
from flask_wtf.csrf import CSRFProtect
csrf = CSRFProtect(app)
```
