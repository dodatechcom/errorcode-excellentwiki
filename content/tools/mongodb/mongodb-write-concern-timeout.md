---
title: "[Solution] MongoDB Write Concern Timeout"
description: "Fix write concern timeout errors during write operations"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Write Concern Timeout Error

A write concern timeout occurs when the server does not satisfy the write concern within the specified time:

```
MongoServerError: operation exceeded time limit for write concern
```

```
WriteConcernError: operation timed out, write concern: { w: "majority", wtimeout: 5000 }
```

## Common Causes

- The `wtimeout` value is too low for current network/server conditions
- A replica set member is slow to acknowledge writes
- The majority is not available (replica set degraded)
- Network latency between the primary and secondary members
- The server is under heavy write load

## How to Fix

### 1. Increase the wtimeout value

```javascript
await db.users.insertOne(
  { name: "John" },
  { writeConcern: { w: "majority", wtimeout: 30000 } }  // 30 seconds
);
```

### 2. Use a less strict write concern for non-critical writes

```javascript
// Less strict: wait for primary only
await db.logs.insertMany(docs, { writeConcern: { w: 1 } });

// Or fire-and-forget (not recommended for critical data)
await db.logs.insertMany(docs, { writeConcern: { w: 0 } });
```

### 3. Set a global write concern

```javascript
db.adminCommand({
  setDefaultWriteConcern: { w: "majority", wtimeout: 30000 }
});
```

### 4. Check replica set health

```javascript
rs.status().members.forEach(m => {
  print(m.name, m.stateStr, m.optimeDate, m.lastHeartbeat);
});
```

## Examples

```bash
# Check current write concern settings
mongosh --eval "db.adminCommand({getDefaultWriteConcern:1})"

# Insert with specific write concern
mongosh --eval '
  db.test.insertOne(
    { data: "test" },
    { writeConcern: { w: "majority", wtimeout: 5000, j: true } }
  )
'

# Monitor replica set lag (cause of write concern timeouts)
mongosh --eval '
  rs.status().members.filter(m => m.stateStr === "SECONDARY").forEach(m => {
    print(m.name, "lag:", (rs.status().date - m.optimeDate) + "ms");
  })
'
```