---
title: "[Solution] ScyllaDB SSTable Error — How to Fix"
description: "Fix ScyllaDB SSTable errors by recovering from corrupted SSTables, resolving format incompatibilities, and fixing descriptor file issues"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB SSTable Error

ScyllaDB SSTable errors occur when SSTable files become corrupted, have incompatible formats, or have missing descriptor files. SSTables are the on-disk storage format for ScyllaDB.

## Why It Happens

- SSTable file is corrupted due to disk I/O error
- SSTable format version mismatch between nodes
- Descriptor file (Data, Index, Filter) is missing or damaged
- Disk failure causes partial SSTable write
- Snapshot operation interrupted mid-write
- Compaction left orphaned SSTable files

## Common Error Messages

```
SSTableCorruptError: Corrupted SSTable: /var/lib/scylla/data/mykeyspace/mytable-uuid/
```

```
InvalidSSTable: Invalid SSTable format
```

```
SSTableNotFoundError: Missing SSTable component
```

```
IOException: Error reading SSTable
```

## How to Fix It

### 1. Identify Corrupted SSTables

```bash
# Verify all SSTables in a table
nodetool verify mykeyspace.mytable

# Check for corrupted SSTables in logs
grep -i "corrupt\|invalid sstable" /var/log/scylla/scylla.log

# List all SSTables for a table
ls -la /var/lib/scylla/data/mykeyspace/mytable-uuid/
```

### 2. Recover from Corruption

```bash
# Scrub corrupted SSTables
nodetool scrub mykeyspace mytable

# If scrub fails, try to repair from replicas
nodetool repair mykeyspace mytable

# If SSTable is completely corrupted, rebuild
nodetool rebuild mykeyspace
```

### 3. Fix SSTable Format Issues

```bash
# Check SSTable version
sstablemetadata /var/lib/scylla/data/mykeyspace/mytable-uuid/*-Data.db

# Upgrade SSTables after ScyllaDB version upgrade
nodetool upgradesstables mykeyspace mytable

# Check for incompatible SSTables
nodetool tablestats mykeyspace.mytable | grep -i sstable
```

### 4. Clean Up Orphaned SSTables

```bash
# Check for pending deletion
ls /var/lib/scylla/data/mykeyspace/mytable-uuid/ | grep -i "tmp\|orphan"

# Remove temporary files
find /var/lib/scylla/data/mykeyspace/ -name "*.tmp" -delete

# Force cleanup
nodetool cleanup mykeyspace

# Compact to merge and remove orphans
nodetool compact mykeyspace mytable
```

## Common Scenarios

- **SSTable corruption after power loss**: Use `nodetool scrub` or rebuild from replicas.
- **Format mismatch after upgrade**: Run `nodetool upgradesstables` to update SSTable format.
- **Missing SSTable after disk failure**: Restore from backup or rebuild the table.

## Prevent It

- Use RAID to protect against disk failures
- Monitor disk I/O errors in system logs
- Take regular snapshots and test restore procedures

## Related Pages

- [ScyllaDB Compaction Error](/tools/scylladb/scylladb-compaction-error)
- [ScyllaDB Disk Error](/tools/scylladb/scylladb-disk-error)
- [ScyllaDB Backup Error](/tools/scylladb/scylladb-backup-error)
