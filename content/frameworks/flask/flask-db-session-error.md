---
title: "[Solution] Flask DB Session Error"
description: "Session not committing."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Session not committing.

## Common Causes

Missing commit.

## How to Fix

Use commit.

## Example

```python
db.session.add(user)
db.session.commit()
```
