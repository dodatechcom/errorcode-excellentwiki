---
title: "[Solution] FastAPI HTTPException Status Code Error"
description: "Fix FastAPI HTTPException status code errors when wrong status codes are returned for different error conditions."
frameworks: ["fastapi"]
error-types: ["framework-error"]
severities: ["error"]
---

Using the wrong HTTP status code in `HTTPException` causes client confusion and incorrect caching behavior.

## Common Causes

- Using 400 (Bad Request) for authentication errors (should be 401)
- Returning 200 OK when an error occurred
- Using 500 (Internal Server Error) for client errors
- Missing status code parameter defaults to 500
- Custom status codes not recognized by HTTP clients

## How to Fix

### Use Correct Status Codes

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/resource/{id}")
def get_resource(id: int):
    if not is_authenticated():
        raise HTTPException(status_code=401, detail="Authentication required")
    if not is_authorized():
        raise HTTPException(status_code=403, detail="Access denied")
    resource = find_resource(id)
    if not resource:
        raise HTTPException(status_code=404, detail="Resource not found")
    if not is_valid(resource):
        raise HTTPException(status_code=422, detail="Invalid resource data")
    return resource
```

### Common Status Code Reference

```text
200 - OK (success)
201 - Created (resource created)
204 - No Content (successful deletion)
400 - Bad Request (malformed input)
401 - Unauthorized (authentication required)
403 - Forbidden (insufficient permissions)
404 - Not Found (resource does not exist)
409 - Conflict (resource already exists)
422 - Unprocessable Entity (validation error)
429 - Too Many Requests (rate limited)
500 - Internal Server Error (server failure)
503 - Service Unavailable (service down)
```

### Return Proper Response for Each Case

```python
@app.post("/items")
def create_item(item: Item):
    existing = db.query(Item).filter(Item.name == item.name).first()
    if existing:
        raise HTTPException(status_code=409, detail="Item already exists")
    return {"id": db.add(item)}
```

## Examples

```python
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Bug -- wrong status codes
@app.get("/wrong")
def wrong():
    user = get_user()
    if not user:
        raise HTTPException(status_code=500, detail="User not found")  # Wrong!
    return user

# Fix
@app.get("/correct")
def correct():
    user = get_user()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
```

Always use the most specific status code that describes the error condition.
