---
title: "[Solution] MongoDB Shard Too Large Error"
description: "Fix MongoDB shard too large or unbalanced shard errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Shard Too Large Error

A shard becomes too large when it has significantly more data than others:

```
// Shard1: 500GB, Shard2: 50GB - unbalanced
```

## Common Causes

- The shard key has low cardinality
- Chunk splits are not happening correctly
- The balancer cannot move chunks efficiently
- Hot spots in the data distribution

## How to Fix

### 1. Choose a better shard key

```javascript
// Bad shard key with low cardinality
sh.shardCollection("mydb.orders", { country: 1 });

// Better: higher cardinality key
sh.shardCollection("mydb.orders", { userId: 1 });
```

### 2. Use a hashed shard key for even distribution

```javascript
sh.shardCollection("mydb.orders", { userId: "hashed" });
```

### 3. Check current distribution

```javascript
sh.getShardDistribution()
```

### 4. Split and move chunks manually

```javascript
sh.splitAt("mydb.orders", { userId: 500 });
sh.moveChunk("mydb.orders", { userId: 250 }, "shard2");
```

## Examples

```bash
# Check shard distribution
mongosh --eval "sh.getShardDistribution()"

# Find the shard with most data
mongosh --eval '
  let dist = sh.getShardDistribution();
  Object.keys(dist).forEach(shard => {
    print(shard, "data:", dist[shard].data, "docs:", dist[shard].docs);
  });
'
```