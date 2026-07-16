---
title: "[Solution] Python ConnectionError — Network Connection Failed Fix"
description: "Fix Python ConnectionError when network connections fail. Check internet, DNS, firewall, and use retry logic with timeout settings."
languages: ["python"]
severities: ["error"]
error_types: ["runtime"]
tags: ["connectionerror", "network", "http", "timeout", "retry"]
weight: 80
---

# ConnectionError — Network Connection Failed Fix

A `ConnectionError` is raised when a network connection fails. It's a subclass of `OSError` and serves as the base class for more specific errors like `ConnectionRefusedError`, `ConnectionResetError`, and `ConnectionAbortedError`.

## Description

Python's `requests`, `urllib`, `httpx`, and socket libraries all raise `ConnectionError` variants when a network operation fails. This covers DNS failures, refused connections, timeouts, and broken pipes.

Common scenarios:

- **Server unreachable** — host is down or IP is wrong.
- **Connection refused** — server not listening on the port.
- **DNS resolution failure** — domain name doesn't resolve.
- **Network timeout** — connection takes too long.
- **Firewall blocking** — outgoing or incoming connection blocked.
- **Proxy misconfiguration** — proxy server not reachable.

## Common Causes

```python
import requests

# Cause 1: Server unreachable
response = requests.get("http://192.168.1.999:8080/api")  # ConnectionError

# Cause 2: Connection refused — server not running
response = requests.get("http://localhost:5000/api")  # ConnectionRefusedError

# Cause 3: DNS failure
response = requests.get("http://nonexistent.example.com")  # ConnectionError

# Cause 4: Timeout
response = requests.get("http://slow-server.com/api", timeout=5)  # Timeout, then ConnectionError

# Cause 5: Firewall blocking
response = requests.get("http://blocked-server.com/api")  # ConnectionError
```

## Solutions

### Fix 1: Check internet connection first

```python
import requests

# Wrong — assumes connection works
def fetch_data(url):
    return requests.get(url).json()

# Correct — verify connectivity
def check_internet():
    try:
        requests.get("https://httpbin.org/get", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def fetch_data(url):
    if not check_internet():
        print("No internet connection")
        return None
    return requests.get(url, timeout=10).json()
```

### Fix 2: Use try/except with proper error handling

```python
import requests

# Wrong — crashes on connection failure
response = requests.get("http://api.example.com/data")
data = response.json()

# Correct — handle connection errors
try:
    response = requests.get("http://api.example.com/data", timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.ConnectionError:
    print("Connection failed — check your network")
    data = None
except requests.Timeout:
    print("Request timed out")
    data = None
except requests.HTTPError as e:
    print(f"HTTP error: {e}")
    data = None
```

### Fix 3: Implement retry logic with exponential backoff

```python
import requests
import time

# Wrong — single attempt
def fetch_data(url):
    return requests.get(url, timeout=10).json()

# Correct — retry with backoff
def fetch_data(url, max_retries=3, backoff_factor=1):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.ConnectionError:
            wait = backoff_factor * (2 ** attempt)
            print(f"Attempt {attempt + 1} failed, retrying in {wait}s...")
            time.sleep(wait)
    print("All retries failed")
    return None
```

### Fix 4: Configure DNS and check resolution

```python
import socket

# Wrong — assumes DNS works
def resolve_host(hostname):
    return socket.gethostbyname(hostname)

# Correct — handle DNS failures
def resolve_host(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        return ip
    except socket.gaierror:
        print(f"DNS resolution failed for {hostname}")
        return None
```

### Fix 5: Use proxy settings correctly

```python
import requests

# Wrong — no proxy configuration when behind proxy
response = requests.get("http://api.example.com")

# Correct — configure proxy
proxies = {
    "http": "http://proxy.example.com:8080",
    "https": "http://proxy.example.com:8080",
}
response = requests.get("http://api.example.com", proxies=proxies, timeout=10)

# Or use environment variables
# export HTTP_PROXY=http://proxy.example.com:8080
# export HTTPS_PROXY=http://proxy.example.com:8080
response = requests.get("http://api.example.com")
```

### Fix 6: Use connection pooling for repeated requests

```python
import requests

# Wrong — creates new connection each time
for url in urls:
    response = requests.get(url, timeout=10)

# Correct — use session for connection pooling
session = requests.Session()
for url in urls:
    try:
        response = session.get(url, timeout=10)
        response.raise_for_status()
    except requests.ConnectionError:
        print(f"Failed to connect to {url}")
        continue
session.close()
```

## Related Errors

- [TimeoutError](#) — connection or read timed out.
- [OSError](#) — generic OS-level error.
- [URLError](#) — URL handling failure.
