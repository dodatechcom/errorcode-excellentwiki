---
title: "MongoDB - operation exceeded time limit"
description: "MongoDB operation fails because it exceeded the configured timeout limit for execution"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A MongoDB timeout error occurs when an operation takes longer than the configured time limit. This can happen with queries, aggregations, or write operations that exceed the `maxTimeMS` or server-side timeout thresholds.

## Common Causes

- Slow or unindexed queries scanning large collections
- Aggregation pipelines with expensive stages
- Network latency causing delayed responses
- Lock contention from concurrent write operations
- `maxTimeMS` set too low for the workload

## How to Fix

1. Add indexes to support slow queries:

```javascript
// Check query performance
await db.collection('orders').explain('executionStats').find({
  userId: 'user123',
  status: 'pending'
});

// Create supporting index
await db.collection('orders').createIndex({ userId: 1, status: 1 });
```

2. Increase timeout for long-running operations:

```javascript
await db.collection('largeData')
  .find({})
  .maxTimeMS(30000)
  .toArray();
```

3. Optimize aggregation pipelines:

```javascript
// Bad: $match late in pipeline
await db.collection('logs').aggregate([
  { $group: { _id: '$userId', count: { $sum: 1 } } },
  { $match: { count: { $gt: 10 } } },
]);

// Good: $match early
await db.collection('logs').aggregate([
  { $match: { timestamp: { $gte: lastWeek } } },
  { $group: { _id: '$userId', count: { $sum: 1 } } },
  { $match: { count: { $gt: 10 } } },
]);
```

4. Use cursor timeout for large result sets:

```javascript
const cursor = db.collection('events').find({}).batchSize(1000);
while (await cursor.hasNext()) {
  const doc = await cursor.next();
  // process each document
}
```

5. Monitor slow operations:

```javascript
db.setProfilingLevel(1, { slowms: 100 });
db.system.profile.find().sort({ ts: -1 }).limit(5);
```

## Examples

```javascript
// Error: operation exceeded time limit
await db.collection('huge').find({}).maxTimeMS(5000).toArray();
// MongoError: operation exceeded time limit

// Fix: add index or increase timeout
await db.collection('huge').createIndex({ createdAt: 1 });
await db.collection('huge').find({}).maxTimeMS(30000).toArray();
```

## Related Errors

- [Connection error]({{< relref "/tools/mongodb/mongodb-connection-error" >}})
- [Index error]({{< relref "/tools/mongodb/mongodb-index-error" >}})
