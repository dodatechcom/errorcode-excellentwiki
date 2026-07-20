---
title: "[Solution] MongoDB Aggregation Accumulator Error"
description: "Fix MongoDB accumulator errors in aggregation pipeline"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Aggregation Accumulator Error

Accumulator errors occur in `$group` or `$setWindowFields`:

```
MongoServerError: Accumulator $sum: args must be numeric
```

```
MongoServerError: $avg requires numeric or array values
```

## Common Causes

- Non-numeric values passed to `$sum` or `$avg`
- `$push` or `$addToSet` used on a field that is null or undefined
- Mixed types in an accumulator (string + number)
- The accumulator receives an empty array when `$first` or `$last` is needed

## How to Fix

### 1. Ensure numeric types for numeric accumulators

```javascript
db.sales.aggregate([
  {
    $group: {
      _id: "$category",
      total: { $sum: "$amount" }  // 'amount' must be numeric
    }
  }
]);

// Use $convert to ensure numeric type
db.sales.aggregate([
  { $addFields: { amountNum: { $convert: { input: "$amount", to: "double", onError: 0 } } } },
  { $group: { _id: "$category", total: { $sum: "$amountNum" } } }
]);
```

### 2. Filter null values before accumulation

```javascript
db.users.aggregate([
  { $match: { score: { $exists: true, $ne: null, $type: "number" } } },
  { $group: { _id: "$department", avgScore: { $avg: "$score" } } }
]);
```

### 3. Use $cond for conditional accumulation

```javascript
db.orders.aggregate([
  {
    $group: {
      _id: "$status",
      count: { $sum: 1 },
      premiumCount: {
        $sum: { $cond: [{ $eq: ["$type", "premium"] }, 1, 0] }
      }
    }
  }
]);
```

## Examples

```bash
# Demonstrate accumulator type errors
mongosh --eval '
  db.data.drop();
  db.data.insertMany([{v:10},{v:20},{v:"thirty"},{v:40}]);
  try {
    db.data.aggregate([{$group:{_id:null, total:{$sum:"$v"}}}]);
  } catch(e) { print("Error:", e.message); }
'

# Fix: filter non-numeric values
mongosh --eval '
  let result = db.data.aggregate([
    {$match:{v:{$type:"number"}}},
    {$group:{_id:null, total:{$sum:"$v"}, avg:{$avg:"$v"}}}
  ]).toArray();
  printjson(result);
'
```