---
title: "[Solution] MySQL Crash Recovery Failure - Fix Redo Log and ibdata Errors"
description: "Fix MySQL crash recovery failures by checking redo logs, using innodb_force_recovery, and rebuilding the InnoDB system tablespace safely"
tools: ["mysql"]
error-types: ["database-error"]
severities: ["critical"]
weight: 5
---

# MySQL Crash Recovery Failure

When MySQL crashes and restarts, InnoDB performs automatic crash recovery using redo logs (ib_logfile) and the undo tablespace. If this recovery fails, MySQL cannot start and requires manual intervention.

## What This Error Means

MySQL reports recovery errors in the error log:

```
InnoDB: Log sequence number 123456789
InnoDB: Last MySQL binlog file position ...
InnoDB: We detected that the database was not shutdown normally
InnoDB: Starting an apply batch of log records to the database...
InnoDB: Apply batch completed!
InnoDB: Error: checksum mismatch in file ./ibdata1
```

Or:

```
InnoDB: Unable to lock ./ib_logfile0
InnoDB: Check that you do not already have another mysqld process
```

InnoDB uses the redo log to replay committed changes that were not yet flushed to the data files. If the redo log is corrupt or incomplete, recovery fails.

## Why It Happens

- The server lost power or was killed without a clean shutdown
- Disk failure corrupted the redo log files
- `innodb_log_file_size` was changed without a clean shutdown first
- The `ibdata1` system tablespace is corrupt
- Filesystem corruption (e.g., from a failed disk or RAID controller)
- The redo log was truncated or partially overwritten
- InnoDB doublewrite buffer pages are corrupted

## How to Fix It

### 1. Check the Error Log

```bash
# Find the error log
tail -200 /var/log/mysql/error.log

# Look for lines starting with InnoDB:
grep "InnoDB:" /var/log/mysql/error.log | tail -50
```

### 2. Verify Redo Log File Sizes Match

```bash
# Check current redo log size
ls -la /var/lib/mysql/ib_logfile*

# Check configured size
SHOW VARIABLES LIKE 'innodb_log_file_size';
```

### 3. Use innodb_force_recovery (Last Resort)

```bash
# In my.cnf
[mysqld]
innodb_force_recovery = 1

# Start MySQL
sudo systemctl start mysql
```

The recovery levels are:
- `1` = Ignore checksum page checks
- `2` = Do not run the background merge and insert buffer thread
- `3` = Do not perform undo log recovery
- `4` = Do not calculate table statistics
- `5` = Do not check for missing undo logs during recovery
- `6` = Do not redo log roll-forward at all

### 4. After Recovery, Dump and Rebuild

```bash
# Once MySQL starts with force_recovery
mysqldump --all-databases --routines --triggers --events > full_backup.sql

# Stop MySQL, remove the corrupted data
sudo systemctl stop mysql
sudo mv /var/lib/mysql /var/lib/mysql_corrupt

# Start fresh
sudo mysql_install_db
sudo systemctl start mysql

# Restore the dump
mysql < full_backup.sql
```

### 5. Fix Corrupted Redo Logs

```bash
# If redo log files are corrupted, delete them and let InnoDB recreate them
# WARNING: this may lose uncommitted transaction data
sudo systemctl stop mysql

# Remove redo logs
rm /var/lib/mysql/ib_logfile*

# Start MySQL -- InnoDB will recreate the redo logs
sudo systemctl start mysql
```

## Common Mistakes

- Using `innodb_force_recovery = 6` without understanding that it skips most recovery checks and can cause data loss
- Forgetting to remove `innodb_force_recovery` from `my.cnf` after recovery -- MySQL will not start normally with this setting
- Not backing up data before attempting recovery operations
- Changing `innodb_log_file_size` without first performing a clean shutdown
- Not using an UPS or journaling filesystem to prevent crash recovery issues in the first place

## Related Pages

- [MySQL InnoDB Error](/tools/mysql/mysql-innodb-error)
- [MySQL OOM](/tools/mysql/mysql-oom)
- [MySQL Max Allowed Packet](/tools/mysql/mysql-max-allowed-packet)
- [PostgreSQL WAL Segment Error](/tools/postgresql/pg-wal-segment-error)
