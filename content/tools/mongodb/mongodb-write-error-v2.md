---
title: "MongoDB - write conflict error"
description: "MongoDB encounters a write conflict when concurrent operations attempt to modify the same document or data"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
tags: ["mongodb", "write-conflict", "concurrent", "transaction", "lock", "retry"]
weight: 5
---

A MongoDB write conflict error occurs when two or more operations try to modify the same document simultaneously in a non-transactional context. MongoDB's document-level locking detects the conflict and aborts one of the operations.

## Common Causes

- Concurrent updates to the same document without transactions
- `$inc` and `$set` operations on the same fields in parallel
- Mix of read and write operations without proper isolation
- Using `findAndModify` with high concurrency on the same documents
- Causal consistency issues in replica sets

## How to Fix

1. Use transactions for multi-document operations:

```javascript
const session = client.startSession();
try {
  await session.withTransaction(async () => {
    await db.collection('accounts').updateOne(
      { _id: fromAccount },
      { $inc: { balance: -amount } },
      { session }
    );
    await db.collection('accounts').updateOne(
      { _id: toAccount },
      { $inc: { balance: amount } },
      { session }
    );
  });
} finally {
  await session.endSession();
}
```

2. Retry on transient write conflicts:

```javascript
async function retryOnConflict(operation, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await operation();
    } catch (error) {
      if (error.code === 112 && i < maxRetries - 1) {
        await new Promise(r => setTimeout(r, 100 * Math.pow(2, i)));
        continue;
      }
      throw error;
    }
  }
}
```

3. Use atomic operations to minimize conflict window:

```javascript
// Avoid: read then write
const doc = await db.collection('items').findOne({ _id: id });
await db.collection('items').updateOne({ _id: id }, { $set: { count: doc.count + 1 } });

// Better: single atomic operation
await db.collection('items').updateOne({ _id: id }, { $inc: { count: 1 } });
```

4. Use `replaceOne` with optimistic concurrency:

```javascript
await db.collection('items').replaceOne(
  { _id: id, version: expectedVersion },
  { ...updatedDoc, version: expectedVersion + 1 }
);
```

## Examples

```javascript
// Error: Write conflict error. Try again
const session = client.startSession();
await session.withTransaction(async () => {
  await coll.updateOne({ _id: 1 }, { $inc: { x: 1 } }, { session });
  await coll.updateOne({ _id: 1 }, { $inc: { y: 1 } }, { session });
});
// WriteConflictError: WriteConflict error
```

## Related Errors

- [Timeout error]({{< relref "/tools/mongodb/mongodb-timeout-error" >}})
- [Duplicate key error]({{< relref "/tools/mongodb/mongodb-duplicate-key-v2" >}})
