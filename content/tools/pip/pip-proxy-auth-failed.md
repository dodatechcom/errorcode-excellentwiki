---
title: "[Solution] pip Proxy Auth Failed -- Fix Proxy Authentication Error"
description: "Fix pip proxy auth failed errors when pip cannot authenticate with the corporate proxy. Configure proxy credentials correctly."
tools: ["pip"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means pip tried to use an HTTP proxy but the proxy rejected the authentication credentials.

## Common Causes

- Proxy username or password is wrong
- Proxy requires NTLM or Kerberos authentication
- Proxy URL format is incorrect
- Password contains special characters

## How to Fix

### 1. Set Proxy with Authentication

```bash
pip install --proxy http://user:pass@proxy:8080 <package>
```

### 2. Use Environment Variables

```bash
export HTTP_PROXY=http://user:pass@proxy:8080
export HTTPS_PROXY=http://user:pass@proxy:8080
```

### 3. URL-Encode Special Characters

```bash
pip install --proxy "http://user:p%40ss@proxy:8080" <package>
```

### 4. Configure in pip.conf

```ini
[global]
proxy = http://user:pass@proxy:8080
```

## Examples

```bash
$ pip install requests
ERROR: Proxy connection failed: 407 Proxy Authentication Required

$ pip install --proxy http://user:p%40ssw0rd@proxy:8080 requests
Successfully installed requests-2.31.0
```
