---
title: "[Solution] MySQL Replication Error - Fix Slave SQL Duplicate Entry"
description: "Fix MySQL replication errors by using SET GLOBAL SQL_SLAVE_SKIP_COUNTER, configuring slave_exec_mode, and handling duplicate entry conflicts"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# MySQL Replication Error

Replication errors occur when the slave (replica) cannot apply a relay log event from the master (source). The most common replication error is a duplicate key conflict, but other errors like missing rows or table mismatches also occur.

## What This Error Means

MySQL returns this error on the replica:

```
Slave SQL: Error executing row event: 'Duplicate entry '123' for key 'PRIMARY'', Error_code: 1062
```

The replica stops applying events and reports the error. This is the default behavior with `slave_exec_mode = STRICT`. In `IDEMPOTENT` mode, duplicate key errors are silently skipped, which is useful for circular replication.

## Why It Happens

- Direct writes on the replica (bypassing replication)
- Circular replication where the same row is updated on multiple masters
- The replica was restored from a backup that is out of sync with the master
- The `auto_increment_increment` and `auto_increment_offset` are not configured correctly for multi-master setups
- A statement on the master produced a different result on the replica (like `UPDATE ... LIMIT` with non-deterministic ordering)
- The replica has different data than the master due to a past replication failure

## How to Fix It

### 1. Check the Replica Status

```sql
SHOW SLAVE STATUS\G

-- Key fields to check:
-- Last_SQL_Error: the actual error message
-- Exec_Master_Log_Pos: where the error occurred in the relay log
-- Relay_Log_File: which relay log file contains the error
```

### 2. Skip the Erroneous Event

```sql
-- Skip one event
STOP SLAVE;
SET GLOBAL SQL_SLAVE_SKIP_COUNTER = 1;
START SLAVE;

-- Skip N events
SET GLOBAL SQL_SLAVE_SKIP_COUNTER = N;
```

### 3. Skip Errors by Error Code

```sql
-- In my.cnf on the replica
[mysqld]
slave_skip_errors = 1062
-- This skips all duplicate key errors (use with caution)

-- Or use ddl_skip_errors for DDL errors only
slave_skip_errors = ddl_exist_errors
```

### 4. Set IDEMPOTENT Mode

```sql
-- On the replica
SET GLOBAL slave_exec_mode = 'IDEMPOTENT';
-- This silently ignores duplicate key and does-not-exist errors
```

### 5. Rebuild the Replica from Scratch

```bash
# If replication is too far out of sync
# On the master
mysqldump --all-databases --master-data > full_backup.sql

# On the replica
mysql < full_backup.sql

# Start replication from the correct position
CHANGE MASTER TO
    MASTER_HOST = 'master_host',
    MASTER_USER = 'replicator',
    MASTER_PASSWORD = 'password',
    MASTER_LOG_FILE = 'mysql-bin.000001',
    MASTER_LOG_POS = 154;

START SLAVE;
```

## Common Mistakes

- Using `SQL_SLAVE_SKIP_COUNTER` without understanding how many events to skip -- skip too few and you hit the same error, skip too many and you lose valid data
- Setting `slave_exec_mode = IDEMPOTENT` without understanding that it silently ignores data differences
- Not investigating why the error occurred before skipping -- skipping is a temporary fix, not a solution
- Forgetting to reset `SQL_SLAVE_SKIP_COUNTER` to 0 after it has been used
- Running `RESET SLAVE` when you meant `RESET SLAVE ALL` -- `RESET SLAVE ALL` removes the entire replication configuration

## Related Pages

- [MySQL InnoDB Error](/tools/mysql/mysql-innodb-error)
- [MySQL Deadlock Detected](/tools/mysql/mysql-deadlock-detected)
- [MySQL Crash Recovery](/tools/mysql/mysql-crash-recovery)
- [PostgreSQL Replication Slots](/tools/postgresql/pg-replication-slots)
