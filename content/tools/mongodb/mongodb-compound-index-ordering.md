---
title: "[Solution] MongoDB Compound Index Ordering Error"
description: "Fix compound index field ordering issues in MongoDB"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Compound Index Ordering Error

Incorrect field ordering in compound indexes leads to inefficient queries:

```
MongoServerError: error processing query: ... Unable to execute query: no index available
```

## Common Causes

- The query fields do not match the index prefix order
- Equality fields appear after range fields in the index
- The index order (ascending/descending) does not match sort requirements
- Missing prefix fields in the query
- Mixed ascending and descending fields in compound sort

## How to Fix

### 1. Put equality fields first, then sort, then range

```javascript
// Query: { status: "active", age: {$gt: 25} } sorted by { createdAt: -1 }
// Good index order: status (equality), createdAt (sort), age (range)
db.users.createIndex({ status: 1, createdAt: -1, age: 1 });
```

### 2. Match the index order with query filter

```javascript
// For query: { a: 1, b: 1, c: {$gt: 5} }
db.collection.createIndex({ a: 1, b: 1, c: 1 });
```

### 3. Use explain() to verify index usage

```javascript
db.users.find({ status: "active", age: {$gt: 25} })
  .sort({ createdAt: -1 })
  .explain("executionStats");
```

### 4. Handle sort with mixed directions

```javascript
// If you need to sort by { a: 1, b: -1 }, create the index with matching directions
db.collection.createIndex({ a: 1, b: -1 });
```

## Examples

```bash
# Compare query plans with different indexes
mongosh --eval '
  db.test.drop();
  for (let i = 0; i < 10000; i++) {
    db.test.insertOne({a: i%100, b: i%10, c: i, d: "val"+i});
  }
  db.test.createIndex({a:1,b:1,c:1});
  print("Index 1 totalKeysExamined:");
  printjson(db.test.find({a:1,b:1,c:{$gt:5}}).sort({c:1}).explain("executionStats").executionStats.totalKeysExamined);
'
```