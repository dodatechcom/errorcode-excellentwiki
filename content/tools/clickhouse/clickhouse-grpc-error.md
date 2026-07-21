---
title: "[Solution] ClickHouse gRPC Error"
description: "Fix ClickHouse gRPC interface errors when gRPC-based connections fail"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse gRPC Error

gRPC errors occur when ClickHouse gRPC service encounters connection or protocol issues.

## Common Causes

- gRPC port not configured or blocked
- Maximum message size exceeded
- gRPC service not enabled in config
- TLS certificate issues for secure gRPC

## How to Fix

Check gRPC port:

```bash
ss -tlnp | grep 9100
```

Enable gRPC in config:

```xml
<grpc_port>9100</grpc_port>
```

Test gRPC connection:

```bash
grpcurl -plaintext localhost:9100 list
```

## Examples

```xml
<grpc>
    <port>9100</port>
    <max_message_size>104857600</max_message_size>
</grpc>
```
