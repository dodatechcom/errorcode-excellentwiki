---
title: "[Solution] npm Registry Error -- registry connection failed"
description: "Fix npm registry error. Resolve network and authentication issues with npm registry."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm Registry Error -- registry connection failed

Registry errors occur when npm cannot connect to the package registry. This may be due to network issues, registry downtime, or configuration problems.

## Common Causes

- Network connectivity issues
- Registry server is down or rate-limiting
- Incorrect registry URL configuration
- Proxy or firewall blocking requests
- SSL certificate issues

## How to Fix

### Check Registry URL

```bash
npm config get registry
```

### Set Default Registry

```bash
npm config set registry https://registry.npmjs.org/
```

### Check Network Connection

```bash
curl -I https://registry.npmjs.org/
```

### Configure Proxy

```bash
npm config set proxy http://proxy-server:8080
npm config set https-proxy http://proxy-server:8080
```

### Disable Strict SSL (temporary)

```bash
npm config set strict-ssl false
```

### Use Different Registry

```bash
npm config set registry https://registry.npm.taobao.org/
```

## Examples

```bash
# Example 1: Connection timeout
npm install express
# npm ERR! code ECONNRESET
# Fix: check network connection and proxy settings

# Example 2: SSL error
npm install express
# npm ERR! code UNABLE_TO_VERIFY_LEAF_SIGNATURE
# Fix: npm config set strict-ssl false (temporary)

# Example 3: Check registry status
curl -I https://registry.npmjs.org/
# HTTP/1.1 200 OK
```

## Related Errors

- [Cache Error]({{< relref "/tools/npm/cache-error" >}}) -- npm cache corruption
- [Package Not Found]({{< relref "/tools/npm/package-not-found2" >}}) -- 404 not found
