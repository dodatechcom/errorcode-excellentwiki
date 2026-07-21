---
title: "[Solution] Prometheus Chunk Not Found Error"
description: "How to fix Prometheus chunk not found errors during query execution"
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Chunk deleted during compaction while being queried
- WAL corruption causing missing chunks
- Disk error removing chunk files
- Race condition between compaction and query

## How to Fix

Check chunk status:

```bash
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_chunks'
```

Restart Prometheus to rebuild chunk index:

```bash
sudo systemctl restart prometheus
```

Check disk for missing files:

```bash
ls -la prometheus-data/chunks_head/
```

## Examples

```bash
# Monitor chunk count
curl -s 'http://localhost:9090/api/v1/query?query=prometheus_tsdb_head_chunks'

# Check for chunk errors in logs
journalctl -u prometheus | grep -i "chunk not found"

# Analyze TSDB
promtool tsdb analyze prometheus-data/
```
