---
title: "[Solution] Prometheus Head Compaction Error"
description: "How to fix Prometheus head compaction failures"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Head block too large for compaction
- Disk space insufficient for new block
- Memory pressure during compaction
- I/O error writing compacted block

## How to Fix

Check head compaction status:

```bash
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_compactions_failed_total'
```

Ensure sufficient disk space:

```bash
df -h prometheus-data/
```

Tune compaction interval:

```yaml
storage:
  tsdb:
    min_block_duration: 2h
    max_block_duration: 36h
```

## Examples

```bash
# Monitor compaction
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_compactions_total'

# Check disk usage
du -sh prometheus-data/

# Monitor compaction duration
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_compactions_duration_seconds'
```
