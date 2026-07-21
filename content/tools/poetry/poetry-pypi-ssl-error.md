---
title: "[Solution] Poetry PyPI SSL Error -- Fix SSL Certificate Verification"
description: "Fix Poetry PyPI SSL error when SSL certificate verification fails during package downloads. Configure certificates and disable strict verification."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry's HTTPS connection to PyPI failed SSL certificate verification. The server's certificate could not be validated.

## Common Causes

- Corporate proxy intercepts HTTPS with a custom CA
- System CA certificates are outdated
- Python's SSL module lacks the necessary CA bundle
- Certificate has expired or is self-signed

## How to Fix

### 1. Update CA Certificates

```bash
sudo apt update && sudo apt install ca-certificates
sudo update-ca-certificates
```

### 2. Set SSL Certificate Path

```bash
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
poetry install
```

### 3. Disable SSL Verification (Temporary)

```bash
poetry config installer.parallel false
export PIP_TRUSTED_HOST=pypi.org
poetry install
```

### 4. Install Certificates for Python

```bash
pip install certifi
export SSL_CERT_FILE=$(python -c "import certifi; print(certifi.where())")
```

## Examples

```bash
$ poetry install
SSLError: SSL certificate verify failed

$ sudo update-ca-certificates
$ poetry install
Installing dependencies from lock file...
```
