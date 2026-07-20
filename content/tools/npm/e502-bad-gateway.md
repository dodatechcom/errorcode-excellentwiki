---
title: "[Solution] npm install E502 Bad Gateway"
description: "Resolve E502 bad gateway errors during npm install by waiting for server recovery, retrying with delays, and using mirrors."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install E502 Bad Gateway

This guide helps you diagnose and resolve npm install E502 Bad Gateway errors encountered when running npm commands.

## Common Causes

- Upstream server behind the gateway is temporarily unavailable
- Load balancer cannot connect to the npm registry backend
- CDN layer is experiencing transient connectivity issues

## How to Fix

### Wait and Retry After a Delay

```bash
sleep 60 && npm install
```

### Use a Registry Mirror

```bash
npm config set registry https://registry.npmmirror.com
```

### Bypass CDN with Direct Registry URL

```bash
npm config set registry https://registry.npmjs.org
```

## Examples

```bash
# CDN returning 502
npm install lodash
# Fix: Use alternative registry
npm config set registry https://registry.npmmirror.com

# Transient gateway error
npm install express
# Fix: Retry with delay
sleep 60 && npm install express

```

## Related Errors

- [E500 Internal Server Error]({{< relref "/tools/npm/e500-internal-error" >}}) -- server error
- [Service Unavailable]({{< relref "/tools/npm/e503-service-unavailable" >}}) -- service down
