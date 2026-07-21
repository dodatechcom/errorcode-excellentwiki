---
title: "[Solution] FastAPI Path Parameter Regex Error"
description: "Fix FastAPI path parameter regex errors when URL patterns with regular expressions fail to match."
frameworks: ["fastapi"]
error-types: ["validation-error"]
severities: ["error"]
---

When using regex patterns for path parameters in FastAPI, URLs may fail to match if the pattern is incorrect.

## Common Causes

- Regex pattern does not account for all valid URL characters
- Special characters in the URL not properly escaped
- Path parameter regex is too restrictive for actual traffic
- Missing `^` and `$` anchors cause partial matches
- URL encoding interferes with regex matching

## How to Fix

### Use Path Parameter with Pattern

```python
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/users/{username}")
def get_user(
    username: str = Path(pattern=r"^[a-zA-Z0-9_-]{3,20}$")
):
    return {"username": username}
```

### Match Specific URL Patterns

```python
@app.get("/orders/{order_id}")
def get_order(
    order_id: str = Path(pattern=r"ORD-\d{4}-\d{6}")
):
    return {"order_id": order_id}
```

## Examples

```python
from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/files/{file_path:path}")
def get_file(file_path: str):
    return {"path": file_path}

# This works for paths like /files/docs/readme.md
# The :path converter matches slashes
```

For stricter validation, add a `pattern` to the `Path` parameter.
