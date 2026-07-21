---
title: "[Solution] ClickHouse gRPC Error"
description: "How to fix ClickHouse gRPC connection errors"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- gRPC port not enabled
- Max message size exceeded
- TLS mismatch on gRPC port

## How to Fix

```xml
<grpc_port>9150</grpc_port>
```

## Examples

```bash
curl -s http://localhost:8123/ping
```
