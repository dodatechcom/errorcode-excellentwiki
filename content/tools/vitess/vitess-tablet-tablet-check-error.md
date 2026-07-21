---
title: "[Solution] Vitess Tablet Health Check Error"
description: "Fix Vitess tablet health check errors when tablets fail health probes from vtgate"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Health Check Error

Health check errors occur when vtgate cannot verify that a tablet is healthy enough to serve queries.

## Common Causes

- Tablet gRPC port unreachable
- MySQL process crashed on tablet host
- Tablet overloaded and not responding
- Health check interval too aggressive

## How to Fix

Check tablet gRPC:

```bash
grpcurl -plaintext localhost:15999 grpc.health.v1.Health/Check
```

Restart MySQL on tablet:

```bash
systemctl restart mysql
```

Adjust health check timeout:

```bash
vtgate -tablet_refresh_interval 30s -tablet_health_timeout 10s
```

## Examples

```bash
vtctlclient Ping cell1-tablet-100
```
