---
title: "[Solution] Python HTTPError / ConnectionError / TimeoutError Fix"
description: "Fix Python requests.HTTPError, ConnectionError, and TimeoutError. Handle network errors, retries, timeouts, and HTTP status codes properly."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["httperror", "connectionerror", "timeouterror", "requests", "network", "http"]
weight: 5
---

# HTTPError / ConnectionError / TimeoutError

Python network errors occur when HTTP requests fail due to connectivity issues, server errors, or timeouts. The `requests` library raises `HTTPError` for bad status codes, `ConnectionError` for network failures, and `TimeoutError` when a request takes too long.

## Description

These errors come from the `requests` library (or `urllib3` under the hood):

- **`requests.HTTPError`** — server returned a 4xx or 5xx status code.
- **`requests.ConnectionError`** — network issue (DNS failure, refused connection).
- **`requests.Timeout`** — request exceeded the timeout threshold.
- **`requests.exceptions.SSLError`** — TLS/SSL certificate verification failed.

## Common Causes

```python
import requests

# Cause 1: Server returns error status code
response = requests.get("https://api.example.com/data")
response.raise_for_status()  # HTTPError if status >= 400

# Cause 2: DNS resolution failure
requests.get("https://nonexistent-domain-12345.com")  # ConnectionError

# Cause 3: Connection refused
requests.get("http://localhost:99999")  # ConnectionError

# Cause 4: Request timeout
requests.get("https://slow-api.example.com", timeout=5)  # Timeout

# Cause 5: SSL certificate issues
requests.get("https://expired-cert.example.com")  # SSLError
```

## How to Fix

### Fix 1: Handle HTTP status codes properly

```python
import requests

# Wrong — crashes on error status
response = requests.get("https://api.example.com/data")
response.raise_for_status()
data = response.json()

# Correct — check status code
response = requests.get("https://api.example.com/data")
if response.status_code == 200:
    data = response.json()
elif response.status_code == 404:
    print("Resource not found")
elif response.status_code >= 500:
    print(f"Server error: {response.status_code}")
```

### Fix 2: Use try/except for network errors

```python
import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout

try:
    response = requests.get("https://api.example.com/data", timeout=10)
    response.raise_for_status()
    data = response.json()
except HTTPError as e:
    print(f"HTTP error: {e.response.status_code}")
except ConnectionError:
    print("Network connection failed")
except Timeout:
    print("Request timed out")
except requests.RequestException as e:
    print(f"Request failed: {e}")
```

### Fix 3: Implement retries with backoff

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Create a session with automatic retries
session = requests.Session()
retries = Retry(
    total=3,
    backoff_factor=1,  # 1s, 2s, 4s
    status_forcelist=[500, 502, 503, 504],
)
adapter = HTTPAdapter(max_retries=retries)
session.mount("http://", adapter)
session.mount("https://", adapter)

response = session.get("https://api.example.com/data")
```

### Fix 4: Set appropriate timeouts

```python
import requests

# Wrong — no timeout, can hang forever
response = requests.get("https://api.example.com/data")

# Correct — set connect and read timeouts
response = requests.get(
    "https://api.example.com/data",
    timeout=(5, 30)  # 5s connect, 30s read
)
```

### Fix 5: Handle SSL certificate issues

```python
import requests

# Wrong — disables SSL verification (insecure)
response = requests.get("https://api.example.com", verify=False)

# Correct — use proper CA bundle
response = requests.get(
    "https://api.example.com",
    verify="/path/to/ca-bundle.crt"
)

# Or disable only in development
import os
if os.environ.get("ENV") == "development":
    response = requests.get(url, verify=False)
else:
    response = requests.get(url, verify=True)
```

### Fix 6: Use a session with persistent connections

```python
import requests

# Wrong — creates new connection for each request
for url in urls:
    response = requests.get(url)

# Correct — reuse connection with a session
session = requests.Session()
for url in urls:
    response = session.get(url)
```

## Examples

This error commonly occurs when:

- API rate limiting returns 429 status
- DNS server is unreachable (firewall or network issue)
- Backend server is down or overloaded
- Request to a slow API exceeds default 30-second timeout

## Related Errors

- [JSONDecodeError](jsondecodeerror) — response body is not valid JSON
- [ConnectionRefusedError](#) — socket connection actively refused
- [OSError](#) — underlying socket-level errors
