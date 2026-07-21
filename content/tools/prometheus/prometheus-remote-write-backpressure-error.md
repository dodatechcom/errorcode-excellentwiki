---
title: "[Solution] Prometheus Remote Write Backpressure Error"
description: "Fix Prometheus remote write backpressure errors. Resolve send queue full conditions in remote write."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

# Prometheus Remote Write Backpressure Error

Prometheus remote write backpressure errors occur when the remote write queue fills up because the receiver cannot keep up with the rate of incoming samples.

## Common Causes

- Remote write receiver is overloaded or slow
- Network bandwidth between Prometheus and receiver is saturated
- Queue capacity too small for the write throughput
- Remote write endpoint returning HTTP 5xx errors

## How to Fix It

### Solution 1: Increase the remote write queue capacity

Adjust queue configuration:

```yaml
remote_write:
  - url: "http://remote-write-receiver:9090/api/v1/write"
    queue_config:
      capacity: 10000
      max_samples_per_send: 5000
      batch_send_deadline: 30s
      min_shards: 4
      max_shards: 32
```

### Solution 2: Use external labels to reduce write volume

Filter metrics before sending:

```yaml
remote_write:
  - url: "http://remote-write-receiver:9090/api/v1/write"
    write_relabel_configs:
      - source_labels: [__name__]
        regex: "go_.*"
        action: drop
```

### Solution 3: Check remote write status

Monitor the remote write queue:

```bash
curl -s http://localhost:9090/api/v1/status/runtimeinfo | \
  python3 -c "import sys,json; d=json.load(sys.stdin)['data']; \
  print(f\"Samples sent: {d.get('samples_scraped', 'N/A')}\")"
```

## Prevent It

- Monitor remote_write_samples_total for dropped samples
- Scale the remote write receiver horizontally
- Tune queue_config based on observed throughput
