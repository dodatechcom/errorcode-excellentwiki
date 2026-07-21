---
title: "[Solution] FastAPI Request Body Stream Error"
description: "Fix FastAPI request body stream errors when reading the raw request body fails or returns empty data."
frameworks: ["fastapi"]
error-types: ["runtime-error"]
severities: ["error"]
---

When reading the raw request body stream in FastAPI, the data may be empty or incomplete if the body was already consumed.

## Common Causes

- Body already consumed by middleware or a previous `request.body()` call
- Request transfer-encoding is chunked and not fully received
- Client sends body as URL-encoded instead of JSON
- Large request body exceeds default buffer size
- Streaming request body not fully buffered

## How to Fix

### Read Body Before Processing

```python
from fastapi import FastAPI, Request
import json

app = FastAPI()

@app.post("/webhook")
async def webhook(request: Request):
    body = await request.body()
    if not body:
        return {"error": "Empty body"}
    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON"}
    return {"received": data}
```

### Use StreamingRequest for Large Bodies

```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/upload")
async def upload(request: Request):
    chunks = []
    async for chunk in request.stream():
        chunks.append(chunk)
    body = b"".join(chunks)
    return {"size": len(body)}
```

## Examples

```python
from fastapi import FastAPI, Request

app = FastAPI()

@app.post("/process")
async def process(request: Request):
    body = await request.body()
    if not body:
        raise HTTPException(status_code=400, detail="Empty request body")
    data = json.loads(body)
    return {"processed": data}
```
