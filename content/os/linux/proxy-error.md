---
title: "[Solution] Linux: proxy-error — proxy configuration error"
description: "Fix Linux proxy-error errors. proxy configuration error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 6
---
# Linux: Proxy Error

Proxy errors occur when HTTP/HTTPS proxy configuration prevents network access or causes connection failures.

## Common Causes

- Proxy server unreachable or not running
- Proxy authentication required but not configured
- Proxy environment variables set incorrectly
- no_proxy settings missing for internal addresses
- Proxy server returning errors (502, 503, 407)

## How to Fix

### 1. Check Proxy Environment Variables

```bash
echo $http_proxy
echo $https_proxy
echo $no_proxy
```

### 2. Test Proxy Connectivity

```bash
curl -v --proxy http://proxy:8080 http://example.com
```

### 3. Set Proxy Correctly

```bash
# For current session
export http_proxy=http://proxy.example.com:8080
export https_proxy=http://proxy.example.com:8080
export no_proxy=localhost,.internal,10.0.0.0/8

# Make permanent in ~/.bashrc or /etc/environment
```

### 4. Configure Proxy for apt

```bash
cat <<EOF | sudo tee /etc/apt/apt.conf.d/90proxy
Acquire::http::Proxy "http://proxy.example.com:8080";
Acquire::https::Proxy "http://proxy.example.com:8080";
EOF
```

## Examples

```bash
$ curl https://google.com
curl: (7) Failed to connect to google.com port 443: Connection timed out

$ echo $http_proxy
http://proxy.example.com:8080

$ curl -v --proxy http://proxy.example.com:8080 https://google.com
# Works when proxy is specified correctly
```
