---
title: "[Solution] MongoDB Oplog Full Error"
description: "Fix MongoDB oplog full errors causing replication to stop"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Oplog Full Error

```
// Oplog is full, secondary cannot catch up
// Replication has stopped
```

## Common Causes

- The write volume exceeds the oplog capacity
- The secondary was down and needs more oplog data than available
- The oplog size was not configured appropriately

## How to Fix

### 1. Check oplog usage

```javascript
rs.printReplicationInfo()
// Output shows the time range covered by the oplog
```

### 2. Resize the oplog

```javascript
// On the primary
db.adminCommand({ resizeOplog: 1, size: 10240 });  // 10 GB
```

### 3. Force a resync on the secondary

```bash
# If the secondary is too far behind
mongosh --eval "db.adminCommand({resync: 1})" --host secondary
```

### 4. Monitor oplog usage regularly

```javascript
// Check oplog stats
db.getReplicationInfo()
```

## Examples

```bash
# Check oplog coverage
mongosh --eval "rs.printReplicationInfo()"

# Check secondary lag
mongosh --eval "rs.printSecondaryReplicationInfo()"

# Get detailed oplog stats
mongosh --eval "db.getReplicationInfo()"

# Monitor continuously
watch -n 10 "mongosh --quiet --eval 'rs.printReplicationInfo()'"
```