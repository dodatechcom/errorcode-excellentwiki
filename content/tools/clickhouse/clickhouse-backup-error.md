---
title: "[Solution] ClickHouse Backup Error — How to Fix"
description: "Fix ClickHouse backup errors including backup tool failures, snapshot issues, and restore problems with backup data"
tools: ["clickhouse"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ClickHouse Backup Error

Backup errors in ClickHouse occur when using the clickhouse-backup tool or manual backup methods. ClickHouse does not have built-in backup commands; backups use filesystem snapshots or the clickhouse-backup utility.

## Why It Happens

- The clickhouse-backup tool is not installed or configured
- Disk space is insufficient for the backup
- The backup is taken while a merge is in progress
- ZooKeeper metadata is not included in the backup
- The backup is corrupted or incomplete
- The restore fails due to version mismatch

## Common Error Messages

```
Error: can't create backup: can't lock /var/lib/clickhouse/backup: directory is busy
```

```
Error: can't create backup: not enough disk space
```

```
Error: can't restore: table already exists
```

```
Error: can't create backup: connection to ZooKeeper failed
```

## How to Fix It

### 1. Install and Configure clickhouse-backup

```bash
# Install clickhouse-backup
sudo apt-get install clickhouse-backup

# Configure /etc/clickhouse-backup/config.yml
remote_storage: s3
clickhouse:
  host: localhost
  port: 9000
s3:
  bucket: my-clickhouse-backups
  region: us-east-1
  path: backups
```

### 2. Create a Backup

```bash
# Create backup
clickhouse-backup create my_backup_20240115

# List backups
clickhouse-backup list

# Upload to S3
clickhouse-backup upload my_backup_20240115
```

### 3. Fix Backup Lock Issues

```bash
# Check if another backup is running
ps aux | grep clickhouse-backup

# Kill stale backup process
kill <pid>

# Retry backup
clickhouse-backup create my_backup_20240115
```

### 4. Restore from Backup

```bash
# Stop ClickHouse
sudo systemctl stop clickhouse-server

# Download backup from S3
clickhouse-backup download my_backup_20240115

# Restore
clickhouse-backup restore my_backup_20240115

# Start ClickHouse
sudo systemctl start clickhouse-server
```

## Common Scenarios

- **Backup fails with lock error**: Another backup process is running. Kill it and retry.
- **Backup to S3 fails with timeout**: Increase S3 timeout settings or use a faster network.
- **Restore fails because table exists**: Delete existing table first or use `--rm` flag.

## Prevent It

- Schedule regular backups with cron and monitor for failures
- Test backup restoration on a staging server regularly
- Store backups in a different region or data center for disaster recovery

## Related Pages

- [ClickHouse Disk Error](/tools/clickhouse/clickhouse-disk-error)
- [ClickHouse Table Error](/tools/clickhouse/clickhouse-table-error)
- [ClickHouse Replication Error](/tools/clickhouse/clickhouse-replication-error)
