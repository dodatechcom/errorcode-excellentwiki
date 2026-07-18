---
title: "[Solution] CouchDB Disk Error — How to Fix"
description: "Fix CouchDB disk errors by freeing storage, configuring disk thresholds, and resolving no_space_left_on_device failures"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Disk Error

CouchDB disk errors occur when the database runs out of storage space or encounters file system issues. CouchDB requires adequate disk space for writes, compaction, and view building.

## Why It Happens

- Disk space is exhausted (no_space_left_on_device)
- Disk I/O errors on the storage device
- Inode exhaustion despite free disk space
- CouchDB data directory permissions are incorrect
- Compaction fails due to insufficient temporary space
- WAL (write-ahead log) grows unbounded

## Common Error Messages

```
{ "error": "io_error", "reason": "no space left on device" }
```

```
{ "error": "io_error", "reason": "Permission denied" }
```

```
{ "error": "internal_server_error", "reason": "compaction_failed" }
```

```
{ "error": "io_error", "reason": "enomem" }
```

## How to Fix It

### 1. Check and Free Disk Space

```bash
# Check disk usage
df -h /opt/couchdb/data

# Find large databases
du -sh /opt/couchdb/data/*.couch | sort -rh | head -10

# Find large attachments
find /opt/couchdb/data -name "*.couch" -size +1G
```

### 2. Compact Databases

```bash
# Compact a specific database
curl -X POST http://localhost:5984/mydb/_compact

# Compact all databases
for db in $(curl -s http://localhost:5984/_all_dbs | jq -r '.[]'); do
  curl -X POST "http://localhost:5984/${db}/_compact"
done

# Compact views
curl -X POST http://localhost:5984/mydb/_view_compact \
  -H "Content-Type: application/json" \
  -d '{"stale": false}'
```

### 3. Configure Disk Threshold

```ini
; In local.ini
[couchdb]
; Stop accepting writes when free disk drops below this (bytes)
; Default: 0 (disabled)
free_disk_space = 1073741824  ; 1GB

; Max database size before warning
max_dbs_size = 100  ; in MB
```

### 4. Fix Permission Issues

```bash
# Check CouchDB data directory ownership
ls -la /opt/couchdb/data/

# Fix permissions
sudo chown -R couchdb:couchdb /opt/couchdb/data/
sudo chmod -R 755 /opt/couchdb/data/

# Verify CouchDB user
id couchdb
```

```bash
# Restart CouchDB after permission fix
sudo systemctl restart couchdb
```

## Common Scenarios

- **Writes fail with no_space**: Run `_compact` on all databases and archive old data.
- **View build fails on disk**: Ensure temp directory has enough space for view index files.
- **Docker CouchDB fills container disk**: Mount a volume for `/opt/couchdb/data`.

## Prevent It

- Set up disk usage monitoring with alerts at 80% and 90% thresholds
- Schedule regular compaction jobs via cron
- Use separate volumes for data and view indexes in production

## Related Pages

- [CouchDB Compaction Error](/tools/couchdb/couchdb-compaction-error)
- [CouchDB Node Error](/tools/couchdb/couchdb-node-error)
- [CouchDB Cluster Error](/tools/couchdb/couchdb-cluster-error)
