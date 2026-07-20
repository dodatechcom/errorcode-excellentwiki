---
title: "[Solution] MongoDB Page Fault Spike Error"
description: "Fix MongoDB excessive page fault errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Page Fault Spike Error

Page faults occur when MongoDB accesses data not in memory:

```
// Detected via monitoring
// page_faults: 15000 (high)
```

## Common Causes

- Working set exceeds available RAM
- The storage engine needs more memory for caching
- Large sequential scans evict hot data
- Too many collections with indexes not fitting in memory

## How to Fix

### 1. Monitor page faults

```javascript
db.serverStatus().extra_info.pageFaults
```

### 2. Increase RAM

The working set should fit in RAM for optimal performance.

### 3. Create indexes to reduce full collection scans

```javascript
db.users.createIndex({ email: 1 });  // Prevents full scan
```

### 4. Use the storage engine cache size

```yaml
# /etc/mongod.conf
storage:
  wiredTiger:
    engineConfig:
      cacheSizeGB: 4  # Set to ~60% of available RAM
```

### 5. Monitor WiredTiger cache usage

```javascript
db.serverStatus().wiredTiger.cache
```

## Examples

```bash
# Check page faults
mongosh --eval "db.serverStatus().extra_info.pageFaults"

# Check cache usage
mongosh --eval "db.serverStatus().wiredTiger.cache"

# Check memory usage
free -h
```