---
title: "[Solution] Prometheus Retention Period Expired"
description: "How to fix Prometheus data retention expiration issues"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Retention period too short for required data range
- Default retention (15 days) insufficient
- Disk space triggering early deletion
- Compaction removing data before retention period

## How to Fix

Increase retention period:

```yaml
storage:
  tsdb:
    retention.time: 30d
    retention.size: 50GB
```

Command-line configuration:

```bash
prometheus --storage.tsdb.retention.time=90d
```

Check current retention:

```bash
curl -s http://localhost:9090/api/v1/status/runtimeinfo | jq '.data.storageRetention'
```

## Examples

```bash
# Check oldest data
curl -s 'http://localhost:9090/api/v1/query?query=min_over_time(up[30d])'

# Monitor disk usage
df -h prometheus-data/

# View retention config
curl -s http://localhost:9090/api/v1/status/config | grep retention
```
