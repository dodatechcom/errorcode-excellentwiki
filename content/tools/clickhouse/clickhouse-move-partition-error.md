---
title: "[Solution] ClickHouse Move Partition Error"
description: "Fix ClickHouse move partition errors when ALTER TABLE MOVE PARTITION fails"
tools: ["clickhouse"]
error-types: ["tool-error"]
severities: ["error"]
---

# ClickHouse Move Partition Error

Move partition errors occur when ClickHouse cannot move data between partitions or tables.

## Common Causes

- Destination table does not exist
- Partition expression mismatch
- Disk volume not available for move
- Concurrent operation on partition

## How to Fix

Check available volumes:

```sql
SELECT name, policy, free_space FROM system.disks;
```

Move partition to another table:

```sql
ALTER TABLE table_a MOVE PARTITION '2024-01' TO table_b;
```

Move partition to different disk:

```sql
ALTER TABLE my_table MOVE PARTITION '2024-01' TO VOLUME 'cold';
```

## Examples

```sql
SELECT partition, disk_name, count() FROM system.parts WHERE table = 'my_table' GROUP BY partition, disk_name;
```
