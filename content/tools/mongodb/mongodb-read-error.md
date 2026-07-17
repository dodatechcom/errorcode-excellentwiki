---
title: "MongoDB Read Error"
description: "MongoDB read operation fails due to network issues, timeouts, or query errors."
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
tags: ["mongodb", "read", "query", "find", "timeout"]
weight: 5
---

# MongoDB Read Error

A MongoDB read error occurs when a read operation (find, aggregate, count) fails. This can be caused by network timeouts, query errors, or read preference issues.

## Common Causes

- Read timeout exceeded
- Query exceeds maximum document size
- Read preference points to unavailable node
- Index missing for query

## How to Fix

### Increase Read Timeout

```javascript
const client = new MongoClient(uri, {
  serverSelectionTimeoutMS: 5000,
  socketTimeoutMS: 60000,
});
```

### Optimize Queries with Indexes

```javascript
// Check query plan
db.collection.find({ email: 'user@example.com' }).explain('executionStats')

// Create index
db.collection.createIndex({ email: 1 })
```

### Fix Read Preference

```javascript
const collection = client.db('mydb').collection('users');
const cursor = collection.find({}).readPreference('secondaryPreferred');
```

### Handle Network Errors

```javascript
try {
  const result = await collection.find({}).toArray();
} catch (e) {
  if (e.name === 'MongoNetworkError') {
    console.log('Network issue, retrying...');
  }
}
```

### Limit Query Results

```javascript
// Use limit to prevent oversized responses
db.collection.find({}).limit(100)
```

## Examples

```javascript
// Query timeout
MongoServerError: operation exceeded time limit

// Missing index
MongoServerError: executor error during find: Overflow sort stage
```

## Related Errors

- [Connection Error]({{< relref "/tools/mongodb/mongodb-connection-error" >}}) — connection failure
- [Timeout Error]({{< relref "/tools/mongodb/timeout-error" >}}) — operation timeout
