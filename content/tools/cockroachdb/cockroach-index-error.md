---
title: "[Solution] CockroachDB Index Error — How to Fix"
description: "Fix CockroachDB index creation and usage errors by resolving invalid index definitions, fixing duplicate indexes, handling index corruption, and optimizing index strategy."
tools: ["cockroachdb"]
error-types: ["index-error"]
severities: ["error"]
weight: 5
comments: true
---

A CockroachDB index error occurs when index creation fails, an existing index becomes corrupted, or the query planner cannot use an index as expected. Indexes are critical for query performance and incorrect index management can cause both errors and slowdowns.

## Why It Happens

Index errors in CockroachDB can occur during creation, usage, or maintenance. The asynchronous index creation process can fail for various reasons, and existing indexes can become stale or corrupted.

- The index definition references columns that do not exist in the table
- A duplicate index already exists with the same columns
- The index creation job fails due to resource constraints or node failure
- Stale statistics cause the query planner to not use an available index
- Index corruption occurs due to hardware failure or software bugs
- Partial indexes with invalid predicates fail to create
- The table is locked by another schema change when index creation starts
- The index creation job exceeds the configured timeout

## Common Error Messages

```text
ERROR: relation "idx_users_email" already exists
```

An index with this name already exists on the table. Use a different name or drop the existing index.

```text
ERROR: column "nonexistent_col" does not exist
```

The index references a column that is not in the table definition.

```text
ERROR: relation "users" does not exist
```

The table that the index is being created on does not exist.

```text
ERROR: duplicate index: index "idx_users_email" already exists with columns (email)
```

An identical index already exists. CockroachDB detects duplicate indexes and prevents creation.

## How to Fix It

### 1. Create Indexes Correctly

```sql
-- Basic index creation
CREATE INDEX idx_users_email ON users (email);

-- Unique index
CREATE UNIQUE INDEX idx_users_email ON users (email);

-- Composite index (multiple columns)
CREATE INDEX idx_orders_customer_date ON orders (customer_id, created_at DESC);

-- Partial index (with WHERE clause)
CREATE INDEX idx_orders_pending ON orders (customer_id) 
    WHERE status = 'pending';

-- Inverted index for JSON columns
CREATE INDEX idx_events_data ON events USING INVERTED (data);

-- Hash-sharded index for range queries on UUIDs
CREATE INDEX idx_users_id_sharded ON users (id) USING HASH WITH (bucket_count = 8);
```

### 2. Fix Duplicate Indexes

```sql
-- Find duplicate indexes
SELECT 
    table_name,
    index_name,
    column_names,
    is_unique
FROM [SHOW INDEXES FROM users]
WHERE table_name = 'users';

-- Drop a duplicate index
DROP INDEX IF EXISTS users@idx_users_email_old;

-- Drop an index by name (table@index syntax)
DROP INDEX IF EXISTS users@idx_users_email;
```

### 3. Monitor Index Creation Jobs

```sql
-- Check index creation progress
SHOW JOBS;

-- Find specific index creation jobs
SELECT job_id, status, fraction_completed, statement
FROM [SHOW JOBS]
WHERE job_type = 'CREATE INDEX'
ORDER BY created DESC;

-- Cancel a stuck index creation
CANCEL JOB <job_id>;

-- Resume a failed index creation
RESUME JOB <job_id>;
```

### 4. Fix Index Not Being Used by Query Planner

```sql
-- Check the query plan to see if the index is used
EXPLAIN (VERBOSE) SELECT * FROM users WHERE email = 'test@example.com';

-- If the index is not used, check statistics
SHOW STATISTICS FOR TABLE users;

-- Refresh statistics
ANALYZE users;

-- Force index usage with a hint (if needed)
SELECT * FROM users@idx_users_email WHERE email = 'test@example.com';
```

### 5. Handle Index Corruption

```sql
-- Check for index corruption
SELECT * FROM crdb_internal.invalid_objects;

-- If corruption is found, rebuild the index
DROP INDEX IF EXISTS users@idx_users_email;
CREATE INDEX idx_users_email ON users (email);

-- Or use the REBUILD option if available
ALTER INDEX users@idx_users_email REBUILD;
```

### 6. Drop Unused Indexes

```sql
-- Find indexes that are not being used
SELECT
    table_name,
    index_name,
    index_type,
    column_names
FROM [SHOW INDEXES FROM mydb]
WHERE table_name NOT LIKE 'crdb_internal_%'
ORDER BY table_name, index_name;

-- Check index usage statistics
SELECT * FROM crdb_internal.index_usage_statistics
ORDER BY rows_read DESC;

-- Drop an unused index
DROP INDEX IF EXISTS users@idx_unused_index;
```

## Common Scenarios

**Index creation fails on a large table.** The index creation job may timeout. Increase `sql.schema.default_timeout` and ensure the node has enough disk space for the temporary index data.

**Query is slow even with an index.** The query planner may be choosing a full table scan because statistics are stale. Run `ANALYZE` on the table to refresh statistics.

**Too many indexes slow down writes.** Each index adds overhead to write operations. Audit indexes with `SHOW INDEXES` and drop any that are not being used by production queries.

## Prevent It

- Create indexes through migration scripts rather than ad-hoc DDL to ensure they are version-controlled and reproducible
- Monitor index usage statistics and drop indexes that are never used to reduce write overhead
- Always run `EXPLAIN ANALYZE` after creating an index to verify the query planner is actually using it
