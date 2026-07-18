---
title: "[Solution] TiDB Restore Error — How to Fix"
description: "Fix TiDB restore errors by resolving BR restore failures, fixing point-in-time recovery, and handling restore version mismatches"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB Restore Error

TiDB restore errors occur when restoring from BR backups or performing point-in-time recovery (PITR). Restore failures can be caused by version mismatches or storage issues.

## Why It Happens

- BR restore cannot access backup data
- Backup was created with incompatible TiDB version
- Restore exceeds timeout limits
- Target cluster has insufficient capacity
- WAL logs for PITR are not available
- Storage credentials are incorrect

## Common Error Messages

```
ERROR: restore failed - backup not found
```

```
ERROR: version mismatch between backup and restore
```

```
ERROR: restore timeout
```

```
ERROR: insufficient capacity for restore
```

## How to Fix It

### 1. Run BR Restore

```bash
# Full restore
br restore full \\
  --pd pd1:2379 \\
  --storage s3://my-bucket/tidb-backup \\
  --send-credentials-to-tikv=true

# Restore specific database
br restore db \\
  --pd pd1:2379 \\
  --db mydb \\
  --storage s3://my-bucket/tidb-backup
```

### 2. Fix Version Mismatch

```bash
# Check backup version
br log --storage s3://my-bucket/tidb-backup | grep version

# Check current cluster version
mysql -h tidb1 -P 4000 -u root -e "SELECT tidb_version()"

# Use same or newer BR version for restore
```

### 3. Point-in-Time Recovery

```bash
# Restore to specific timestamp
br restore point \\
  --pd pd1:2379 \\
  --storage s3://my-bucket/tidb-backup \\
  --lastbackupts \$(date -d '2024-01-15 10:00:00' +%s)000 \\
  --send-credentials-to-tikv=true
```

### 4. Monitor Restore Progress

```bash
# Check restore progress
br log \\
  --pd pd1:2379 \\
  --storage s3://my-bucket/tidb-backup

# Monitor TiKV during restore
curl http://tikv1:20180/metrics | grep restore
```

## Common Scenarios

- **Restore times out**: Increase timeout and ensure network stability.
- **Version mismatch**: Use compatible BR version for restore.
- **PITR fails**: Ensure WAL logs are available for the recovery window.

## Prevent It

- Keep BR version consistent with cluster version
- Test restore procedures regularly
- Monitor restore progress with br log

## Related Pages

- [TiDB Backup Error](/tools/tidb/tidb-backup-error)
- [TiDB BR Error](/tools/tidb/tidb-br-error)
- [TiDB TiKV Error](/tools/tidb/tidb-tikv-error)
