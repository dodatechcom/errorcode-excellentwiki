---
title: "[Solution] FastAPI Custom OpenAPI Error"
description: "Custom OpenAPI schema failing."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Custom OpenAPI schema failing.

## Common Causes

Wrong override.

## How to Fix

Override correctly.

## Example

```python
def custom_openapi():
    if app.openapi_schema: return app.openapi_schema
    app.openapi_schema = get_openapi(...)
    return app.openapi_schema
app.openapi = custom_openapi
```
