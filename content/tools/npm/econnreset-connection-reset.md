---
title: "[Solution] npm install ECONNRESET Connection Reset"
description: "Resolve ECONNRESET connection reset errors in npm install by configuring keep-alive settings and adjusting network timeout values."
tools: ["npm"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# npm install ECONNRESET Connection Reset

This guide helps you diagnose and resolve npm install ECONNRESET Connection Reset errors encountered when running npm commands.

## Common Causes

- Server dropped the connection unexpectedly during data transfer
- Firewall or proxy is resetting long-lived HTTP connections
- Network instability causing TCP connection drops mid-transfer

## How to Fix

### Set Keep-Alive Timeout

```bash
npm config set fetch-timeout 60000
```

### Retry with Exponential Backoff

```bash
for i in 1 2 3; do npm install && break || sleep $((i*10)); done
```

### Increase Retry Count

```bash
npm config set fetch-retries 5
```

## Examples

```bash
# Connection reset on large download
npm install @angular/cli
# Fix: Increase timeout and retry
npm config set fetch-timeout 120000

# Proxy resetting connections
npm install react
# Fix: Adjust timeout and retries
npm config set fetch-retries 5

```

## Related Errors

- [Connection Refused]({{< relref "/tools/npm/econnrefused-connection-refused" >}}) -- connection refused
- [Socket Timeout]({{< relref "/tools/npm/err-socket-timeout-socket-timeout" >}}) -- socket timeout
