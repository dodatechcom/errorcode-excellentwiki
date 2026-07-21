---
title: "[Solution] Poetry Source Unreachable -- Fix Package Source Connection"
description: "Fix Poetry source unreachable errors when Poetry cannot connect to a configured package source. Check network access and source URLs."
tools: ["poetry"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

This error means Poetry could not reach one of the configured package sources. The connection failed due to network, DNS, or authentication issues.

## Common Causes

- The source URL is incorrect or has changed
- The source requires VPN or corporate network access
- DNS resolution fails for the source host
- SSL certificate verification fails for the source
- The source is down or experiencing outages

## How to Fix

### 1. Check Source Configuration

```bash
poetry source --list
```

### 2. Test the Source URL

```bash
curl -I https://your-private-pypi.example.com/simple/
```

### 3. Skip Certificate Verification (Temporary)

```toml
[[tool.poetry.source]]
name = "private"
url = "https://pypi.internal.com/simple/"
```

### 4. Disable the Unreachable Source

```bash
poetry source disable private
```

## Examples

```bash
$ poetry install
ConnectionError: HTTPSConnectionPool(host='pypi.internal.com', port=443):
Max retries exceeded

$ curl -I https://pypi.internal.com/simple/
HTTP/1.1 200 OK

$ poetry install
Installing dependencies from lock file...
```
