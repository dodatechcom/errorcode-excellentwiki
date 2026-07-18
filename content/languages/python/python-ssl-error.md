---
title: "[Solution] Python SSL Certificate Verification Error — How to Fix"
description: "Fix Python SSL certificate verification errors. Resolve SSL handshake and certificate issues."
languages: ["python"]
error-types: ["runtime-error"]
severities: ["error"]
comments: true
weight: 5
---

# Python SSL Certificate Verification Error

A `SSLCertVerificationError` occurs when Python's ssl module fails when it cannot verify the server's certificate during HTTPS connections..

## Why It Happens

This happens when the system CA bundle is missing, the certificate is self-signed, or the certificate has expired. Python enforces strict type and state checking.

## Common Error Messages

- `certificate verify failed`
- `WRONG_VERSION_NUMBER`
- `max retries exceeded`

## How to Fix It

### Fix 1: Use ssl.create_default_context()

```python
import ssl
import urllib.request

ctx = ssl.create_default_context()
response = urllib.request.urlopen('https://example.com', context=ctx)
```

### Fix 2: Load custom CA certificate

```python
import ssl

ctx = ssl.create_default_context()
ctx.load_verify_locations('ca-bundle.crt')
```

### Fix 3: Disable verification for testing only

```python
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
```

### Fix 4: Use requests library

```python
import requests

response = requests.get('https://example.com', verify='ca-bundle.crt')
```

## Common Scenarios

- **Self-signed certificates** — Development servers use self-signed certs not in system CA bundle.
- **Expired certificates** — Server certificate has passed its validity period.
- **Corporate proxies** — Corporate proxies intercept HTTPS with their own certs.

## Prevent It

- Always use ssl.create_default_context() instead of manual SSL wrapping
- Never disable SSL verification in production
- Keep CA certificates updated with certifi package

## Related Errors

- - [ConnectionError](/languages/python/connectionerror/) — network connection failure
- - [TimeoutError](/languages/python/timeouterror/) — operation timed out
- - [urllib3 Error](/languages/python/urllib3-error/) — HTTP client errors
