---
title: "PostgreSQL Deadlock Detected Error"
description: "PostgreSQL detects deadlock between competing transactions and aborts one"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# PostgreSQL Deadlock Detected Error

PostgreSQL detects deadlock between competing transactions and aborts one

## Common Causes

- Two transactions locking rows in opposite order
- Missing or suboptimal indexes causing table locks
- Long-running transactions holding locks
- Application code not handling deadlocks with retry

## How to Fix

1. Check PostgreSQL logs for deadlock details
2. Analyze query plans with EXPLAIN
3. Add indexes to reduce lock scope
4. Implement application-level retry logic
5. Reduce transaction isolation level if possible

## Examples

```sql
-- Check for locks
SELECT * FROM pg_locks WHERE NOT granted;

-- Check deadlocks in logs
SHOW log_lock_waits;

-- Analyze query plan
EXPLAIN ANALYZE SELECT * FROM mytable WHERE id = 1;
```
