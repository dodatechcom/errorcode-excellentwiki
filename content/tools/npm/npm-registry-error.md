---
title: "[Solution] npm Registry Connection Error"
description: "Fix npm registry connection errors. Resolve registry connectivity issues."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

A npm registry connection error occurs when npm cannot connect to the package registry. This can be caused by network issues, proxy configuration, or registry downtime.

## Common Causes

- Network connectivity issues
- Proxy or firewall blocking npm traffic
- Registry server is down or rate limiting
- DNS resolution failure for registry domain
- SSL certificate issues

## How to Fix

### Check Registry Configuration

```bash
npm config get registry
```

### Test Registry Connectivity

```bash
curl -v https://registry.npmjs.org/
```

### Configure Proxy

```bash
npm config set proxy http://proxy.company.com:8080
npm config set https-proxy http://proxy.company.com:8080
```

### Use Alternative Registry

```bash
npm config set registry https://registry.npmjs.org/
```

### Increase Timeout

```bash
npm config set fetch-timeout 60000
```

## Examples

```bash
# Example 1: Registry unreachable
npm install
# npm ERR! code ENOTFOUND
# npm ERR! getaddrinfo ENOTFOUND registry.npmjs.org
# Fix: check network connection

# Example 2: Configure proxy
npm config set proxy http://proxy.company.com:8080
npm install
```

## Related Errors

- [npm Token Error]({{< relref "/tools/npm/npm-token-error" >}}) — token authentication failed
- [npm Pack Error]({{< relref "/tools/npm/npm-pack-error" >}}) — npm pack error
