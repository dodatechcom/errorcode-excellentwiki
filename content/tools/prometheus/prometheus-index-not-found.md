---
title: "[Solution] Prometheus Index Not Found Error"
description: "How to fix Prometheus TSDB index not found errors"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- TSDB index files corrupted
- Index not built after fresh start
- Disk error during index creation
- Incomplete block after compaction

## How to Fix

Check index files:

```bash
ls -la prometheus-data/index/
```

Rebuild index by restarting:

```bash
sudo systemctl stop prometheus
sudo systemctl start prometheus
```

If persistent, clear data and re-scrape:

```bash
sudo systemctl stop prometheus
rm -rf prometheus-data/
sudo systemctl start prometheus
```

## Examples

```bash
# Check index status
curl -s 'http://localhost:9090/api/v1/status/tsdb' | jq '.data.indexStats'

# Monitor index operations
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_reloads_failures_total'
```
