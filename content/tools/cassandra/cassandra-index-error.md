---
title: "[Solution] Cassandra Index Error - Fix Secondary Index Build Failed"
description: "Fix Cassandra secondary index build failures. Resolve index creation, query performance, and index-related schema errors."
tools: ["cassandra"]
error-types: ["index-error"]
severities: ["error"]
weight: 5
---

This error means a Cassandra secondary index could not be created or is causing query failures. Secondary indexes have significant performance implications in Cassandra.

## What This Error Means

When a secondary index operation fails, you see:

```
InvalidRequestException: No index defined on table
# or
UnavailableException: Not enough replicas for index query
# or
WriteTimeoutException: Timed out creating index
```

Secondary indexes in Cassandra index a single column across all partitions. They are fundamentally different from relational database indexes.

## Why It Happens

- The column being indexed has high cardinality (many unique values)
- The index is being created on a large table without sufficient resources
- The table is under heavy write load during index creation
- The indexed column has many null values
- The index query does not include the partition key
- The index was dropped but queries still reference it

## How to Fix It

### Create the index properly

```cql
CREATE INDEX idx_users_email ON users (email);
```

### Use a WHERE clause that includes the partition key

```cql
-- Good: Includes partition key
SELECT * FROM users WHERE user_id = 1 AND email = 'alice@example.com';

-- Bad: Full table scan using only index
SELECT * FROM users WHERE email = 'alice@example.com';
```

### Consider materialized views instead

```cql
CREATE MATERIALIZED VIEW users_by_email AS
  SELECT * FROM users
  WHERE email IS NOT NULL AND user_id IS NOT NULL
  PRIMARY KEY (email, user_id);
```

Materialized views provide better query performance for read patterns.

### Drop unused indexes

```cql
DROP INDEX idx_users_email;
```

Indexes slow down writes. Remove indexes that are not used.

### Use ALLOW FILTERING carefully

```cql
SELECT * FROM users WHERE email = 'alice@example.com' ALLOW FILTERING;
```

ALLOW FILTERING forces a full table scan, which is inefficient.

### Monitor index build progress

```bash
nodetool tablestats keyspace_name.users
```

Check the index write latency and pending tasks.

### Create indexes on tables with sufficient resources

```bash
nodetool status
nodetool tpstats
```

Ensure the cluster is healthy before creating indexes.

### Use SASI indexes for full-text search

```cql
CREATE CUSTOM INDEX idx_users_name ON users (name)
  USING 'org.apache.cassandra.index.sasi.SASIIndex'
  WITH OPTIONS = {
    'mode': 'CONTAINS',
    'analyzer_class': 'org.apache.cassandra.index.sasi.analyzer.StandardAnalyzer'
  };
```

SASI indexes support LIKE queries and full-text search.

## Common Mistakes

- Creating secondary indexes on high-cardinality columns without understanding performance impact
- Assuming Cassandra indexes work like relational database indexes
- Not dropping indexes that slow down writes
- Using ALLOW FILTERING in production queries
- Creating indexes on large tables without checking cluster health

## Related Pages

- [Cassandra Schema Error]({{< relref "/tools/cassandra/cassandra-schema-error" >}}) -- schema issues
- [Cassandra Write Timeout]({{< relref "/tools/cassandra/cassandra-write-timeout" >}}) -- write timeouts
- [Cassandra Unavailable]({{< relref "/tools/cassandra/cassandra-unavailable" >}}) -- availability issues
