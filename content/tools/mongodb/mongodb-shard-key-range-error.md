---
title: "[Solution] MongoDB Shard Key Range Error"
description: "Fix MongoDB shard key range errors in queries"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Shard Key Range Error

```
MongoServerError: bad shard key pattern: not a valid prefix of compound shard key
```

```
shard key range not supported
```

## Common Causes

- The query filter on the shard key is invalid
- The range query on a hashed shard key is not supported
- The shard key pattern does not match the expected format

## How to Fix

### 1. Use equality or range on prefix of shard key

```javascript
// For shard key { a: 1, b: 1 }
db.coll.find({ a: 1 })             // Works (prefix)
db.coll.find({ a: 1, b: 1 })      // Works (full key)
db.coll.find({ b: 1 })             // Missing prefix 'a'
```

### 2. For hashed shard keys, use equality only

```javascript
// For hashed shard key { userId: "hashed" }
db.orders.find({ userId: 123 })    // Works (equality)
db.orders.find({ userId: { $gt: 100 } })  // Does NOT work
```

### 3. Use targeted queries with the shard key

```javascript
db.orders.find({ userId: 123, status: "shipped" })
```

## Examples

```bash
# Check shard key type
mongosh --eval '
  let stats = db.orders.stats();
  print("Shard key:", JSON.stringify(stats.shardKey));
'

# Verify query uses shard key
mongosh --eval '
  db.orders.find({userId:123}).explain().executionStats
'
```