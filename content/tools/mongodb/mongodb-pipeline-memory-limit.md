---
title: "[Solution] MongoDB Pipeline Memory Limit Exceeded Error"
description: "Fix MongoDB pipeline memory limit exceeded error when aggregation stages consume more than the allowed memory"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Pipeline Memory Limit Exceeded Error

The aggregation pipeline exceeds the per-stage memory limit during execution. This happens when stages like $sort, $group, or $lookup accumulate too much data in memory.

## Common Causes

- $sort or $group stages process too many documents at once
- $lookup returns an unbounded number of matching documents
- $unwind creates many documents from large arrays
- Pipeline combines multiple memory-intensive stages
- No allowDiskUse flag set on the aggregation

## How to Fix

### Enable Disk Spill

```javascript
db.collection('orders').aggregate([
  { $match: { status: 'active' } },
  { $group: { _id: '$customerId', total: { $sum: '$amount' } } },
  { $sort: { total: -1 } }
], { allowDiskUse: true })
```

### Reduce Documents Per Stage

```javascript
// Filter early to reduce pipeline volume
db.collection('orders').aggregate([
  { $match: {
    createdAt: { $gte: new Date('2025-01-01') },  // filter first
    status: 'active'
  }},
  { $group: { _id: '$customerId', total: { $sum: '$amount' } } }
], { allowDiskUse: true })
```

### Use $limit Early

```javascript
db.collection('logs').aggregate([
  { $match: { level: 'error' } },
  { $limit: 10000 },  // limit early before expensive stages
  { $group: { _id: '$source', count: { $sum: 1 } } },
  { $sort: { count: -1 } }
])
```

### Increase Memory Limit

```javascript
// Default is 100MB per stage
db.adminCommand({
  setParameter: 1,
  internalQueryMaxMemoryUsageBytes: 268435456  // 256MB
})
```

## Examples

```
MongoServerError: Plan executor error during command:
  caused by "Exceeded memory limit for $sort"
  Allow disk use to allow disk usage.

MongoServerError: $group stage used more than 100MB of RAM.
  Use allowDiskUse:true to enable external sorting.
```

## Related Errors

- [MongoDB Sort Memory Limit]({{< relref "/tools/mongodb/mongodb-sort-memory-limit" >}}) -- sort memory
- [MongoDB Group Memory Limit]({{< relref "/tools/mongodb/mongodb-group-memory-limit" >}}) -- group memory
- [MongoDB Facet Memory Limit]({{< relref "/tools/mongodb/mongodb-facet-memory-limit" >}}) -- facet memory
