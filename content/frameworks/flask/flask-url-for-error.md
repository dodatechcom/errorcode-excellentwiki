---
title: "[Solution] Flask url_for Error"
description: "url_for raises BuildError."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

url_for raises BuildError.

## Common Causes

Wrong endpoint name.

## How to Fix

Check names.

## Example

```python
@app.route('/u/<int:id>')
def u(id): pass
url_for('u', id=42)
```
