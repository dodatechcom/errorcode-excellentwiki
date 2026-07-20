---
title: "[Solution] npm install ERR_SOCKET_TIMEOUT Socket Timeout"
description: "Fix ERR_SOCKET_TIMEOUT socket timeout errors in npm install by increasing socket timeouts and optimizing network connection stability."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install ERR_SOCKET_TIMEOUT Socket Timeout

This guide helps you diagnose and resolve npm install ERR_SOCKET_TIMEOUT Socket Timeout errors encountered when running npm commands.

## Common Causes

- Default socket timeout is too low for slow network connections
- Registry server is slow to respond to package metadata requests
- Network congestion causing delayed responses from npm servers

## How to Fix

### Increase Socket Timeout

```bash
npm config set fetch-timeout 120000
```

### Set HTTP Pool Size

```bash
npm config set maxsockets 10
```

### Use a Faster Registry

```bash
npm config set registry https://registry.npmmirror.com
```

## Examples

```bash
# Default timeout too short
npm install moment
# Fix: Increase timeout
npm config set fetch-timeout 120000
npm config set maxsockets 10

# Slow registry response
npm install lodash
# Fix: Use faster registry
npm config set registry https://registry.npmmirror.com

```

## Related Errors

- [ETIMEDOUT Timeout]({{< relref "/tools/npm/etimedout-timeout" >}}) -- request timeout
- [Connection Reset]({{< relref "/tools/npm/econnreset-connection-reset" >}}) -- connection reset
