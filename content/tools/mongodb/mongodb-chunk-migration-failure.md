---
title: "[Solution] MongoDB Chunk Migration Failure"
description: "Fix MongoDB chunk migration errors in sharded cluster"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Chunk Migration Failure

```
Migration failed for chunk ...
```

```
chunk migration failed: write conflict
```

## Common Causes

- The destination shard does not have enough resources
- Network connectivity between shards is lost
- The chunk is too large to migrate
- Write conflicts during migration
- The balancer lock was lost

## How to Fix

### 1. Check chunk sizes

```javascript
sh.status()
```

### 2. Split large chunks manually

```javascript
sh.splitAt("mydb.orders", { userId: 500 });
```

### 3. Check shard disk space

```bash
ssh shard1 "df -h /var/lib/mongodb"
ssh shard2 "df -h /var/lib/mongodb"
```

### 4. Move chunks manually

```javascript
sh.moveChunk("mydb.orders", { userId: 100 }, "shard2");
```

## Examples

```bash
# Check chunk distribution
mongosh --eval "sh.status()"

# Split a chunk manually
mongosh --eval 'sh.splitAt("mydb.orders", {userId:1000})'

# Move a specific chunk
mongosh --eval 'sh.moveChunk("mydb.orders", {userId:500}, "shard2")'
```