---
title: "[Solution] MySQL Table is Full Error — How to Fix"
description: "Fix MySQL table is full errors by expanding disk space, adjusting tablespace settings, archiving old data, and optimizing table storage"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# MySQL Table is Full Error

This error means MySQL cannot allocate more space for the table because it has reached the disk space limit, the maximum table size, or the tablespace file has hit its configured boundary. This typically affects InnoDB tables that use file-per-table tablespaces.

## Why It Happens

- The filesystem hosting the InnoDB data directory has run out of disk space
- The InnoDB tablespace file has reached the 64TB maximum size
- The `innodb_file_per_table` tablespace has hit the `innodb_autoextend_increment` limit
- A BLOB or TEXT column is storing data that exceeds available space
- The tmpdir partition is full and MySQL cannot create temporary tables
- Binary logs or relay logs have consumed all remaining disk space
- The table was altered to a larger row format and no room exists

## Common Error Messages

```
ERROR 1114 (HY000): The table 'my_table' is full
```

```
ERROR 3 (HY000): Error writing file '/tmp/MYxxxxx' (Errcode: 28 - No space left on device)
```

```
ERROR 1114 (HY000): The table '/var/lib/mysql/mydb/my_table' is full
```

## How to Fix It

### 1. Check Disk Space

```bash
# Check disk usage on the MySQL data directory
df -h /var/lib/mysql

# Find the largest files in the data directory
du -sh /var/lib/mysql/*
du -sh /var/lib/mysql/mydb/*
```

### 2. Check InnoDB Tablespace Size

```sql
-- Check table sizes
SELECT
    table_name,
    ROUND(data_length / 1024 / 1024, 2) AS data_mb,
    ROUND(index_length / 1024 / 1024, 2) AS index_mb,
    ROUND(data_free / 1024 / 1024, 2) AS free_mb
FROM information_schema.tables
WHERE table_schema = 'mydb'
ORDER BY data_length DESC;
```

### 3. Clean Up Disk Space

```bash
# Remove old binary logs
mysql -e "PURGE BINARY LOGS BEFORE DATE_SUB(NOW(), INTERVAL 3 DAY);"

# Clean up temp files
sudo find /tmp -name 'MY*' -mtime +1 -delete

# Remove old log files
sudo journalctl --vacuum-size=500M
```

### 4. Optimize or Archive the Table

```sql
-- Optimize to reclaim fragmented space
OPTIMIZE TABLE my_table;

-- Archive old rows
DELETE FROM my_table
WHERE created_at < DATE_SUB(NOW(), INTERVAL 1 YEAR)
LIMIT 10000;
```

### 5. Expand the Tablespace

```sql
-- Check current autoextend settings
SHOW VARIABLES LIKE 'innodb_autoextend_increment';

-- Increase autoextend increment (in MB)
SET GLOBAL innodb_autoextend_increment = 64;
```

### 6. Move to a Larger Disk

```bash
# Stop MySQL
sudo systemctl stop mysql

# Move data directory to a larger volume
sudo rsync -av /var/lib/mysql/ /mnt/larger-volume/mysql/

# Update datadir in my.cnf
# datadir = /mnt/larger-volume/mysql

# Start MySQL
sudo systemctl start mysql
```

## Common Scenarios

- **Log table grows without bound**: An audit log or session table accumulates millions of rows. Partition by date and drop old partitions regularly.
- **Binary logs fill the disk**: Default binlog retention can be unlimited. Set `expire_logs_days` or `binlog_expire_logs_seconds` to auto-purge.
- **tmpdir full during large sort**: Large `ORDER BY` or `GROUP BY` operations use temp files. Set `tmpdir` to a dedicated volume with enough space.

## Prevent It

- Set up disk space monitoring with alerts at 80% and 90% thresholds
- Configure `expire_logs_days` to auto-purge old binary logs
- Use table partitioning for time-series data and drop old partitions on a schedule

## Related Pages

- [MySQL InnoDB Error](/tools/mysql/mysql-innodb-error)
- [MySQL Too Many Connections](/tools/mysql/mysql-too-many-connections)
- [PostgreSQL Disk Full](/tools/postgresql/pg-disk-full)
