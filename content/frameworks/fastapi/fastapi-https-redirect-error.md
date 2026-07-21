---
title: "[Solution] FastAPI HTTPS Redirect Error"
description: "HTTP not redirecting to HTTPS."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

HTTP not redirecting to HTTPS.

## Common Causes

Not configured.

## How to Fix

Add middleware.

## Example

```python
from fastapi.middleware.httpsredirect import HTTPSRedirectMiddleware
app.add_middleware(HTTPSRedirectMiddleware)
```
