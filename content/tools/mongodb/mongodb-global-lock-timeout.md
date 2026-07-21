---
title: "[Solution] MongoDB Global Lock Timeout Error"
description: "Fix MongoDB global lock timeout error when the database-level lock is held too long blocking all operations"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Global Lock Timeout Error

A global lock timeout occurs when the database-wide lock is held too long by one operation, blocking all other operations on that database. In WiredTiger, this surfaces as an admin lock contention issue.

## Common Causes

- Long-running operations hold the global lock (e.g., compact, repair, drop)
- DDL operations block while metadata is being updated
- High write load causes WiredTiger checkpoint lock contention
- Background index builds compete with foreground operations
- fsyncLock is held during backup operations

## How to Fix

### Use Background Operations

```javascript
// Build indexes in the background
db.collection('orders').createIndex(
  { createdAt: -1 },
  { background: true }
)

// For MongoDB 4.2+, index builds are non-blocking by default
db.collection('orders').createIndex({ createdAt: -1 })
```

### Avoid Long Locks During Backup

```javascript
// Use filesystem snapshots instead of fsyncLock
// If you must use fsyncLock, keep it brief
db.fsyncLock()
// ... perform snapshot ...
db.fsyncUnlock()
```

### Monitor Lock Waiters

```javascript
db.adminCommand({ currentOp: 1, desc: /lock/ })

// Check global lock statistics
db.serverStatus().locks
```

### Use readPreference Secondary for Heavy Reads

```javascript
const client = new MongoClient(uri, {
  readPreference: 'secondaryPreferred'
});
```

## Examples

```
MongoServerError: command { compact: 1 } was interrupted
  because global lock was held for too long

MongoDB has been shutting down due to global lock timeout
  db.fsyncLock() exceeded maximum duration
```

## Related Errors

- [MongoDB Operation Timed Out]({{< relref "/tools/mongodb/mongodb-operation-timed-out" >}}) -- operation timeout
- [MongoDB Write Concern Timeout]({{< relref "/tools/mongodb/mongodb-write-concern-timeout" >}}) -- write concern
- [MongoDB Transaction Timed Out]({{< relref "/tools/mongodb/mongodb-transaction-timed-out" >}}) -- transaction timeout
