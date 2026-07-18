---
title: "[Solution] MariaDB Backup Error — How to Fix"
description: "Fix MariaDB backup errors including mariabackup failures, lock timeouts during backup, incomplete backups, and restore verification problems"
tools: ["mariadb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MariaDB Backup Error

Backup errors occur when `mariabackup`, `mysqldump`, or other tools fail to create a consistent backup due to insufficient disk space, lock contention, InnoDB log issues, or permission problems.

## Why It Happens

- The backup destination does not have enough disk space
- `mariabackup` cannot acquire necessary locks
- InnoDB redo logs are too small for the backup duration
- Backup directory has incorrect file permissions
- A backup was interrupted and left partial files
- `FLUSH TABLES WITH READ LOCK` times out

## Common Error Messages

```
mariabackup: error: Cannot lock data directory: Resource temporarily unavailable
```

```
mariabackup: error: failed to open delta file '/var/lib/mysql/#innodb_aep/page.delt'
```

```
[ERROR] mariabackup: Failed to copy '/var/lib/mysql/ibdata1'
```

```
mysqldump: Error 2013: Lost connection to MySQL server during query
```

## How to Fix It

### 1. Ensure Sufficient Disk Space

```bash
df -h /backup
mysql -e "SELECT table_schema, ROUND(SUM(data_length+index_length)/1024/1024,2) AS size_mb
FROM information_schema.TABLES GROUP BY table_schema;"

# Stream backup to avoid local disk usage
mariabackup --backup --stream=xbstream 2>/dev/null | gzip > /backup/full.sql.gz
```

### 2. Fix mariabackup Lock Errors

```bash
mysql -e "SHOW PROCESSLIST;"
mysql -e "KILL <blocking_thread_id>;"
mariabackup --backup --target-dir=/backup/full
```

### 3. Fix mariabackup Restore

```bash
mariabackup --prepare --target-dir=/backup/full
sudo systemctl stop mariadb
sudo rm -rf /var/lib/mysql.old
sudo mv /var/lib/mysql /var/lib/mysql.old
sudo mkdir /var/lib/mysql
sudo chown mysql:mysql /var/lib/mysql
mariabackup --copy-back --target-dir=/backup/full
sudo chown -R mysql:mysql /var/lib/mysql
sudo systemctl start mariadb
```

### 4. Fix mysqldump Connection Loss

```bash
mysqldump --all-databases   --net_read_timeout=600   --net_write_timeout=600   --max_allowed_packet=1G   --single-transaction   --routines --triggers --events > /backup/full_dump.sql
```

## Common Scenarios

- **mariabackup fails with lock error**: Another backup is running. Kill it and retry.
- **mysqldump times out on large table**: Use mariabackup for physical backup instead.
- **Backup restore produces corrupted data**: Always run `--prepare` after `--backup`.

## Prevent It

- Verify backups weekly by restoring to a test instance
- Use mariabackup for large databases instead of mysqldump
- Monitor backup job duration and alert on anomalies

## Related Pages

- [MariaDB InnoDB Error](/tools/mariadb/mariadb-innodb-error)
- [MariaDB Table Corruption](/tools/mariadb/mariadb-table-corruption)
- [MySQL Backup Error](/tools/mysql/mysql-backup-error)
