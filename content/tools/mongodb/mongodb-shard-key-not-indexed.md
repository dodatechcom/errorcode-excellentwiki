---
title: "[Solution] MongoDB Shard Key Not Indexed Error"
description: "Fix MongoDB shard key must be indexed errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Shard Key Not Indexed Error

```
MongoServerError: shard key must be an indexed field
```

```
Please create an index that starts with the shard key
```

## Common Causes

- The shard key field is not indexed
- The index on the shard key was dropped

## How to Fix

### 1. Create the required index

```javascript
db.orders.createIndex({ userId: 1 });
sh.shardCollection("mydb.orders", { userId: 1 });
```

### 2. For hashed shard keys

```javascript
db.orders.createIndex({ userId: "hashed" });
sh.shardCollection("mydb.orders", { userId: "hashed" });
```

### 3. For compound shard keys

```javascript
db.orders.createIndex({ customerId: 1, orderId: 1 });
sh.shardCollection("mydb.orders", { customerId: 1, orderId: 1 });
```

## Examples

```bash
# Check current indexes before sharding
mongosh --eval "db.orders.getIndexes()"

# Create the index and shard
mongosh --eval '
  db.orders.createIndex({userId:1});
  sh.shardCollection("mydb.orders", {userId:1});
  print("Collection sharded successfully");
'
```