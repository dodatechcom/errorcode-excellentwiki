---
title: "[Solution] Python HTTPX Async Client Error — How to Fix"
description: "Fix Python HTTPX async client errors. Resolve connection, timeout, and request issues with httpx async and sync clients."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python HTTPX Async Client Error

An HTTPX error occurs when the `httpx` library fails to make an HTTP request due to connection issues, timeouts, or invalid request configurations. HTTPX supports both sync and async HTTP clients.

## Why It Happens

HTTPX wraps the underlying connection pool and SSL verification. Common failures include DNS resolution errors when the server hostname is unreachable, timeouts when the server is slow, and too many redirects when a redirect loop exists.

## Common Error Messages

- `httpx.ConnectError: [Errno -2] Name or service not known`
- `httpx.TimeoutException: Timed out connecting to server`
- `httpx.TooManyRedirects: Exceeded maximum allowed redirects`
- `httpx.HTTPStatusError: Server error '500 Internal Server Error'`

## How to Fix It

### Fix 1: Use async client inside async context

```python
import httpx
import asyncio

async def fetch():
    async with httpx.AsyncClient() as client:
        response = await client.get('https://api.example.com/data')
        return response.json()

asyncio.run(fetch())
```

### Fix 2: Configure timeouts properly

```python
import httpx

async with httpx.AsyncClient() as client:
    response = await client.get(
        'https://api.example.com/slow',
        timeout=httpx.Timeout(30.0, connect=5.0)
    )
```

### Fix 3: Handle connection errors with retries

```python
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(min=1, max=10))
async def fetch_with_retry(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.json()
```

### Fix 4: Use connection pooling

```python
import httpx

async with httpx.AsyncClient() as client:
    r1 = await client.get('https://api.example.com/users')
    r2 = await client.get('https://api.example.com/posts')
    print(r1.status_code, r2.status_code)
```

## Common Scenarios

- **Async in sync context** — Calling await on HTTPX request without running in an event loop.
- **Connection pool exhaustion** — Too many concurrent requests exhaust the default connection pool.
- **SSL certificate verification** — Self-signed or expired certificates cause ConnectError.

## Prevent It

- Always use async with httpx.AsyncClient() as client: for proper cleanup
- Set explicit timeouts for all requests
- Use connection pooling via a persistent client for high-throughput apps

## Related Errors

- - [ConnectionError](/languages/python/connectionerror/) — network connection failure
- - [TimeoutError](/languages/python/timeouterror/) — operation timed out
