---
title: "[Solution] MongoDB Compact Command Failed Error"
description: "Fix MongoDB compact command failed error when storage compaction or defragmentation encounters issues"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Compact Command Failed Error

The compact command fails when MongoDB cannot defragment the storage for a collection or index. This commonly affects WiredTiger collections with heavy fragmentation.

## Common Causes

- Not enough free disk space for compaction temporary files
- Collection is too large and compaction times out
- WiredTiger cache is under pressure during compaction
- Replica set member is in a degraded state
- Compact was run on a sharded collection directly instead of per-shard

## How to Fix

### Check Available Disk Space

```javascript
db.adminCommand({ dbStats: 1 })
db.adminCommand({ collStats: 'orders' })
```

### Compact on the Primary

```javascript
// WiredTiger compaction
db.runCommand({ compact: 'orders' })

// Compact with padding (use with caution)
db.runCommand({ compact: 'orders', force: true })
```

### Monitor Compaction Progress

```javascript
// Check WiredTiger cache statistics
db.serverStatus().wiredTiger.cache

// Monitor disk usage during compaction
db.adminCommand({ serverStatus: 1 }).wiredTiger
```

### Schedule During Low Traffic

```javascript
// Schedule compaction during maintenance window
// Use the compactionSchedule in MongoDB Atlas or cron
use admin
db.adminCommand({
  configureCollectionBalancing: 'mydb.orders',
  chunkSize: 64
})
```

## Examples

```
MongoServerError: cannot compact collection -- not enough free disk space
  require 2.5GB but only 1.2GB available

MongoServerError: compact failed: {
  "ok": 0,
  "errmsg": "cannot compact collection with an index",
  "code": 10107
}
```

## Related Errors

- [MongoDB No Free Disk Space]({{< relref "/tools/mongodb/mongodb-no-free-disk-space" >}}) -- disk full
- [MongoDB WiredTiger Cache Full]({{< relref "/tools/mongodb/mongodb-wiredtiger-cache-full" >}}) -- cache pressure
- [MongoDB Index Build Failed]({{< relref "/tools/mongodb/mongodb-index-build-failed" >}}) -- index operations
