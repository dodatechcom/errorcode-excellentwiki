---
title: "[Solution] MongoDB Stale Secondary Error"
description: "Fix MongoDB stale secondary errors during reads"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Stale Secondary Error

A stale secondary has fallen too far behind the primary:

```
MongoServerError: command secondaryAllowed : stale
```

## Common Causes

- The secondary cannot keep up with the primary's write volume
- Network latency between primary and secondary
- The secondary is performing heavy read operations
- The oplog is too small to retain the necessary operations
- The secondary was down for too long and needs to resync

## How to Fix

### 1. Check replication lag

```javascript
rs.printReplicationInfo()    // Primary's oplog
rs.printSecondaryReplicationInfo()  // Secondary's lag
```

### 2. Increase the oplog size

```bash
mongosh --eval '
  db.adminCommand({
    resizeOplog: 1,
    size: 10240  // 10 GB
  });
'
```

### 3. Reduce read load on secondaries

```javascript
const client = new MongoClient(uri, {
  readPreference: 'primary'
});
```

### 4. Monitor and fix replication lag

```bash
mongosh --eval '
  let primary = rs.printReplicationInfo();
  let secondary = rs.printSecondaryReplicationInfo();
'
```

### 5. Resync a severely lagging secondary

```bash
# On the lagging secondary
mongosh --eval "db.adminCommand({resync: 1})"
```

## Examples

```bash
# Check replication status
mongosh --eval "rs.printReplicationInfo()"
mongosh --eval "rs.printSecondaryReplicationInfo()"

# Check oplog size and usage
mongosh --eval '
  let stats = db.replicationInfo();
  print("Oplog size:", stats.logSizeMB, "MB");
  print("Used:", stats.usedMB, "MB");
  print("Time window:", stats.tFirst, "to", stats.tLast);
'
```