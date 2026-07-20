---
title: "[Solution] MongoDB Transaction Too Large Error"
description: "Fix MongoDB transaction exceeds size limits"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Transaction Too Large Error

```
MongoServerError: oplog is too large for this transaction
```

```
Transaction too large, cannot fit in memory
```

## Common Causes

- Too many write operations in a single transaction
- Writing large documents in a transaction
- The oplog cannot accommodate the transaction's operations
- Multiple collections with large writes in one transaction

## How to Fix

### 1. Break large transactions into smaller ones

```javascript
// Instead of one large transaction
const BATCH_SIZE = 100;
for (let i = 0; i < documents.length; i += BATCH_SIZE) {
  const session = client.startSession();
  await session.startTransaction();
  for (const doc of documents.slice(i, i + BATCH_SIZE)) {
    await db.users.updateOne({ _id: doc._id }, { $set: doc }, { session });
  }
  await session.commitTransaction();
  session.endSession();
}
```

### 2. Use write concern at transaction level

```javascript
await session.commitTransaction({ writeConcern: { w: "majority" } });
```

### 3. Reduce document sizes in transactions

```javascript
// Only update necessary fields
await db.users.updateOne({ _id: 1 }, { $set: { balance: newBalance } }, { session });
// Instead of replacing the entire document
```

## Examples

```bash
# Check transaction size limits
mongosh --eval "db.adminCommand({getParameter:1, transactionLifetimeLimitSeconds:1})"

# Monitor active transactions
mongosh --eval "db.currentOp({desc: /transaction/})"
```