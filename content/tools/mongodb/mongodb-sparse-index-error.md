---
title: "[Solution] MongoDB Sparse Index Exception"
description: "Fix MongoDB sparse index issues and missing documents"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Sparse Index Exception

Sparse indexes exclude documents that do not have the indexed field:

```
// Queries using sparse indexes may return fewer results than expected
```

## Common Causes

- A query uses a sparse index but documents without the field are excluded
- The sparse index does not contain all documents in the collection
- A unique sparse index allows multiple documents without the field
- An aggregation pipeline uses the sparse index and misses documents

## How to Fix

### 1. Understand sparse vs non-sparse behavior

```javascript
// Sparse: only documents with 'email' field are indexed
db.users.createIndex({ email: 1 }, { sparse: true });

// Non-sparse (default): all documents are indexed
// Documents without 'email' have null indexed
db.users.createIndex({ email: 1 });
```

### 2. Use partialFilterExpression instead of sparse

```javascript
db.users.createIndex(
  { email: 1 },
  {
    partialFilterExpression: {
      email: { $exists: true, $ne: null }
    }
  }
);
```

### 3. Be aware of unique sparse index behavior

```javascript
// Multiple documents WITHOUT the field are allowed
db.users.createIndex({ email: 1 }, { unique: true, sparse: true });

// These are all allowed:
db.users.insertOne({ name: "Alice" });           // No email
db.users.insertOne({ name: "Bob" });             // No email
db.users.insertOne({ name: "Charlie", email: "c@test.com" });
```

### 4. Use hint to avoid sparse index when needed

```javascript
db.users.find({ email: { $exists: false } }).hint("_id_");
```

## Examples

```bash
# Demonstrate sparse index behavior
mongosh --eval '
  db.test.drop();
  db.test.createIndex({email:1}, {sparse:true});
  db.test.insertMany([{name:"A"},{name:"B"},{name:"C",email:"c@test.com"}]);
  print("Documents with email:", db.test.countDocuments({email:{$exists:true}}));
  print("Documents without email:", db.test.countDocuments({email:{$exists:false}}));
  print("All documents:", db.test.countDocuments());
'
```