---
title: "[Solution] FastAPI OpenAPI Docs Error"
description: "Fix FastAPI OpenAPI docs errors when Swagger UI or ReDoc fails to render or shows incorrect API documentation."
frameworks: ["fastapi"]
error-types: ["documentation-error"]
severities: ["error"]
---

When FastAPI's built-in documentation pages fail to load or display incorrectly, the OpenAPI schema is usually malformed.

## Common Causes

- Custom OpenAPI schema override has syntax errors
- Response model uses unsupported Pydantic types
- Circular model references break the schema generator
- Documentation disabled accidentally with `docs_url=None`
- Custom routes added to OpenAPI schema with invalid JSON

## How to Fix

### Verify Schema Generation

```python
from fastapi import FastAPI

app = FastAPI(
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

@app.get("/items")
def get_items():
    return [{"id": 1, "name": "Widget"}]

# Access schema at /openapi.json to verify
```

### Fix Circular References

```python
from pydantic import BaseModel
from typing import Optional

class Node(BaseModel):
    id: int
    children: list["Node"] = []

Node.model_rebuild()
```

### Disable Docs When Not Needed

```python
app = FastAPI(docs_url=None, redoc_url=None)
```

## Examples

```python
from fastapi import FastAPI

app = FastAPI()

# Bug -- custom route returns invalid JSON for OpenAPI
@app.get("/custom")
def custom():
    return {"openapi": "3.0.0"}  # Conflicts with built-in schema

# Fix -- use the built-in schema customization
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    schema = get_openapi(title="API", version="1.0", routes=app.routes)
    app.openapi_schema = schema
    return app.openapi_schema

app.openapi = custom_openapi
```
