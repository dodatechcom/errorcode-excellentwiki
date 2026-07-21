---
title: "[Solution] ScyllaDB Table Compact Error — How to Fix"
description: "Fix ScyllaDB table compaction errors when nodetool compact fails on specific tables"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Table Compact Error

Table compaction errors occur when nodetool compact fails to compact a specific table due to SSTable issues, resource constraints, or configuration problems.

## Why It Happens

- SSTables are locked by ongoing read operations
- Insufficient disk space for compaction output
- Table has too many SSTables for efficient compaction
- Compaction strategy encounters an unexpected error
- Node is in a bad state and cannot perform compaction

## Common Error Messages

```
error: compaction failed for table mykeyspace.users
```

```
Compaction interrupted: SSTable is locked by read operation
```

```
error: unable to compact, insufficient disk space
```

## How to Fix It

### 1. Check Table SSTable Count

```bash
nodetool tablestats mykeyspace users | grep "SSTable count"
```

### 2. Free Disk Space

```bash
df -h /var/lib/scylla/data
# Remove old snapshots if needed
nodetool clearsnapshot --tag old_backup
```

### 3. Force Compaction

```bash
nodetool compact mykeyspace users --force
```

### 4. Use TWCS for Time-Series Tables

```cql
ALTER TABLE mykeyspace.events WITH compaction = {
  'class': 'TimeWindowCompactionStrategy',
  'compaction_window_size': '1',
  'compaction_window_unit': 'DAYS'
};
```

## Examples

```
$ nodetool compact mykeyspace users
Starting compaction for mykeyspace.users
Compaction completed successfully.
  Before: 25 SSTables (5GB)
  After: 3 SSTables (4.8GB)
```

## Prevent It

- Monitor SSTable count per table
- Schedule compaction during low-traffic periods
- Ensure sufficient disk space before compaction

## Related Pages

- [ScyllaDB Compaction Error](/tools/scylladb/scylladb-compaction-error)
- [ScyllaDB Compaction Failed](/tools/scylladb/scylladb-compaction-failed)
- [ScyllaDB Disk Error](/tools/scylladb/scylladb-disk-error)
