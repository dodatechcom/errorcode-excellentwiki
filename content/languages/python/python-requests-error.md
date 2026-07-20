---
title: "[Solution] Python requests Error — HTTP Request Failures"
description: "Fix Python requests errors like ConnectionError, Timeout, TooManyRedirects, HTTPError, and SSLError. Copy-paste solutions with code examples."
languages: ["python"]
severities: ["error"]
error-types: ["runtime"]
weight: 425
---

# Python requests Error — HTTP Request Failures

The requests library errors occur when connections fail, timeouts are exceeded, too many redirects are followed, HTTP errors are not handled, or SSL certificates are invalid. These are among the most common errors in Python web interaction.

## Common Causes

```python
# ConnectionError: failed to connect
import requests
requests.get("https://nonexistent-domain-xyz.com")

# Timeout: server took too long to respond
requests.get("https://slow-server.example.com", timeout=0.001)

# HTTPError: 4xx or 5xx status code
response = requests.get("https://api.example.com/data")
response.raise_for_status()  # raises HTTPError

# TooManyRedirects: redirect loop
requests.get("https://example.com/loop", allow_redirects=True)

# SSLError: certificate verification failed
requests.get("https://self-signed.example.com", verify=True)
```

## How to Fix

### Fix 1: Set Appropriate Timeouts
Always set a timeout to prevent indefinite hanging.
```python
import requests

# Timeout as (connect, read) tuple
response = requests.get("https://api.example.com", timeout=(3.05, 30))
```

### Fix 2: Handle HTTP Errors Properly
Check status codes and handle errors gracefully.
```python
import requests

response = requests.get("https://api.example.com/data")
if response.status_code == 200:
    data = response.json()
elif response.status_code == 404:
    print("Resource not found")
else:
    response.raise_for_status()
```

### Fix 3: Use Retry Logic for Transient Failures
Implement retries with backoff for network issues.
```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(total=3, backoff_factor=1, status_forcelist=[500, 502, 503, 504])
adapter = HTTPAdapter(max_retries=retry)
session.mount("https://", adapter)
response = session.get("https://api.example.com/data")
```

### Fix 4: Handle SSL Certificate Issues
Control SSL verification as needed.
```python
import requests

# Disable verification (not recommended for production)
response = requests.get("https://self-signed.example.com", verify=False)

# Use a custom CA bundle
response = requests.get("https://api.example.com", verify="/path/to/ca-bundle.crt")
```

### Fix 5: Limit Redirects
Control maximum number of redirects.
```python
import requests

try:
    response = requests.get("https://example.com/redirect", allow_redirects=True, max_redirects=5)
except requests.TooManyRedirects:
    print("Too many redirects, stopping")
```

## Examples

```python
# Production-ready API client
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def create_session():
    session = requests.Session()
    retry = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
    adapter = HTTPAdapter(max_retries=retry)
    session.mount("https://", adapter)
    session.headers.update({"User-Agent": "MyApp/1.0"})
    return session

def fetch_json(url):
    session = create_session()
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.ConnectionError:
        print(f"Failed to connect to {url}")
    except requests.Timeout:
        print(f"Request to {url} timed out")
    except requests.HTTPError as e:
        print(f"HTTP error: {e}")
```

## Related Errors

- [Python httpx Error](/languages/python/python-httpx-error/)
- [Python Scrapy Error](/languages/python/python-scrapy-error/)
- [Python Selenium Error](/languages/python/python-selenium-error/)
