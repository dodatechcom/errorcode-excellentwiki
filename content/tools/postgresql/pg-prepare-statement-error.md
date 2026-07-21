---
title: "[Solution] PostgreSQL Prepared Statement Error"
description: "Fix PostgreSQL prepared statement errors. Resolve issues with unnamed or out-of-sync prepared statements."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
---

# PostgreSQL Prepared Statement Error

ERROR: prepared statement does not exist / cached plan must not change result type

This error occurs when a prepared statement is referenced after it has been deallocated, or when the underlying table schema changes after the statement was prepared.

## Common Causes

- Connection pooler (like PgBouncer) discarding prepared statement state
- Schema migration altered a table used by a prepared statement
- DEALLOCATE was called or the session was reset
- Prepared statement name collision across pooled connections

## How to Fix

1. Redefine the prepared statement after schema changes:

```sql
DEALLOCATE IF EXISTS get_user_by_id;
PREPARE get_user_by_id AS
SELECT id, name, email, created_at FROM users WHERE id = $1;
EXECUTE get_user_by_id(42);
```

2. Disable prepared statements in PgBouncer:

```ini
# pgbouncer.ini
pool_mode = session
max_user_connections = 100
```

3. Use unnamed prepared statements for pooled connections:

```sql
-- This is safer in pooled environments
PREPARE AS SELECT * FROM users WHERE id = $1;
```

## Examples

```sql
-- Check active prepared statements
SELECT name, statement, prepare_time
FROM pg_prepared_statements;

-- Safely prepare with existence check
DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_prepared_statements WHERE name = 'my_query') THEN
    PREPARE my_query AS SELECT count(*) FROM orders WHERE created_at > $1;
  END IF;
END $$;
```
