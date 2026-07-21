---
title: "[Solution] Flask Current App Error"
description: "current_app not accessible."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

current_app not accessible.

## Common Causes

Outside context.

## How to Fix

Use within context.

## Example

```python
with app.app_context():
    db.init_app(current_app)
```
