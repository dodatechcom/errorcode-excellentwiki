---
title: "[Solution] MongoDB $sort Memory Limit Exceeded"
description: "Fix MongoDB $sort exceeds memory limit errors in aggregation"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB $sort Memory Limit Exceeded

The `$sort` stage has a default memory limit of 100 MB:

```
$sort stage exceeded memory limit of 100 MB
```

## Common Causes

- Sorting a large result set without a preceding $match or $limit
- Sorting on a field with high cardinality
- The pipeline produces more than 100 MB before sorting
- The sort is not covered by an index

## How to Fix

### 1. Use allowDiskUse

```javascript
db.largeCollection.aggregate([
  { $sort: { createdAt: -1 } }
], { allowDiskUse: true });
```

### 2. Reduce data before sorting

```javascript
db.largeCollection.aggregate([
  { $match: { status: "active" } },
  { $limit: 1000 },
  { $sort: { createdAt: -1 } }
]);
```

### 3. Use $sort with $limit (optimized in MongoDB 4.4+)

```javascript
// MongoDB optimizes $sort + $limit to use less memory
db.largeCollection.aggregate([
  { $sort: { score: -1 } },
  { $limit: 100 }
]);
```

### 4. Create an index to support the sort

```javascript
db.largeCollection.createIndex({ createdAt: -1 });
```

## Examples

```bash
# Check if allowDiskUse is needed
mongosh --eval '
  let result = db.logs.aggregate([
    {$sort:{timestamp:-1}},
    {$limit:10}
  ], {allowDiskUse: true}).explain("executionStats");
  print("Sort usage:", result.stages ? "in-memory" : "index");
'

# Optimize with $sort + $limit
mongosh --eval '
  db.logs.aggregate([
    {$sort:{timestamp:-1}},
    {$limit:10}
  ], {allowDiskUse:true}).toArray();
'
```