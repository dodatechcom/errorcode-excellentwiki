---
title: "[Solution] Prometheus Relabel Hashmod Action Error"
description: "How to fix Prometheus hashmod relabel action for shard-based scraping"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Hashmod value out of range for shard count
- Mismatch between hashmod and total_shards
- Wrong source_labels for hashing
- Hashmod action used with non-static targets

## How to Fix

Configure hashmod for sharded scraping:

```yaml
scrape_configs:
  - job_name: 'sharded-app'
    relabel_configs:
      - source_labels: [__address__]
        modulus: 3
        target_label: __tmp_hash
        action: hashmod
      - source_labels: [__tmp_hash]
        regex: 0
        action: keep
```

Each Prometheus instance uses a different hashmod value:

```yaml
# Instance 0
- source_labels: [__address__]
  modulus: 3
  target_label: __tmp_hash
  action: hashmod
- source_labels: [__tmp_hash]
  regex: 0
  action: keep

# Instance 1
- regex: 1
  action: keep

# Instance 2
- regex: 2
  action: keep
```

## Examples

```bash
# Check shard distribution
curl -s 'http://localhost:9090/api/v1/query?query=count by (job)(up)'

# Verify targets per shard
curl -s http://localhost:9090/api/v1/targets | jq '.data.activeTargets | length'
```
