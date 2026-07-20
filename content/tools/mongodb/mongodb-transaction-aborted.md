---
title: "[Solution] MongoDB Transaction Aborted"
description: "Fix MongoDB transaction aborted errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Transaction Aborted Error

```
MongoServerError: transaction aborted
```

```
TransactionAborted: caused by TransientTransactionError
```

## Common Causes

- A transient error occurred (network issue, replica set election)
- The transaction timed out
- An operation in the transaction failed
- Write conflict detected
- The server rolled back the transaction

## How to Fix

### 1. Implement retry logic

```javascript
async function executeWithRetry(operation, maxRetries = 3) {
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    const session = client.startSession();
    try {
      await session.startTransaction();
      await operation(session);
      await session.commitTransaction();
      return { success: true };
    } catch (err) {
      await session.abortTransaction();
      if (err.hasErrorLabel("TransientTransactionError") && attempt < maxRetries - 1) {
        continue;
      }
      throw err;
    } finally {
      session.endSession();
    }
  }
}
```

### 2. Use commitTransaction with retryable write concern

```javascript
await session.commitTransaction({
  writeConcern: { w: "majority", wtimeout: 10000 },
  retryWrites: true
});
```

### 3. Check for error labels

```javascript
try {
  await session.commitTransaction();
} catch (err) {
  if (err.hasErrorLabel("TransientTransactionError")) {
    // Safe to retry the entire transaction
  } else if (err.hasErrorLabel("UnknownTransactionCommitResult")) {
    // Commit may have succeeded, check server state
  }
}
```

## Examples

```bash
# Monitor transaction aborts
mongosh --eval "db.serverStatus().metrics.transactions"

# Check for failed transactions
mongosh --eval "db.currentOp({active: true, desc: /transaction/})"
```