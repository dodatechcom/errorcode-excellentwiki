---
title: "[Solution] MongoDB Snapshot Too Old Error"
description: "Fix MongoDB snapshot too old error when point-in-time reads cannot find the required historical data snapshot"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Snapshot Too Old Error

A read operation requires a historical snapshot that has already been garbage collected. The server can no longer provide the requested consistent point-in-time view.

## Common Causes

- Read transaction started too long ago and its snapshot was evicted
- WiredTiger history store has pruned old snapshots
- Long-running transactions hold snapshots that conflict with cleanup
- SnapshotTooOldTooOldErrors increase due to clock drift or pauses
- WiredTiger cache pressure triggers aggressive snapshot pruning

## How to Fix

### Reduce Snapshot Hold Time

```javascript
// Finish transactions faster to release snapshots
const session = client.startSession();
try {
  const result = await session.withTransaction(async () => {
    // Do work quickly and commit
    return await db.collection('orders').find({}, { session }).toArray();
  }, { maxCommitTimeMS: 30000 });
} finally {
  await session.endSession();
}
```

### Increase WiredTiger History Store Capacity

```javascript
// Check history store statistics
db.serverStatus().wiredTiger

// Increase cache size
db.adminCommand({
  setParameter: 1,
  wiredTigerEngineRuntimeConfig: 'cache_size=4G'
})
```

### Retry on SnapshotTooOld

```javascript
async function readWithRetry(collection, filter, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await collection.find(filter).toArray();
    } catch (err) {
      if (err.code === 240 || err.code === 286) {
        console.log(`Snapshot too old, retry ${i + 1}/${maxRetries}`);
        await new Promise(r => setTimeout(r, 100 * (i + 1)));
        continue;
      }
      throw err;
    }
  }
  throw new Error('Max retries exceeded for snapshot-too-old');
}
```

### Avoid Long Transactions

```javascript
// Instead of one long transaction, use smaller batches
async function processOrders() {
  const cursor = db.collection('orders').find({ processed: false });
  while (await cursor.hasNext()) {
    const batch = [];
    for (let i = 0; i < 100 && await cursor.hasNext(); i++) {
      batch.push(await cursor.next());
    }
    // Process small batch in its own transaction
    const session = client.startSession();
    await session.withTransaction(async () => {
      for (const order of batch) {
        await db.collection('orders').updateOne(
          { _id: order._id },
          { $set: { processed: true } },
          { session }
        );
      }
    });
    await session.endSession();
  }
}
```

## Examples

```
MongoServerError: SnapshotTooOld: Operation failed due to
  snapshot being too old. Increase --wiredTigerEngineRuntimeConfig
  or reduce transaction duration.

MongoServerError: read concern "snapshot" failed:
  history store is too old for requested timestamp
```

## Related Errors

- [MongoDB Transaction Timed Out]({{< relref "/tools/mongodb/mongodb-transaction-timed-out" >}}) -- transaction timeout
- [MongoDB WiredTiger Cache Full]({{< relref "/tools/mongodb/mongodb-wiredtiger-cache-full" >}}) -- cache pressure
- [MongoDB Oplog Too Small]({{< relref "/tools/mongodb/mongodb-oplog-too-small" >}}) -- oplog issues
