---
title: "[Solution] Flask DB Create All Error"
description: "db.create_all not creating."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

db.create_all not creating.

## Common Causes

Model not imported.

## How to Fix

Import models.

## Example

```python
with app.app_context():
    from models import User
    db.create_all()
```
