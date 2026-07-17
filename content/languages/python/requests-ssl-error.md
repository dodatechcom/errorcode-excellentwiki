---
title: "[Solution] requests SSLError: Certificate Verify Failed Fix"
description: "Fix requests SSLError certificate verify failed. Handle SSL certificates, configure verification, and resolve CA bundle issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["requests", "ssl", "certificate", "https", "security"]
weight: 5
---

# requests SSLError: Certificate Verify Failed Fix

A `requests.exceptions.SSLError` is raised when the `requests` library cannot verify the SSL certificate of the remote server.

## What This Error Means

Common messages:

- `requests.exceptions.SSLError: HTTPSConnectionPool: certificate verify failed`
- `SSLError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed`
- `SSLError: certificate has expired`

The SSL/TLS handshake failed because the server's certificate could not be verified against the trusted CA certificates. This can indicate a security issue or a misconfigured environment.

## Common Causes

```python
import requests

# Cause 1: Self-signed certificate
response = requests.get("https://internal-server.example.com")  # SSLError

# Cause 2: Missing CA certificates on system
response = requests.get("https://example.com")  # SSLError on minimal systems

# Cause 3: Expired certificate on server
response = requests.get("https://expired-server.example.com")

# Cause 4: Certificate hostname mismatch
response = requests.get("https://www.example.com")  # Certificate for example.com

# Cause 5: Corporate proxy intercepting HTTPS
response = requests.get("https://api.example.com")  # Proxy CA not trusted
```

## How to Fix

### Fix 1: Install certifi and update CA bundle

```bash
pip install certifi --upgrade
```

```python
import certifi
import requests

response = requests.get("https://example.com", verify=certifi.where())
```

### Fix 2: Provide custom CA bundle

```python
import requests

response = requests.get(
    "https://internal-server.example.com",
    verify="/path/to/custom-ca-bundle.crt",
)
```

### Fix 3: Verify only for internal/self-signed servers

```python
import requests

# WARNING: Only disable verification for trusted internal servers
response = requests.get("https://internal-server.example.com", verify=False)
```

### Fix 4: Use session with persistent settings

```python
import requests

session = requests.Session()
session.verify = "/path/to/ca-bundle.crt"

response = session.get("https://api.example.com")
```

### Fix 5: Handle corporate proxy certificates

```python
import requests
import os

# Set CA bundle via environment variable
os.environ["REQUESTS_CA_BUNDLE"] = "/path/to/corporate-ca-bundle.crt"

response = requests.get("https://api.example.com")
```

### Fix 6: Suppress InsecureRequestWarning when verify=False

```python
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
response = requests.get("https://internal-server", verify=False)
```

## Related Errors

- {{< relref "connectionreseterror" >}} — Connection reset by peer.
- {{< relref "httpx-timeout-error" >}} — HTTPX timeout error.
