---
title: "[Solution] TiDB Temp Table Error — How to Fix"
description: "Fix TiDB temporary table errors by resolving creation failures, handling memory limits, and fixing session cleanup issues"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Temp Table Error

TiDB temp table errors occur when creating, querying, or dropping temporary tables that fail due to naming conflicts, memory limits, or session state issues.

## Why It Happens

- Temporary table name conflicts with a persistent table
- Memory quota for temporary tables is exceeded
- Session disconnects leaving orphaned temporary tables
- Temporary table references a non-existent table in CREATE TEMPORARY ... AS SELECT
- Temporary table DDL is used in an explicit transaction
- Multiple sessions create temp tables with the same name

## Common Error Messages

```
ERROR: Table already exists
```

```
ERROR: temporary table memory quota exceeded
```

```
ERROR: unknown table in expression
```

```
ERROR: can not create temporary table in transaction
```

## How to Fix It

### 1. Create Temporary Tables Correctly

```sql
-- Create local temporary table
CREATE TEMPORARY TABLE temp_orders (
  id INT PRIMARY KEY,
  total DECIMAL(10,2),
  created_at DATETIME
);

-- Create from existing table structure
CREATE TEMPORARY TABLE temp_users LIKE users;

-- Create from SELECT
CREATE TEMPORARY TABLE temp_stats AS
SELECT user_id, COUNT(*) AS order_count
FROM orders
GROUP BY user_id;
```

### 2. Fix Memory Quota Issues

```sql
-- Set memory limit for temporary tables
SET GLOBAL tidb_mem_oom_action = 'CANCEL';
SET tidb_mem_quota_query = 1073741824;  -- 1GB

-- Check temp table memory usage
SELECT * FROM information_schema.TEMP_TABLES
WHERE TABLE_SCHEMA = 'tempdb';
```

### 3. Handle Naming Conflicts

```sql
-- Drop existing temp table before creating
DROP TEMPORARY TABLE IF EXISTS temp_orders;

-- Use unique naming convention
CREATE TEMPORARY TABLE temp_orders_v2 (
  id INT PRIMARY KEY,
  total DECIMAL(10,2)
);
```

### 4. Fix Transaction Issues

```sql
-- Temp tables cannot be created inside explicit transactions
-- Wrong:
BEGIN;
CREATE TEMPORARY TABLE temp_data (id INT);
-- ERROR!

-- Correct: create temp table before transaction
CREATE TEMPORARY TABLE temp_data (id INT);
BEGIN;
INSERT INTO temp_data SELECT id FROM source_table;
COMMIT;
```

## Common Scenarios

- **Temp table name collision**: Use `DROP TEMPORARY TABLE IF EXISTS` before creating.
- **Session crashes leave temp tables**: Temp tables are automatically dropped when the session ends.
- **Application reuses temp table name**: Use unique names per session or use temporary table prefixes.

## Prevent It

- Always use `DROP TEMPORARY TABLE IF EXISTS` before creating
- Monitor temporary table memory usage
- Do not create temporary tables inside explicit transactions

## Related Pages

- [TiDB DDL Error](/tools/tidb/tidb-ddl-error)
- [TiDB OOM Error](/tools/tidb/tidb-oom-error)
- [TiDB Statement Error](/tools/tidb/tidb-statement-error)
