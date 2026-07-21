---
title: "[Solution] Flask Current User Error"
description: "current_user not expected."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

current_user not expected.

## Common Causes

Not logged in.

## How to Fix

Check auth.

## Example

```python
from flask_login import current_user
if current_user.is_authenticated: pass
```
