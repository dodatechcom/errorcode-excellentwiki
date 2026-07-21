---
title: "[Solution] Prometheus TSDB Compaction Error"
description: "How to fix Prometheus TSDB compaction failures"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Insufficient disk space for compaction
- Too many blocks causing memory pressure
- I/O error during block merge
- Compaction running too frequently

## How to Fix

Check compaction status:

```bash
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_compactions_failed_total'
```

Ensure sufficient disk space (2x data size needed):

```bash
df -h prometheus-data/
du -sh prometheus-data/
```

Tune compaction settings:

```yaml
storage:
  tsdb:
    min_block_duration: 2h
    max_block_duration: 36h
    retention.time: 15d
```

## Examples

```bash
# Check compaction metrics
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_compactions_total'

# Monitor block count
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_blocks_loaded'

# Check disk I/O
iostat -x 1 5
```
