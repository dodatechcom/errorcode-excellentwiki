---
title: "MongoDB - index build failed - disk full"
description: "MongoDB index creation fails because the disk does not have enough space to complete the build operation"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
tags: ["mongodb", "index", "build", "disk", "storage", "space"]
weight: 5
---

An index build failed disk full error occurs when MongoDB cannot create or rebuild an index because there is insufficient disk space on the data volume. This can happen during initial index creation, index rebuilds after a crash, or during compaction.

## Common Causes

- Disk space exhausted on the data volume
- Large collection requires more temporary space than available
- Journal files consuming additional disk space
- Multiple index builds running simultaneously
- WiredTiger cache consuming memory-mapped space

## How to Fix

1. Check available disk space:

```bash
df -h /var/lib/mongodb
du -sh /var/lib/mongodb/*
```

2. Free up disk space:

```bash
# Remove old log files
find /var/log/mongodb -name "*.log" -mtime +30 -delete

# Compact collection to reclaim space
db.runCommand({ compact: 'collectionName' })

# Drop unused indexes
db.collection.dropIndex('unused_index_1')
```

3. Create indexes in the background to minimize impact:

```javascript
await db.collection('largeCollection').createIndex(
  { field: 1 },
  { background: true }
);
```

4. Use `maxDiskUse` to limit index build space:

```javascript
await db.collection('largeCollection').createIndex(
  { field: 1 },
  { maxDiskUse: 50 * 1024 * 1024 * 1024 } // 50GB limit
);
```

5. Monitor disk usage during index builds:

```bash
# Watch disk usage
watch -n 5 'df -h /var/lib/mongodb'
```

6. Drop and recreate indexes if space is critically low:

```javascript
// Drop first to free space, then recreate
await db.collection('logs').dropIndex('timestamp_1');
await db.collection('logs').createIndex({ timestamp: 1 });
```

## Examples

```javascript
// Error: Index build failed. Reason: [CannotIndex]磁盘上没有足够的空间
await db.collection('events').createIndex({ timestamp: 1, userId: 1 });
// PlanExecutor error during stage BUILD_INDEXES: error processing query:
// cannot build index: not enough disk space

// Fix: free space first
db.runCommand({ compact: 'events' });
await db.collection('events').createIndex({ timestamp: 1, userId: 1 });
```

## Related Errors

- [Index error]({{< relref "/tools/mongodb/mongodb-index-error" >}})
- [Write error]({{< relref "/tools/mongodb/mongodb-write-error-v2" >}})
