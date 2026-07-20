---
title: "[Solution] npm install ETIMEDOUT Timeout"
description: "Fix ETIMEDOUT timeout errors in npm install by adjusting network settings and using reliable registry mirrors."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install ETIMEDOUT Timeout

This guide helps you diagnose and resolve npm install ETIMEDOUT Timeout errors encountered when running npm commands.

## Common Causes

- Slow or unstable internet connection causing request timeouts
- Corporate firewall or proxy blocking npm registry access
- npm registry server experiencing high latency

## How to Fix

### Increase npm Timeout Duration

```bash
npm config set fetch-timeout 60000
```

### Switch to a Faster Registry Mirror

```bash
npm config set registry https://registry.npmmirror.com
```

### Configure Proxy Settings

```bash
npm config set proxy http://proxy-server:port
npm config set https-proxy http://proxy-server:port
```

## Examples

```bash
# Default timeout on slow connection
npm install express
# Fix: Increase timeout
npm config set fetch-timeout 120000
npm install express

# Corporate network blocking registry
npm install react
# Fix: Use mirror and set proxy
npm config set registry https://registry.npmmirror.com
npm install react

```

## Related Errors

- [Connection Refused]({{< relref "/tools/npm/econnrefused-connection-refused" >}}) -- connection refused
- [DNS Error]({{< relref "/tools/npm/enotfound-dns-error" >}}) -- DNS resolution failed
