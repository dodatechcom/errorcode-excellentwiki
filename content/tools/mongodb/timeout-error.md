---
title: "MongoDB operation timed out"
description: "MongoDB client or server times out waiting for a response during a database operation"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

This error occurs when a MongoDB operation exceeds the configured timeout limit. The client or server aborts the operation before it completes.

## Common Causes

- Query is too slow due to missing indexes or full collection scan
- Network latency between application and MongoDB server
- TimeoutMS set too low in connection options
- Server is under heavy load and cannot respond in time

## How to Fix

1. Increase the operation timeout:

```javascript
db.users.find({ email: "user@example.com" }).maxTimeMS(10000)
```

2. Add an index to speed up slow queries:

```javascript
db.users.createIndex({ email: 1 })
```

3. Set a longer timeout in the connection options:

```javascript
const client = new MongoClient(uri, {
  serverSelectionTimeoutMS: 30000,
  socketTimeoutMS: 30000
})
```

4. Profile slow operations:

```javascript
db.setProfilingLevel(1, { slowms: 100 })
db.system.profile.find().sort({ ts: -1 }).limit(5).pretty()
```

## Examples

```javascript
// Query without index on large collection times out
await db.users.find({ email: "user@example.com" }).maxTimeMS(5000)
// MongoServerError: operation exceeded time limit
```

## Related Errors

- [Connection Refused](/tools/mongodb/connection-refused)
