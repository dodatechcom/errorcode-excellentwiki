---
title: "[Solution] ScyllaDB Index Not Found Error — How to Fix"
description: "Fix ScyllaDB index not found errors when queries reference non-existent or dropped secondary indexes"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Index Not Found Error

Index not found errors occur when a CQL query references a secondary index that does not exist, was dropped, or has not finished building.

## Why It Happens

- Query uses the wrong index name
- Index was dropped but application code still references it
- Index is still in BUILD_IN_PROGRESS state
- Keyspace name is incorrect in the query
- Index was created on a dropped table

## Common Error Messages

```
Invalid: Secondary index users_email_idx not found
```

```
error: index does not exist on table users
```

```
InvalidRequest: No index found for query on column email
```

## How to Fix It

### 1. List Existing Indexes

```cql
DESCRIBE INDEX mykeyspace.users_email_idx;
SELECT * FROM system_schema.indexes WHERE keyspace_name = 'mykeyspace';
```

### 2. Recreate the Index

```cql
CREATE INDEX IF NOT EXISTS users_email_idx ON mykeyspace.users (email);
```

### 3. Use the Correct Index Name in Queries

```cql
-- Use the actual index name
SELECT * FROM users USING INDEX users_email_idx WHERE email = 'alice@example.com';
```

### 4. Build Index on Existing Table

```cql
-- Wait for build to complete
SELECT index_name, status FROM system_schema.indexes WHERE keyspace_name = 'mykeyspace';
```

## Examples

```
cqlsh> SELECT * FROM users USING INDEX users_email_idx WHERE email = 'test';
Invalid: Secondary index users_email_idx not found

cqlsh> CREATE INDEX users_email_idx ON users (email);
cqlsh> SELECT * FROM users USING INDEX users_email_idx WHERE email = 'test';
```

## Prevent It

- Verify index existence before querying
- Handle schema changes in application code
- Monitor index build status after creation

## Related Pages

- [ScyllaDB Index Error](/tools/scylladb/scylladb-index-error)
- [ScyllaDB Secondary Index Error](/tools/scylladb/scylladb-secondary-index-error)
- [ScyllaDB Schema Error](/tools/scylladb/scylladb-schema-error)
