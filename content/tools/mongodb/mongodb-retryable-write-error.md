---
title: "[Solution] MongoDB Retryable Write Error"
description: "Fix MongoDB retryable write errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Retryable Write Error

```
MongoServerError: RetryableWriteError
```

```
MongoNetworkError: connection pool was cleared
```

## Common Causes

- The primary stepped down during a write operation
- Network timeout caused the write to be interrupted
- The server accepted the write but the acknowledgment was lost
- The driver retried the write on a new primary

## How to Fix

### 1. Ensure retryWrites is enabled

```javascript
const client = new MongoClient(uri, {
  retryWrites: true,  // Default in modern drivers
  retryReads: true
});
```

### 2. Handle retryable write errors in code

```javascript
try {
  await db.users.updateOne({ _id: 1 }, { $inc: { counter: 1 } });
} catch (err) {
  if (err.hasErrorLabel("RetryableWriteError")) {
    // The driver should have retried automatically
    // If it still fails, manually retry
    await db.users.updateOne({ _id: 1 }, { $inc: { counter: 1 } });
  }
}
```

### 3. Use write concern with retryable writes

```javascript
await db.users.insertOne(
  { name: "test" },
  { writeConcern: { w: "majority" } }
);
```

### 4. Check for connection pool issues

```javascript
db.serverStatus().connections
```

## Examples

```bash
# Check retryable writes configuration
mongosh --eval "db.adminCommand({getParameter:1, retryableWritesEnabled:1})"

# Monitor connection pool
mongosh --eval "db.serverStatus().connections"

# Test a retryable write
mongosh --eval '
  db.test.drop();
  db.test.insertOne({a:1});
  print("Write succeeded");
'
```