---
title: "[Solution] CouchDB Compaction Disk Error — How to Fix"
description: "Fix CouchDB compaction disk errors by resolving disk space issues during compaction, fixing disk I/O problems, and handling compaction storage failures"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Compaction Disk Error

CouchDB compaction disk errors occur when compaction fails due to insufficient disk space, slow disk I/O, or disk corruption.

## Why It Happens

- Disk space is insufficient for compaction
- Disk I/O is too slow
- Disk is full during compaction
- Disk corruption detected
- File system is read-only
- Disk quota exceeded

## Common Error Messages

```
{ "error": "internal_server_error", "reason": "Insufficient disk space for compaction" }
```

```
{ "error": "internal_server_error", "reason": "Disk I/O error during compaction" }
```

```
{ "error": "internal_server_error", "reason": "Disk quota exceeded" }
```

```
{ "error": "internal_server_error", "reason": "File system read-only" }
```

## How to Fix It

### 1. Check Disk Space

```bash
# Check available disk space
df -h /opt/couchdb/data

# Check CouchDB data directory size
du -sh /opt/couchdb/data

# Check shard sizes
du -sh /opt/couchdb/data/shards/*
```

### 2. Free Disk Space

```bash
# Delete old backups
rm -f /opt/couchdb/backups/*.tar.gz

# Delete unused databases
curl -X DELETE http://localhost:5984/old_database

# Compact after freeing space
curl -X POST http://localhost:5984/mydb/_compact

# Clean up temp files
find /opt/couchdb/data -name "*.compact*" -delete
```

### 3. Fix Disk I/O Issues

```bash
# Check disk I/O performance
iostat -x 1 5

# Check for disk errors
dmesg | grep -i "error\|fault\|bad"

# Run disk check
sudo fsck /dev/sda1
```

### 4. Move Data to Larger Disk

```bash
# Stop CouchDB
sudo systemctl stop couchdb

# Move data directory
sudo mv /opt/couchdb/data /new/path/data

# Update configuration
sudo sed -i 's|/opt/couchdb/data|/new/path/data|' /opt/couchdb/etc/local.ini

# Start CouchDB
sudo systemctl start couchdb
```

## Common Scenarios

- **Disk full during compaction**: Free space or move to larger disk.
- **Disk I/O slow**: Upgrade to faster storage (SSD).
- **Disk corruption**: Run disk check and restore from backup.

## Prevent It

- Monitor disk space regularly
- Use fast storage for CouchDB data
- Schedule compaction when disk is not busy

## Related Pages

- [CouchDB Compaction Error](/tools/couchdb/couchdb-compaction-error)
- [CouchDB Disk Error](/tools/couchdb/couchdb-disk-error)
- [CouchDB Storage Error](/tools/couchdb/couchdb-storage-error)
