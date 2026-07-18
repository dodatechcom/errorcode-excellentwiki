---
title: "[Solution] MariaDB Binary Log Error — How to Fix"
description: "Fix MariaDB binary log errors including missing logs, corruption, purging issues, and GTID inconsistencies between primary and replica servers"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Binary Log Error

Binary log errors occur when the server cannot read, write, or find binary log files. These logs are essential for replication and point-in-time recovery.

## Why It Happens

- Binary log files were manually deleted from the filesystem
- Disk space ran out while writing binary logs
- `expire_logs_days` purged logs too aggressively
- A replica references a binlog position that has been purged
- Binary log file header is corrupted
- GTID state file is out of sync with actual binlog content

## Common Error Messages

```
ERROR: Error reading log event; read 4, expected 15
```

```
Got fatal error 1236 from master when reading data from binary log:
'could not find next log'
```

```
[ERROR] Could not open log file '/var/log/mysql/mysql-bin.000025': No such file or directory
```

```
[Warning] Disk is full writing './mysql-bin.000030' (errno: 28)
```

## How to Fix It

### 1. Regenerate Missing Binary Logs

```bash
# On primary, flush and rotate
mysql -e "FLUSH BINARY LOGS;"

# On replica, reset and reconfigure
mysql -e "STOP SLAVE; RESET SLAVE ALL;"
mysql -e "SHOW MASTER STATUS;"
mysql -e "CHANGE MASTER TO
  MASTER_HOST='primary-host',
  MASTER_LOG_FILE='mysql-bin.000010',
  MASTER_LOG_POS=4;"
mysql -e "START SLAVE;"
```

### 2. Fix Disk Space

```bash
df -h /var/lib/mysql
ls -lhS /var/lib/mysql/mysql-bin.*
mysql -e "PURGE BINARY LOGS BEFORE DATE_SUB(NOW(), INTERVAL 3 DAY);"
mysql -e "SET GLOBAL expire_logs_days = 7;"
```

### 3. Fix Binary Log Corruption

```bash
mysqlbinlog --base64-output=DECODE-ROWS -v /var/lib/mysql/mysql-bin.000025
rm /var/lib/mysql/mysql-bin.000025
mysql -e "FLUSH BINARY LOGS;"
```

### 4. Fix GTID Position After Binlog Purge

```sql
SELECT * FROM mysql.gtid_slave_pos;
STOP SLAVE;
RESET SLAVE ALL;
CHANGE MASTER TO
  MASTER_HOST='primary-host',
  MASTER_USER='repl_user',
  MASTER_USE_GTID=slave_pos;
START SLAVE;
```

## Common Scenarios

- **Replica fails after primary purges logs**: Reset replica and restart from current position.
- **Disk full stops the server**: Free space, then purge old logs.
- **Manual deletion of binlog files**: Regenerate logs and reset the replica.

## Prevent It

- Never manually delete binary log files; use `PURGE BINARY LOGS`
- Monitor disk space before binlog directory fills up
- Use GTID-based replication for automatic position tracking

## Related Pages

- [MariaDB Replication Error](/tools/mariadb/mariadb-replication-error)
- [MariaDB InnoDB Error](/tools/mariadb/mariadb-innodb-error)
- [MySQL Binary Log Error](/tools/mysql/mysql-binary-log-error)
