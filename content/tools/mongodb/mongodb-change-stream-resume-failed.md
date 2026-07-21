---
title: "[Solution] MongoDB Change Stream Resume Failed Error"
description: "Fix MongoDB change stream resume failed error when the resume token is no longer available in the oplog"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Change Stream Resume Failed Error

A change stream cannot resume because the resume token references an oplog entry that has been deleted. The server no longer has the data needed to replay missed events.

## Common Causes

- Oplog is too small and rolls over before the client reconnects
- Client was disconnected for longer than the oplog window
- Resume token is from a dropped collection or sharded namespace
- Replica set member was offline past the oplog retention period
- Oplog size was reduced while change streams were active

## How to Fix

### Increase Oplog Size

```javascript
// Check current oplog size
rs.printReplicationInfo()

// Increase oplog size on a replica set member
use local
db.runCommand({
  replSetResizeOplog: 1,
  size: 10240,  // 10GB in MB
  $maxSize: 20480  // 20GB max in MB
})
```

### Track Resume Token Progress

```javascript
const changeStream = db.collection('orders').watch([], {
  fullDocument: 'updateLookup'
});

changeStream.on('change', (change) => {
  // Save the resume token periodically
  fs.writeFileSync('resume-token.json', JSON.stringify({
    _data: change._id._data
  }));
});
```

### Handle Resume Failure Gracefully

```javascript
async function startWatching() {
  let resumeToken = loadSavedToken();
  const pipeline = [];

  try {
    const options = resumeToken
      ? { resumeAfter: resumeToken }
      : {};

    const stream = db.collection('orders').watch(pipeline, options);

    stream.on('change', (change) => {
      processChange(change);
      saveResumeToken(change._id._data);
    });

    stream.on('error', async (err) => {
      if (err.code === 286 || err.code === 280) {
        console.log('Resume token stale, starting from now');
        const freshStream = db.collection('orders').watch(pipeline, {
          startAfter: undefined  // start from current
        });
        freshStream.on('change', (change) => {
          processChange(change);
          saveResumeToken(change._id._data);
        });
      }
    });
  } catch (err) {
    console.error('Change stream error:', err);
  }
}
```

## Examples

```
MongoServerError: Plan executor error during command in safemode :
  caused by "resume token not found in oplog"

ChangeStreamStopped:Resume of change stream was not able to be resumed.
  The resume token was not found in the oplog.
```

## Related Errors

- [MongoDB Oplog Full]({{< relref "/tools/mongodb/mongodb-oplog-full" >}}) -- oplog capacity issue
- [MongoDB Change Stream Error]({{< relref "/tools/mongodb/mongodb-change-stream-error" >}}) -- general change stream issues
- [MongoDB Replication Lag]({{< relref "/tools/mongodb/mongodb-replication-lag" >}}) -- replica set lag
