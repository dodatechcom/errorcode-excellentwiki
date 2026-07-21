---
title: "[Solution] ScyllaDB Backup Failed Error — How to Fix"
description: "Fix ScyllaDB backup failures when nodetool backup or Scylla Manager cannot create consistent snapshots"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Backup Failed Error

Backup failures occur when ScyllaDB cannot create consistent snapshots of SSTables due to disk space, permission, or timeout issues.

## Why It Happens

- Insufficient disk space for snapshot files
- SSTable files are locked by ongoing compaction
- Snapshot directory permissions are incorrect
- Network storage mount is unavailable
- Too many snapshots consuming disk space

## Common Error Messages

```
error: Snapshot directory already exists
```

```
nodetool: Failed to create snapshot: no space left on device
```

```
Backup failed: unable to flush memtable before snapshot
```

## How to Fix It

### 1. Free Space Before Backup

```bash
nodetool clearsnapshot --tag backup_old
df -h /var/lib/scylla/data
```

### 2. Flush Memtable First

```bash
nodetool flush mykeyspace
nodetool snapshot --tag manual_backup mykeyspace
```

### 3. Check Snapshot Status

```bash
nodetool listsnapshots
```

### 4. Use Scylla Manager for Automated Backups

```bash
scylla-manager-client task create -t backup -- keyspace 'mykeyspace'
```

## Examples

```
$ nodetool snapshot --tag backup_2024 mykeyspace
Requested creating snapshot for snapshot tag [backup_2024] for keyspace [mykeyspace]
Snapshot created successfully.
```

## Prevent It

- Schedule backups during low-traffic periods
- Monitor snapshot disk usage
- Use Scylla Manager for consistent automated backups

## Related Pages

- [ScyllaDB Backup Error](/tools/scylladb/scylladb-backup-error)
- [ScyllaDB Incremental Backup Error](/tools/scylladb/scylladb-incremental-backup-error)
- [ScyllaDB Disk Error](/tools/scylladb/scylladb-disk-error)
