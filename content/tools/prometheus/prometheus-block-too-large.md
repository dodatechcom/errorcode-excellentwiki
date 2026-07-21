---
title: "[Solution] Prometheus Block Too Large Error"
description: "How to fix Prometheus block size exceeding limits"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Too many samples in a single block
- High cardinality metrics creating large blocks
- Block duration too long
- Memory limit for block processing exceeded

## How to Fix

Adjust block duration:

```yaml
storage:
  tsdb:
    min_block_duration: 2h
    max_block_duration: 24h
```

Reduce metric cardinality:

```yaml
scrape_configs:
  - job_name: 'app'
    metric_relabel_configs:
      - source_labels: [__name__]
        regex: 'high_cardinality_.*'
        action: drop
```

Monitor block sizes:

```bash
du -sh prometheus-data/chunks_head/*/
```

## Examples

```bash
# Check block count and sizes
curl -s 'http://localhost:9090/api/v1/status/tsdb' | jq '.data.blockStats'

# Monitor block creation
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_chunks'
```
