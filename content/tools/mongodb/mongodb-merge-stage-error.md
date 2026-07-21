---
title: "[Solution] MongoDB Merge Stage Error"
description: "Fix MongoDB merge stage error in change streams when the $merge output fails due to conflicts or permissions"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Merge Stage Error

The $merge aggregation stage fails when it cannot write to the target collection due to unique key conflicts, missing collection permissions, or schema mismatches.

## Common Causes

- Target collection has a unique index that conflicts with incoming documents
- `whenMatched` action conflicts with unique constraints
- Target collection does not exist and `whenMatched` is not set to insert
- Pipeline output schema does not match the target collection indexes
- Write permissions on target collection are insufficient

## How to Fix

### Handle Unique Key Conflicts

```javascript
db.collection('events').aggregate([
  { $match: { type: 'purchase' } },
  { $group: {
    _id: '$userId',
    totalSpent: { $sum: '$amount' },
    lastPurchase: { $max: '$createdAt' }
  }},
  {
    $merge: {
      into: 'user_stats',
      on: '_id',
      whenMatched: 'replace',   // replace instead of merge
      whenNotMatched: 'insert'
    }
  }
])
```

### Use whenMatched to Merge Fields

```javascript
{
  $merge: {
    into: 'user_stats',
    on: '_id',
    whenMatched: [
      { $set: {
        totalSpent: { $add: ['$$this.totalSpent', '$totalSpent'] },
        lastPurchase: { $max: ['$$this.lastPurchase', '$lastPurchase'] },
        count: { $add: ['$$$this.count', 1] }
      }}
    ],
    whenNotMatched: 'insert'
  }
}
```

### Create Target Collection First

```javascript
// Ensure target exists before merge
db.createCollection('user_stats')
db.collection('user_stats').createIndex({ totalSpent: -1 })

// Then run the aggregation
db.collection('events').aggregate([...pipeline, {
  $merge: { into: 'user_stats' }
}])
```

## Examples

```
MongoServerError: $merge failed due to unique key violation
  duplicate key: { _id: "user-42" } in collection: user_stats

MongoServerError: $merge target collection 'user_stats' has
  incompatible unique index
```

## Related Errors

- [MongoDB Duplicate Key]({{< relref "/tools/mongodb/mongodb-duplicate-key" >}}) -- unique constraint
- [MongoDB Aggregation Error]({{< relref "/tools/mongodb/mongodb-aggregation-error" >}}) -- aggregation issues
- [MongoDB Write Error]({{< relref "/tools/mongodb/mongodb-write-error" >}}) -- write failures
