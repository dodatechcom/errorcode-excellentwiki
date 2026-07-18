---
title: "[Solution] YugabyteDB Backup Error — How to Fix"
description: "Fix YugabyteDB backup errors by resolving yb_backup failures, fixing S3 upload issues, and handling backup timeout problems"
tools: ["yugabyte"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# YugabyteDB Backup Error

YugabyteDB backup errors occur when using yb_backup, YugabyteDB Backup Utility, or manual backup procedures to create data backups.

## Why It Happens

- yb_backup cannot connect to Master or TServer
- S3/GCS/Azure storage credentials are incorrect
- Backup exceeds timeout limits
- Insufficient disk space for temporary backup files
- Backup encounters locked tables
- Network timeout during large backup uploads

## Common Error Messages

```
ERROR: backup failed - connection timeout
```

```
ERROR: S3 upload failed - access denied
```

```
ERROR: backup exceeded time limit
```

```
ERROR: could not create backup snapshot
```

## How to Fix It

### 1. Run yb_backup Correctly

```bash
# Basic backup
yb_backup --master_addresses yb-master-1:7100,yb-master-2:7100,yb-master-3:7100 \\
  --keyspace mykeyspace \\
  --output_dir /backup/yugabyte

# Backup to S3
yb_backup --master_addresses yb-master-1:7100 \\
  --keyspace mykeyspace \\
  --s3bucket s3://my-backups \\
  --s3region us-east-1 \\
  --output_dir /backup/yugabyte
```

### 2. Fix S3 Credentials

```bash
# Set AWS credentials
export AWS_ACCESS_KEY_ID=AKIA...
export AWS_SECRET_ACCESS_KEY=...

# Or use IAM role (recommended)
# Ensure EC2 instance has proper IAM role attached

# Test S3 access
aws s3 ls s3://my-backups/
```

### 3. Fix Backup Timeout

```bash
# Increase timeout for large backups
yb_backup --master_addresses yb-master-1:7100 \\
  --keyspace mykeyspace \\
  --snapshot_id backup_$(date +%Y%m%d) \\
  --timeout 3600
```

### 4. Monitor Backup Progress

```bash
# Check backup status
ls -la /backup/yugabyte/

# Check S3 backup
aws s3 ls s3://my-backups/ --recursive | tail -20

# Monitor backup in Master logs
grep "backup" /home/yugabyte/yugabyte-data/master/logs/yb-master.INFO | tail -10
```

## Common Scenarios

- **Backup times out on large tables**: Increase timeout and ensure network stability.
- **S3 upload fails**: Check IAM permissions and bucket policy.
- **Backup disk full**: Ensure sufficient temporary space for snapshot data.

## Prevent It

- Schedule regular backups with cron
- Test backup restoration periodically
- Monitor backup completion with alerts

## Related Pages

- [YugabyteDB Restore Error](/tools/yugabyte/yugabyte-restore-error)
- [YugabyteDB DR Error](/tools/yugabyte/yugabyte-dr-error)
- [YugabyteDB TServer Error](/tools/yugabyte/yugabyte-tserver-error)
