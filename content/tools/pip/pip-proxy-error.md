---
title: "[Solution] Pip Proxy Connection Failed Error Fix"
description: "Fix 'pip proxy connection failed' errors. Configure pip proxy settings for HTTP and HTTPS connections in Python."
tools: ["pip"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# Pip Proxy Connection Failed Error Fix

The pip proxy connection failed error occurs when pip cannot connect to PyPI through a proxy server due to wrong proxy configuration or proxy server issues.

## What This Error Means

pip uses proxy settings to route HTTP/HTTPS traffic through proxy servers. When proxy settings are wrong, authentication fails, or the proxy server is unreachable, pip cannot download packages.

A typical error:

```
ERROR: Could not find a version that satisfies the requirement package-name
ERROR: Connection error: Cannot connect to proxy
```

## Why It Happens

Common causes include:

- **Wrong proxy URL** — Incorrect proxy address or port.
- **Proxy authentication required** — Credentials not provided.
- **Proxy server down** — Proxy not reachable.
- **HTTPS proxy issues** — Different proxy for HTTPS.
- **Environment variable conflicts** — Proxy env vars conflicting.
- **Proxy does not support PyPI** — Corporate proxy blocks package sites.

## How to Fix It

### Fix 1: Configure proxy in pip.conf

```ini
# RIGHT: Set proxy in pip.conf
[global]
proxy = http://proxy.example.com:8080

# With authentication
proxy = http://user:password@proxy.example.com:8080
```

### Fix 2: Use environment variables

```bash
# RIGHT: Set proxy environment variables
export HTTP_PROXY=http://proxy.example.com:8080
export HTTPS_PROXY=http://proxy.example.com:8080
export NO_PROXY=localhost,127.0.0.1

pip install package-name
```

### Fix 3: Use command line proxy

```bash
# RIGHT: Specify proxy on command line
pip install package-name --proxy http://proxy.example.com:8080

# For different protocols
pip install package-name --proxy socks5://proxy.example.com:1080
```

### Fix 4: Test proxy connectivity

```bash
# RIGHT: Test proxy works
curl -x http://proxy.example.com:8080 https://pypi.org/simple/

# Test with pip
pip install package-name -v  # Verbose shows connection details
```

### Fix 5: Bypass proxy for local packages

```bash
# RIGHT: No proxy for local
export NO_PROXY=localhost,127.0.0.1,10.0.0.0/8

# Or in pip.conf
[global]
no-proxy = localhost,127.0.0.1
```

## Common Mistakes

- **Using HTTP proxy for HTTPS** — Most proxies need HTTPS proxy setting.
- **Not encoding special characters in password** — URL-encode special characters.
- **Forgetting that --proxy does not persist** — Use pip.conf for persistent settings.

## Related Pages

- [Pip Config Error](pip-config-file-error) — Configuration issues
- [Pip Download Error](pip-download-error) — Download issues
- [Pip Install Error](/tools/pip/pip-install-error) — Installation problems
