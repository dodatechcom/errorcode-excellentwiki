---
title: "[Solution] MongoDB Snapshot Unavailable Error"
description: "Fix MongoDB snapshot unavailable errors in transactions"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Snapshot Unavailable Error

```
MongoServerError: SnapshotUnavailable
```

```
MongoServerError: cannot provide snapshot when timestamp is too old
```

## Common Causes

- The oplog has rolled over and the required snapshot timestamp is no longer available
- The transaction ran for too long and the snapshot is stale
- The oplog size is too small for the workload

## How to Fix

### 1. Increase the oplog size

```javascript
db.adminCommand({ resizeOplog: 1, size: 10240 });  // 10 GB
```

### 2. Keep transactions short

```javascript
// Read needed data first, then start transaction
const docs = await db.users.find({ status: "active" }).toArray();
// Process outside transaction
const processed = docs.map(d => processDoc(d));
// Start transaction only for writes
const session = client.startSession();
await session.startTransaction();
for (const doc of processed) {
  await db.users.updateOne({ _id: doc._id }, { $set: doc }, { session });
}
await session.commitTransaction();
session.endSession();
```

### 3. Use `startAtOperationTime` carefully

```javascript
// Don't start transactions too far in the past
const session = client.startSession({
  snapshot: { readConcern: { level: "snapshot" } }
});
```

## Examples

```bash
# Check oplog window
mongosh --eval "rs.printReplicationInfo()"

# Check if snapshot timestamp is available
mongosh --eval "db.adminCommand({getOptime: 1})"
```