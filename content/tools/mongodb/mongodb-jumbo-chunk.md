---
title: "[Solution] MongoDB Jumbo Chunk Error"
description: "Fix MongoDB jumbo chunk errors in sharded cluster"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Jumbo Chunk Error

A jumbo chunk cannot be moved because it exceeds the chunk size limit:

```
chunk is jumbo: moveChunk failed
```

## Common Causes

- The chunk size exceeds the configured chunkSize (default 64 MB)
- The shard key has low cardinality
- The balancer cannot split the chunk further

## How to Fix

### 1. Check for jumbo chunks

```javascript
sh.status({ verbose: 1 })
```

### 2. Split the jumbo chunk

```javascript
sh.splitAt("mydb.orders", { userId: 500 })
```

### 3. Increase chunk size

```javascript
use config
db.settings.updateOne(
  { _id: "chunksize" },
  { $set: { value: 128 } },
  { upsert: true }
);
```

## Examples

```bash
# Find jumbo chunks
mongosh --eval '
  db.chunks.find({ns:"mydb.orders"}).forEach(chunk => {
    let size = chunk.jumbo ? "JUMBO" : "normal";
    print(size, JSON.stringify(chunk.min), "->", JSON.stringify(chunk.max));
  });
'

# Update chunk size
mongosh --eval '
  use config;
  db.settings.updateOne({_id:"chunksize"}, {$set:{value:128}}, {upsert:true});
  print("Chunk size updated to 128 MB");
'
```