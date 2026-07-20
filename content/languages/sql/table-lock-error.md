---
title: "[Solution] Table Is Locked"
description: "Fix 'Table is locked' when a query cannot proceed because the table is locked by another operation."
date: 2026-07-17T10:00:00+08:00
draft: false
language: "sql"
tags: ["sql", "performance, lock, table"]
severity: "error"
---

# Table Is Locked

## Error Message

```
ERROR 1205: Lock wait timeout exceeded / Table 'X' is locked — The table is locked by another transaction or operation and cannot be accessed.
```

## Common Causes

- Another transaction holds an exclusive lock on the table (e.g., ALTER TABLE, DROP TABLE)
- MyISAM tables use table-level locks instead of row-level locks
- Long-running ANALYZE TABLE or OPTIMIZE TABLE operation holds a lock
- Replication or backup operations lock the table during data transfer

## Solutions

### Solution 1: Wait for the lock to be released or find the blocking process

Identify which process holds the lock and decide whether to wait or terminate it.

```sql
-- MySQL: find the process holding the lock
SHOW PROCESSLIST;

-- Kill the blocking process
KILL <process_id>;

-- MySQL: check table locks
SHOW OPEN TABLES WHERE In_use > 0;

-- PostgreSQL: find locks on a table
SELECT
    relation::regclass AS table_name,
    pid,
    mode,
    granted,
    query
FROM pg_locks
JOIN pg_stat_activity USING (pid)
WHERE relation = 'users'::regclass;

-- SQL Server: find table locks
SELECT
    OBJECT_NAME(resource_associated_entity_id) AS table_name,
    request_session_id,
    request_mode,
    request_status
FROM sys.dm_tran_locks
WHERE resource_type = 'OBJECT';
```

### Solution 2: Use row-level locking instead of table locking

Ensure you are using a storage engine that supports row-level locking.

```sql
-- Wrong: MyISAM uses table-level locks
CREATE TABLE users (
    id INT,
    name VARCHAR(100)
) ENGINE = MyISAM;

-- Correct: InnoDB uses row-level locks
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100)
) ENGINE = InnoDB;

-- Convert MyISAM to InnoDB
ALTER TABLE users ENGINE = InnoDB;

-- Use SELECT ... FOR UPDATE for explicit row locking
START TRANSACTION;
SELECT * FROM users WHERE id = 1 FOR UPDATE;
UPDATE users SET name = 'Alice' WHERE id = 1;
COMMIT;
```

### Solution 3: Avoid long-running DDL operations on busy tables

Schedule table maintenance during low-traffic periods.

```sql
-- Wrong: ALTER TABLE on a busy table during peak hours
ALTER TABLE users ADD COLUMN bio TEXT; -- blocks all operations

-- Correct: use online DDL where available (MySQL)
ALTER TABLE users ADD COLUMN bio TEXT, ALGORITHM=INPLACE, LOCK=NONE;

-- PostgreSQL: use CREATE INDEX CONCURRENTLY
CREATE INDEX CONCURRENTLY idx_users_email ON users(email);

-- Schedule maintenance during off-peak hours
-- Use pt-online-schema-change for MySQL (Percona Toolkit)
-- pt-online-schema-change --alter "ADD COLUMN bio TEXT" D=mydb,t=users
```

## Prevention Tips

- Use InnoDB (MySQL) or the default row-level locking engine to minimize table-level lock contention
- Avoid DDL operations (ALTER TABLE, CREATE INDEX) during peak traffic hours
- Monitor SHOW OPEN TABLES or pg_locks regularly to detect lock contention early

## Related Errors

- [Lock Timeout]({{< relref "/languages/sql/lock-timeout.md" >}})
- [Deadlock Error]({{< relref "/languages/sql/deadlock-error.md" >}})
- [Slow Query]({{< relref "/languages/sql/slow-query.md" >}})
