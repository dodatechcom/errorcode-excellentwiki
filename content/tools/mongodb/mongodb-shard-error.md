---
title: "MongoDB Shard Error"
description: "MongoDB sharded cluster encounters issues with shard balancing or chunk migration."
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
tags: ["mongodb", "shard", "cluster", "balancer", "chunk"]
weight: 5
---

# MongoDB Shard Error

A MongoDB shard error occurs when the sharded cluster encounters issues with shard balancing, chunk migration, or chunk distribution. This affects data distribution across shards.

## Common Causes

- Shard is unavailable or unreachable
- Balancer is stopped or failing
- Chunks not distributed evenly
- Shard key causes hotspot

## How to Fix

### Check Cluster Status

```javascript
sh.status()
```

### Check Shard Health

```javascript
db.adminCommand({ listShards: 1 })
```

### Enable Balancer

```javascript
sh.enableBalancing('mydb.collection')
```

### Check Balancer Status

```javascript
sh.isBalancerRunning()
```

### Move Chunk Manually

```javascript
sh.moveChunk('mydb.collection', { shardKey: 'value' }, 'shard2')
```

### Fix Shard Key Issues

```javascript
// Choose a good shard key
sh.shardCollection('mydb.collection', { userId: 1, timestamp: 1 })
```

## Examples

```javascript
// Shard unavailable
sh.status()
// shard1: DOWN

// Balancer not running
sh.isBalancerRunning()  // false
sh.startBalancer()
```

## Related Errors

- [Connection Error]({{< relref "/tools/mongodb/mongodb-connection-error" >}}) — connection failure
- [Replica Set Error]({{< relref "/tools/mongodb/mongodb-replica-set-error" >}}) — replica set issue
