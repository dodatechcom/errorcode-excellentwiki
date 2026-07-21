---
title: "[Solution] Vitess Tablet gRPC Error"
description: "How to fix Vitess tablet gRPC errors"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- gRPC port not listening
- gRPC TLS mismatch
- gRPC message too large

## How to Fix

```bash
vttablet --grpc_port=15999
```

## Examples

```bash
curl -k https://tablet-host:15999/debug/status
```
