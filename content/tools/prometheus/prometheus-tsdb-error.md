---
title: "[Solution] Prometheus TSDB Error"
description: "Fix Prometheus tsdb errors. Learn why this happens and how to resolve it quickly."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Prometheus TSDB Error

Prometheus TSDB errors occur when the time-series database encounters issues with data storage or retrieval.

## Why This Happens

- Head block full
- Compaction failed
- WAL corruption
- Index error

## Common Error Messages

- `tsdb_head_full`
- `tsdb_compaction_failed`
- `tsdb_wal_error`
- `tsdb_index_error`

## How to Fix It

### Solution 1: Check TSDB status

View TSDB status:

```bash
curl http://localhost:9090/api/v1/status/tsdb
```

### Solution 2: Monitor compaction

Watch compaction metrics:

```promql
prometheus_tsdb_compactions_total
```

### Solution 3: Handle WAL issues

If WAL is corrupted, you may need to replay or rebuild.


## Common Scenarios

- **Head block full:** Increase block duration or optimize write performance.
- **Compaction failing:** Check disk space and IO performance.

## Prevent It

- Monitor TSDB metrics
- Optimize write patterns
- Check disk health
