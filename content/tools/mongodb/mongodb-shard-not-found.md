---
title: "[Solution] MongoDB Shard Not Found Error"
description: "Fix MongoDB shard not found errors in sharded cluster"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Shard Not Found Error

```
MongoServerError: shard <shard_name> was not found
```

## Common Causes

- The shard was removed from the cluster
- The config servers have stale data
- The shard name in the connection string is wrong
- The shard was never added to the cluster

## How to Fix

### 1. Add the shard to the cluster

```javascript
sh.addShard("shard1/mongo-shard1:27017");
```

### 2. Check current shards

```javascript
sh.status()
// or
db.adminCommand({ listShards: 1 })
```

### 3. Verify the config server is healthy

```bash
mongosh --host config1:27017 --eval "db.adminCommand({listShards:1})"
```

## Examples

```bash
# List all shards in the cluster
mongosh --eval "sh.status()"

# Add a new shard
mongosh --eval 'sh.addShard("shard2/mongo-shard2:27017")'

# Check which shard a collection is on
mongosh --eval "db.orders.getShardDistribution()"
```