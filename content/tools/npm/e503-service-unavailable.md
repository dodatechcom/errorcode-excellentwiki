---
title: "[Solution] npm install E503 Service Unavailable"
description: "Handle E503 service unavailable errors in npm install by checking registry status, using mirrors, and retrying after maintenance."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install E503 Service Unavailable

This guide helps you diagnose and resolve npm install E503 Service Unavailable errors encountered when running npm commands.

## Common Causes

- npm registry is undergoing scheduled maintenance
- Server is overloaded and cannot handle additional requests
- Service has been temporarily disabled due to incident response

## How to Fix

### Check npm Registry Status

```bash
curl https://status.npmjs.org
```

### Use an Alternative Registry

```bash
npm config set registry https://registry.npmmirror.com
```

### Retry After Maintenance Window

```bash
sleep 300 && npm install
```

## Examples

```bash
# Registry in maintenance mode
npm install webpack
# Fix: Check status and use mirror
curl https://status.npmjs.org

# Overloaded server
npm install next
# Fix: Wait and retry
sleep 120 && npm install next

```

## Related Errors

- [E502 Bad Gateway]({{< relref "/tools/npm/e502-bad-gateway" >}}) -- gateway error
- [E504 Gateway Timeout]({{< relref "/tools/npm/e504-gateway-timeout" >}}) -- gateway timeout
