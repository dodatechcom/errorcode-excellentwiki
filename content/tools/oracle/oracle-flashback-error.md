---
title: "Oracle - ORA-01555: snapshot too old"
description: "Oracle query fails because a read-consistent snapshot of data has been overwritten by concurrent changes"
tools: ["oracle"]
error-types: ["database-error"]
severities: ["error"]
tags: ["oracle", "snapshot", "ora-01555", "undo", "read-consistency", "long-query"]
weight: 5
---

ORA-01555: snapshot too old (rollback segment too small) occurs when Oracle cannot maintain a read-consistent view of data because the undo information needed by a long-running query has been overwritten by newer transactions.

## Common Causes

- Long-running query spanning many DML operations
- UNDO tablespace too small to retain enough history
- FETCH across COMMIT in cursor operations
- Batch processing without periodic commits
- UNDO_RETENTION too short for the workload

## How to Fix

1. Check UNDO tablespace usage:

```sql
SELECT tablespace_name, round(sum_bytes/1024/1024/1024, 2) as size_gb
FROM (
  SELECT tablespace_name, sum(bytes) as sum_bytes
  FROM dba_data_files
  WHERE tablespace_name = (SELECT value FROM v$parameter WHERE name = 'undo_tablespace')
  GROUP BY tablespace_name
);
```

2. Increase UNDO tablespace size:

```sql
ALTER DATABASE DATAFILE '/u01/oradata/mydb/undotbs01.dbf'
AUTOEXTEND ON NEXT 1G MAXSIZE 30G;
```

3. Increase UNDO retention:

```sql
ALTER SYSTEM SET UNDO_RETENTION = 3600; -- 1 hour
```

4. Use FOR UPDATE SKIP LOCKED for concurrent processing:

```sql
DECLARE
  CURSOR c_orders IS
    SELECT order_id FROM orders WHERE status = 'pending'
    FOR UPDATE SKIP LOCKED;
BEGIN
  FOR rec IN c_orders LOOP
    -- process without blocking
    UPDATE orders SET status = 'processing' WHERE order_id = rec.order_id;
    COMMIT;
  END LOOP;
END;
```

5. Optimize long-running queries:

```sql
-- Add indexes to reduce query time
CREATE INDEX idx_orders_status ON orders(status);

-- Use parallel query for large scans
SELECT /*+ PARALLEL(4) */ * FROM large_table;
```

6. Increase PGA for sort operations:

```sql
ALTER SYSTEM SET pga_aggregate_target = 4G;
```

## Examples

```sql
-- Error: ORA-01555: snapshot too old: rollback segment number 15 with name "_SYSSMU15$" too small
DECLARE
  CURSOR c IS SELECT * FROM large_table;
BEGIN
  FOR rec IN c LOOP
    DBMS_LOCK.SLEEP(1); -- simulate slow processing
    -- Other sessions modifying large_table
  END LOOP;
END;

-- Fix: commit periodically or increase UNDO
ALTER SYSTEM SET UNDO_RETENTION = 7200;
```

## Related Errors

- [Lock error]({{< relref "/tools/oracle/oracle-lock-error" >}})
- [Tablespace error]({{< relref "/tools/oracle/oracle-tablespace-error" >}})
