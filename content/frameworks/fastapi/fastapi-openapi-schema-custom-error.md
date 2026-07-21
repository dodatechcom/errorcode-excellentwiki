---
title: "[Solution] FastAPI OpenAPI Schema Custom Error"
description: "Fix FastAPI custom OpenAPI schema errors when generated documentation does not match actual API behavior."
frameworks: ["fastapi"]
error-types: ["documentation-error"]
severities: ["error"]
---

When customizing the OpenAPI schema in FastAPI, the documentation may show incorrect endpoint descriptions or missing models.

## Common Causes

- Overwriting the entire OpenAPI schema instead of merging with the default
- Custom response model overrides the auto-generated schema
- Response model annotations conflict with Pydantic model definitions
- Tags or descriptions not applied to the correct routes
- `openapi_extra` dict contains invalid schema properties

## How to Fix

### Customize Schema Incrementally

```python
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="My API",
        version="1.0.0",
        description="Custom API description",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://example.com/logo.png"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
```

## Examples

```python
from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

app = FastAPI()

# Bug -- this overwrites the entire schema
@app.get("/openapi.json")
def custom_schema():
    return {"openapi": "3.0.0", "info": {"title": "Custom", "version": "1.0"}}

# Correct -- customize the existing schema
def my_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    schema = get_openapi(title="Custom API", version="1.0.0", routes=app.routes)
    app.openapi_schema = schema
    return app.openapi_schema

app.openapi = my_openapi
```
