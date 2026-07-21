---
title: "[Solution] MongoDB Lookup Infinite Recursion Error"
description: "Fix MongoDB lookup infinite recursion error when $lookup joins cause circular reference loops in collections"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Lookup Infinite Recursion Error

A $lookup stage enters infinite recursion when two collections reference each other, causing the pipeline to run until memory or time limits are exceeded.

## Common Causes

- Two collections reference each other via foreign keys (A -> B -> A)
- Self-join on a collection without depth limiting
- Cyclic foreign key references in hierarchical data
- Missing pipeline filter allows unbounded recursion
- Correlated subquery lookup creates circular dependency

## How to Fix

### Use $graphLookup Instead

```javascript
// Instead of recursive $lookup for hierarchical data
db.collection('departments').aggregate([
  {
    $graphLookup: {
      from: 'departments',
      startWith: '$parentId',
      connectFromField: 'parentId',
      connectToField: '_id',
      as: 'ancestors',
      maxDepth: 10
    }
  }
])
```

### Add a Depth Limiter Pipeline

```javascript
db.collection('employees').aggregate([
  {
    $lookup: {
      from: 'employees',
      let: { empId: '$_id', depth: { $ifNull: ['$depth', 0] } },
      pipeline: [
        { $match: { $expr: { $and: [
          { $eq: ['$reportsTo', '$$empId'] },
          { $lt: ['$$depth', 5] }
        ]}}}
      ],
      as: 'reports'
    }
  }
])
```

### Break Circular References in Data

```javascript
// Detect cycles
db.collection('categories').aggregate([
  { $project: { name: 1, parentId: 1 } },
  { $graphLookup: {
    from: 'categories',
    startWith: '$_id',
    connectFromField: '_id',
    connectToField: 'parentId',
    as: 'cycleCheck',
    maxDepth: 0,
    restrictSearchWithMatch: { parentId: '$_id' }
  }},
  { $match: { 'cycleCheck.0': { $exists: true } } }
])
```

## Examples

```
MongoServerError: $lookup with correlated pipeline caused stack overflow
  detected recursive reference between collections: orders, refunds

Exceeded memory limit for $lookup. Use allowDiskUse to allow disk usage.
  Possible infinite recursion detected in joined collections.
```

## Related Errors

- [MongoDB Aggregation Error]({{< relref "/tools/mongodb/mongodb-aggregation-error" >}}) -- aggregation issues
- [MongoDB Lookup Size Limit]({{< relref "/tools/mongodb/mongodb-lookup-size-limit" >}}) -- result size limits
- [MongoDB Facet Memory Limit]({{< relref "/tools/mongodb/mongodb-facet-memory-limit" >}}) -- memory limits
