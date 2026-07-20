---
title: "[Solution] MongoDB Write Conflict Error"
description: "Fix MongoDB write conflict errors in transactions"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Write Conflict Error

```
MongoServerError: WriteConflict error: this operation cannot be performed because a storage engine-level conflict is preventing it
```

## Common Causes

- Two concurrent transactions modifying the same document
- A non-transactional write conflicts with a transactional write
- The storage engine detected a conflict between operations
- An operation in a snapshot transaction modified data changed by another transaction

## How to Fix

### 1. Retry on write conflicts (TransientTransactionError)

```javascript
const session = client.startSession();
while (true) {
  try {
    await session.startTransaction();
    await db.users.updateOne({ _id: 1 }, { $inc: { balance: -10 } }, { session });
    await db.accounts.updateOne({ _id: 1 }, { $inc: { balance: 10 } }, { session });
    await session.commitTransaction();
    break;
  } catch (err) {
    if (err.hasErrorLabel("TransientTransactionError")) {
      await session.abortTransaction();
      continue;
    }
    throw err;
  }
}
session.endSession();
```

### 2. Use optimistic concurrency with version fields

```javascript
const doc = await db.users.findOne({ _id: 1 });
const session = client.startSession();
await session.startTransaction();
await db.users.updateOne(
  { _id: 1, version: doc.version },
  { $set: { balance: doc.balance - 10 }, $inc: { version: 1 } },
  { session }
);
await session.commitTransaction();
session.endSession();
```

### 3. Reduce transaction scope

```javascript
// Only include writes that must be atomic in the transaction
// Do reads outside the transaction
```

## Examples

```bash
# Monitor write conflicts
mongosh --eval "db.serverStatus().locks"

# Check for conflicts
mongosh --eval "db.currentOp({active: true, desc: /update/})"
```