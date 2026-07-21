---
title: "[Solution] Flask Flask Session Secret Error"
description: "Session secret not set."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Session secret not set.

## Common Causes

No secret.

## How to Fix

Set secret.

## Example

```python
app.secret_key = os.urandom(24)
```
