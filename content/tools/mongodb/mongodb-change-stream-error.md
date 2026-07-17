---
title: "MongoDB Change Stream Error"
description: "MongoDB change stream encounters errors during real-time event watching."
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# MongoDB Change Stream Error

A MongoDB change stream error occurs when the real-time event watching mechanism encounters issues. Change streams allow applications to watch for changes in collections, databases, or clusters.

## Common Causes

- Change stream resume token expired
- Replica set or sharded cluster not configured
- Network interruption during change stream
- Event document exceeds 16MB limit

## How to Fix

### Check Change Stream Support

```javascript
// Requires replica set or sharded cluster
db.collection.watch()
```

### Handle Resume Token

```javascript
const pipeline = [];
const options = { fullDocument: 'updateLookup' };

const changeStream = db.collection.watch(pipeline, options);

changeStream.on('change', (change) => {
  console.log(change);
  // Save resume token
  resumeToken = change._id;
});

// Resume from token
const changeStream = db.collection.watch(pipeline, {
  resumeAfter: resumeToken
});
```

### Handle Errors

```javascript
const changeStream = db.collection.watch();
changeStream.on('error', (error) => {
  console.log('Change stream error:', error);
  // Reconnect with resume token
});
```

### Check Replica Set Status

```javascript
rs.status()
// Ensure replica set is healthy
```

### Handle Network Interruptions

```javascript
async function watchWithRetry(collection) {
  try {
    const stream = collection.watch();
    for await (const change of stream) {
      console.log(change);
    }
  } catch (e) {
    console.log('Stream interrupted, reconnecting...');
    await watchWithRetry(collection);
  }
}
```

## Examples

```javascript
// Resume token expired
MongoServerError: Resume of change stream was not possible
// Resume token not found in oplog

// Fix: start new change stream without resume token
const stream = collection.watch();
```

## Related Errors

- [Connection Error]({{< relref "/tools/mongodb/mongodb-connection-error" >}}) — connection failure
- [Replica Set Error]({{< relref "/tools/mongodb/mongodb-replica-set-error" >}}) — replica set issue
