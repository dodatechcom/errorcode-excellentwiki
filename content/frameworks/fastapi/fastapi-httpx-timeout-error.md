---
title: "[Solution] FastAPI HTTPX Timeout Error"
description: "Fix FastAPI HTTPX timeout errors when outgoing client requests take too long or fail to connect."
frameworks: ["fastapi"]
error-types: ["timeout-error"]
severities: ["error"]
---

When FastAPI makes outgoing HTTP requests using `httpx`, timeouts cause `httpx.ReadTimeout` or `httpx.ConnectTimeout` exceptions.

## Common Causes

- Default timeout (5 seconds) is too short for slow endpoints
- External service is under heavy load or rate-limiting
- DNS resolution takes too long for the target hostname
- Large response bodies take time to download
- Connection pool exhaustion causes waiting

## How to Fix

### Set Custom Timeouts

```python
import httpx

async def call_external_api():
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get("https://api.example.com/slow-endpoint")
        return response.json()
```

### Configure Per-Operation Timeouts

```python
import httpx

async def call_api():
    timeout = httpx.Timeout(
        connect=5.0,
        read=60.0,
        write=5.0,
        pool=5.0,
    )
    async with httpx.AsyncClient(timeout=timeout) as client:
        response = await client.get("https://api.example.com/data")
        return response.json()
```

### Add Retry Logic with Backoff

```python
import httpx
import asyncio

async def resilient_request(url: str, retries: int = 3):
    for attempt in range(retries):
        try:
            async with httpx.AsyncClient(timeout=30.0) as client:
                response = await client.get(url)
                response.raise_for_status()
                return response.json()
        except httpx.TimeoutException:
            if attempt == retries - 1:
                raise
            await asyncio.sleep(2 ** attempt)
```

## Examples

```python
from fastapi import FastAPI
import httpx

app = FastAPI()

@app.get("/fetch")
async def fetch_data():
    async with httpx.AsyncClient() as client:
        # Default timeout is 5 seconds -- may timeout on slow APIs
        response = await client.get("https://api.slow-service.com/data")
        return response.json()
```

Increase the timeout and add retry logic for production use.
