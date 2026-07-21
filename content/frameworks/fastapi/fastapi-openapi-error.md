---
title: "[Solution] FastAPI OpenAPI Error -- How to Fix"
description: "Fix FastAPI OpenAPI errors. Resolve schema generation, documentation, and specification issues."
frameworks: ["fastapi"]
error-types: ["api-error"]
severities: ["warning"]
weight: 5
comments: true
---

A FastAPI OpenAPI error occurs when the auto-generated OpenAPI schema has issues, missing endpoints, or incorrect type definitions.

## Why It Happens

OpenAPI errors happen due to circular type references, incorrect model definitions, missing response models, or custom type serialization issues.

## Common Error Messages

```
ValueError: schema_extra conflicts with existing keys
```

```
RecursionError: maximum recursion depth exceeded
```

```
TypeError: Object of type set is not JSON serializable
```

```
OpenAPIError: duplicate operationId
```

## How to Fix It

### 1. Customize OpenAPI Schema

Configure schema generation.

```python
app = FastAPI(
    title='My API',
    description='A sample API',
    version='1.0.0',
    openapi_tags=[{'name': 'users', 'description': 'User operations'}]
)

@app.get('/openapi.json')
async def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    from fastapi.openapi.utils import get_openapi
    app.openapi_schema = get_openapi(title='My API', version='1.0.0', routes=app.routes)
    return app.openapi_schema
```

### 2. Fix Schema Generation Issues

Handle complex types correctly.

```python
class UserResponse(BaseModel):
    id: int
    name: str
    tags: list[str]

    class Config:
        schema_extra = {'example': {'id': 1, 'name': 'John', 'tags': ['admin']}}
```

### 3. Add Response Models

Define response models for endpoints.

```python
@app.get('/users/{user_id}', response_model=UserResponse)
async def get_user(user_id: int):
    return UserResponse(id=user_id, name='John', tags=[])
```

### 4. Disable OpenAPI When Not Needed

Turn off for production.

```python
app = FastAPI(openapi_url=None if ENV == 'production' else '/openapi.json')
```

## Common Scenarios

**Scenario 1: Docs show missing endpoints.**
Check that endpoints have proper type hints.

**Scenario 2: Schema fails with recursion.**
Use `update_forward_refs()`.

**Scenario 3: Custom types not serialized.**
Add `schema_extra` to models.

## Prevent It

1. **Validate OpenAPI schema.**
Use Swagger UI to verify.

2. **Test API docs in CI.**
Generate and validate in tests.

3. **Keep models simple.**
Avoid complex nested structures.

