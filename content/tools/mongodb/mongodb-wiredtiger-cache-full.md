---
title: "[Solution] MongoDB WiredTiger Cache Full Error"
description: "Fix MongoDB WiredTiger cache full and eviction errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB WiredTiger Cache Full Error

```
WiredTiger error: cache eviction thread timed out
```

```
Cache capacity: 95% full
```

## Common Causes

- The cache is at or near capacity
- Heavy write load causing cache pressure
- Large documents evicting other useful pages
- Insufficient RAM for the working set

## How to Fix

### 1. Monitor cache usage

```javascript
db.serverStatus().wiredTiger.cache
```

Key metrics:
- `bytes currently in the cache`: current usage
- `maximum bytes configured`: max cache size
- `tracked dirty bytes in the cache`: dirty data waiting to be written

### 2. Adjust cache size

```yaml
# /etc/mongod.conf
storage:
  wiredTiger:
    engineConfig:
      cacheSizeGB: 4  # Set to ~60% of available RAM
```

### 3. Reduce write pressure

- Use bulk writes instead of individual inserts
- Reduce the frequency of writes
- Use write concern `{ w: 1 }` for non-critical writes

### 4. Check for large operations

```javascript
db.currentOp({ active: true, secs_running: { $gt: 10 } })
```

## Examples

```bash
# Check cache stats
mongosh --eval "db.serverStatus().wiredTiger.cache"

# Check eviction activity
mongosh --eval "db.serverStatus().wiredTiger.cache['eviction server candidate cache hit count']"

# Check dirty cache
mongosh --eval "db.serverStatus().wiredTiger.cache['tracked dirty bytes in the cache']"
```