---
title: "[Solution] MongoDB Oplog Too Small Error"
description: "Fix MongoDB oplog too small errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Oplog Too Small Error

```
// Secondary cannot keep up because the oplog is too small
// Oplog window: 24 hours (insufficient for the workload)
```

## Common Causes

- The oplog size is too small for the write volume
- The secondary was down for too long and the required operations rolled off the oplog
- Heavy write operations fill the oplog quickly

## How to Fix

### 1. Check the current oplog size

```javascript
rs.printReplicationInfo()
```

### 2. Increase the oplog size

```javascript
db.adminCommand({
  resizeOplog: 1,
  size: 10240  // 10 GB
});
```

### 3. Monitor oplog window

```javascript
let primaryLog = rs.printReplicationInfo();
let secondaryLog = rs.printSecondaryReplicationInfo();
```

### 4. Reduce oplog usage

- Use bulk operations instead of individual writes
- Reduce the amount of data written
- Use `w: 1` write concern for non-critical writes

## Examples

```bash
# Check oplog size and window
mongosh --eval "rs.printReplicationInfo()"
mongosh --eval "rs.printSecondaryReplicationInfo()"

# Check oplog stats
mongosh --eval "db.printReplicationInfo()"

# Resize oplog
mongosh --eval "db.adminCommand({resizeOplog: 1, size: 20480})"
```