---
title: "[Solution] MongoDB $unwind Array Error"
description: "Fix MongoDB $unwind aggregation array errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB $unwind Array Error

The `$unwind` stage fails when the input field is not an array:

```
MongoServerError: $unwind requires that the value of 'path' must be an array
```

```
Cannot unwind non-array field 'tags'
```

## Common Causes

- The field being unwound does not exist in some documents
- The field is not an array type (it is a string or object)
- Using `$unwind` on a nested field without first projecting it
- The array is empty, causing the document to be excluded
- Missing `preserveNullAndEmptyArrays` when nulls are expected

## How to Fix

### 1. Ensure the field is an array before unwinding

```javascript
db.articles.aggregate([
  { $match: { tags: { $type: "array" } } },
  { $unwind: "$tags" }
]);
```

### 2. Use preserveNullAndEmptyArrays

```javascript
db.articles.aggregate([
  {
    $unwind: {
      path: "$tags",
      preserveNullAndEmptyArrays: true
    }
  }
]);
```

### 3. Convert non-array fields to arrays first

```javascript
db.articles.aggregate([
  {
    $addFields: {
      tags: {
        $cond: {
          if: { $eq: [{ $type: "$tags" }, "array"] },
          then: "$tags",
          else: ["$tags"]
        }
      }
    }
  },
  { $unwind: "$tags" }
]);
```

## Examples

```bash
# Demonstrate unwind with missing arrays
mongosh --eval '
  db.posts.drop();
  db.posts.insertMany([
    {title:"Post1", tags:["mongo","db"]},
    {title:"Post2", tags:"single-tag"},
    {title:"Post3"}
  ]);

  try {
    db.posts.aggregate([{$unwind:"$tags"}]);
  } catch(e) { print("Error:", e.message); }

  let result = db.posts.aggregate([
    {$match:{tags:{$type:"array"}}},
    {$unwind:"$tags"},
    {$group:{_id:"$tags", count:{$sum:1}}}
  ]).toArray();
  printjson(result);
'
```