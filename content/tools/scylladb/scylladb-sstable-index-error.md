---
title: "[Solution] ScyllaDB SSTable Index Corruption Error — How to Fix"
description: "Fix ScyllaDB SSTable index corruption errors when secondary indexes or SASI indexes contain invalid data"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB SSTable Index Corruption Error

SSTable index corruption errors occur when ScyllaDB detects invalid or corrupted data in secondary indexes, causing incorrect query results or read failures.

## Why It Happens

- Power failure during index write operation
- Disk I/O error corrupted the index file
- Bug in index compaction logic
- Index was built on a table with schema changes
- Memory corruption during index creation

## Common Error Messages

```
SSTable index corruption detected for table mykeyspace.users
```

```
error: secondary index file is corrupted, rebuild required
```

```
IndexReader: checksum mismatch in index file
```

## How to Fix It

### 1. Drop and Recreate the Index

```cql
DROP INDEX IF EXISTS mykeyspace.idx_user_email;
CREATE INDEX idx_user_email ON mykeyspace.users (email);
```

### 2. Run Scrub to Repair

```bash
nodetool scrub mykeyspace users
```

### 3. Use sstableutil to Check

```bash
sstableutil check /var/lib/scylla/data/mykeyspace/users-1234/
```

### 4. Rebuild SSTable Index

```bash
nodetool rebuild_index mykeyspace users idx_user_email
```

## Examples

```
$ nodetool scrub mykeyspace users
Scrub of mykeyspace.users completed.
  0 out of 125 SSTables had issues.
  Rebuilt 1 corrupted secondary index.
```

## Prevent It

- Use a UPS to prevent power loss during writes
- Monitor SSTable integrity with regular scrub operations
- Run sstableutil check periodically

## Related Pages

- [ScyllaDB SSTable Corrupt](/tools/scylladb/scylladb-sstable-corrupt)
- [ScyllaDB SSTable Error](/tools/scylladb/scylladb-sstable-error)
- [ScyllaDB Index Error](/tools/scylladb/scylladb-index-error)
