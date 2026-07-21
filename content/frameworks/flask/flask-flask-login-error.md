---
title: "[Solution] Flask Flask-Login Error"
description: "Login not authenticating."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Login not authenticating.

## Common Causes

No user_loader.

## How to Fix

Implement loader.

## Example

```python
from flask_login import LoginManager
lm = LoginManager(app)
@lm.user_loader
def load(id): return User.query.get(int(id))
```
