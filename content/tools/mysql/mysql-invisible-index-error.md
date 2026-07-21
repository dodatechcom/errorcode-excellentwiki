---
title: "[Solution] MySQL Invisible Index Error"
description: "Fix MySQL invisible index error when queries fail because optimizer ignores an index marked as invisible"
tools: ["mysql"]
error-types: ["tool-error"]
severities: ["error"]
---

# MySQL Invisible Index Error

A query performs poorly or fails because an index is marked as INVISIBLE. The optimizer does not use invisible indexes unless explicitly hinted, causing full table scans.

## Common Causes

- Index was marked INVISIBLE during testing and not reverted
- Developer used INVISIBLE to test query performance without the index
- Migration script inadvertently set an index to invisible
- Query hint references an invisible index without FORCE INDEX

## How to Fix

### Check Index Visibility

```sql
-- View all indexes and their visibility
SELECT
  INDEX_NAME,
  IS_VISIBLE,
  NON_UNIQUE
FROM INFORMATION_SCHEMA.STATISTICS
WHERE TABLE_NAME = 'orders';
```

### Make Index Visible

```sql
-- Restore visibility so the optimizer uses it
ALTER TABLE orders ALTER INDEX idx_status VISIBLE;
```

### Use FORCE INDEX for Invisible Indexes

```sql
-- Force optimizer to use the invisible index
SELECT * FROM orders FORCE INDEX (idx_status)
WHERE status = 'active';
```

### Drop or Rebuild Invisible Indexes

```sql
-- If the invisible index is not needed
ALTER TABLE orders DROP INDEX idx_status;

-- If it needs to be recreated properly
ALTER TABLE orders DROP INDEX idx_status;
ALTER TABLE orders ADD INDEX idx_status (status) VISIBLE;
```

### Review All Invisible Indexes

```sql
-- Find all invisible indexes in the database
SELECT
  TABLE_SCHEMA,
  TABLE_NAME,
  INDEX_NAME
FROM INFORMATION_SCHEMA.STATISTICS
WHERE IS_VISIBLE = 'NO'
  AND TABLE_SCHEMA = 'mydb';
```

## Examples

```
-- Query is slow because idx_status is invisible
EXPLAIN SELECT * FROM orders WHERE status = 'active';
-- Shows: type=ALL, rows=1000000 (full table scan)

-- After making visible
ALTER TABLE orders ALTER INDEX idx_status VISIBLE;
EXPLAIN SELECT * FROM orders WHERE status = 'active';
-- Shows: type=ref, rows=50 (index scan)
```

## Related Errors

- [MySQL Index Corruption]({{< relref "/tools/mysql/mysql-index-corruption" >}}) -- index corruption
- [MySQL Explain Error]({{< relref "/tools/mysql/mysql-explain-error" >}}) -- explain issues
- [MySQL Unknown Column]({{< relref "/tools/mysql/mysql-unknown-column" >}}) -- column issues
