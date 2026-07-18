---
title: "[Solution] Prometheus Thanos Error"
description: "Fix Prometheus thanos errors. Learn why this happens and how to resolve it quickly."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Prometheus Thanos Error

Thanos errors occur when the Thanos sidecar, store, or query components fail to operate correctly.

## Why This Happens

- Sidecar not connected
- Store gateway unreachable
- Query timeout
- Object storage error

## Common Error Messages

- `thanos_sidecar_error`
- `thanos_store_error`
- `thanos_query_error`
- `thanos_storage_error`

## How to Fix It

### Solution 1: Check sidecar status

Verify the sidecar is running and connected.

### Solution 2: Verify store gateway

Check if the store gateway is accessible.

### Solution 3: Configure object storage

Set up S3-compatible storage:

```yaml
objstore:
  type: S3
  config:
    bucket: thanos
    endpoint: s3.amazonaws.com
```


## Common Scenarios

- **Sidecar not connecting:** Check network connectivity to Prometheus.
- **Store gateway unreachable:** Verify the store gateway is running.

## Prevent It

- Monitor Thanos components
- Set up alerts
- Test failover
