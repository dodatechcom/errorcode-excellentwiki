---
title: "[Solution] MongoDB Operation Timed Out Error"
description: "Fix MongoDB operation timeout errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Operation Timed Out Error

```
MongoServerError: operation exceeded time limit
```

```
MongoNetworkError: operation timed out
```

## Common Causes

- The operation is too large or complex
- The server is under heavy load
- No indexes are available for the query
- The operation is waiting for a lock
- Network latency is high

## How to Fix

### 1. Set maxTimeMS on operations

```javascript
db.users.find({ status: "active" }).maxTimeMS(5000);
db.users.aggregate([...]).maxTimeMS(30000);
```

### 2. Optimize the query

```javascript
// Use explain to find bottlenecks
db.users.find({ email: "test@example.com" }).explain("executionStats");

// Add appropriate indexes
db.users.createIndex({ email: 1 });
```

### 3. Kill long-running operations

```javascript
db.currentOp({ active: true, secs_running: { $gt: 60 } })
```

```javascript
db.killOp(<opId>)
```

### 4. Break large operations into smaller ones

```javascript
// Instead of one large aggregation
db.largeCollection.aggregate([
  { $match: { date: { $gte: ISODate("2024-01-01") } } },
  { $group: { _id: "$category", total: { $sum: "$amount" } } }
], { maxTimeMS: 10000 });
```

## Examples

```bash
# Check long-running operations
mongosh --eval "db.currentOp({active:true, secs_running:{$gt:30}})"

# Kill an operation
mongosh --eval "db.killOp(<opId>)"

# Set maxTimeMS on a find
mongosh --eval "db.users.find({}).maxTimeMS(5000).toArray()"
```