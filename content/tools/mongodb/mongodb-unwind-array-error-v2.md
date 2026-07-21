---
title: "[Solution] MongoDB $unwind Array Too Large Error"
description: "Fix MongoDB $unwind array too large error when unwinding arrays with too many elements causes memory or performance issues"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB $unwind Array Too Large Error

The $unwind stage fails or produces excessive output when a document contains an array with too many elements. Unwinding creates one document per array element, which can exhaust memory.

## Common Causes

- Documents have very large arrays (thousands of elements)
- $unwind is applied before filtering reduces dataset size
- Multiple $unwind stages multiply the document count
- Array contains nested documents that increase per-element size
- No $limit applied before expensive unwind operations

## How to Fix

### Filter Before Unwinding

```javascript
db.collection('orders').aggregate([
  // Filter first to reduce array sizes
  { $match: { createdAt: { $gte: new Date('2025-01-01') } } },
  { $unwind: '$items' },
  { $group: { _id: '$items.productId', total: { $sum: '$items.qty' } } }
])
```

### Use $slice to Limit Array Elements

```javascript
db.collection('logs').aggregate([
  { $project: {
    // Only unwind the first 100 array elements
    recentEvents: { $slice: ['$events', 100] }
  }},
  { $unwind: '$recentEvents' },
  { $group: { _id: '$recentEvents.type', count: { $sum: 1 } } }
])
```

### Allow Disk Use for Large Unwinds

```javascript
db.collection('analytics').aggregate([
  { $unwind: '$events' },
  { $group: { _id: '$events.action', count: { $sum: 1 } } }
], { allowDiskUse: true })
```

### Use $reduce Instead of $unwind When Possible

```javascript
// Instead of unwinding and re-grouping
db.collection('orders').aggregate([
  { $project: {
    totalAmount: {
      $reduce: {
        input: '$items',
        initialValue: 0,
        in: { $add: ['$$value', '$$this.amount'] }
      }
    }
  }}
])
```

## Examples

```
MongoServerError: $unwind produced 500000 documents from 100 input
  documents. Memory limit exceeded.

Plan executor error during $unwind:
  caused by "cannot create cursor for array with 0 elements"
```

## Related Errors

- [MongoDB Sort Memory Limit]({{< relref "/tools/mongodb/mongodb-sort-memory-limit" >}}) -- memory limits
- [MongoDB Aggregation Error]({{< relref "/tools/mongodb/mongodb-aggregation-error" >}}) -- aggregation issues
- [MongoDB Facet Memory Limit]({{< relref "/tools/mongodb/mongodb-facet-memory-limit" >}}) -- memory limits
