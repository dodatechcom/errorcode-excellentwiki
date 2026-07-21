---
title: "[Solution] Prometheus Remote Write Queue Backpressure"
description: "How to fix Prometheus remote write queue buildup and backpressure"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Remote storage cannot keep up with ingestion rate
- Network bandwidth saturation
- Queue shards too low
- `max_samples_per_send` too small
- Remote storage under heavy load

## How to Fix

Tune queue configuration:

```yaml
remote_write:
  - url: 'http://remote-storage:9201/api/v1/write'
    queue_config:
      max_samples_per_send: 10000
      batch_send_deadline: 10s
      max_shards: 500
      min_shards: 10
      capacity: 10000
```

Monitor queue depth:

```bash
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_remote_storage_queue_highest_sent_timestamp_seconds'
```

Increase network bandwidth or add compression:

```yaml
    remote_write:
      - url: 'http://remote-storage:9201/api/v1/write'
        enable_http2: true
```

## Examples

```bash
# Check queue shards
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_remote_storage_shards'

# Monitor send rate
curl -s 'http://localhost:9090/api/v1/query?query=rate(prometheus_remote_storage_samples_sent_total[5m])'
```
