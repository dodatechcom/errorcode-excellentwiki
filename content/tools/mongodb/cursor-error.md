---
title: "MongoDB CursorNotFound: cursor not found"
description: "MongoDB server loses a cursor because it timed out or was killed during a long-running query"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

This error occurs when a client tries to fetch the next batch of results from a cursor, but the server has already closed it. The cursor may have timed out due to inactivity or been killed explicitly.

## Common Causes

- Cursor idle timeout exceeded (default 10 minutes)
- Client took too long between `batchSize` fetches
- Another process killed the cursor
- Large result sets without proper batching

## How to Fix

1. Increase the cursor timeout:

```javascript
const cursor = db.users.find().noCursorTimeout()
```

2. Use `tailable` cursors for capped collections:

```javascript
const cursor = db.events.find().addOption(0x2 /* DBQuery.tailable */)
```

3. Use `batchSize` to control how many documents are returned per request:

```javascript
const cursor = db.users.find().batchSize(1000)
while (await cursor.hasNext()) {
  const batch = await cursor.next()
}
```

4. Close cursors explicitly when done:

```javascript
await cursor.close()
```

## Examples

```javascript
const cursor = db.users.find({ status: "active" })
// ... application processes other work for > 10 minutes ...
await cursor.next()
// CursorNotFound: cursor id not found on server
```

## Related Errors

- [MongoDB operation timed out](/tools/mongodb/timeout-error)
