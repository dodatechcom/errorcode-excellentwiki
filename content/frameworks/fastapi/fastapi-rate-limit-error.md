---
title: "[Solution] FastAPI Rate Limit Error"
description: "Fix FastAPI rate limit errors when requests are blocked by rate limiting middleware or custom throttling."
frameworks: ["fastapi"]
error-types: ["rate-limit-error"]
severities: ["error"]
---

When rate limiting is applied to a FastAPI application, clients receive 429 Too Many Requests errors.

## Common Causes

- Rate limit threshold too low for expected traffic
- All requests share the same rate limit key
- Rate limit counter not reset after the window expires
- Redis-backed rate limiter connection fails
- Burst traffic from legitimate clients exceeds per-second limits

## How to Fix

### Use SlowAPI for Rate Limiting

```python
from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter

@app.get("/api/data")
@limiter.limit("100/minute")
async def get_data(request: Request):
    return {"data": "value"}
```

### Custom Rate Limit Key

```python
def get_user_key(request: Request) -> str:
    user = get_current_user(request)
    return f"user:{user.id}"

limiter = Limiter(key_func=get_user_key)

@app.get("/api/profile")
@limiter.limit("50/minute")
async def get_profile(request: Request):
    return {"profile": "data"}
```

## Examples

```python
from fastapi import FastAPI, Request
from slowapi import Limiter
from slowapi.util import get_remote_address

app = FastAPI()
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter

@app.get("/search")
@limiter.limit("5/minute")
async def search(request: Request, q: str):
    return {"results": []}
```

After 5 requests within 1 minute, the 6th request returns a 429 error.
