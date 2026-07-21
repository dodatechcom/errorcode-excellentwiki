---
title: "[Solution] Flask Teardown Request Error"
description: "Teardown not cleaning."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Teardown not cleaning.

## Common Causes

Resources not closed.

## How to Fix

Use teardown_request.

## Example

```python
@app.teardown_request
def teardown(exc=None): db.session.remove()
```
