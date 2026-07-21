---
title: "[Solution] Flask Flask Config Debug Error"
description: "Debug mode on in prod."
frameworks: ["flask"]
error-types: ["framework-error"]
severities: ["error"]
---

Debug mode on in prod.

## Common Causes

DEBUG=True.

## How to Fix

Set False.

## Example

```python
app.config['DEBUG'] = False
```
