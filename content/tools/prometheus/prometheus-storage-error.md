---
title: "[Solution] Prometheus Storage Error"
description: "Fix Prometheus storage errors. Learn why this happens and how to resolve it quickly."
tools: ["prometheus"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Prometheus Storage Error

Prometheus storage errors occur when data cannot be written to or read from the storage backend.

## Why This Happens

- Disk full
- Corruption detected
- Retention policy active
- WAL replay failed

## Common Error Messages

- `storage_write_failed`
- `storage_corruption`
- `retention_active`
- `wal_replay_error`

## How to Fix It

### Solution 1: Check disk space

Monitor disk usage:

```bash
df -h /prometheus
```

### Solution 2: Configure retention

Set retention period:

```bash
prometheus --storage.tsdb.retention.time=30d
```

### Solution 3: Handle corruption

Rebuild storage if corruption is detected:

```bash
prometheus --storage.tsdb.path=/prometheus --storage.tsdb.retention.time=0
```


## Common Scenarios

- **Disk full:** Clean up old data or increase disk space.
- **WAL replay failed:** Check WAL files for corruption.

## Prevent It

- Monitor disk usage
- Set retention policies
- Backup data regularly
