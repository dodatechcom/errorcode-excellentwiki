---
title: "[Solution] npm audit Registry Unavailable"
description: "Fix npm audit registry unavailable errors by checking registry status, using alternative endpoints, and configuring fallback registries."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm audit Registry Unavailable

This guide helps you diagnose and resolve npm audit Registry Unavailable errors encountered when running npm commands.

## Common Causes

- npm registry is down or undergoing maintenance
- Audit API endpoint is temporarily disabled
- Network issues preventing access to registry audit service

## How to Fix

### Check npm Registry Status

```bash
curl https://status.npmjs.org/api/v2/status.json
```

### Try Alternative Registry

```bash
npm config set registry https://registry.npmmirror.com
```

### Skip Audit Temporarily

```bash
npm install --no-audit
```

## Examples

```bash
# Registry in maintenance
npm audit
# Fix: Check status and retry later
curl https://status.npmjs.org/api/v2/status.json

# Audit endpoint unreachable
npm audit
# Fix: Use alternative or skip
npm audit --registry https://registry.npmmirror.com

```

## Related Errors

- [ETIMEDOUT Timeout]({{< relref "/tools/npm/etimedout-timeout" >}}) -- request timeout
- [Service Unavailable]({{< relref "/tools/npm/e503-service-unavailable" >}}) -- service down
