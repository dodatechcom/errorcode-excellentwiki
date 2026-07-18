---
title: "[Solution] MariaDB Lock Error — How to Fix"
description: "Fix MariaDB lock timeout and metadata lock errors by optimizing transaction duration, adding indexes, and configuring lock wait settings"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Lock Error

Lock errors occur when a transaction waits too long to acquire a lock held by another transaction. This includes `LOCK WAIT timeout` and `metadata lock` errors.

## Why It Happens

- A long-running transaction holds row or table locks
- A DDL statement waits for all transactions using the table to finish
- Missing indexes cause InnoDB to lock more rows than necessary
- Large batch operations hold locks for extended periods
- Table-level locks from MyISAM tables block InnoDB operations

## Common Error Messages

```
ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction
```

```
ERROR 1213 (40001): Deadlock found when trying to get lock
```

```
ERROR 1205 (HY000): Lock wait timeout exceeded
Query: 'ALTER TABLE mydb.big_table ADD COLUMN new_col INT'
```

```
Waiting for table metadata lock: 'mydb.big_table'
```

## How to Fix It

### 1. Identify Blocking Transactions

```sql
SELECT
  r.trx_id AS waiting_trx,
  r.trx_query AS waiting_query,
  b.trx_id AS blocking_trx,
  b.trx_query AS blocking_query,
  b.trx_started AS blocking_started
FROM information_schema.INNODB_TRX r
JOIN information_schema.INNODB_TRX b ON 1=1
WHERE r.trx_state = 'LOCK WAIT';
```

### 2. Kill the Blocking Transaction

```sql
SHOW PROCESSLIST;
KILL <thread_id>;
```

### 3. Increase Lock Wait Timeout

```sql
SET GLOBAL innodb_lock_wait_timeout = 120;
```

### 4. Use Online Schema Change

```bash
pt-online-schema-change --alter "ADD COLUMN new_col INT"   D=mydb,t=big_table --execute
```

### 5. Optimize Long Transactions

```sql
SELECT trx_id, trx_started,
  TIMESTAMPDIFF(SECOND, trx_started, NOW()) AS age_seconds,
  trx_query
FROM information_schema.INNODB_TRX ORDER BY trx_started;

SET SESSION max_statement_time = 30;
```

## Common Scenarios

- **Online schema change on busy table**: Use `pt-online-schema-change` to avoid blocking.
- **Stale transaction left open**: Kill the stale transaction holding locks.
- **SELECT locks entire table for ALTER**: Set `max_statement_time` to kill long queries.

## Prevent It

- Use online schema change tools for DDL on production tables
- Set `max_statement_time` to auto-kill long queries
- Monitor `INNODB_TRX` for stale transactions

## Related Pages

- [MariaDB Deadlock Error](/tools/mariadb/mariadb-deadlock-error)
- [MariaDB InnoDB Error](/tools/mariadb/mariadb-innodb-error)
- [MySQL Lock Wait Timeout](/tools/mysql/mysql-lock-wait-timeout)
