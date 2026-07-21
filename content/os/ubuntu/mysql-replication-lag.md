---
title: "MySQL Replication Lag Error"
description: "Slave server falls behind master in replication causing data inconsistency"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# MySQL Replication Lag Error

Slave server falls behind master in replication causing data inconsistency

## Common Causes

- Slave server slower than master (CPU/IO bound)
- Large transactions on master causing lag
- Network latency between master and slave
- Single-threaded replication on slave

## How to Fix

1. Check replication status: `SHOW SLAVE STATUS\G`
2. Enable parallel replication: `slave_parallel_workers=4`
3. Optimize queries on slave
4. Check network: `ping master-server`

## Examples

```sql
-- Check replication lag
SHOW SLAVE STATUS\G

-- Enable parallel replication
SET GLOBAL slave_parallel_workers = 4;
SET GLOBAL slave_parallel_type = 'LOGICAL_CLOCK';
```
