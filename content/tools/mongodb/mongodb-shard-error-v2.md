---
title: "MongoDB - cannot target write to replica set"
description: "MongoDB cannot route a write operation to a shard because the targeted replica set or shard key is invalid"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A "cannot target write to replica set" error occurs in sharded MongoDB clusters when a write operation cannot be routed to the correct shard. This typically happens when the shard key is not included in the write operation or the cluster metadata is inconsistent.

## Common Causes

- Shard key not included in the update or delete operation
- Shard key value cannot be determined from the operation
- Chunk migration in progress during the write
- Config servers are inconsistent or unreachable
- Collection not sharded but operation expects sharded routing

## How to Fix

1. Include the shard key in all write operations:

```javascript
// Bad: missing shard key
await db.collection('orders').updateOne(
  { orderId: '12345' },
  { $set: { status: 'shipped' } }
);

// Good: include shard key
await db.collection('orders').updateOne(
  { orderId: '12345', userId: 'user123' }, // userId is shard key
  { $set: { status: 'shipped' } }
);
```

2. Use targeted operations with the shard key:

```javascript
// Delete with shard key
await db.collection('orders').deleteOne({
  orderId: '12345',
  userId: 'user123', // shard key
});
```

3. Check sharding status:

```javascript
const shardInfo = await db.admin().command({ listShards: 1 });
console.log('Shards:', shardInfo.shards);

const chunks = await configServer.chunks.find({ ns: 'mydb.orders' }).toArray();
console.log('Chunks:', chunks.length);
```

4. Use `$merge` with shard key for aggregation writes:

```javascript
await db.collection('events').aggregate([
  { $group: { _id: '$userId', count: { $sum: 1 } } },
  {
    $merge: {
      into: 'userStats',
      on: '_id', // matches shard key
    }
  }
]);
```

5. Resolve config server issues:

```bash
mongosh --configReplSet
rs.status()
```

## Examples

```javascript
// Error: cannot target write to replica set while sharding
await db.collection('logs').deleteMany({ timestamp: { $lt: oldDate } });
// Missing shard key in delete

// Fix: include shard key or use targeted delete
await db.collection('logs').deleteMany({
  tenantId: 'tenant1', // shard key
  timestamp: { $lt: oldDate },
});
```

## Related Errors

- [Shard error]({{< relref "/tools/mongodb/mongodb-shard-error-v2" >}})
- [Write error]({{< relref "/tools/mongodb/mongodb-write-error-v2" >}})
