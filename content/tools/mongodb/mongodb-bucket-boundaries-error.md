---
title: "[Solution] MongoDB $bucket Boundaries Error"
description: "Fix MongoDB $bucket aggregation boundary errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB $bucket Boundaries Error

The `$bucket` stage fails with boundary errors:

```
MongoServerError: $bucket boundaries must be monotonically increasing
```

```
MongoServerError: $bucket requires boundaries to be comparable
```

## Common Causes

- Boundaries are not in ascending order
- Boundary values are of mixed types (string and number)
- The default bucket range does not cover all documents
- Boundaries have duplicate values

## How to Fix

### 1. Provide monotonically increasing boundaries

```javascript
db.sales.aggregate([
  {
    $bucket: {
      groupBy: "$amount",
      boundaries: [0, 50, 100, 500, 1000],
      default: "Other",
      output: { count: { $sum: 1 } }
    }
  }
]);
```

### 2. Use consistent types for boundaries

```javascript
// Correct: all numeric
boundaries: [0, 50, 100, 500, 1000]
```

### 3. Use $bucketAuto for automatic boundaries

```javascript
db.sales.aggregate([
  {
    $bucketAuto: {
      groupBy: "$amount",
      buckets: 4,
      output: { count: { $sum: 1 }, avgAmount: { $avg: "$amount" } }
    }
  }
]);
```

## Examples

```bash
# Set up test data
mongosh --eval '
  db.scores.drop();
  db.scores.insertMany([{s:10},{s:25},{s:45},{s:70},{s:85},{s:95}]);

  let result = db.scores.aggregate([
    {$bucket:{
      groupBy:"$s",
      boundaries:[0,30,60,80,100],
      default:"Other",
      output:{count:{$sum:1},values:{$push:"$s"}}
    }}
  ]).toArray();
  printjson(result);
'
```