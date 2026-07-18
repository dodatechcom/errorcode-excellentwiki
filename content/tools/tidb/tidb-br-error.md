---
title: "[Solution] TiDB BR Error — How to Fix"
description: "Fix TiDB Backup & Restore errors by resolving BR tool failures, fixing backup corruption, and handling restore validation issues"
tools: ["tidb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# TiDB BR Error

TiDB BR (Backup & Restore) errors occur when the BR tool fails during backup, restore, or log operations. BR is the primary backup tool for TiDB.

## Why It Happens

- BR version is incompatible with TiDB cluster
- BR cannot connect to PD or TiKV
- Backup data is corrupted or incomplete
- BR encounters lock contention during backup
- BR process runs out of memory
- Storage backend is not accessible

## Common Error Messages

```
ERROR: BR version mismatch
```

```
ERROR: cannot connect to PD
```

```
ERROR: backup data corrupted
```

```
ERROR: BR out of memory
```

## How to Fix It

### 1. Check BR Version

```bash
# Check BR version
br --version

# Ensure BR version matches TiDB cluster
# BR version should be >= TiDB cluster version
mysql -h tidb1 -P 4000 -u root -e "SELECT tidb_version()"
```

### 2. Fix BR Connection Issues

```bash
# Test PD connectivity
curl http://pd1:2379/pd/api/v1/cluster/status

# Run BR with verbose logging
br backup full \\
  --pd pd1:2379 \\
  --storage local:///backup/tidb \\
  --log-file /var/log/br.log
```

### 3. Fix Backup Corruption

```bash
# Verify backup integrity
br validate \\
  --storage s3://my-bucket/tidb-backup

# Check backup metadata
br log --storage s3://my-bucket/tidb-backup | head -20
```

### 4. Optimize BR Performance

```bash
# Increase concurrency for faster backup
br backup full \\
  --pd pd1:2379 \\
  --storage s3://my-bucket/tidb-backup \\
  --concurrency 16

# Increase memory limit
br backup full \\
  --pd pd1:2379 \\
  --storage s3://my-bucket/tidb-backup \\
  --send-credentials-to-tikv=true
```

## Common Scenarios

- **BR version mismatch**: Download matching BR version for your TiDB cluster.
- **BR backup is slow**: Increase concurrency and ensure network stability.
- **BR restore fails**: Check backup integrity and version compatibility.

## Prevent It

- Use BR version that matches TiDB cluster version
- Test backup and restore regularly
- Monitor BR operations with log files

## Related Pages

- [TiDB Backup Error](/tools/tidb/tidb-backup-error)
- [TiDB Restore Error](/tools/tidb/tidb-restore-error)
- [TiDB TiKV Error](/tools/tidb/tidb-tikv-error)
