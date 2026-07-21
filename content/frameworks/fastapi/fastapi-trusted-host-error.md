---
title: "[Solution] FastAPI Trusted Host Error"
description: "Request rejected by host."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Request rejected by host.

## Common Causes

Host not trusted.

## How to Fix

Add host.

## Example

```python
from fastapi.middleware.trustedhost import TrustedHostMiddleware
app.add_middleware(TrustedHostMiddleware, allowed_hosts=['example.com'])
```
