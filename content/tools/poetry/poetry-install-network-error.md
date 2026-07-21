---
title: "[Solution] Poetry Install Network Error -- Fix Connection Failures"
description: "Fix Poetry install network error when package downloads fail due to connectivity issues. Configure proxies and alternative mirrors."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry could not download packages due to a network error. The connection was refused, reset, or timed out.

## Common Causes

- No internet connection or restricted network
- Corporate firewall blocks PyPI
- DNS resolution fails
- Proxy settings are not configured
- VPN is not connected

## How to Fix

### 1. Check Network Connectivity

```bash
curl -I https://pypi.org/simple/
```

### 2. Configure Proxy

```bash
export HTTPS_PROXY=http://proxy.company.com:8080
poetry install
```

### 3. Use a Local Mirror

```toml
[[tool.poetry.source]]
name = "local-mirror"
url = "https://pypi-mirror.company.com/simple/"
priority = "supplemental"
```

### 4. Retry with Increased Timeout

```bash
poetry config http.timeout 300
poetry install
```

## Examples

```bash
$ poetry install
ConnectionError: HTTPSConnectionPool(host='pypi.org', port=443):
Max retries exceeded: Name or service not known

$ export HTTPS_PROXY=http://proxy:8080
$ poetry install
Installing dependencies from lock file...
```
