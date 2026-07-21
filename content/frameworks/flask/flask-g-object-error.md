---
title: "[Solution] Flask G Object Error"
description: "G object not persisting."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

G object not persisting.

## Common Causes

Wrong storage.

## How to Fix

Use g attributes.

## Example

```python
from flask import g
@app.before_request
def load(): g.user = User.query.get(session['uid'])
```
