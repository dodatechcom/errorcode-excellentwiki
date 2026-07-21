---
title: "[Solution] MongoDB No Shard Key in Query Error"
description: "Fix MongoDB no shard key in query error when scatter-gather queries fail because the shard key is missing from the filter"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB No Shard Key in Query Error

Queries on sharded collections without the shard key must be sent to all shards (scatter-gather), which is slow and can exceed limits for high-throughput workloads.

## Common Causes

- Query filter does not include the shard key
- Application performs lookups without the shard key
- Analytics queries scan the full collection across all shards
- Aggregation pipelines run without shard key filtering
- Secondary reads on sharded collections without shard key

## How to Fix

### Include Shard Key in Queries

```javascript
// Shard key is { customerId: 1, region: 1 }

// Bad: scatter-gather across all shards
db.collection('orders').find({ status: 'active' })

// Good: includes shard key, routes to correct shard
db.collection('orders').find({ customerId: 'user-42', region: 'us-east' })
```

### Use Targeted Aggregation

```javascript
// Good: $match with shard key at the start
db.collection('orders').aggregate([
  { $match: { customerId: 'user-42', region: 'us-east' } },
  { $group: { _id: '$status', total: { $sum: '$amount' } } }
])

// Bad: full collection scan across shards
db.collection('orders').aggregate([
  { $group: { _id: '$customerId', total: { $sum: '$amount' } } }
])
```

### Create Indexes for Common Queries

```javascript
// Even with scatter-gather, indexes help each shard
db.collection('orders').createIndex({ status: 1, createdAt: -1 })
db.collection('orders').createIndex({ customerId: 1 })
```

### Use Chunk Queries for Analytics

```javascript
// For read-heavy analytics, query with shard key ranges
db.collection('orders').aggregate([
  { $match: {
    customerId: { $gte: 'A', $lt: 'M' },  // target specific shard range
    createdAt: { $gte: new Date('2025-01-01') }
  }},
  { $group: { _id: '$status', count: { $sum: 1 } } }
], { allowDiskUse: true })
```

## Examples

```
MongoServerError: cannot use 'partialFilterExpression' on sharded
  collection without shard key in query filter

mongos> db.orders.find({ status: 'active' })
Warning: using implicit collection scan across all shards.
  Consider adding shard key to query for better performance.
```

## Related Errors

- [MongoDB No Shard Key]({{< relref "/tools/mongodb/mongodb-no-shard-key" >}}) -- missing shard key
- [MongoDB Shard Key Not Indexed]({{< relref "/tools/mongodb/mongodb-shard-key-not-indexed" >}}) -- index issues
- [MongoDB Query Not Covered]({{< relref "/tools/mongodb/mongodb-query-not-covered" >}}) -- query performance
