---
title: "[Solution] MongoDB $lookup Size Limit Error"
description: "Fix MongoDB $lookup aggregation pipeline size limit errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB $lookup Size Limit Error

The `$lookup` stage has limitations that can cause errors:

```
MongoServerError: $lookup containing an expression cannot be applied to a constant
```

```
MongoServerError: $lookup with pipeline may not specify 'let' without a pipeline
```

## Common Causes

- Using `$lookup` with a `localField` that does not exist
- The foreign collection is very large and the lookup exceeds memory
- Using `$lookup` with `let` variables but no pipeline
- Referencing a system collection in `$lookup`
- The `foreignField` does not exist in the foreign collection
- Nested `$lookup` depth exceeds 4 levels (pre-MongoDB 5.0)

## How to Fix

### 1. Use the simple `$lookup` syntax correctly

```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "products",
      localField: "productId",
      foreignField: "_id",
      as: "product"
    }
  }
]);
```

### 2. Use pipeline-based `$lookup` for complex joins

```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "products",
      let: { productId: "$productId" },
      pipeline: [
        { $match: { $expr: { $eq: ["$_id", "$$productId"] } } },
        { $project: { name: 1, price: 1 } }
      ],
      as: "product"
    }
  }
]);
```

### 3. Add indexes on the foreign collection

```javascript
db.products.createIndex({ _id: 1 });
db.orders.createIndex({ customerId: 1 });
```

### 4. Limit the result size with $unwind and $limit

```javascript
db.orders.aggregate([
  {
    $lookup: {
      from: "products",
      localField: "productId",
      foreignField: "_id",
      as: "product"
    }
  },
  { $unwind: "$product" },
  { $limit: 100 }
]);
```

## Examples

```bash
# Set up test data
mongosh --eval '
  db.orders.drop(); db.products.drop();
  db.products.insertMany([{_id:1,name:"Widget"},{_id:2,name:"Gadget"}]);
  db.orders.insertMany([{productId:1,qty:5},{productId:2,qty:3},{productId:1,qty:10}]);
'

# Simple lookup
mongosh --eval '
  let result = db.orders.aggregate([
    {$lookup:{from:"products",localField:"productId",foreignField:"_id",as:"product"}},
    {$unwind:"$product"},
    {$project:{orderQty:"$qty",productName:"$product.name"}}
  ]).toArray();
  printjson(result);
'
```