---
title: "[Solution] FastAPI Path Converter Error"
description: "Fix FastAPI path converter errors when path parameters do not match the expected type conversion."
frameworks: ["fastapi"]
error-types: ["validation-error"]
severities: ["error"]
---

FastAPI uses path converters to automatically convert URL path parameters to Python types. When a URL segment does not match the expected type, a 422 Validation Error is returned.

## Common Causes

- URL contains a string where an `int` path parameter is expected
- Path parameter uses `float` but receives non-numeric characters
- UUID path parameter receives an invalid UUID format
- Boolean path parameter receives values other than `true` or `false`
- Custom path converter fails to parse the URL segment

## How to Fix

### Use Correct Type Annotations

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

@app.get("/items/{item_uuid}")
def get_item(item_uuid: str):
    return {"item_uuid": item_uuid}
```

### Use Path Parameters with Regex Constraints

```python
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/products/{product_code}")
def get_product(
    product_code: str = Path(pattern="^[A-Z]{2}-\\d{4}$")
):
    return {"product_code": product_code}
```

## Examples

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id}
```

Requesting `/items/abc` returns a 422 error because `"abc"` is not a valid integer. Change the parameter type to `str` if non-numeric values are valid.
