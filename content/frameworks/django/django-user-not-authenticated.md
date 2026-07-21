---
title: "[Solution] Django User Not Authenticated"
description: "AnonymousUser error."
frameworks: ["django"]
error-types: ["framework-error"]
severities: ["error"]
---

AnonymousUser error.

## Common Causes

Not logged in.

## How to Fix

Check auth.

## Example

```python
if request.user.is_authenticated: pass
```
