---
title: "[Solution] MongoDB Network Timeout Error"
description: "Fix MongoDB network timeout errors during operations"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Network Timeout Error

A network timeout occurs when a socket operation does not complete in time:

```
MongoNetworkError: connection 5 to mongo.example.com:27017 timed out
```

```
MongoNetworkError: Socket was unexpectedly closed
```

## Common Causes

- The server is under heavy load and cannot respond in time
- A long-running operation blocks the socket
- Network congestion between client and server
- The default socket timeout is too short for the workload
- Firewall is rate-limiting or dropping connections
- The server is performing a long compaction or checkpoint

## How to Fix

### 1. Increase the socket timeout

```javascript
const client = new MongoClient(uri, {
  socketTimeoutMS: 120000,   // 2 minutes
  connectTimeoutMS: 15000,
  serverSelectionTimeoutMS: 30000
});
```

### 2. Break large operations into smaller batches

```javascript
// Instead of inserting 1M documents at once
const batchSize = 1000;
for (let i = 0; i < documents.length; i += batchSize) {
  const batch = documents.slice(i, i + batchSize);
  await collection.insertMany(batch);
}
```

### 3. Optimize queries causing long-running operations

```javascript
// Add indexes to prevent full collection scans
db.users.createIndex({ email: 1 });

// Use .explain() to check query plans
db.users.find({ email: "test@example.com" }).explain("executionStats");
```

### 4. Monitor server health

```bash
# Check for slow operations
grep "Slow query" /var/log/mongodb/mongod.log | tail -20

# Check server status
mongosh --eval "db.serverStatus()"
```

## Examples

```bash
# Test with an extended timeout
mongosh --eval "db.runCommand({ping:1})" --socketTimeoutMS 60000

# Check for network issues
mtr mongo.example.com

# Monitor current operations
mongosh --eval "db.currentOp()"

# Kill long-running operations
mongosh --eval "db.killOp(<opId>)"
```