---
title: "[Solution] ScyllaDB SSTable Split Error — How to Fix"
description: "Fix ScyllaDB SSTable split errors when sstablesplit fails to separate compacted SSTables"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB SSTable Split Error

SSTable split errors occur when the sstablesplit tool fails to separate large compacted SSTables into smaller, manageable files.

## Why It Happens

- SSTable contains data for too many partitions
- Disk space is insufficient for the split output
- SSTable is corrupted and cannot be parsed
- sstablesplit encounters unexpected data format
- Tool is run on an SSTable that is still being written

## Common Error Messages

```
sstablesplit: error reading SSTable, file is corrupted
```

```
error: not enough disk space for SSTable split operation
```

```
sstablesplit: unsupported SSTable format version
```

## How to Fix It

### 1. Check SSTable Integrity

```bash
sstableutil check /var/lib/scylla/data/mykeyspace/users-1234/
```

### 2. Ensure Sufficient Disk Space

```bash
df -h /var/lib/scylla/data
# Need at least 2x the SSTable size for splitting
```

### 3. Run sstablesplit on Stopped Node

```bash
sudo systemctl stop scylla-server
sstablesplit --min-split-size 10 --split-points /var/lib/scylla/data/mykeyspace/users-1234/mc-1-big-Data.db
sudo systemctl start scylla-server
```

### 4. Use Compact Instead

```bash
nodetool compact mykeyspace users
```

## Examples

```
$ sstablesplit --min-split-size 10 /var/lib/scylla/data/mykeyspace/users-1234/mc-1-big-Data.db
Splitting /var/lib/scylla/data/mykeyspace/users-1234/mc-1-big-Data.db
  Wrote 3 new SSTables
```

## Prevent It

- Use leveled compaction to prevent oversized SSTables
- Monitor SSTable size distribution
- Run sstablesplit during maintenance windows

## Related Pages

- [ScyllaDB SSTable Error](/tools/scylladb/scylladb-sstable-error)
- [ScyllaDB SSTable Split Error](/tools/scylladb/scylladb-sstablesplit-error)
- [ScyllaDB Compaction Error](/tools/scylladb/scylladb-compaction-error)
