---
title: "[Solution] httpx.TimeoutException: Read Timeout Fix"
description: "Fix httpx read timeout errors. Configure timeouts, use async clients, and implement retry strategies."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["httpx", "http", "timeout", "async", "client"]
weight: 5
---

# httpx.TimeoutException: Read Timeout Fix

An `httpx.TimeoutException` is raised when an HTTP request times out waiting for a response from the server. This includes connect, read, write, and pool timeouts.

## What This Error Means

Common messages:

- `httpx.TimeoutException: Read timeout`
- `httpx.ConnectTimeout: Connect timeout`
- `httpx.ReadTimeout: Read timeout while reading response body`

The HTTP client waited longer than the configured timeout for the server to respond or send data. This indicates a slow server, network issues, or overly aggressive timeout settings.

## Common Causes

```python
import httpx

# Cause 1: Default timeout too short for slow endpoint
client = httpx.Client()
response = client.get("https://slow-api.example.com")  # TimeoutException

# Cause 2: Large response taking too long to download
response = client.get("https://api.example.com/large-dataset")

# Cause 3: Server under high load
response = client.get("https://overloaded-server.example.com/api")

# Cause 4: Network latency
response = client.get("https://far-away-server.example.com")
```

## How to Fix

### Fix 1: Increase timeout values

```python
import httpx

# Set individual timeouts
client = httpx.Client(
    timeout=httpx.Timeout(
        connect=5.0,
        read=60.0,
        write=5.0,
        pool=5.0,
    )
)

response = client.get("https://api.example.com")
```

### Fix 2: Use no timeout for long-running requests

```python
import httpx

# Disable timeout entirely (use with caution)
client = httpx.Client(timeout=None)
response = client.get("https://api.example.com/large-dataset")
```

### Fix 3: Use async client for concurrent requests

```python
import httpx
import asyncio

async def fetch_all(urls):
    async with httpx.AsyncClient(timeout=30.0) as client:
        tasks = [client.get(url) for url in urls]
        responses = await asyncio.gather(*tasks, return_exceptions=True)
        return responses

urls = ["https://api.example.com/1", "https://api.example.com/2"]
results = asyncio.run(fetch_all(urls))
```

### Fix 4: Implement retry with backoff

```python
import httpx
from tenacity import retry, stop_after_attempt, wait_exponential

@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=2, max=10))
def fetch_with_retry(url):
    with httpx.Client(timeout=30.0) as client:
        return client.get(url)

response = fetch_with_retry("https://api.example.com")
```

### Fix 5: Stream large responses

```python
import httpx

with httpx.Client(timeout=httpx.Timeout(read=300.0)) as client:
    with client.stream("GET", "https://api.example.com/large") as response:
        for chunk in response.iter_bytes():
            process(chunk)
```

## Related Errors

- {{< relref "requests-ssl-error" >}} — SSL certificate verification failed.
- {{< relref "timeouterror" >}} — Python TimeoutError.
