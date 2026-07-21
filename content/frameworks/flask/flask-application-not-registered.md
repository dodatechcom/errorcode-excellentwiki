---
title: "[Solution] Flask Application Not Registered"
description: "App context not set up."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

App context not set up.

## Common Causes

Accessing outside request.

## How to Fix

Create and configure app.

## Example

```python
from flask import Flask
app = Flask(__name__)
with app.app_context(): pass
```
