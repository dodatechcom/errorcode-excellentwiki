---
title: "[Solution] Python httpx Error — HTTP Client Connection Failures"
description: "Fix Python httpx errors like ConnectError, TimeoutException, HTTPStatusError, and AsyncClient errors. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 424
---

# Python httpx Error — HTTP Client Connection Failures

httpx errors occur when the client cannot establish a connection, encounters timeouts, receives unexpected HTTP status codes, or misuses the async client. These are common in modern Python HTTP workflows.

## Common Causes

```python
# ConnectError: cannot connect to server
import httpx
client = httpx.Client()
client.get("https://nonexistent-domain-xyz.com")

# TimeoutException: request took too long
client = httpx.Client(timeout=1.0)
client.get("https://slow-server.example.com")

# HTTPStatusError: server returned 4xx or 5xx
response = client.get("https://api.example.com/data")
response.raise_for_status()  # raises if status >= 400

# RuntimeError: AsyncClient used in synchronous context
async def main():
    client = httpx.AsyncClient()
    client.get("https://example.com")  # must use await

# TooManyRedirects
client = httpx.Client(follow_redirects=False)
response = client.get("https://example.com/redirect-loop")
```

## How to Fix

### Fix 1: Handle Connection Errors with Retry Logic
Wrap requests in try/except and retry on transient failures.
```python
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def fetch(url):
    with httpx.Client() as client:
        response = client.get(url)
        response.raise_for_status()
        return response.json()
```

### Fix 2: Configure Appropriate Timeouts
Set per-operation or connection-level timeouts.
```python
import httpx

# Single timeout for all operations
client = httpx.Client(timeout=30.0)

# Granular timeout configuration
timeout = httpx.Timeout(connect=5.0, read=30.0, write=5.0, pool=5.0)
client = httpx.Client(timeout=timeout)
response = client.get("https://api.example.com/data")
```

### Fix 3: Check HTTP Status Codes
Handle status codes gracefully instead of raising on every error.
```python
import httpx

with httpx.Client() as client:
    response = client.get("https://api.example.com/data")
    if response.status_code == 200:
        data = response.json()
    elif response.status_code == 404:
        print("Resource not found")
    elif response.status_code >= 500:
        print("Server error, retry later")
```

### Fix 4: Use AsyncClient Correctly
Always await async requests and use async context managers.
```python
import httpx
import asyncio

async def fetch_all(urls):
    async with httpx.AsyncClient() as client:
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks)
        return [r.json() for r in responses]
```

### Fix 5: Enable Redirect Following
Configure redirect behavior for pages that redirect.
```python
import httpx

with httpx.Client(follow_redirects=True, max_redirects=10) as client:
    response = client.get("https://example.com/redirect")
    print(response.url)  # final URL after redirects
```

## Examples

```python
# Robust API client with httpx
import httpx

class APIClient:
    def __init__(self, base_url, token=None):
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        self.client = httpx.Client(base_url=base_url, headers=headers, timeout=10.0)

    def get_user(self, user_id):
        response = self.client.get(f"/users/{user_id}")
        response.raise_for_status()
        return response.json()

    def create_user(self, data):
        response = self.client.post("/users", json=data)
        response.raise_for_status()
        return response.json()
```

## Related Errors

- [Python Requests Error](/languages/python/python-requests-error/)
- [Python Scrapy Error](/languages/python/python-scrapy-error/)
- [Python Selenium Error](/languages/python/python-selenium-error/)
