---
title: "[Solution] ScyllaDB Import SSTable Error — How to Fix"
description: "Fix ScyllaDB SSTable import errors when bulk loading data from external SSTable files fails"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Import SSTable Error

SSTable import errors occur when ScyllaDB cannot bulk-load data from external SSTable files using sstableloader or similar tools.

## Why It Happens

- SSTable format version does not match the ScyllaDB version
- SSTable files are corrupted or incomplete
- Target keyspace or table does not exist
- Schema of the SSTable does not match the target table
- Network connection to the target node fails during streaming

## Common Error Messages

```
sstableloader: error connecting to target node
```

```
error: SSTable format version not supported
```

```
StreamException: failed to stream SSTable data
```

```
IncompatibleSchema: SSTable schema does not match target table
```

## How to Fix It

### 1. Verify SSTable Compatibility

```bash
sstableutil identify /path/to/sstables/
```

### 2. Create Target Table Schema

```cql
-- Match the schema of the SSTable being imported
CREATE TABLE IF NOT EXISTS mykeyspace.users (
    id UUID PRIMARY KEY,
    name TEXT,
    email TEXT,
    created_at TIMESTAMP
);
```

### 3. Use sstableloader Correctly

```bash
sstableloader \
  --host node1 \
  --throttle 256 \
  --parallel 4 \
  /path/to/sstables/mykeyspace/users-1234/
```

### 4. Fix Schema Mismatch

```bash
# Check SSTable schema
sstableutil identify /path/to/sstables/
# Ensure target table has matching column types
```

## Examples

```
$ sstableloader --host 10.0.0.1 /var/lib/scylla/data/mykeyspace/users-1234/
Streaming /var/lib/scylla/data/mykeyspace/users-1234/
Progress: [UCCEEDED] - 100%
```

## Prevent It

- Verify SSTable version compatibility before import
- Test import on a staging environment first
- Ensure target table schema matches SSTable schema

## Related Pages

- [ScyllaDB Import Error](/tools/scylladb/scylladb-import-error)
- [ScyllaDB SSTable Error](/tools/scylladb/scylladb-sstable-error)
- [ScyllaDB Streaming Error](/tools/scylladb/scylladb-streaming-error)
