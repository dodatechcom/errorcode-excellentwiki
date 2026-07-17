---
title: "MongoDB Operation Timeout"
description: "MongoDB operation fails due to timeout exceeded."
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
tags: ["mongodb", "timeout", "slow", "performance", "latency"]
weight: 5
---

# MongoDB Operation Timeout

A MongoDB timeout error occurs when an operation exceeds the configured timeout limit. This can be caused by slow queries, network latency, or overloaded servers.

## Common Causes

- Slow queries without proper indexes
- Network latency to MongoDB server
- Server overloaded with too many operations
- Too large result set

## How to Fix

### Increase Timeout

```javascript
const client = new MongoClient(uri, {
  serverSelectionTimeoutMS: 30000,
  socketTimeoutMS: 120000,
  connectTimeoutMS: 30000,
});
```

### Add Indexes for Common Queries

```javascript
db.collection.createIndex({ field: 1 })
db.collection.createIndex({ field1: 1, field2: 1 })
```

### Use Explain to Analyze Slow Queries

```javascript
db.collection.find({ name: 'test' }).explain('executionStats')
```

### Optimize Query Patterns

```javascript
// Use projection to limit returned fields
db.collection.find({ name: 'test' }, { name: 1, email: 1 })

// Use limit
db.collection.find({}).limit(100)
```

### Check Server Status

```javascript
db.serverStatus()
db.currentOp()
```

## Examples

```javascript
// Connection timeout
MongoServerSelectionError: connect ECONNREFUSED 127.0.0.1:27017

// Operation timeout
MongoServerError: operation timed out
```

## Related Errors

- [Connection Error]({{< relref "/tools/mongodb/mongodb-connection-error" >}}) — connection failure
- [Read Error]({{< relref "/tools/mongodb/mongodb-read-error" >}}) — read operation error
