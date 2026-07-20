---
title: "[Solution] MongoDB Cursor Not Found Error"
description: "Fix MongoDB cursor not found errors"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
---

## MongoDB Cursor Not Found Error

```
MongoServerError: cursor id not found on server
```

```
MongoServerError: cursor not found (cursor may have timed out)
```

## Common Causes

- The cursor timed out (default 10 minutes of inactivity)
- The server was restarted, destroying all cursors
- The cursor was killed by the server due to resource pressure
- The client tried to use a cursor after a network reconnection

## How to Fix

### 1. Increase the cursor timeout

```javascript
db.adminCommand({ setParameter: 1, cursorTimeoutMillis: 600000 });  // 10 minutes
```

### 2. Use tailable cursors for capped collections

```javascript
const cursor = db.logs.find().sort({ $natural: -1 }).tailable();
```

### 3. Implement retry logic for cursor operations

```javascript
async function iterateCursorWithRetry(collection, query) {
  let cursor = collection.find(query);
  try {
    while (await cursor.hasNext()) {
      const doc = await cursor.next();
      // process
    }
  } catch (err) {
    if (err.message.includes("cursor not found")) {
      // Restart from where we left off if possible
      cursor = collection.find(query);
      // Continue iteration
    }
  }
}
```

### 4. Use noCursorTimeout to prevent automatic closing

```javascript
const cursor = db.users.find().noCursorTimeout();
// Remember to close manually when done
```

## Examples

```bash
# Check cursor statistics
mongosh --eval "db.serverStatus().metrics.cursor"

# List open cursors
mongosh --eval "db.adminCommand({listCommands:1}).commands | grep cursor"

# Create a noCursorTimeout cursor
mongosh --eval '
  db.test.find().noCursorTimeout();
  print("Cursor will not timeout");
'
```