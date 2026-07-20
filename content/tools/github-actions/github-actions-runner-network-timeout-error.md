---
title: "[Solution] GitHub Actions Runner Network Timeout Error"
description: "Fix GitHub Actions runner network timeout errors during workflow execution."
tools: ["github-actions"]
error-types: ["tool-error"]
severities: ["error"]
---

## Error Description

Network timeout errors occur when the runner cannot reach external services:

```
Error: network timeout while connecting to github.com:443
fatal: unable to access 'https://github.com/': Could not resolve host
```

## Common Causes

- DNS resolution failure on the runner.
- Firewall blocking outbound connections.
- Corporate proxy not configured.

## How to Fix

**Configure DNS:**

```bash
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
```

**Set environment variables for the workflow:**

```yaml
env:
  HTTP_PROXY: http://proxy.example.com:8080
  HTTPS_PROXY: http://proxy.example.com:8080
steps:
  - uses: actions/checkout@v4
```

## Examples

```bash
# Test connectivity
curl -I https://github.com
```
