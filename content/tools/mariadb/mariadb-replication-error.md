---
title: "[Solution] MariaDB Replication Error — How to Fix"
description: "Fix MariaDB replication errors caused by binary log gaps, slave lag, GTID mismatches, and network issues between primary and replica servers"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Replication Error

Replication in MariaDB copies data from a primary server to replicas. Replication errors occur when the replica cannot find or apply the next binary log event, often due to purged logs, network interruptions, or schema mismatches.

## Why It Happens

- The primary purged binary logs that the replica still needs
- Network interruption caused the replica to lose its connection mid-event
- The replica SQL thread encountered a statement it cannot execute
- GTID positions are inconsistent between primary and replica
- The replica was restored from a backup that does not match the primary's binlog position
- `expire_logs_days` caused premature log rotation

## Common Error Messages

```
Last_IO_Error: Got fatal error 1236 from master when reading data from
binary log: 'could not find next log'
```

```
Slave_SQL_Running: No
Last_SQL_Error: Could not execute Write_rows event on table mydb.users;
Duplicate entry '100' for key 'PRIMARY'
```

```
ERROR: Error reading log event; read 4, expected 15, could not read position
-- from master
```

```
Last_IO_Error: Fatal error reading replication stream: error_code=1236
```

## How to Fix It

### 1. Rebuild Replica from Primary's Current Position

```bash
# On primary, get current position
mysql -e "SHOW MASTER STATUS;"

# On replica, reset and reconfigure
mysql -e "STOP SLAVE; RESET SLAVE ALL;"
mysql -e "CHANGE MASTER TO
  MASTER_HOST='primary-host',
  MASTER_USER='repl_user',
  MASTER_PASSWORD='repl_pass',
  MASTER_LOG_FILE='mysql-bin.000010',
  MASTER_LOG_POS=1234;"
mysql -e "START SLAVE;"
```

### 2. Use GTID-Based Replication

```sql
-- On primary (my.cnf)
-- [mysqld]
-- gtid_strict_mode=ON

-- On replica
CHANGE MASTER TO
  MASTER_HOST='primary-host',
  MASTER_USER='repl_user',
  MASTER_PASSWORD='repl_pass',
  MASTER_USE_GTID=slave_pos;
START SLAVE;
```

### 3. Skip a Problematic Statement

```sql
-- For statement-based replication
STOP SLAVE;
SET GLOBAL sql_slave_skip_counter = 1;
START SLAVE;

-- For GTID-based replication
STOP SLAVE;
SET GTID_NEXT='aaaaaaaa-bbbb-cccc-dddd-eeeeeeeeeeee:123';
BEGIN; COMMIT;
SET GTID_NEXT='AUTOMATIC';
START SLAVE;
```

### 4. Extend Binary Log Retention

```sql
SET GLOBAL expire_logs_days = 7;
SET GLOBAL max_binlog_size = 1073741824; -- 1GB
```

## Common Scenarios

- **Replica falls far behind**: Primary purges logs before replica catches up. Use `CHANGE MASTER` with current position or switch to GTID.
- **Duplicate key after restore**: Restored replica has conflicting data. Use `sql_slave_skip_counter` or rebuild.
- **Schema mismatch after DDL**: An ALTER TABLE on primary changed column types that break queries on replica.

## Prevent It

- Use GTID-based replication to avoid manual position tracking
- Set `expire_logs_days=7` minimum on the primary
- Monitor replication lag with `SHOW SLAVE STATUS` and alert on delays

## Related Pages

- [MariaDB Binary Log Error](/tools/mariadb/mariadb-binary-log-error)
- [MariaDB Connection Error](/tools/mariadb/mariadb-connection-error)
- [MySQL Replication Error](/tools/mysql/mysql-replication-error)
