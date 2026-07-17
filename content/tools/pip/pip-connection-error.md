---
title: "[Solution] pip Connection Error — Fix Network Failures During Install"
description: "Fix pip connection errors when pip cannot reach PyPI or package indexes to download packages. Resolve proxy, firewall, and DNS issues blocking installs."
tools: ["pip"]
error-types: ["network-error"]
severities: ["error"]
weight: 5
---

This error means pip could not establish a network connection to the package index server. The download fails before any installation begins, usually with a `ConnectionError` or `SSLError` traceback.

## What This Error Means

pip needs to reach `https://pypi.org/simple/` (or your configured index) to resolve and download packages. When the TCP connection times out, is refused, or is intercepted by a proxy/firewall, pip raises a connection error. Typical output:

```
ERROR: Could not find a version that satisfies the requirement <package>
ERROR: Retrying (Retry(total=3, ...)) after connection broken by 'SSLError'
```

## Why It Happens

- You are behind a corporate proxy that blocks or intercepts HTTPS traffic
- A firewall or security group blocks outbound port 443
- DNS resolution fails for `pypi.org` or your private index server
- The PyPI mirror or index server is temporarily down
- VPN or network adapter is misconfigured

## How to Fix It

### Test Basic Connectivity

```bash
curl -I https://pypi.org/simple/
```

If this fails, the problem is at the network level, not with pip.

### Configure Proxy Settings

```bash
pip install <package> --proxy http://proxy-server:8080
```

Or set environment variables:

```bash
export HTTP_PROXY=http://proxy-server:8080
export HTTPS_PROXY=http://proxy-server:8080
pip install <package>
```

### Use a PyPI Mirror

Switch to a closer or more reliable mirror:

```bash
pip install <package> -i https://pypi.tuna.tsinghua.edu.cn/simple/
```

### Increase Retry and Timeout

```bash
pip install <package> --retries 10 --timeout 60
```

### Disable SSL Verification (Temporary Only)

For self-signed corporate proxies:

```bash
pip install <package> --trusted-host pypi.org --trusted-host files.pythonhosted.org
```

Do not leave this permanent -- fix the root cause.

### Check DNS Resolution

```bash
nslookup pypi.org
python3 -c "import socket; print(socket.getaddrinfo('pypi.org', 443))"
```

## Common Mistakes

- Forgetting to set proxy variables for both HTTP and HTTPS
- Leaving `--trusted-host` in a global pip config permanently
- Not checking if the VPN is connected before blaming pip
- Using a corporate mirror that is behind a firewall with no direct internet

## Related Pages

- [pip SSL Error]({{< relref "/tools/pip/pip-ssl-error" >}}) -- SSL certificate verification failed
- [pip Install Error]({{< relref "/tools/pip/pip-install-error" >}}) -- environment error during install
- [pip Version Error]({{< relref "/tools/pip/pip-version-error" >}}) -- no matching distribution found
