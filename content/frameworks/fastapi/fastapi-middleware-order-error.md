---
title: "[Solution] FastAPI Middleware Order Error"
description: "Middleware wrong order."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Middleware wrong order.

## Common Causes

Wrong addition order.

## How to Fix

Last added runs first.

## Example

```python
app.add_middleware(A)  # runs second
app.add_middleware(B)  # runs first
```
