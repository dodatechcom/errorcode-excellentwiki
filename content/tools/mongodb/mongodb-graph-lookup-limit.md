---
title: "[Solution] MongoDB Graph Lookup Recursion Limit Error"
description: "Fix MongoDB graph lookup recursion limit error when traversing deeply nested hierarchical data exceeds the maximum depth"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Graph Lookup Recursion Limit Error

The $graphLookup stage exceeds the maximum recursion depth when traversing hierarchical or tree-structured data. MongoDB caps the search depth to prevent infinite loops.

## Common Causes

- Data contains circular references in parent-child relationships
- `maxDepth` is set too low for the required traversal depth
- Collection has deeply nested hierarchical structures
- `connectFromField` and `connectToField` create cycles in the graph
- Default recursion limit of 100 is insufficient for large org charts or category trees

## How to Fix

### Increase maxDepth

```javascript
db.collection('employees').aggregate([
  {
    $graphLookup: {
      from: 'employees',
      startWith: '$managerId',
      connectFromField: 'managerId',
      connectToField: '_id',
      as: 'reportingChain',
      maxDepth: 200  // increase from default 100
    }
  }
])
```

### Detect Circular References

```javascript
db.collection('employees').aggregate([
  {
    $graphLookup: {
      from: 'employees',
      startWith: '$managerId',
      connectFromField: 'managerId',
      connectToField: '_id',
      as: 'ancestors',
      maxDepth: 50,
      depthField: 'level'
    }
  },
  { $unwind: '$ancestors' },
  { $group: { _id: '$ancestors.level', count: { $sum: 1 } } },
  { $sort: { _id: -1 } }
])
```

### Limit Results to Prevent Memory Exhaustion

```javascript
db.collection('categories').aggregate([
  {
    $graphLookup: {
      from: 'categories',
      startWith: '$parentId',
      connectFromField: 'parentId',
      connectToField: '_id',
      as: 'ancestors',
      maxDepth: 3
    }
  },
  { $limit: 1000 }
], { allowDiskUse: true })
```

## Examples

```
MongoServerError: $graphLookup - recursion limit reached at depth 100
  for document _id: "dept-42"

MongoServerError: $graphLookup caused too much memory usage.
  Allow disk usage and try again.
```

## Related Errors

- [MongoDB Aggregation Error]({{< relref "/tools/mongodb/mongodb-aggregation-error" >}}) -- aggregation issues
- [MongoDB Sort Memory Limit]({{< relref "/tools/mongodb/mongodb-sort-memory-limit" >}}) -- memory issues
- [MongoDB Group Memory Limit]({{< relref "/tools/mongodb/mongodb-group-memory-limit" >}}) -- memory limits
