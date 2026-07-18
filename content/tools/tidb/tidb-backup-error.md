---
title: "[Solution] TiDB Backup Error — How to Fix"
description: "Fix TiDB backup errors by resolving BR backup failures, fixing S3 upload issues, and handling incremental backup problems"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Backup Error

TiDB backup errors occur when using Backup & Restore (BR) tool or SQL-based backups. BR is the recommended backup tool for TiDB clusters.

## Why It Happens

- BR cannot connect to PD or TiKV
- Backup exceeds timeout limits
- S3/GCS storage credentials are incorrect
- Backup disk space is insufficient
- Backup encounters lock contention
- Incremental backup fails due to missing base

## Common Error Messages

```
ERROR: backup failed - PD not reachable
```

```
ERROR: S3 upload failed
```

```
ERROR: backup timeout
```

```
ERROR: backup disk space insufficient
```

## How to Fix It

### 1. Run BR Backup

```bash
# Full backup
br backup full \\
  --pd pd1:2379 \\
  --storage s3://my-bucket/tidb-backup \\
  --send-credentials-to-tikv=true

# Backup specific database
br backup db \\
  --pd pd1:2379 \\
  --db mydb \\
  --storage s3://my-bucket/tidb-backup
```

### 2. Fix BR Connection Issues

```bash
# Ensure PD is accessible
curl http://pd1:2379/pd/api/v1/cluster/status

# Check BR version compatibility
br --version

# Test backup to local storage first
br backup full \\
  --pd pd1:2379 \\
  --storage local:///backup/tidb
```

### 3. Fix S3 Credentials

```bash
# Set AWS credentials
export AWS_ACCESS_KEY_ID=AKIA...
export AWS_SECRET_ACCESS_KEY=...

# Test S3 access
aws s3 ls s3://my-bucket/

# Use send-credentials-to-tikv for backup
br backup full \\
  --pd pd1:2379 \\
  --storage s3://my-bucket/tidb-backup \\
  --send-credentials-to-tikv=true
```

### 4. Monitor Backup Progress

```bash
# Check backup progress
br log \\
  --pd pd1:2379 \\
  --storage s3://my-bucket/tidb-backup

# Monitor TiKV during backup
curl http://tikv1:20180/metrics | grep backup
```

## Common Scenarios

- **BR backup times out**: Increase timeout and ensure network stability.
- **S3 upload fails**: Check IAM permissions and bucket policy.
- **Backup is slow**: Increase backup concurrency with --concurrency flag.

## Prevent It

- Schedule regular backups with BR
- Test backup restoration periodically
- Monitor backup completion with alerts

## Related Pages

- [TiDB Restore Error](/tools/tidb/tidb-restore-error)
- [TiDB BR Error](/tools/tidb/tidb-br-error)
- [TiDB TiKV Error](/tools/tidb/tidb-tikv-error)
