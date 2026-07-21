---
title: "[Solution] PostgreSQL GIN Index Corruption"
description: "Fix PostgreSQL GIN index corruption errors. Rebuild and recover damaged GIN indexes on JSONB or FTS columns."
tools: ["postgresql"]
error-types: ["tool-error"]
severities: ["error"]
---

# PostgreSQL GIN Index Corruption

ERROR: invalid memory alloc request size / index corruption detected

This error occurs when a GIN (Generalized Inverted Index) becomes corrupted, often after a crash or improper shutdown while the index was being updated.

## Common Causes

- Server crash or unclean shutdown during a GIN index write operation
- Insufficient disk space during index creation causing partial writes
- Bug in third-party extension contributing to GIN index maintenance

## How to Fix

1. Detect corruption using amcheck:

```sql
CREATE EXTENSION IF NOT EXISTS amcheck;
SELECT bt_index_check(c.oid)
FROM pg_index i
JOIN pg_class c ON i.indexrelid = c.oid
JOIN pg_am am ON c.relam = am.oid
WHERE am.amname = 'gin';
```

2. Rebuild the corrupted GIN index:

```sql
REINDEX INDEX CONCURRENTLY my_jsonb_index;
```

3. Rebuild all GIN indexes on a table:

```sql
REINDEX TABLE CONCURRENTLY documents;
```

## Examples

```bash
# Check for corrupted indexes across the database
psql -d mydb -c "
SELECT schemaname, tablename, indexname
FROM pg_stat_user_indexes
WHERE indexrelid IN (
  SELECT i.indexrelid FROM pg_index i
  JOIN pg_class c ON i.indexrelid = c.oid
  JOIN pg_am am ON c.relam = am.oid
  WHERE am.amname = 'gin'
);"
```
