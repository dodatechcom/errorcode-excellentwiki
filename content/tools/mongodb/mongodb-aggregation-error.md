---
title: "MongoDB - aggregation pipeline error"
description: "MongoDB aggregation pipeline fails due to stage errors, memory limits, or invalid operations"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
tags: ["mongodb", "aggregation", "pipeline", "memory", "group", "stage"]
weight: 5
---

A MongoDB aggregation pipeline error occurs when one or more stages in the pipeline fail to execute. This can be caused by memory limits, invalid stage operations, or data type mismatches within the pipeline stages.

## Common Causes

- `$group` stage exceeds 100MB memory limit without `allowDiskUse`
- Invalid accumulation operator or expression syntax
- Missing `$match` stage causing full collection scan
- Field type mismatches between stages
- Using operators not supported in aggregation context

## How to Fix

1. Enable disk usage for large aggregations:

```javascript
await db.collection('orders').aggregate([
  { $group: { _id: '$userId', total: { $sum: '$amount' } } },
], { allowDiskUse: true }).toArray();
```

2. Add early `$match` stage to reduce data volume:

```javascript
await db.collection('orders').aggregate([
  { $match: { createdAt: { $gte: lastMonth } } },
  { $group: { _id: '$status', count: { $sum: 1 } } },
]);
```

3. Check pipeline stage syntax:

```javascript
// Valid aggregation pipeline
await db.collection('orders').aggregate([
  { $match: { status: 'active' } },
  { $unwind: '$items' },
  { $group: {
    _id: '$userId',
    totalItems: { $sum: '$items.quantity' },
    avgPrice: { $avg: '$items.price' },
  }},
  { $sort: { totalItems: -1 } },
  { $limit: 10 },
]);
```

4. Use `$project` to limit fields early:

```javascript
await db.collection('logs').aggregate([
  { $project: { userId: 1, action: 1, timestamp: 1 } },
  { $group: { _id: '$userId', count: { $sum: 1 } } },
]);
```

5. Increase memory limit with `allowDiskUse`:

```javascript
// Aggregation with disk usage
const cursor = db.collection('events').aggregate([
  { $group: { _id: '$category', count: { $sum: 1 } } },
], {
  allowDiskUse: true,
  maxTimeMS: 60000,
});
const results = await cursor.toArray();
```

## Examples

```bash
# Error: $group stage must have access to disk
# Exceeded memory limit for $group
db.orders.aggregate([
  { $group: { _id: '$customerId', total: { $sum: '$amount' } } }
])
# PlanExecutor error: $group is not allowed to use more than 100MB of RAM

# Fix: enable disk usage
db.orders.aggregate([
  { $group: { _id: '$customerId', total: { $sum: '$amount' } } }
], { allowDiskUse: true })
```

## Related Errors

- [Timeout error]({{< relref "/tools/mongodb/mongodb-timeout-error-v2" >}})
- [Index error]({{< relref "/tools/mongodb/mongodb-index-error" >}})
