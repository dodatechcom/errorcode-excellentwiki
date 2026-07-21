---
title: "[Solution] Flask Rollback Error"
description: "Rollback not working."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Rollback not working.

## Common Causes

Not in except.

## How to Fix

Use in except.

## Example

```python
try: db.session.commit()
except:
    db.session.rollback()
    raise
```
