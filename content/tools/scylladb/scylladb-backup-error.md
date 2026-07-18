---
title: "[Solution] ScyllaDB Backup Error — How to Fix"
description: "Fix ScyllaDB backup errors by resolving snapshot failures, fixing S3 upload issues, and recovering from incomplete backups"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Backup Error

ScyllaDB backup errors occur when snapshot creation, data export, or backup upload operations fail. Regular backups are essential for data recovery.

## Why It Happens

- Snapshot creation fails due to insufficient disk space
- Backup script cannot access SSTable files
- S3 upload fails due to network issues or permissions
- Snapshot directory is not writable
- Backup process is interrupted by node restart
- SSTable format incompatibility between backup and restore

## Common Error Messages

```
SnapshotError: Failed to create snapshot
```

```
IOError: Unable to create snapshot directory
```

```
BackupError: Backup upload failed
```

```
S3Error: Access Denied when uploading to S3
```

## How to Fix It

### 1. Create Snapshot Manually

```bash
# Create snapshot
nodetool snapshot mykeyspace -t backup_$(date +%Y%m%d)

# List snapshots
nodetool listsnapshots

# Verify snapshot
ls -la /var/lib/scylla/data/mykeyspace/mytable-uuid/snapshots/

# Clean old snapshots
nodetool clearsnapshot -t backup_20240101
```

### 2. Backup to S3

```bash
#!/bin/bash
# backup_scylla.sh
SNAPSHOT_NAME="backup_$(date +%Y%m%d_%H%M%S)"
S3_BUCKET="s3://my-scylla-backups"
DATA_DIR="/var/lib/scylla/data"

# Create snapshot
nodetool snapshot mykeyspace -t $SNAPSHOT_NAME

# Upload to S3
for table_dir in $DATA_DIR/mykeyspace/*/snapshots/$SNAPSHOT_NAME; do
  aws s3 cp "$table_dir" "$S3_BUCKET/$SNAPSHOT_NAME/" --recursive
done

# Verify upload
aws s3 ls "$S3_BUCKET/$SNAPSHOT_NAME/" | wc -l

# Clean local snapshot after successful upload
nodetool clearsnapshot -t $SNAPSHOT_NAME
```

### 3. Fix Snapshot Permission Issues

```bash
# Check data directory permissions
ls -la /var/lib/scylla/data/

# Fix permissions
sudo chown -R scylla:scylla /var/lib/scylla/data/
sudo chmod -R 755 /var/lib/scylla/data/

# Create snapshot directory if missing
sudo -u scylla mkdir -p /var/lib/scylla/data/mykeyspace/snapshots/

# Test snapshot creation
nodetool snapshot mykeyspace -t test_snapshot
```

### 4. Restore from Backup

```bash
# Stop ScyllaDB
sudo systemctl stop scylla-server

# Clear existing data (CAUTION)
rm -rf /var/lib/scylla/data/mykeyspace/*

# Copy snapshot data back
cp -r /backup/mykeyspace/* /var/lib/scylla/data/mykeyspace/

# Fix permissions
sudo chown -R scylla:scylla /var/lib/scylla/data/mykeyspace/

# Start ScyllaDB
sudo systemctl start scylla-server

# Verify data
nodetool status mykeyspace
```

## Common Scenarios

- **Snapshot fails with no space**: Clean old snapshots first or add disk space.
- **S3 upload times out**: Use `aws s3 multipart` for large uploads.
- **Restore fails with format error**: Ensure backup was taken from same ScyllaDB version.

## Prevent It

- Automate backup verification by restoring to a test environment
- Monitor backup job completion with alerts
- Keep at least 7 days of backup retention

## Related Pages

- [ScyllaDB SSTable Error](/tools/scylladb/scylladb-sstable-error)
- [ScyllaDB Disk Error](/tools/scylladb/scylladb-disk-error)
- [ScyllaDB Import Error](/tools/scylladb/scylladb-import-error)
