---
title: "[Solution] MongoDB Index Merge Error"
description: "Fix MongoDB index merge error when the query planner cannot merge multiple index scans efficiently"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Index Merge Error

The query planner fails to merge results from multiple index scans when a query uses a compound filter that would benefit from intersecting two or more indexes. The planner decides a collection scan is cheaper.

## Common Causes

- Query uses `$or` or `$and` with fields from different indexes
- Index statistics are stale or outdated
- Index intersection is more expensive than a collection scan
- Insufficient indexes force the planner to reject intersection
- Query planner cost model rejects the intersection plan

## How to Fix

### Create a Compound Index

```javascript
// Instead of relying on index intersection, create a compound index
db.collection('orders').createIndex({ status: 1, region: 1 })

// Query now uses a single index scan
db.collection('orders').find({ status: 'active', region: 'us-east' })
```

### Analyze Query Plan

```javascript
const explanation = await db.collection('orders')
  .find({ status: 'active', region: 'us-east' })
  .explain('executionStats');

console.log(JSON.stringify(explanation.queryPlanner, null, 2));
```

### Force Index Intersection for $or

```javascript
db.collection('orders').find({
  $or: [
    { status: 'active' },
    { priority: { $gte: 10 } }
  ]
}).explain('executionStats')

// Add separate indexes for each $or branch
db.collection('orders').createIndex({ status: 1 })
db.collection('orders').createIndex({ priority: 1 })
```

### Run Stats to Update Planner Data

```javascript
db.collection('orders').stats()
// Or re-analyze with:
db.collection('orders').aggregate([{ $collStats: { storageStats: {} } }])
```

## Examples

```
MongoDB query planner rejected index intersection
  using collection scan on: orders

Index intersection not supported for query:
  { status: "active", $or: [{region: "eu"}, {region: "us"}] }
```

## Related Errors

- [MongoDB Index Error]({{< relref "/tools/mongodb/mongodb-index-error" >}}) -- index issues
- [MongoDB Query Not Covered]({{< relref "/tools/mongodb/mongodb-query-not-covered" >}}) -- query performance
- [MongoDB Sort Memory Limit]({{< relref "/tools/mongodb/mongodb-sort-memory-limit" >}}) -- memory issues
