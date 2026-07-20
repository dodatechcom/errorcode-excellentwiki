---
title: "[Solution] npm install E504 Gateway Timeout"
description: "Fix E504 gateway timeout errors in npm install by adjusting timeout settings, using faster mirrors, and optimizing network paths."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install E504 Gateway Timeout

This guide helps you diagnose and resolve npm install E504 Gateway Timeout errors encountered when running npm commands.

## Common Causes

- Gateway server timed out waiting for upstream response
- Network latency between client and registry is too high
- Large package download exceeded the default timeout threshold

## How to Fix

### Increase Fetch Timeout

```bash
npm config set fetch-timeout 120000
```

### Increase Retry Count

```bash
npm config set fetch-retries 5
```

### Switch to a Closer Registry Mirror

```bash
npm config set registry https://registry.npmmirror.com
```

## Examples

```bash
# Timeout on large package
npm install @angular/core
# Fix: Increase timeout
npm config set fetch-timeout 120000
npm config set fetch-retries 5

# High latency network
npm install typescript
# Fix: Use closer mirror
npm config set registry https://registry.npmmirror.com

```

## Related Errors

- [ETIMEDOUT Timeout]({{< relref "/tools/npm/etimedout-timeout" >}}) -- request timeout
- [E503 Service Unavailable]({{< relref "/tools/npm/e503-service-unavailable" >}}) -- service down
