---
title: "Oracle - ORA-14400: inserted partition key does not map"
description: "Oracle INSERT fails because the partition key value does not match any existing partition"
tools: ["oracle"]
error-types: ["database-error"]
severities: ["error"]
tags: ["oracle", "partition", "key", "ora-14400", "range", "insert"]
weight: 5
---

ORA-14400: inserted partition key does not map to any partition occurs when an INSERT statement tries to add a row with a partition key value that does not fall into any defined partition. This is common with range-partitioned tables when new date ranges are needed.

## Common Causes

- Partition range does not cover the inserted date/value
- Missing partition for the current time period
- MAXVALUE partition not defined
- Monthly/weekly partitions not created for future dates
- Incorrect partition key value

## How to Fix

1. Check existing partitions:

```sql
SELECT partition_name, high_value
FROM user_tab_partitions
WHERE table_name = 'SALES'
ORDER BY partition_position;
```

2. Add a new partition for the missing range:

```sql
ALTER TABLE sales ADD PARTITION p_2024_01
VALUES LESS THAN (TO_DATE('2024-02-01', 'YYYY-MM-DD'));
```

3. Add a catch-all MAXVALUE partition:

```sql
ALTER TABLE sales ADD PARTITION p_future VALUES LESS THAN (MAXVALUE);
```

4. Use interval partitioning for automatic partition creation:

```sql
CREATE TABLE sales (
  sale_id NUMBER,
  sale_date DATE,
  amount NUMBER
)
PARTITION BY RANGE (sale_date)
INTERVAL (NUMTOYMINTERVAL(1, 'MONTH'))
(
  PARTITION p_initial VALUES LESS THAN (TO_DATE('2024-01-01', 'YYYY-MM-DD'))
);
```

5. Split an existing partition to accommodate new values:

```sql
ALTER TABLE sales SPLIT PARTITION p_future
AT (TO_DATE('2024-06-01', 'YYYY-MM-DD'))
INTO (PARTITION p_2024_h1, PARTITION p_future);
```

6. Use DBMS_SCHEDULER to create future partitions automatically:

```sql
BEGIN
  DBMS_SCHEDULER.CREATE_JOB(
    job_name => 'CREATE_MONTHLY_PARTITIONS',
    job_type => 'PLSQL_BLOCK',
    job_action => 'BEGIN create_next_partition(); END;',
    start_date => SYSTIMESTAMP,
    repeat_interval => 'FREQ=MONTHLY;BYMONTHDAY=28',
    enabled => TRUE
  );
END;
```

## Examples

```sql
-- Error: ORA-14400: inserted partition key does not map to any partition
INSERT INTO sales VALUES (1, TO_DATE('2024-03-15', 'YYYY-MM-DD'), 1000);
-- ORA-14400: inserted partition key does not map to any partition

-- Fix: add partition for March 2024
ALTER TABLE sales ADD PARTITION p_2024_03
VALUES LESS THAN (TO_DATE('2024-04-01', 'YYYY-MM-DD'));

INSERT INTO sales VALUES (1, TO_DATE('2024-03-15', 'YYYY-MM-DD'), 1000);
-- 1 row created.
```

## Related Errors

- [Tablespace error]({{< relref "/tools/oracle/oracle-tablespace-error" >}})
- [Lock error]({{< relref "/tools/oracle/oracle-lock-error" >}})
