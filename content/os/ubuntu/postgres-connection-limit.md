---
title: "PostgreSQL Connection Limit Reached"
description: "PostgreSQL refuses new connections because max_connections is reached"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PostgreSQL Connection Limit Reached

PostgreSQL refuses new connections because max_connections is reached

## Common Causes

- Too many concurrent connections from applications
- Idle connections not being released (connection leak)
- max_connections set too low for workload
- PgBouncer or connection pooler not configured

## How to Fix

1. Check connections: `SELECT count(*) FROM pg_stat_activity;`
2. Kill idle connections: `SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE state='idle';`
3. Increase max_connections: edit postgresql.conf
4. Configure PgBouncer as connection pooler

## Examples

```sql
-- Check current connections
SELECT count(*), state FROM pg_stat_activity GROUP BY state;

-- Find idle connections
SELECT pid, usename, state FROM pg_stat_activity WHERE state='idle';

-- Terminate idle connections older than 1 hour
SELECT pg_terminate_backend(pid) FROM pg_stat_activity WHERE state='idle' AND query_start < now() - interval '1 hour';
```
