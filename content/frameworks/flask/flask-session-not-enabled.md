---
title: "[Solution] Flask Session Not Enabled"
description: "Sessions not working."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Sessions not working.

## Common Causes

No secret key.

## How to Fix

Set secret key.

## Example

```python
app.secret_key = 'secret'
```
