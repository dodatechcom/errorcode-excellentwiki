---
title: "[Solution] YugabyteDB Query Error — How to Fix"
description: "Fix YugabyteDB query errors by correcting SQL syntax, resolving distributed query issues, and fixing YSQL/YCQL compatibility problems"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Query Error

YugabyteDB query errors occur when SQL queries fail due to syntax issues, distributed execution problems, or unsupported features. YugabyteDB supports both YSQL (PostgreSQL-compatible) and YCQL (Cassandra-compatible).

## Why It Happens

- Query uses unsupported PostgreSQL extensions
- Distributed query execution times out
- Query plan is inefficient for distributed tables
- Table is not colocated and causes cross-node queries
- SQL syntax is incompatible with YSQL
- Query references non-existent system tables

## Common Error Messages

```
ERROR: relation "table_name" does not exist
```

```
ERROR: function not supported in distributed mode
```

```
ERROR: distributed query failed
```

```
ERROR: unsupported SQL statement
```

## How to Fix It

### 1. Use YSQL Correctly

```sql
-- YugabyteDB YSQL is PostgreSQL-compatible
-- Most standard SQL works

-- Create table with primary key
CREATE TABLE users (
  user_id UUID DEFAULT gen_random_uuid(),
  name TEXT NOT NULL,
  email TEXT UNIQUE,
  created_at TIMESTAMPTZ DEFAULT NOW(),
  PRIMARY KEY (user_id)
);

-- Insert data
INSERT INTO users (name, email) VALUES ('Alice', 'alice@example.com');

-- Query with proper indexing
SELECT * FROM users WHERE email = 'alice@example.com';
```

### 2. Fix Distributed Query Issues

```sql
-- Use colocated tables for small reference tables
CREATE TABLE reference_data (
  id SERIAL PRIMARY KEY,
  name TEXT,
  value TEXT
) TABLEGROUP colocated;

-- Check query plan
EXPLAIN ANALYZE
SELECT * FROM users WHERE name = 'Alice';

-- Use distributed aggregation
SELECT department, COUNT(*)
FROM employees
GROUP BY department;
```

### 3. Handle Unsupported Features

```sql
-- Some PostgreSQL extensions not supported in YugabyteDB
-- Check available extensions
SELECT * FROM pg_available_extensions;

-- Use YCQL for Cassandra-compatible workloads
-- CREATE TABLE sensor_data (
--   sensor_id UUID,
--   event_time TIMESTAMP,
--   data MAP<TEXT, TEXT>,
--   PRIMARY KEY (sensor_id, event_time)
-- );
```

### 4. Optimize Query Performance

```sql
-- Add appropriate indexes
CREATE INDEX idx_users_email ON users (email);

-- Use hash-sharded indexes for range queries
CREATE INDEX idx_users_name_hash ON users USING lsm (name HASH);

-- Analyze query plan
EXPLAIN (ANALYZE, BUFFERS)
SELECT * FROM users WHERE created_at > '2024-01-01';
```

## Common Scenarios

- **Query times out on large table**: Add proper indexes and use colocated tables where possible.
- **Extension not supported**: Check YugabyteDB documentation for supported extensions.
- **Cross-node query is slow**: Use tablegroups for colocated tables.

## Prevent It

- Design schema with distribution in mind from the start
- Use `EXPLAIN ANALYZE` to verify query plans
- Choose appropriate tablegroup for related tables

## Related Pages

- [YugabyteDB TServer Error](/tools/yugabyte/yugabyte-tserver-error)
- [YugabyteDB DDL Error](/tools/yugabyte/yugabyte-ddl-error)
- [YugabyteDB DML Error](/tools/yugabyte/yugabyte-dml-error)
