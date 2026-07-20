---
title: "[Solution] MongoDB Query Not Covered Error"
description: "Fix MongoDB query not covered by index errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Query Not Covered Error

```
// Performance issue: query requires fetching documents from disk
// planSummary: COLLSCAN
```

## Common Causes

- The query does not use any index
- The query requires a fetch stage to retrieve documents
- The index does not cover all fields in the query
- No index exists for the query fields

## How to Fix

### 1. Create a compound index that covers the query

```javascript
// For query: { status: "active", email: 1 }
db.users.createIndex({ status: 1, email: 1 });

// For covered query: include all fields in the index
db.users.find({ status: "active" }, { _id: 0, status: 1, email: 1 });
```

### 2. Use explain to check query plans

```javascript
db.users.find({ status: "active" }).explain("executionStats")
```

### 3. Create a partial index for selective queries

```javascript
db.users.createIndex(
  { status: 1 },
  { partialFilterExpression: { status: "active" } }
);
```

### 4. Use projection to match index

```javascript
// If index is { status: 1, email: 1 }
db.users.find({ status: "active" }, { _id: 0, status: 1, email: 1 });
```

## Examples

```bash
# Check query plan
mongosh --eval "db.users.find({status:'active'}).explain('executionStats')"

# Check for COLLSCAN
mongosh --eval '
  db.users.find({status:"active"}).explain("executionStats").executionStats.stage
'

# Create a covering index
mongosh --eval '
  db.users.createIndex({status:1, email:1});
  let plan = db.users.find({status:"active"},{_id:0,status:1,email:1}).explain("executionStats");
  print("Stage:", plan.executionStats.stage);
'
```