---
title: "[Solution] InfluxDB Meta Node Error — How to Fix"
description: "Fix InfluxDB meta service errors including metadata inconsistencies, meta node failures, and cluster metadata synchronization issues"
tools: ["influxdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# InfluxDB Meta Node Error

Meta node errors in InfluxDB Enterprise occur when the metadata service fails, metadata becomes inconsistent, or cluster metadata cannot synchronize.

## Why It Happens

- The meta service is not running or unreachable
- Meta node disk is full and cannot write metadata
- Meta nodes cannot communicate with each other
- The metadata directory has wrong permissions
- The cluster has an odd number of meta nodes but some are down

## Common Error Messages

```
meta service error: connection refused
```

```
error: meta node failed to join cluster
```

```
meta sync error: metadata inconsistent
```

```
error: no space left on device in meta directory
```

## How to Fix It

### 1. Check Meta Service Status

```bash
sudo systemctl status influxdb-meta
curl http://meta-host:8091/status
```

### 2. Fix Meta Node Join

```bash
# Join a new meta node
influxd-meta -join meta-host1:8091,meta-host2:8091

# Check meta nodes
influxd-meta -show
```

### 3. Fix Meta Disk Space

```bash
# Check meta directory
df -h /var/lib/influxdb/meta

# Clean old meta snapshots
ls -la /var/lib/influxdb/meta/
```

### 4. Fix Metadata Inconsistency

```bash
# Stop all meta nodes
sudo systemctl stop influxdb-meta

# Remove meta directory on the problematic node
sudo rm -rf /var/lib/influxdb/meta/*

# Start the node - it will sync from other meta nodes
sudo systemctl start influxdb-meta
```

## Common Scenarios

- **Meta service down**: Restart the meta service and check logs.
- **Meta disk full**: Free space or move meta directory to a larger disk.
- **Metadata inconsistent**: Remove and resync from healthy meta nodes.

## Prevent It

- Run an odd number of meta nodes (3 or 5) for fault tolerance
- Monitor meta service health and disk usage
- Back up meta directory regularly

## Related Pages

- [InfluxDB Connection Error](/tools/influxdb/influxdb-connection-error)
- [InfluxDB Shard Error](/tools/influxdb/influxdb-shard-error)
- [InfluxDB Backup Error](/tools/influxdb/influxdb-backup-error)
