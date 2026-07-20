---
title: "[Solution] MongoDB Open Cursor Limit Error"
description: "Fix MongoDB too many open cursors errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Open Cursor Limit Error

```
MongoServerError: too many open cursors
```

```
MongoServerError: number of open cursors exceeds limit
```

## Common Causes

- Cursors are not being closed after use
- The application creates many cursors without consuming results
- Batch size is too small, creating too many cursors
- Long-running cursors accumulate

## How to Fix

### 1. Close cursors when done

```javascript
const cursor = db.users.find({ status: "active" });
try {
  while (await cursor.hasNext()) {
    const doc = await cursor.next();
    // process document
  }
} finally {
  await cursor.close();
}
```

### 2. Increase the cursor limit (temporary)

```javascript
db.adminCommand({ setParameter: 1, cursorTimeoutMillis: 600000 });
```

### 3. Use batchSize to reduce open cursors

```javascript
const cursor = db.users.find().batchSize(1000);
```

### 4. Check current cursor count

```javascript
db.serverStatus().metrics.cursor
```

## Examples

```bash
# Check open cursors
mongosh --eval "db.serverStatus().metrics.cursor"

# Set cursor timeout
mongosh --eval "db.adminCommand({setParameter:1, cursorTimeoutMillis:300000})"

# Kill stale cursors
mongosh --eval "db.adminCommand({killCursors: 'users', cursors: []})"
```