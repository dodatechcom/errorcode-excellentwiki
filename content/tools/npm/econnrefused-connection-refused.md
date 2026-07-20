---
title: "[Solution] npm install ECONNREFUSED Connection Refused"
description: "Resolve ECONNREFUSED connection refused errors in npm install by checking network configuration and registry settings."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install ECONNREFUSED Connection Refused

This guide helps you diagnose and resolve npm install ECONNREFUSED Connection Refused errors encountered when running npm commands.

## Common Causes

- Registry server is down or unreachable from your network
- Local proxy server is not running or misconfigured
- Firewall rules blocking outgoing connections to npm registry

## How to Fix

### Verify Registry Accessibility

```bash
curl -I https://registry.npmjs.org
```

### Check and Configure Proxy

```bash
npm config get proxy
npm config set proxy http://proxy:port
```

### Try an Alternative Registry

```bash
npm config set registry https://registry.npmmirror.com
```

## Examples

```bash
# Registry server unreachable
npm install lodash
# Fix: Test connectivity and switch registry
curl -I https://registry.npmjs.org
npm config set registry https://registry.npmmirror.com

# Corporate proxy blocking
npm install axios
# Fix: Set proxy configuration
npm config set proxy http://corporate-proxy:8080
npm config set https-proxy http://corporate-proxy:8080

```

## Related Errors

- [ETIMEDOUT Timeout]({{< relref "/tools/npm/etimedout-timeout" >}}) -- connection timeout
- [Host Unreachable]({{< relref "/tools/npm/ehostunreach-host-unreachable" >}}) -- host unreachable
