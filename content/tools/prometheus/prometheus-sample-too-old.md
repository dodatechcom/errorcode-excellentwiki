---
title: "[Solution] Prometheus Sample Too Old Error"
description: "How to fix Prometheus out-of-order or too-old sample errors during ingestion"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Target sending samples with timestamps too far in the past
- Clock skew between Prometheus server and target
- `out_of_order_time_window` exceeded
- Remote write lag causing stale timestamps

## How to Fix

Check time synchronization on all hosts:

```bash
chronyc tracking
timedatectl status
```

Enable out-of-order ingestion (Prometheus 2.39+):

```yaml
storage:
  tsdb:
    out_of_order_time_window: 30m
```

Increase tolerance for old samples:

```yaml
storage:
  tsdb:
    min_block_duration: 2h
    max_block_duration: 36h
```

## Examples

```bash
# Check for out-of-order errors in logs
journalctl -u prometheus | grep "out of order"

# Verify time on servers
date -u; ssh target-host date -u

# Monitor ingestion errors
curl -s http://localhost:9090/api/v1/status/tsdb | jq '.data.headStats'
```
