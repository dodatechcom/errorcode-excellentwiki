---
title: "[Solution] pip Install Certificate Error -- Fix SSL Certificate Problem"
description: "Fix pip install certificate error when SSL certificate verification fails. Update certificates or use trusted hosts."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip's HTTPS connection failed because SSL certificate verification failed.

## Common Causes

- Corporate proxy intercepts HTTPS
- System CA certificates are outdated
- Using self-signed certificates
- Python does not have access to CA bundle

## How to Fix

### 1. Update CA Certificates

```bash
sudo apt update && sudo apt install ca-certificates
sudo update-ca-certificates
```

### 2. Install Certifi

```bash
pip install certifi
export SSL_CERT_FILE=$(python -c "import certifi; print(certifi.where())")
```

### 3. Use Trusted Host (Temporary)

```bash
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org <package>
```

### 4. Set Certificate Path

```bash
export REQUESTS_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
```

## Examples

```bash
$ pip install requests
ERROR: SSL: CERTIFICATE_VERIFY_FAILED

$ sudo update-ca-certificates
$ pip install requests
Successfully installed requests-2.31.0
```
