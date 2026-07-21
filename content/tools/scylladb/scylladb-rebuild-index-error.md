---
title: "[Solution] ScyllaDB Rebuild Index Error — How to Fix"
description: "Fix ScyllaDB rebuild index errors when nodetool rebuild_index fails to reconstruct secondary indexes"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Rebuild Index Error

Rebuild index errors occur when nodetool rebuild_index fails to reconstruct secondary indexes from the base table SSTables.

## Why It Happens

- Base table SSTables are corrupted
- Insufficient disk space for new index files
- Index name does not match an existing index
- Memory is insufficient for the index rebuild process
- Ongoing compaction conflicts with index rebuild

## Common Error Messages

```
error: rebuild_index failed for index users_email_idx
```

```
nodetool: unable to rebuild index, SSTable corruption detected
```

```
error: not enough disk space for index rebuild
```

## How to Fix It

### 1. Verify Index Exists

```cql
SELECT index_name, target_options FROM system_schema.indexes 
WHERE keyspace_name = 'mykeyspace' AND table_name = 'users';
```

### 2. Free Disk Space

```bash
df -h /var/lib/scylla/data
```

### 3. Drop and Recreate Index

```cql
DROP INDEX IF EXISTS mykeyspace.users_email_idx;
CREATE INDEX users_email_idx ON mykeyspace.users (email);
```

### 4. Run Rebuild with Memory Limit

```bash
# Stop compaction during rebuild
nodetool compaction -p -d mykeyspace
nodetool rebuild_index mykeyspace users users_email_idx
```

## Examples

```
$ nodetool rebuild_index mykeyspace users users_email_idx
Rebuilding index users_email_idx for mykeyspace.users
Progress: 100%
Index rebuilt successfully.
```

## Prevent It

- Monitor disk space before index rebuilds
- Stop compaction during index rebuild for better performance
- Use DROP INDEX + CREATE INDEX as alternative

## Related Pages

- [ScyllaDB Index Error](/tools/scylladb/scylladb-index-error)
- [ScyllaDB SSTable Index Error](/tools/scylladb/scylladb-sstable-index-error)
- [ScyllaDB Secondary Index Error](/tools/scylladb/scylladb-secondary-index-error)
