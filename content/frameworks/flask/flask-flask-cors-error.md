---
title: "[Solution] Flask Flask-CORS Error"
description: "CORS not allowing."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

CORS not allowing.

## Common Causes

Not configured.

## How to Fix

Add CORS.

## Example

```python
from flask_cors import CORS
CORS(app, resources={r'/api/*': {'origins': '*'}})
```
