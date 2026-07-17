---
title: "MongoDB Index Error"
description: "MongoDB index operation fails due to index creation issues or performance problems."
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# MongoDB Index Error

A MongoDB index error occurs when index creation fails or indexes cause performance issues. Proper indexing is critical for query performance.

## Common Causes

- Index creation exceeds index key size limit
- Too many indexes on a collection
- Index builds blocking operations
- Duplicate index definitions

## How to Fix

### Check Existing Indexes

```javascript
db.collection.getIndexes()
```

### Create Index with Options

```javascript
// Background index build (non-blocking)
db.collection.createIndex(
  { email: 1 },
  { background: true, name: 'email_index' }
)
```

### Check Index Size

```javascript
db.collection.stats().indexSizes
```

### Drop Unused Indexes

```javascript
db.collection.dropIndex('old_index')
```

### Use explain() to Verify Index Usage

```javascript
db.collection.find({ email: 'test@example.com' }).explain('executionStats')
```

### Handle Index Build Errors

```javascript
// Use commitQuorum for replica sets
db.collection.createIndex(
  { field: 1 },
  { commitQuorum: 'majority' }
)
```

## Examples

```javascript
// Index key too large
MongoServerError: BSONObj size limit exceeded

// Index already exists
MongoServerError: index already exists with a different name
```

## Related Errors

- [Duplicate Key Error]({{< relref "/tools/mongodb/duplicate-key" >}}) — duplicate key violation
- [Read Error]({{< relref "/tools/mongodb/mongodb-read-error" >}}) — slow query error
