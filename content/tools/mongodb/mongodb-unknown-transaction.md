---
title: "[Solution] MongoDB Unknown Transaction Error"
description: "Fix MongoDB unknown transaction errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Unknown Transaction Error

```
MongoServerError: unknown transaction
```

```
MongoServerError: no transaction started
```

## Common Causes

- The transaction was already committed or aborted
- The session ID is invalid
- The transaction was started on a different session
- The session timed out
- The transaction was started on a different connection

## How to Fix

### 1. Start a new transaction

```javascript
const session = client.startSession();
session.startTransaction();
// ... operations ...
await session.commitTransaction();
session.endSession();
```

### 2. Check for active transactions

```javascript
db.currentOp({ "active": true, "desc": /transaction/ })
```

### 3. Handle session reuse properly

```javascript
const session = client.startSession();
try {
  await session.startTransaction();
  await db.users.updateOne({ _id: 1 }, { $inc: { balance: -10 } }, { session });
  await session.commitTransaction();
} catch (err) {
  await session.abortTransaction();
  throw err;
} finally {
  session.endSession();
}
```

## Examples

```bash
# Check current transactions
mongosh --eval "db.currentOp({desc: /transaction/})"

# Check for prepared transactions
mongosh --eval "db.adminCommand({currentOp: true, desc: /prepared/})"
```