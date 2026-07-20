---
title: "[Solution] MongoDB Aggregation Pipeline Timeout"
description: "Fix MongoDB aggregation timeout errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Aggregation Pipeline Timeout

Aggregation pipelines can timeout on large collections:

```
MongoServerError: operation exceeded time limit
```

```
MongoServerError: aggregation timed out
```

## Common Causes

- The pipeline is processing too many documents
- Multiple stages without index support
- The pipeline runs during peak hours
- No `$match` or `$limit` early in the pipeline
- The pipeline uses expensive stages like `$lookup` on large collections

## How to Fix

### 1. Optimize pipeline stage order

```javascript
// Good: filter early
db.sales.aggregate([
  { $match: { date: { $gte: ISODate("2024-01-01") } } },
  { $match: { status: "completed" } },
  { $group: { _id: "$category", total: { $sum: "$amount" } } },
  { $sort: { total: -1 } }
]);
```

### 2. Use allowDiskUse for large datasets

```javascript
db.sales.aggregate([...pipeline], { allowDiskUse: true });
```

### 3. Add indexes to support $match stages

```javascript
db.sales.createIndex({ date: 1 });
db.sales.createIndex({ status: 1 });
```

### 4. Use $limit early in the pipeline

```javascript
db.sales.aggregate([
  { $match: { date: { $gte: ISODate("2024-01-01") } } },
  { $limit: 10000 },
  { $group: { _id: "$category", total: { $sum: "$amount" } } }
]);
```

## Examples

```bash
# Test aggregation performance
mongosh --eval '
  let start = Date.now();
  let result = db.sales.aggregate([
    {$match:{date:{$gte:new Date("2024-01-01")}}},
    {$group:{_id:"$category",total:{$sum:"$amount"}}},
    {$sort:{total:-1}}
  ], {allowDiskUse:true}).toArray();
  print("Aggregation took:", Date.now()-start, "ms");
  print("Results:", result.length);
'
```