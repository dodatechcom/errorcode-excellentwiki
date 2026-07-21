---
title: "[Solution] MongoDB Query Plan Hash Mismatch Error"
description: "Fix MongoDB query plan hash mismatch error when cached query plans become invalid after index or schema changes"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Query Plan Hash Mismatch Error

The server detects that a cached query plan no longer matches the current query shape. This causes a plan cache miss or stale plan execution that returns incorrect results.

## Common Causes

- Index was dropped or created after the plan was cached
- Collection was compacted, changing document distribution
- Schema changes altered the query planner's cost estimates
- Query shape was updated but the plan cache still has the old plan
- Feature compatibility version was upgraded

## How to Fix

### Clear Plan Cache

```javascript
// Clear plan cache for a specific collection
db.collection('orders').getPlanCache().clear()

// Clear all plans for a collection
db.runCommand({ planCacheClear: 'orders' })
```

### Monitor Plan Cache

```javascript
// Check plan cache entries
db.collection('orders').getPlanCache().list()

// Check for plan cache warnings
db.currentOp({ 'command.planCacheClear': { $exists: true } })
```

### Evict Stale Plans Automatically

```javascript
// Force re-evaluation of cached plans
db.collection('orders').getPlanCache().clear()
// The next query will rebuild the plan with current statistics
db.collection('orders').find({ status: 'active' }).explain()
```

### Update Collection Statistics

```javascript
// Re-analyze collection for planner
db.collection('orders').aggregate([{ $collStats: { storageStats: {} } }])

// Or run analyze on specific indexes
db.collection('orders').analyze()
```

## Examples

```
MongoServerError: Plan cache entry hash mismatch for query
  { status: "active" } on collection orders.
  Cache entry has been evicted due to index change.

QueryPlanError: cached plan no longer matches query shape.
  Dropping cached plan and re-planning.
```

## Related Errors

- [MongoDB Query Not Covered]({{< relref "/tools/mongodb/mongodb-query-not-covered" >}}) -- query performance
- [MongoDB Index Error]({{< relref "/tools/mongodb/mongodb-index-error" >}}) -- index issues
- [MongoDB Explain Plan Error]({{< relref "/tools/mongodb/mongodb-explain-plan-error" >}}) -- explain issues
