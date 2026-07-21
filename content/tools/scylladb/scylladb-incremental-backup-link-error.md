---
title: "[Solution] ScyllaDB Incremental Backup Error — How to Fix"
description: "Fix ScyllaDB incremental backup errors when hard links for backup snapshots fail to be created"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Incremental Backup Error

Incremental backup errors occur when ScyllaDB fails to create hard links for SSTable files as part of the incremental backup process, preventing point-in-time recovery.

## Why It Happens

- Filesystem does not support hard links
- Insufficient disk space for incremental backup markers
- SSTable is locked by ongoing compaction during backup
- Incremental backup directory has incorrect permissions
- Too many incremental backups consume inode resources

## Common Error Messages

```
error: incremental backup failed: unable to create hard link
```

```
IncrementalBackup: filesystem does not support hard links
```

```
nodetool: incremental snapshot failed for shard
```

## How to Fix It

### 1. Enable Incremental Backups

```yaml
# In scylla.yaml
incremental_backups: true
```

### 2. Verify Filesystem Supports Hard Links

```bash
touch /var/lib/scylla/data/test_file
ln /var/lib/scylla/data/test_file /var/lib/scylla/data/test_link
ls -la /var/lib/scylla/data/test*
rm /var/lib/scylla/data/test_file /var/lib/scylla/data/test_link
```

### 3. Free Inodes

```bash
df -i /var/lib/scylla/data
```

### 4. Clear Old Incremental Backups

```bash
nodetool clearincrementalbackups
```

## Examples

```
$ ls /var/lib/scylla/data/mykeyspace/users-1234/
SCYLLA-KEYSPACE-COMPACTED-TIMESTAMP.txt
mc-1-big-Data.db
mc-1-big-Data.db.link  # incremental backup hard link
```

## Prevent It

- Use a filesystem that supports hard links (ext4, XFS)
- Monitor inode usage regularly
- Clear old incremental backups before taking new ones

## Related Pages

- [ScyllaDB Incremental Backup Error](/tools/scylladb/scylladb-incremental-backup-error)
- [ScyllaDB Backup Error](/tools/scylladb/scylladb-backup-error)
- [ScyllaDB Backup Failed Error](/tools/scylladb/scylladb-backup-failed-error)
