---
title: "[Solution] MongoDB Shard Key Cannot Change Error"
description: "Fix MongoDB shard key cannot change error when attempting to reshard a collection with an existing shard key"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Shard Key Cannot Change Error

Once a collection is sharded, the shard key cannot be changed. Attempting to modify, drop, or replace the shard key on an already sharded collection fails.

## Common Causes

- Application needs a different shard key after initial sharding
- Poor shard key choice caused hotspots or uneven data distribution
- Misunderstanding that shard key is immutable after sharding
- Attempting to update metadata directly to change the shard key
- Need to reshard due to schema evolution

## How to Fix

### Create a New Collection with the Correct Key

```javascript
// 1. Create new collection with the right shard key
db.createCollection('orders_v2')
sh.shardCollection('mydb.orders_v2', { customerId: 1, createdAt: -1 })

// 2. Copy data from old to new
db.orders.aggregate([
  { $match: {} },
  { $out: 'orders_v2' }
])

// 3. Verify data
db.orders_v2.countDocuments()
db.orders_v2.getShardDistribution()

// 4. Swap collections
db.orders.renameCollection('orders_old')
db.orders_v2.renameCollection('orders')

// 5. Drop old collection
db.orders_old.drop()
```

### Use Reshard Collection (MongoDB 5.0+)

```javascript
// Reshard in place (requires MongoDB 5.0+)
db.runCommand({
  reshardCollection: 'mydb.orders',
  key: { customerId: 1, region: 1 },  // new shard key
  numInitialChunks: 8                  // optional
})
```

### Prevent Future Issues with Smart Key Selection

```javascript
// Choose a shard key with:
// - High cardinality (many unique values)
// - Even distribution (avoid hotspots)
// - Query alignment (matches common query patterns)

sh.shardCollection('mydb.events', { eventType: 1, timestamp: -1 })
```

## Examples

```
MongoServerError: cannot change _id for a sharded collection
MongoServerError: After a collection has been sharded, the shard key
  cannot be changed. Use reshardCollection command (MongoDB 5.0+).
```

## Related Errors

- [MongoDB Shard Error]({{< relref "/tools/mongodb/mongodb-shard-error" >}}) -- sharding issues
- [MongoDB No Shard Key]({{< relref "/tools/mongodb/mongodb-no-shard-key" >}}) -- missing shard key
- [MongoDB Shard Key Not Indexed]({{< relref "/tools/mongodb/mongodb-shard-key-not-indexed" >}}) -- index issues
