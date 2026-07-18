---
title: "Fix Vitess Backup Error — How to Fix"
description: "Resolve Vitess backup errors by checking storage and backup configuration"
tools: ["vitess"]
error-types: ["vitess-backup-error"]
severities: ["warning"]
weight: 13
comments:
  - "Check backup storage"
  - "Verify backup credentials"
---

# Vitess Backup Error — How to Fix

## Why It Happens

Backup errors occur when Vitess cannot create or store backups due to storage issues, permission problems, or configuration errors in the backup system.

## Common Error Messages

- `backup error: failed to create backup`
- `backup error: storage not accessible`
- `backup error: permission denied`
- `backup error: disk space full`

## How to Fix It

### 1. Check backup storage accessibility

Verify backup storage is available:

```bash
# Check storage mount
df -h /backup

# Test storage access
touch /backup/test_write && rm /backup/test_write

# Check storage credentials
cat /etc/vitess/backup-storage.json
```

### 2. Verify backup permissions

Check file permissions:

```bash
# Check backup directory permissions
ls -la /backup/

# Fix permissions if needed
chmod 755 /backup
chown vitess:vitess /backup
```

### 3. Check disk space

Ensure sufficient storage space:

```bash
# Check available space
df -h

# Clean old backups if needed
find /backup -name "*.gz" -mtime +30 -delete
```

### 4. Test backup creation

Try creating a manual backup:

```bash
# Create backup
vtctldclient backup --server localhost:15999 <tablet-alias>

# Check backup status
vtctldclient list_backups --server localhost:15999 <keyspace>/<shard>
```

## Common Scenarios

**Scenario 1: S3 credentials expired**

If using S3 for backups:

```bash
# Check AWS credentials
aws sts get-caller-identity

# Refresh credentials if needed
aws configure
```

**Scenario 2: Backup compression failed**

If backup compression fails:

```bash
# Check available memory
free -m

# Increase compression memory if needed
export GOGC=200
```

## Prevent It

1. Monitor backup storage space
2. Test backups regularly
3. Set up backup rotation policy

## Related Pages

- [Vitess Restore Error](vitess-restore-error)
- [Vitess Tablet Error](vitess-tablet-error)
- [Vitess Shard Error](vitess-shard-error)
