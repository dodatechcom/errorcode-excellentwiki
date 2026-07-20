---
title: "[Solution] MongoDB Prepared Transaction Error"
description: "Fix MongoDB prepared transaction errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Prepared Transaction Error

```
MongoServerError: cannot prepare transaction in a different session
```

```
Transaction has already been prepared
```

## Common Causes

- The transaction was prepared on a different session
- Trying to prepare an already prepared transaction
- The prepared transaction was rolled back by the server
- Session migration failed during failover

## How to Fix

### 1. Use the same session for prepare and commit

```javascript
const session = client.startSession();
await session.startTransaction();
// ... operations ...
await session.commitTransaction({ prepareCommit: true });  // Prepare
// Later, on the same session
await session.commitTransaction();  // Commit
session.endSession();
```

### 2. Handle prepared transaction recovery after failover

```javascript
// After a failover, the server will roll back prepared transactions
// Check server logs for recovery information
```

### 3. Set transaction lifetime appropriately

```javascript
db.adminCommand({
  setParameter: 1,
  transactionLifetimeLimitSeconds: 120
});
```

## Examples

```bash
# Check for prepared transactions
mongosh --eval "db.adminCommand({currentOp: true, desc: /prepared/})"

# Check transaction recovery
grep -i "prepared transaction" /var/log/mongodb/mongod.log | tail -10
```