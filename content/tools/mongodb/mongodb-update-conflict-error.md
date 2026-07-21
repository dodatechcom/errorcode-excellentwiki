---
title: "[Solution] MongoDB Update Conflict Error"
description: "Fix MongoDB update conflict error when concurrent upsert operations cause write conflicts on the same document"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Update Conflict Error

A write conflict occurs when two operations attempt to modify the same document simultaneously in WiredTiger. One operation succeeds and the other fails or retries internally.

## Common Causes

- Concurrent upserts target the same document
- Multiple application instances update overlapping documents
- Atomic counter increments on the same field
- $push and $pull on the same array field simultaneously
- Transaction aborts due to write conflict detection

## How to Fix

### Use findOneAndUpdate with Retry

```javascript
async function safeUpdate(collection, filter, update, options = {}) {
  const maxRetries = 5;
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await collection.findOneAndUpdate(filter, update, {
        upsert: true,
        returnDocument: 'after',
        ...options
      });
    } catch (err) {
      if (err.code === 112 || err.message.includes('WriteConflict')) {
        await new Promise(r => setTimeout(r, 10 * Math.pow(2, i)));
        continue;
      }
      throw err;
    }
  }
  throw new Error('Write conflict retries exhausted');
}

// Usage
await safeUpdate(
  db.collection('counters'),
  { _id: 'page_views' },
  { $inc: { count: 1 } }
);
```

### Use Atomic Operations

```javascript
// Instead of read-modify-write, use atomic $inc
await db.collection('inventory').updateOne(
  { _id: 'product-42', stock: { $gte: 1 } },
  { $inc: { stock: -1 } }
)
```

### Reduce Contention with Document-Level Granularity

```javascript
// Instead of updating one shared document per user
await db.collection('sessions').updateOne(
  { _id: `session-${userId}-${process.pid}` },
  { $set: { lastActive: new Date() } },
  { upsert: true }
)
```

### Enable Retryable Writes

```javascript
const client = new MongoClient(uri, {
  retryWrites: true  // default: true in driver 3.6+
});
```

## Examples

```
MongoServerError: Write conflict during update.
  Retrying write to collection "counters" due to conflict.

MongoServerError:TransientTransactionError: write conflict
  on upsert to document { _id: "counter-1" }
```

## Related Errors

- [MongoDB Write Conflict Transaction]({{< relref "/tools/mongodb/mongodb-write-conflict-transaction" >}}) -- transaction conflicts
- [MongoDB Duplicate Key]({{< relref "/tools/mongodb/mongodb-duplicate-key" >}}) -- key conflicts
- [MongoDB Write Error]({{< relref "/tools/mongodb/mongodb-write-error" >}}) -- write failures
