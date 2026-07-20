---
title: "[Solution] MongoDB Working Set Exceeded Error"
description: "Fix MongoDB working set size exceeded errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Working Set Exceeded Error

```
// Working set size exceeds available memory
// This causes performance degradation
```

## Common Causes

- The frequently accessed data exceeds available RAM
- Large collections with random access patterns
- Indexes are too large to fit in memory
- Inefficient queries causing full collection scans

## How to Fix

### 1. Monitor the working set size

```javascript
db.serverStatus().wiredTiger.cache
```

### 2. Increase the WiredTiger cache size

```yaml
# /etc/mongod.conf
storage:
  wiredTiger:
    engineConfig:
      cacheSizeGB: 8  # Adjust based on available RAM
```

### 3. Optimize query patterns

```javascript
// Use covered queries to reduce data loading
db.users.find({ email: "test@example.com" }, { _id: 0, email: 1 });
```

### 4. Shard the collection to distribute the working set

```javascript
sh.shardCollection("mydb.largeCollection", { userId: 1 });
```

### 5. Use compression

```yaml
storage:
  wiredTiger:
    collectionConfig:
      blockCompressor: snappy
```

## Examples

```bash
# Check cache usage
mongosh --eval "db.serverStatus().wiredTiger.cache"

# Check which collections are largest
mongosh --eval '
  db.getCollectionNames().forEach(coll => {
    let stats = db[coll].stats();
    print(coll, ":", (stats.size / 1024 / 1024).toFixed(2), "MB");
  });
'

# Check index sizes
mongosh --eval '
  db.getCollectionNames().forEach(coll => {
    let stats = db[coll].stats();
    print(coll, "indexSize:", (stats.totalIndexSize / 1024 / 1024).toFixed(2), "MB");
  });
'
```