---
title: "Solved Python httpx Error — How to Fix"
date: 2026-03-12T09:50:00+00:00
description: "Learn how to resolve Python httpx connection, timeout, and transport errors in modern async HTTP."
categories: ["python"]
keywords: ["python httpx", "httpx error", "httpx timeout", "httpx connection", "httpx transport error"]
error-types: ["runtime-error"]
severities: ["error"]
languages: ["python"]
weight: 5
comments: true
---

## Why It Happens

httpx errors occur when the modern Python HTTP client encounters connection failures, transport-level issues, or timeout misconfigurations. httpx supports both sync and async, and errors manifest differently depending on the mode used.

Common causes include:
- Connection pool exhaustion with too many concurrent requests
- SSL/TLS handshake failures with custom certificates
- Read or write timeouts exceeding server response times
- HTTP/2 protocol negotiation failures
- Transport errors when using custom transports or proxies

## Common Error Messages

```python
import httpx

try:
    response = httpx.get("https://httpbin.org/delay/10", timeout=3.0)
except httpx.TimeoutException as e:
    print(f"Timeout: {e}")
# httpx.ReadTimeout
```

```python
# Connection refused
try:
    response = httpx.get("http://localhost:99999/test")
except httpx.ConnectError as e:
    print(f"Connect error: {e}")
```

```python
# Too many redirects
try:
    response = httpx.get("https://httpbin.org/redirect/15", follow_redirects=False)
except httpx.TooManyRedirects:
    print("Too many redirects")
```

## How to Fix It

### 1. Use Persistent Client with Connection Pooling

Create a shared client instance for connection reuse.

```python
import httpx
import asyncio

class HttpClient:
    def __init__(self):
        self.client = httpx.AsyncClient(
            limits=httpx.Limits(
                max_connections=100,
                max_keepalive_connections=20,
                keepalive_expiry=30
            ),
            timeout=httpx.Timeout(
                connect=5.0,
                read=30.0,
                write=10.0,
                pool=5.0
            ),
            follow_redirects=True,
            max_redirects=10,
            http2=True
        )
    
    async def __aenter__(self):
        return self
    
    async def __aexit__(self, *exc):
        await self.client.aclose()
    
    async def get(self, url, **kwargs):
        try:
            response = await self.client.get(url, **kwargs)
            response.raise_for_status()
            return response
        except httpx.HTTPStatusError as e:
            print(f"HTTP {e.response.status_code}: {url}")
            raise
        except httpx.RequestError as e:
            print(f"Request error: {e}")
            raise

async def main():
    async with HttpClient() as client:
        resp = await client.get("https://api.example.com/data")
        print(resp.json())

asyncio.run(main())
```

### 2. Configure Retries with Exponential Backoff

Implement automatic retries for transient failures.

```python
import httpx
import time
from functools import wraps

def retry_on_error(max_retries=3, backoff_factor=2, retry_on_status=(502, 503, 504)):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            
            for attempt in range(max_retries + 1):
                try:
                    response = func(*args, **kwargs)
                    if response.status_code in retry_on_status:
                        if attempt == max_retries:
                            return response
                        wait = backoff_factor ** attempt
                        time.sleep(wait)
                        continue
                    return response
                except (httpx.ConnectError, httpx.TimeoutException) as e:
                    last_exception = e
                    if attempt == max_retries:
                        raise
                    wait = backoff_factor ** attempt
                    time.sleep(wait)
            
            raise last_exception
        return wrapper
    return decorator

@retry_on_error(max_retries=3)
def fetch_with_retry(url):
    return httpx.get(url, timeout=10.0)

response = fetch_with_retry("https://api.example.com/data")
```

### 3. Handle SSL Certificate Issues

Configure SSL for self-signed or custom certificate environments.

```python
import httpx
import ssl

# Disable verification (development only)
client = httpx.Client(verify=False)

# Custom CA bundle
client = httpx.Client(verify="/path/to/custom-ca-bundle.crt")

# Client certificate authentication
client = httpx.Client(
    cert=("/path/to/client.crt", "/path/to/client.key")
)

# Async version
async_client = httpx.AsyncClient(
    verify=True,
    cert=("/path/to/client.pem", "/path/to/client.key")
)

# Handle SSL errors gracefully
async def safe_request(url):
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(url)
            return resp
    except httpx.ConnectError as e:
        if "SSL" in str(e):
            print("SSL handshake failed - check certificates")
            async with httpx.AsyncClient(verify=False) as client:
                return await client.get(url)
        raise

response = asyncio.run(safe_request("https://self-signed.example.com"))
```

## Common Scenarios

### Scenario 1: API Client with Pagination

Building a robust paginated API client:

```python
import httpx
from typing import Iterator, List

class PaginatedAPI:
    def __init__(self, base_url, token, page_size=100):
        self.base_url = base_url
        self.page_size = page_size
        self.headers = {"Authorization": f"Bearer {token}"}
    
    def _get_page(self, url, params=None):
        try:
            response = httpx.get(url, headers=self.headers, params=params, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            if e.response.status_code == 429:
                retry_after = int(e.response.headers.get("Retry-After", 60))
                print(f"Rate limited, waiting {retry_after}s")
                time.sleep(retry_after)
                return self._get_page(url, params)
            raise
    
    def iterate_all(self, endpoint) -> Iterator[dict]:
        url = f"{self.base_url}{endpoint}"
        params = {"limit": self.page_size, "offset": 0}
        
        while True:
            data = self._get_page(url, params)
            items = data.get("results", data if isinstance(data, list) else [])
            
            yield from items
            
            if not data.get("next"):
                break
            params["offset"] += self.page_size

api = PaginatedAPI("https://api.example.com/v1", "token123")
for item in api.iterate_all("/users"):
    print(item)
```

## Prevent It

- Reuse `httpx.Client` or `httpx.AsyncClient` instances for connection pooling
- Set explicit timeouts for connect, read, write, and pool operations
- Use `response.raise_for_status()` to catch HTTP errors immediately
- Implement retry logic with exponential backoff for transient failures
- Enable HTTP/2 with `http2=True` for better multiplexing performance