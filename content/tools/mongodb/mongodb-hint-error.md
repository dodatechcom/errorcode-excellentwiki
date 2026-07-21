---
title: "[Solution] MongoDB Hint Error"
description: "Fix MongoDB hint error when the suggested index hint does not exist or cannot be used for the query"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Hint Error

A hint error occurs when the application specifies an index hint that does not exist, is dropped, or is incompatible with the query operation.

## Common Causes

- The hinted index was dropped or renamed
- Index name changed after a migration or rebuild
- Hint references a field that is not in the query filter
- Hint is used with a query that cannot use the specified index
- Stale client code references an old index name

## How to Fix

### Verify Index Exists

```javascript
db.collection('orders').getIndexes()
```

### Use Correct Hint Syntax

```javascript
// By index name
db.collection('orders').find({ status: 'active' }).hint('status_1')

// By index key pattern
db.collection('orders').find({ status: 'active' }).hint({ status: 1 })

// Compound index hint
db.collection('orders')
  .find({ status: 'active', region: 'us-east' })
  .hint({ status: 1, region: 1 })
```

### Drop Hint on Failure

```javascript
async function queryWithFallback(collection, filter, hintName) {
  try {
    return await collection.find(filter).hint(hintName).toArray();
  } catch (err) {
    if (err.code === 291 || err.message.includes('hint')) {
      console.warn('Hint failed, using query planner default');
      return await collection.find(filter).toArray();
    }
    throw err;
  }
}
```

### Remove Outdated Hints

```javascript
// After renaming an index, update all hints
db.collection('orders').dropIndex('status_1_createdAt_1')
db.collection('orders').createIndex(
  { status: 1, createdAt: -1 },
  { name: 'status_createdAt_idx' }
)
// Then update application code to use 'status_createdAt_idx'
```

## Examples

```
MongoServerError: bad hint: unknown index name "status_1"
MongoServerError: bad hint: cannot use hint for this query type
  (hint is for find but query is a text search)
```

## Related Errors

- [MongoDB Index Error]({{< relref "/tools/mongodb/mongodb-index-error" >}}) -- index issues
- [MongoDB Index Not Found]({{< relref "/tools/mongodb/mongodb-index-not-found" >}}) -- missing index
- [MongoDB Query Not Covered]({{< relref "/tools/mongodb/mongodb-query-not-covered" >}}) -- query performance
