---
title: "[Solution] Poetry Remote Timeout -- Fix Package Download Timeout"
description: "Fix Poetry remote timeout errors when downloading packages from PyPI fails due to network timeouts. Configure timeouts and use alternative sources."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry's request to PyPI or a custom source timed out before receiving a response. The download or resolution process was interrupted.

## Common Causes

- Slow network connection or high latency
- PyPI server is experiencing high load
- Corporate proxy is throttling requests
- Firewall is blocking or delaying HTTPS connections
- DNS resolution is slow

## How to Fix

### 1. Increase Timeout

```bash
poetry config http.timeout 120
```

### 2. Use a Mirror or CDN

```toml
[[tool.poetry.source]]
name = "pypi-mirror"
url = "https://mirrors.aliyun.com/pypi/simple/"
priority = "supplemental"
```

### 3. Retry with Verbose Output

```bash
poetry install -vvv
```

### 4. Clear Cache and Retry

```bash
poetry cache clear --all pypi
poetry install
```

## Examples

```bash
$ poetry install
HTTPSConnectionPool(host='pypi.org', port=443): Read timed out. (read timeout=30)

$ poetry config http.timeout 120
$ poetry install
Installing dependencies from lock file...
```
