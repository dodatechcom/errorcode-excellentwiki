---
title: "[Solution] Flask Commit Error"
description: "Commit failing."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Commit failing.

## Common Causes

Validation error.

## How to Fix

Check data.

## Example

```python
try: db.session.commit()
except:
    db.session.rollback()
    raise
```
