---
title: "[Solution] MongoDB No Shard Key Error"
description: "Fix MongoDB missing shard key errors for sharded collections"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB No Shard Key Error

```
MongoServerError: no shard key found in query
```

```
No shard key exists in the query: { }
```

## Common Causes

- The collection is sharded but the query does not include the shard key
- The shard key field was misspelled in the query
- The insert/update operation does not include the shard key

## How to Fix

### 1. Include the shard key in all queries

```javascript
// If the collection is sharded on { userId: 1 }
db.orders.find({ userId: 123, status: "shipped" });  // Correct
db.orders.find({ status: "shipped" });  // Missing shard key
```

### 2. Use scatter-gather queries when shard key is unknown

```javascript
db.orders.find({ status: "shipped" }).comment("scatter-gather");
```

### 3. Shard the collection with a proper key

```javascript
sh.shardCollection("mydb.orders", { userId: 1 });
```

## Examples

```bash
# Check shard distribution
mongosh --eval "sh.status()"

# Check which shard a document lives on
mongosh --eval '
  db.orders.find({userId:123}).explain().shards
'
```