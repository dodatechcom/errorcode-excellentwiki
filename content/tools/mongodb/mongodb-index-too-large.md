---
title: "[Solution] MongoDB Index Too Large Error"
description: "Fix MongoDB index size limit and too large index errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Index Too Large Error

An index can exceed the maximum key size or the available memory:

```
MongoServerError: Error: key too large to index (10485770 bytes)
```

```
MongoServerError: WiredTiger cannot find the file to compact
```

## Common Causes

- A text index includes very long text fields
- An indexed array field has too many elements
- The index key exceeds the WiredTiger key limit
- Insufficient RAM to hold the index
- Too many indexes on a collection (32 index limit)

## How to Fix

### 1. Limit the index key size with prefix

```javascript
// For text indexes, limit the indexed fields
db.articles.createIndex({ title: "text", content: "text" }, {
  weights: { title: 10, content: 5 },
  default_language: "english"
});
```

### 2. Use partial indexes for selective indexing

```javascript
// Only index documents where status is "active"
db.orders.createIndex(
  { status: 1 },
  { partialFilterExpression: { status: "active" } }
);
```

### 3. Drop unused indexes

```javascript
// List all indexes
db.users.getIndexes();

// Drop a specific index
db.users.dropIndex("unusedIndex_1");
```

### 4. Reduce indexed field sizes

```javascript
// Instead of indexing a large string, hash it
db.users.createIndex({ emailHash: 1 });
```

## Examples

```bash
# Check total index size for a collection
mongosh --eval "db.users.totalIndexSize()"

# Check index sizes individually
mongosh --eval '
  db.users.getIndexes().forEach(idx => {
    let stats = db.users.stats().indexSizes[idx.name];
    print(idx.name, ":", stats, "bytes");
  });
'

# Check WiredTiger cache usage
mongosh --eval "db.serverStatus().wiredTiger.cache"
```