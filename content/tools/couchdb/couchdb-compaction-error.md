---
title: "[Solution] CouchDB Compaction Error — How to Fix"
description: "Fix CouchDB compaction errors by resolving disk space issues, fixing corrupted databases, and tuning compaction thresholds"
tools: ["couchdb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# CouchDB Compaction Error

CouchDB compaction errors occur when the database cannot reclaim disk space by rewriting b-tree files. Compaction is essential for keeping CouchDB performant and space-efficient.

## Why It Happens

- Insufficient disk space for temporary compaction files
- Database file is corrupted or has integrity issues
- Compaction is interrupted by restart or crash
- View compaction fails due to corrupted view index
- Concurrent writes during compaction cause conflicts
- Compaction threshold is too low, triggering excessive compaction

## Common Error Messages

```
{ "error": "internal_server_error", "reason": "compaction_failed" }
```

```
{ "error": "io_error", "reason": "compaction file write error" }
```

```
{ "error": "internal_server_error", "reason": "db_needs_compaction" }
```

```
{ "error": "bad_request", "reason": "database is already compacted" }
```

## How to Fix It

### 1. Ensure Adequate Disk Space

```bash
# Compaction needs roughly 2x the current database size
du -sh /opt/couchdb/data/mydb.couch

# Check available space
df -h /opt/couchdb/data

# Ensure at least 2x database size is free
# If DB is 5GB, need at least 10GB free during compaction
```

### 2. Manual Compaction with Cleanup

```bash
# Stop CouchDB and compact offline
sudo systemctl stop couchdb

# Use couch_compact tool
/opt/couchdb/bin/couch_compact /opt/couchdb/data/mydb.couch

# Or use the HTTP API
curl -X POST http://localhost:5984/mydb/_compact

# For views
curl -X POST http://localhost:5984/mydb/_view_compact \
  -H "Content-Type: application/json" \
  -d '{}'
```

### 3. Configure Compaction Thresholds

```ini
; In local.ini
[compactions]
; Only compact when fragmentation exceeds 20%
db_fragmentation = 20
; Only compact views when fragmentation exceeds 30%
view_fragmentation = 30
; Run compaction during off-peak hours
checkpoint_after = 86400000  ; 24 hours in milliseconds
```

```bash
# Check current compaction settings
curl http://localhost:5984/_node/_local/_config/compactions
```

### 4. Fix Corrupted Database Files

```bash
# Check database integrity
curl -X POST http://localhost:5984/mydb/_compact
# If this fails, the database may be corrupted

# Restore from backup
cp /backup/mydb.couch /opt/couchdb/data/mydb.couch

# Or force rebuild from replication
curl -X DELETE http://localhost:5984/mydb
curl -X PUT http://localhost:5984/mydb
# Then replicate from source
curl -X POST http://localhost:5984/_replicate \
  -H "Content-Type: application/json" \
  -d '{"source": "http://source:5984/mydb", "target": "http://localhost:5984/mydb"}'
```

## Common Scenarios

- **Compaction runs out of space**: Archive old databases or increase disk before compacting.
- **Compaction loop**: If a database constantly needs compaction, consider splitting it.
- **View compaction fails**: Rebuild the view index from scratch by deleting view files.

## Prevent It

- Schedule compaction during low-traffic periods
- Monitor fragmentation levels via `_stats` endpoint
- Set up automated compaction with appropriate thresholds

## Related Pages

- [CouchDB Disk Error](/tools/couchdb/couchdb-disk-error)
- [CouchDB View Error](/tools/couchdb/couchdb-view-error)
- [CouchDB Node Error](/tools/couchdb/couchdb-node-error)
