---
title: "[Solution] Cassandra Truncate Table Failed - Fix Truncate Errors"
description: "Fix Cassandra TRUNCATE failures by verifying MODIFY permissions on the table, checking schema agreement across all nodes, and ensuring all nodes are healthy"
tools: ["cassandra"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A Cassandra truncate error occurs when the `TRUNCATE` command fails to remove all rows from a table. The operation may fail with a timeout, a permission error, or a schema disagreement error depending on the underlying cause.

## What This Error Means

The `TRUNCATE` command in Cassandra is a schema-level operation that atomically drops and recreates the table's data. It is not a simple delete of rows. For `TRUNCATE` to succeed, all nodes in the cluster must agree on the schema, the user must have `MODIFY` permission on the table, and no streaming operations can be in progress for that table.

When `TRUNCATE` fails, the error may be `InvalidRequestException`, `UnauthorizedException`, or `TruncateError` depending on whether the issue is permissions, schema agreement, or internal state.

## Why It Happens

- Schema disagreement across nodes prevents the schema change from propagating
- The user lacks `MODIFY` or `TRUNCATE` permission on the target table
- A node is down or unreachable during the truncate operation
- Compaction is actively running on the table
- The table is involved in an ongoing streaming operation
- Truncate with a WHERE clause (not supported in Cassandra)
- Timeout is too short for large tables

## How to Fix It

### 1. Verify Permissions

```cql
-- Check your role permissions
LIST ALL PERMISSIONS OF app_user;

-- Grant modify permission
GRANT MODIFY ON KEYSPACE my_keyspace TO app_user;
```

### 2. Check Schema Agreement

```bash
nodetool describecluster
# All nodes should show the same schema version
```

### 3. Retry After Node Recovery

```bash
# If a node was down, wait for it to rejoin and sync schema
nodetool status
# Once all nodes show UN, retry TRUNCATE
```

### 4. Use TRUNCATE Properly

```cql
-- Correct syntax
TRUNCATE TABLE my_keyspace.my_table;

-- This is NOT valid in Cassandra
TRUNCATE TABLE my_keyspace.my_table WHERE id = ?;
```

### 5. Increase Timeout

```bash
# In cqlsh
TRUNCATE TABLE my_keyspace.my_table;
# If it times out, check node health first
```

### 6. Drop and Recreate as Last Resort

```cql
-- Only if TRUNCATE consistently fails
DROP TABLE IF EXISTS my_keyspace.my_table;
CREATE TABLE my_keyspace.my_table (
    id UUID PRIMARY KEY,
    name TEXT
);
```

## Common Mistakes

- Attempting `TRUNCATE` during a rolling restart when not all nodes are up
- Using `TRUNCATE` in application code without handling the permission requirement
- Assuming `TRUNCATE` is a fast operation on very large tables with many SSTables
- Not checking `nodetool describecluster` before running DDL operations

## Related Pages

- [Cassandra Schema Error](/tools/cassandra/cassandra-schema-error)
- [Cassandra WriteTimeoutException](/tools/cassandra/cassandra-write-timeout)
- [Cassandra Compaction Error](/tools/cassandra/cassandra-compaction-error)
