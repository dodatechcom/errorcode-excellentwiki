---
title: "[Solution] MongoDB $group Memory Limit Exceeded"
description: "Fix MongoDB aggregation $group exceeds memory limit errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB $group Memory Limit Exceeded

The `$group` stage has a default memory limit of 100 MB:

```
$group stage exceeded memory limit of 100 MB
```

## Common Causes

- The grouping key has too many unique values
- The accumulator produces large result sets
- The collection has high cardinality on the grouping field
- No `$sort` or `$match` was applied before `$group` to reduce the dataset

## How to Fix

### 1. Allow disk spill with `allowDiskUse`

```javascript
db.sales.aggregate([
  { $group: { _id: "$category", total: { $sum: "$amount" } } }
], { allowDiskUse: true });
```

### 2. Reduce the dataset before grouping

```javascript
db.sales.aggregate([
  { $match: { date: { $gte: ISODate("2024-01-01") } } },
  { $group: { _id: "$category", total: { $sum: "$amount" } } }
]);
```

### 3. Use `$bucket` or `$bucketAuto` for large cardinality

```javascript
db.sales.aggregate([
  {
    $bucket: {
      groupBy: "$amount",
      boundaries: [0, 100, 500, 1000, Infinity],
      default: "Other",
      output: { count: { $sum: 1 }, total: { $sum: "$amount" } }
    }
  }
]);
```

## Examples

```bash
# Generate test data
mongosh --eval '
  db.sales.drop();
  let ops = [];
  for (let i = 0; i < 100000; i++) {
    ops.push({category:["A","B","C","D","E"][i%5], amount: Math.random()*1000});
  }
  db.sales.insertMany(ops);
'

# Use allowDiskUse for large aggregations
mongosh --eval '
  let result = db.sales.aggregate([
    {$group:{_id:"$category", total:{$sum:"$amount"}, count:{$sum:1}}}
  ], {allowDiskUse: true}).toArray();
  printjson(result);
'
```