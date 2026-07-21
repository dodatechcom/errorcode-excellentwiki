---
title: "[Solution] MongoDB Transaction Size Limit Error"
description: "Fix MongoDB transaction size limit error when transaction oplog entry exceeds the 16MB limit"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Transaction Size Limit Error

A transaction fails because its total oplog entry exceeds the 16MB size limit. Too many operations or large document modifications within a single transaction cause this error.

## Common Causes

- Too many write operations in a single transaction
- Large documents are updated multiple times within the transaction
- Transaction processes thousands of documents at once
- Nested updates create large oplog entries
- Array modifications that significantly change document size

## How to Fix

### Batch Operations into Smaller Transactions

```javascript
async function processInBatches(items, batchSize = 500) {
  for (let i = 0; i < items.length; i += batchSize) {
    const batch = items.slice(i, i + batchSize);
    const session = client.startSession();

    try {
      await session.withTransaction(async () => {
        for (const item of batch) {
          await db.collection('orders').updateOne(
            { _id: item._id },
            { $set: { processed: true, result: item.result } },
            { session }
          );
        }
      });
    } finally {
      await session.endSession();
    }
  }
}
```

### Reduce Document Modification Size

```javascript
// Instead of updating all fields at once, update only what changed
// Bad: rewrites entire document
await db.collection('users').updateOne(
  { _id: userId },
  { $set: fullUserObject },
  { session }
);

// Good: update only changed fields
await db.collection('users').updateOne(
  { _id: userId },
  { $set: { lastLogin: new Date(), loginCount: { $inc: 1 } } },
  { session }
);
```

### Use Bulk Write Outside Transaction

```javascript
// For independent writes, skip the transaction
await db.collection('orders').bulkWrite(
  items.map(item => ({
    updateOne: {
      filter: { _id: item._id },
      update: { $set: { status: 'shipped' } }
    }
  })),
  { ordered: false }
);
```

## Examples

```
MongoServerError: Total size of oplog entries in transaction
  exceeds 16MB limit. Operation count: 8547, estimated size: 18.3MB

MongoServerError: Transaction too large.
  Reduce the number of operations per transaction.
```

## Related Errors

- [MongoDB Transaction Too Large]({{< relref "/tools/mongodb/mongodb-transaction-too-large" >}}) -- transaction size
- [MongoDB Transaction Timed Out]({{< relref "/tools/mongodb/mongodb-transaction-timed-out" >}}) -- timeouts
- [MongoDB Bulk Write Error]({{< relref "/tools/mongodb/mongodb-bulk-write-error" >}}) -- bulk write issues
