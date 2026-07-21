---
title: "[Solution] MongoDB Explain Plan Error"
description: "Fix MongoDB explain plan errors when query execution analysis reveals invalid plans or unsupported operations"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Explain Plan Error

The explain plan command fails or returns unexpected results when the query cannot be analyzed, the collection is empty, or the pipeline uses unsupported stages.

## Common Causes

- Running explain on an empty collection with no indexes
- Using explain with write operations in unsupported modes
- Query planner encounters invalid index hints
- explain("executionStats") on a very large collection times out
- Pipeline references views that do not exist

## How to Fix

### Run Explain Properly

```javascript
// Standard explain
db.collection('orders').find({ status: 'pending' }).explain()

// With execution stats
db.collection('orders').find({ status: 'pending' }).explain('executionStats')

// With all plans (detailed)
db.collection('orders').find({ status: 'pending' }).explain('allPlansExecution')
```

### Check Index Usage

```javascript
const explanation = await db.collection('orders')
  .find({ status: 'pending', createdAt: { $gte: new Date('2025-01-01') } })
  .explain('executionStats');

console.log('Total docs examined:', explanation.executionStats.totalDocsExamined);
console.log('Total keys examined:', explanation.executionStats.totalKeysExamined);
console.log('Execution time:', explanation.executionStats.executionTimeMillis);
console.log('Stage:', explanation.queryPlanner.winningPlan.stage);
```

### Fix Invalid Index Hints

```javascript
// This fails if the hint index does not exist
db.collection('orders')
  .find({ status: 'pending' })
  .hint('status_1')  // must be a valid index name
  .explain()

// List available indexes first
db.collection('orders').getIndexes()
```

## Examples

```
MongoServerError: Unable to explain query plan for query:
  unknown top level stage: invalidHint

MongoServerError: cannot explain delete operations
MongoServerError: no collection found for explain on view: pendingOrders
```

## Related Errors

- [MongoDB Index Error]({{< relref "/tools/mongodb/mongodb-index-error" >}}) -- index issues
- [MongoDB Query Not Covered]({{< relref "/tools/mongodb/mongodb-query-not-covered" >}}) -- query performance
- [MongoDB Sort Memory Limit]({{< relref "/tools/mongodb/mongodb-sort-memory-limit" >}}) -- sort issues
