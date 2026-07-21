---
title: "[Solution] MongoDB Parallel Scan Error"
description: "Fix MongoDB parallel scan error when concurrent scan cursors exceed the maximum allowed per collection"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Parallel Scan Error

MongoDB limits the number of parallel scan cursors per collection. When too many concurrent scans are opened, new scans are rejected with an error.

## Common Causes

- Too many concurrent parallel scans on a single collection
- Long-running cursors hold their scan slot while processing slowly
- Application creates a new scan cursor for each request without closing old ones
- Multiple workers scan the same collection simultaneously
- Default limit of 100 parallel scans per collection is reached

## How to Fix

### Close Unused Cursors

```javascript
const cursor = db.collection('orders').find({ status: 'pending' });

// Process results and close promptly
try {
  while (await cursor.hasNext()) {
    const doc = await cursor.next();
    await processDocument(doc);
  }
} finally {
  await cursor.close();
}
```

### Use Batch Processing Instead

```javascript
async function processInBatches(collection, filter, batchSize = 1000) {
  let processed = 0;
  let lastId = null;

  while (true) {
    const query = lastId
      ? { ...filter, _id: { $gt: lastId } }
      : filter;

    const batch = await collection.find(query)
      .sort({ _id: 1 })
      .limit(batchSize)
      .toArray();

    if (batch.length === 0) break;

    for (const doc of batch) {
      await processDocument(doc);
    }

    lastId = batch[batch.length - 1]._id;
    processed += batch.length;
  }

  return processed;
}
```

### Increase Parallel Scan Limit

```javascript
// Check current limit
db.adminCommand({ setParameter: 1, internalQueryMaxParallelScanSlots: 200 })
```

## Examples

```
MongoServerError: Too many parallel scans on collection "orders".
  Current limit: 100, active scans: 100

MongoQueryPlanError: cannot open new parallel scan cursor --
  collection limit exceeded for orders
```

## Related Errors

- [MongoDB Open Cursor Limit]({{< relref "/tools/mongodb/mongodb-open-cursor-limit" >}}) -- cursor limits
- [MongoDB Cursor Not Found]({{< relref "/tools/mongodb/mongodb-cursor-not-found" >}}) -- cursor issues
- [MongoDB Operation Timed Out]({{< relref "/tools/mongodb/mongodb-operation-timed-out" >}}) -- timeouts
