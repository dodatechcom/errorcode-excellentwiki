---
title: "[Solution] FastAPI Static Files Mount Error"
description: "Fix FastAPI static files mount errors when serving static assets fails or routes conflict with API endpoints."
frameworks: ["fastapi"]
error-types: ["deployment-error"]
severities: ["error"]
---

When mounting static files in FastAPI, route conflicts occur if the mount path overlaps with API routes.

## Common Causes

- Static mount path `/static` conflicts with an API route at `/static/health`
- Mount registered after API routes that should take precedence
- Directory path does not exist or has incorrect permissions
- Missing trailing slash causes path resolution issues
- Files served but content-type headers are incorrect

## How to Fix

### Mount Static Files at a Unique Path

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()

static_dir = Path("static")
static_dir.mkdir(exist_ok=True)

app.mount("/assets", StaticFiles(directory="static"), name="static")

@app.get("/api/health")
def health():
    return {"status": "ok"}
```

### Place Mount After API Routes

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/api/data")
def get_data():
    return {"data": "value"}

# Mount static last so API routes take precedence
app.mount("/", StaticFiles(directory="public", html=True), name="static")
```

## Examples

```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Bug -- /static overlaps with API route
@app.get("/static/config")
def get_config():
    return {"debug": True}

app.mount("/static", StaticFiles(directory="static"), name="static")
# /static/config serves the file, not the API endpoint
```

Fix by using a different mount path like `/assets`.
