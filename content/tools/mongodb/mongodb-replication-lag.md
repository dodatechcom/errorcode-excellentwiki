---
title: "[Solution] MongoDB Replication Lag Error"
description: "Fix MongoDB replication lag issues between primary and secondary"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Replication Lag Error

Replication lag is the delay between the primary and secondary:

```
// Primary optime: 2024-01-15T12:00:00Z
// Secondary optime: 2024-01-15T11:50:00Z
// Lag: 10 minutes
```

## Common Causes

- Insufficient network bandwidth between replica set members
- The secondary is under heavy read load
- Write volume exceeds the secondary's replication capacity
- Disk I/O bottleneck on the secondary
- Large operations causing lag
- The oplog is too small

## How to Fix

### 1. Monitor lag continuously

```javascript
rs.status().members.filter(m => m.stateStr === "SECONDARY").forEach(m => {
  const lag = rs.status().date - m.optimeDate;
  print(m.name, "lag:", lag + "ms");
});
```

### 2. Increase oplog size

```javascript
db.adminCommand({ resizeOplog: 1, size: 10240 });
```

### 3. Optimize secondary performance

```bash
# Ensure the secondary has good I/O
iostat -x 1 5

# Check WiredTiger cache pressure
mongosh --eval "db.serverStatus().wiredTiger.cache"
```

### 4. Reduce primary write volume

- Use bulk operations instead of individual inserts
- Batch writes to reduce oplog entries
- Consider sharding for write scaling

## Examples

```bash
# Create a lag monitoring script
mongosh --eval '
  setInterval(() => {
    let status = rs.status();
    status.members.filter(m => m.stateStr === "SECONDARY").forEach(m => {
      let lag = status.date - m.optimeDate;
      let status = lag > 10000 ? "WARNING" : "OK";
      print(`[${status}] ${m.name}: lag ${lag}ms`);
    });
  }, 5000);
'
```