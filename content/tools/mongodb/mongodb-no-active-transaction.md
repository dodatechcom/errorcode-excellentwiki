---
title: "[Solution] MongoDB No Active Transaction"
description: "Fix MongoDB no active transaction errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB No Active Transaction Error

```
MongoServerError: no active transaction to commit
```

```
MongoServerError: cannot commit in a transaction without starting one
```

## Common Causes

- Trying to commit without starting a transaction
- The transaction was already committed or aborted
- The session was ended before commit
- The session timed out and the transaction was aborted

## How to Fix

### 1. Always start a transaction before committing

```javascript
const session = client.startSession();
await session.startTransaction();  // Must start first
// ... operations ...
await session.commitTransaction();  // Then commit
session.endSession();
```

### 2. Check session state before operations

```javascript
if (session.inTransaction()) {
  await session.commitTransaction();
} else {
  console.log("No active transaction");
}
```

### 3. Handle errors properly

```javascript
try {
  await session.startTransaction();
  await db.users.updateOne({ _id: 1 }, { $set: { balance: 90 } }, { session });
  await session.commitTransaction();
} catch (err) {
  // If commit fails, the transaction may already be aborted
  if (!err.message.includes("cannot commit")) {
    await session.abortTransaction();
  }
} finally {
  session.endSession();
}
```

## Examples

```bash
# Test transaction lifecycle
mongosh --eval '
  const session = db.getMongo().startSession();
  session.startTransaction();
  db.test.insertOne({a:1}, {session});
  session.commitTransaction();
  print("Transaction committed successfully");
  session.endSession();
'
```