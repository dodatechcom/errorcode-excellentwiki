---
title: "[Solution] Flask Application Context Error"
description: "Context not active."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Context not active.

## Common Causes

Using current_app outside.

## How to Fix

Push context first.

## Example

```python
with app.app_context():
    current_app.config['K'] = 'v'
```
