---
title: "Solved Python urllib3 Error — How to Fix"
date: 2026-03-12T10:00:15+00:00
description: "Learn how to resolve Python urllib3 connection pool, SSL, and protocol errors in low-level HTTP."
categories: ["python"]
keywords: ["python urllib3", "urllib3 error", "urllib3 pool", "urllib3 ssl", "urllib3 connection error"]
error-types: ["runtime-error"]
severities: ["error"]
languages: ["python"]
weight: 5
comments: true
---

## Why It Happens

urllib3 errors occur at the lower HTTP transport layer when connection pools are misconfigured, SSL contexts are invalid, or protocol constraints are violated. These errors often surface when using urllib3 directly or through libraries like requests.

Common causes include:
- Connection pool overflow causing request queuing
- SSL certificate verification failures
- HTTP version mismatch between client and server
- Chunked transfer encoding issues
- Maximum retry count exceeded

## Common Error Messages

```python
import urllib3

http = urllib3.PoolManager()
try:
    response = http.request("GET", "https://expired.badssl.com/")
except urllib3.exceptions.SSLError as e:
    print(f"SSL error: {e}")
```

```python
# Pool timeout
pool = urllib3.HTTPConnectionPool("localhost", 8080, maxsize=1)
try:
    pool.request("GET", "/slow", timeout=5)
except urllib3.exceptions.TimeoutError as e:
    print(f"Timeout: {e}")
```

```python
# Max retries exceeded
from urllib3.util.retry import Retry

retry = Retry(total=2)
pool = urllib3.HTTPConnectionPool("localhost", 8080)
try:
    pool.request("GET", "/fail", retries=retry)
except urllib3.exceptions.MaxRetryError as e:
    print(f"Max retries exceeded: {e.reason}")
```

## How to Fix It

### 1. Configure Pool Manager with Proper Limits

Set appropriate pool size and timeout configurations.

```python
import urllib3
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

def create_pool_manager(
    max_connections=10,
    max_per_host=5,
    timeout=30,
    retries=3
):
    retry_strategy = Retry(
        total=retries,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["HEAD", "GET", "PUT", "DELETE", "OPTIONS"]
    )
    
    pool = urllib3.PoolManager(
        num_pools=max_connections,
        maxsize=max_per_host,
        block=True,
        retries=retry_strategy,
        timeout=urllib3.Timeout(
            connect=5.0,
            read=timeout,
            total=timeout + 5
        )
    )
    
    return pool

pool = create_pool_manager()
response = pool.request("GET", "https://api.example.com/data")
print(response.status)
```

### 2. Handle SSL Certificate Issues

Configure SSL context for different certificate scenarios.

```python
import urllib3
import ssl
import certifi

def create_ssl_context(verify=True, client_cert=None):
    if not verify:
        return urllib3.util.ssl_.create_urllib3_context(
            cert_reqs=ssl.CERT_NONE
        )
    
    ssl_ctx = urllib3.util.ssl_.create_urllib3_context()
    
    if client_cert:
        ssl_ctx.load_cert_chain(
            certfile=client_cert["cert"],
            keyfile=client_cert.get("key")
        )
    
    return ssl_ctx

# Standard verified connection
pool_verified = urllib3.PoolManager(
    ssl_context=create_ssl_context(verify=True),
    cert_reqs="CERT_REQUIRED"
)

# Self-signed certificate (development only)
pool_unverified = urllib3.PoolManager(
    ssl_context=create_ssl_context(verify=False),
    cert_reqs="CERT_NONE"
)

# Client certificate authentication
pool_mtls = urllib3.PoolManager(
    ssl_context=create_ssl_context(
        verify=True,
        client_cert={
            "cert": "/path/to/client.crt",
            "key": "/path/to/client.key"
        }
    )
)

# Make request with specific SSL context
response = pool_verified.request("GET", "https://api.example.com/secure")
```

### 3. Use Low-Level Connection for Custom Protocols

Direct HTTPConnection for non-standard requirements.

```python
import urllib3
import json

class CustomHTTPClient:
    def __init__(self, host, port=None, ssl=False):
        if ssl:
            self.pool = urllib3.HTTPSConnectionPool(
                host, port=port or 443,
                maxsize=5,
                timeout=urllib3.Timeout(connect=5, read=30),
                cert_reqs="CERT_REQUIRED",
                ca_certs=certifi.where()
            )
        else:
            self.pool = urllib3.HTTPConnectionPool(
                host, port=port or 80,
                maxsize=5,
                timeout=urllib3.Timeout(connect=5, read=30)
            )
    
    def request(self, method, path, body=None, headers=None):
        headers = headers or {}
        
        if body and isinstance(body, dict):
            body = json.dumps(body).encode()
            headers["Content-Type"] = "application/json"
        
        try:
            response = self.pool.urlopen(
                method=method,
                url=path,
                body=body,
                headers=headers,
                retries=3
            )
            return {
                "status": response.status,
                "headers": dict(response.headers),
                "body": response.data.decode()
            }
        except urllib3.exceptions.MaxRetryError as e:
            print(f"Request failed after retries: {e}")
            raise
        except urllib3.exceptions.TimeoutError:
            print("Request timed out")
            raise

client = CustomHTTPClient("localhost", 8080)
result = client.request("POST", "/api/data", {"key": "value"})
print(result)
```

## Common Scenarios

### Scenario 1: Proxy Configuration

Setting up HTTP/HTTPS proxy support:

```python
import urllib3

# HTTP proxy
proxy_pool = urllib3.ProxyManager(
    "http://proxy.example.com:8080",
    num_pools=10,
    maxsize=10
)

# HTTPS proxy with authentication
proxy_auth = urllib3.ProxyManager(
    "http://user:pass@proxy.example.com:8080",
    proxy_headers=urllib3.make_headers(proxy_basic_auth="user:pass")
)

response = proxy_pool.request("GET", "https://target.example.com/api")
print(response.status)

# SOCKS proxy requires urllib3[socks]
# proxy_socks = urllib3.ProxyManager("socks5://localhost:1080")
```

## Prevent It

- Always set `maxsize` on pool connections to prevent connection starvation
- Use `urllib3.Timeout` with separate connect and read timeout values
- Configure `cert_reqs="CERT_REQUIRED"` in production with valid CA certificates
- Set `retries` parameter on every request for automatic failure recovery
- Monitor pool utilization with `pool.connections` and `pool.num_connections`