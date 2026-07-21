---
title: "[Solution] MongoDB Disk Usage Critical Error"
description: "Fix MongoDB disk usage critical error when the data directory runs low on available space"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Disk Usage Critical Error

The MongoDB data directory has critically low disk space. Operations fail when the server cannot write to data files, journal, or temporary files.

## Common Causes

- Data files have grown to fill available disk space
- Journal files consume excessive space due to unclean shutdowns
- Oplog has not been truncated and retains old entries
- Temporary aggregation files exceed available space
- Index builds require temporary disk space that is unavailable

## How to Fix

### Check Current Disk Usage

```javascript
// Check database sizes
db.adminCommand({ dbStats: 1 })

// Check collection sizes
db.getCollectionNames().forEach(name => {
  const stats = db.getCollection(name).stats();
  console.log(name, (stats.size / 1024 / 1024).toFixed(2) + 'MB');
});
```

### Drop Unused Collections and Indexes

```javascript
// Drop large temporary collections
db.temp_analytics.drop()

// Drop unused indexes
db.orders.dropIndex('legacy_status_idx')
```

### Enable TTL on Log Collections

```javascript
db.collection('access_logs').createIndex(
  { createdAt: 1 },
  { expireAfterSeconds: 2592000 }  // 30 days
)
```

### Compact to Reclaim Space

```javascript
// Compact a specific collection
db.runCommand({ compact: 'orders' })

// Check free space after compaction
db.collection('orders').stats()
```

### Monitor Disk Proactively

```bash
# Set up disk space alert
df -h /data/db
# Alert if usage exceeds 85%

# Find largest files
du -sh /data/db/* | sort -rh | head -20
```

## Examples

```
MongoServerError: Unable to write to data directory.
  No space left on device (ENOSPC)

MongoServerError: journal: write error while writing to journal
  No space left on device
```

## Related Errors

- [MongoDB No Free Disk Space]({{< relref "/tools/mongodb/mongodb-no-free-disk-space" >}}) -- disk full
- [MongoDB WiredTiger Cache Full]({{< relref "/tools/mongodb/mongodb-wiredtiger-cache-full" >}}) -- cache issues
- [MongoDB Oplog Full]({{< relref "/tools/mongodb/mongodb-oplog-full" >}}) -- oplog issues
