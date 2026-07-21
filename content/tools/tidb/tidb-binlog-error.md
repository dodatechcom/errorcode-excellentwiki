---
title: "[Solution] TiDB Binlog Error — How to Fix"
description: "Fix TiDB binlog errors by resolving Drainer failures, fixing Pump write issues, and restoring binlog synchronization across the cluster"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Binlog Error

TiDB binlog errors occur when the binlog system fails to record DML changes or when Drainer cannot consume binlog entries from Pump.

## Why It Happens

- Pump node is unreachable or crashed
- Drainer falls behind and cannot keep up with write throughput
- Binlog data is corrupted on disk
- Network partition between Pump and Drainer
- Binlog compaction removes data Drainer has not yet consumed
- Storage space is exhausted on Pump nodes

## Common Error Messages

```
ERROR: binlog not found in Pump
```

```
ERROR: Drainer exceeded the GC life time
```

```
ERROR: pump write binlog failed
```

```
ERROR: binlog type not supported
```

## How to Fix It

### 1. Check Pump Status

```bash
# Check Pump nodes via HTTP API
curl http://pump1:8250/status

# List all Pump nodes
curl http://pd:2379/pd/api/v1/config

# Check Drainer status
curl http://drainer:8249/status
```

### 2. Resolve Pump Write Failures

```bash
# Restart a specific Pump node
systemctl restart tikv-pump

# Check Pump logs for errors
tail -100 /data/pump/pump.log | grep -i error

# Verify Pump disk space
df -h /data/pump
```

### 3. Fix Drainer Lag

```sql
-- Check Drainer checkpoint
SELECT * FROM tidb_binlog.checkpoint;

-- Increase Drainer worker count in drainer.toml
-- [binlog]
-- worker-count = 16
```

```bash
# Restart Drainer with updated config
systemctl restart drainer

# Monitor Drainer sync status
curl http://drainer:8249/status | jq '.synced'
```

### 4. Recover from Binlog Corruption

```bash
# Stop Drainer first
systemctl stop drainer

# Delete corrupted Pump data and rebuild
rm -rf /data/pump/ckpt/*
rm -rf /data/pump/meta/*

# Restart Pump
systemctl start tikv-pump

# Reset Drainer checkpoint and restart
mysql -h tidb -u root -e "DELETE FROM tidb_binlog.checkpoint"
systemctl start drainer
```

## Common Scenarios

- **Drainer cannot keep up**: Increase `worker-count` and `txn-batch` in drainer.toml.
- **Pump disk full**: Increase disk size or reduce `duration` in Pump config to speed up compaction.
- **Binlog not found after GC**: Decrease `gc-life-time` or ensure Drainer processes entries faster.

## Prevent It

- Monitor Pump and Drainer status endpoints regularly
- Set alerts on Drainer lag exceeding threshold
- Ensure adequate disk space on Pump nodes

## Related Pages

- [TiDB Drainer Error](/tools/tidb/tidb-drainer-error)
- [TiDB Pump Error](/tools/tidb/tidb-pump-error)
- [TiDB CDC Error](/tools/tidb/tidb-cdc-error)
