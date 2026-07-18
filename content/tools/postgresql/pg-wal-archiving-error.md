---
title: "[Solution] PostgreSQL WAL Archiving Failed Error — How to Fix"
description: "Fix PostgreSQL WAL archiving errors by restoring archive commands, checking disk space, verifying permissions, and recovering from failed archive slots"
tools: ["postgresql"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# PostgreSQL WAL Archiving Failed Error

This error means PostgreSQL failed to archive a Write-Ahead Log (WAL) segment to the configured archive destination. WAL archiving is required for point-in-time recovery (PITR) and streaming replication setups.

## Why It Happens

- The archive command returns a non-zero exit code
- The archive destination disk is full or inaccessible
- The archive command script has incorrect permissions or path
- A network-mounted archive destination (NFS, S3) is unreachable
- WAL segments are being generated faster than they can be archived
- `archive_timeout` forces frequent segment switches that overwhelm the archiver
- The archive process is not running (`archive_mode = on` but `archive_command` is misconfigured)
- Permission denied on the archive directory

## Common Error Messages

```
WARNING: archive command failed with exit code 1
DETAIL: The failed archive command was: cp %p /archive/%f
```

```
LOG: archival command failed: archive timeout while archiving WAL segment
```

```
ERROR: could not open file "/archive/postgresql/00000001000000030000001A": No space left on device
```

## How to Fix It

### 1. Check Archive Status

```sql
-- Check if archiving is enabled
SHOW archive_mode;
SHOW archive_command;

-- Check WAL archiving status
SELECT
    archived_count,
    failed_count,
    last_archived_wal,
    last_archived_time,
    last_failed_wal,
    last_failed_time
FROM pg_stat_archiver;
```

### 2. Fix the Archive Command

```sql
-- Test the archive command manually
-- %p = full path to WAL segment
-- %f = WAL segment file name

-- Example with rsync to a remote server
ALTER SYSTEM SET archive_command = 'rsync -a %p user@backup:/archive/%f';
SELECT pg_reload_conf();
```

```bash
# Test the command manually
rsync -a /var/lib/postgresql/14/main/pg_wal/00000001000000030000001A user@backup:/archive/

# Verify the file was copied
ssh user@backup ls -la /archive/00000001000000030000001A
```

### 3. Check Disk Space on Archive Destination

```bash
# Check disk space
df -h /archive

# Check archive directory
du -sh /archive/*
ls -la /archive/ | head -20

# Clean old archives if needed
find /archive -name "0000000100000000*" -mtime +30 -delete
```

### 4. Fix Permissions

```bash
# Ensure the postgres user owns the archive directory
sudo chown -R postgres:postgres /archive
sudo chmod 750 /archive

# If using a script, ensure it is executable
sudo chmod +x /archive_wal.sh
```

### 5. Set Archive Timeout

```sql
-- Force WAL segment switch every 300 seconds (5 minutes)
-- This limits the maximum data loss window for PITR
ALTER SYSTEM SET archive_timeout = 300;
SELECT pg_reload_conf();
```

### 6. Monitor and Alert

```sql
-- Alert when failed_count increases
SELECT
    failed_count,
    last_failed_wal,
    last_failed_time
FROM pg_stat_archiver
WHERE failed_count > 0;

-- Check for stuck WAL segments
SELECT
    slot_name,
    restart_lsn,
    confirmed_flush_lsn,
    pg_wal_lsn_diff(confirmed_flush_lsn, restart_lsn) AS retained_bytes
FROM pg_replication_slots;
```

## Common Scenarios

- **NFS mount went down**: The archive destination is on NFS and the server rebooted. Remount the NFS share and restart PostgreSQL.
- **S3 upload throttling**: Using `aws s3 cp` for archiving hits S3 rate limits during high WAL generation. Use `aws s3 sync` or batch uploads.
- **Archive disk full**: WAL segments accumulate because old archives are not cleaned up. Implement a lifecycle policy or cron job to delete archives older than the retention period.

## Prevent It

- Monitor `pg_stat_archiver.failed_count` and alert when it increases
- Keep the archive destination at least 50% free at all times
- Test your PITR restore process regularly to ensure archives are valid

## Related Pages

- [PostgreSQL Replication Lag](/tools/postgresql/pg-replication-lag)
- [PostgreSQL Checkpoint Error](/tools/postgresql/pg-checkpoint-error)
- [MySQL InnoDB Error](/tools/mysql/mysql-innodb-error)
