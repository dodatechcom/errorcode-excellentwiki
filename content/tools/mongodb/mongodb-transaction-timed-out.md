---
title: "[Solution] MongoDB Transaction Timed Out"
description: "Fix MongoDB transaction timeout errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Transaction Timed Out Error

```
MongoServerError: transaction timeout
```

```
TransactionAborted: transaction timed out after 60 seconds
```

## Common Causes

- The transaction ran longer than the default lifetime (60 seconds)
- Lock contention caused the transaction to wait too long
- Network delays between operations
- Deadlock detected in multi-document transactions

## How to Fix

### 1. Increase transaction lifetime

```javascript
db.adminCommand({
  setParameter: 1,
  transactionLifetimeLimitSeconds: 120  // 2 minutes
});
```

### 2. Keep transactions short

```javascript
// Do reads outside the transaction, then start transaction for writes only
const user = await db.users.findOne({ _id: 1 });
// ... processing ...
const session = client.startSession();
await session.startTransaction();
await db.users.updateOne({ _id: 1 }, { $set: { balance: newBalance } }, { session });
await db.accounts.updateOne({ _id: "checking" }, { $inc: { total: -10 } }, { session });
await session.commitTransaction();
session.endSession();
```

### 3. Add retry logic for transient transaction errors

```javascript
async function runTransactionWithRetry(fn) {
  while (true) {
    const session = client.startSession();
    try {
      await session.startTransaction();
      await fn(session);
      await session.commitTransaction();
      return;
    } catch (err) {
      if (err.errorLabels && err.errorLabels.includes("TransientTransactionError")) {
        continue; // Retry
      }
      await session.abortTransaction();
      throw err;
    } finally {
      session.endSession();
    }
  }
}
```

## Examples

```bash
# Check transaction timeout settings
mongosh --eval "db.adminCommand({getParameter:1, transactionLifetimeLimitSeconds:1})"

# Monitor transaction performance
mongosh --eval "db.currentOp({active: true, desc: /transaction/})"
```