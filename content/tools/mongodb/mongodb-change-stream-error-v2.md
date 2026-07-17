---
title: "MongoDB - change stream resume error"
description: "MongoDB change stream fails to resume from a saved resume token due to oplog window expiration or token invalidation"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
tags: ["mongodb", "change-stream", "resume", "oplog", "token", "watch"]
weight: 5
---

A change stream resume error occurs when MongoDB cannot resume a change stream from a previously saved resume token. This typically happens when the oplog entry referenced by the token has been overwritten or the token is no longer valid.

## Common Causes

- Resume token too old and oplog entry has been truncated
- Replica set member lost data during failover
- `resumeAfter` token from a dropped collection
- Oplog size too small for the change stream's idle period
- Token corruption or serialization error

## How to Fix

1. Use `startAfter` instead of `resumeAfter` for resilience:

```javascript
const resumeToken = await getLastSavedToken();
const changeStream = db.collection('events').watch([], {
  startAfter: resumeToken, // more resilient than resumeAfter
});
```

2. Handle resume failures gracefully:

```javascript
async function watchWithResume(collection) {
  let resumeToken = await getLastSavedToken();

  while (true) {
    try {
      const changeStream = collection.watch([], {
        resumeAfter: resumeToken,
      });

      for await (const change of changeStream) {
        await processChange(change);
        resumeToken = change._id;
        await saveResumeToken(resumeToken);
      }
    } catch (error) {
      if (error.code === 286 || error.code === 260) {
        console.log('Resume token invalidated, starting from latest');
        resumeToken = null;
        await saveResumeToken(null);
      } else {
        throw error;
      }
    }
  }
}
```

3. Increase oplog size to keep resume tokens valid longer:

```javascript
// On replica set member
use local
db.runCommand({
  replSetResizeOplog: 1,
  size: 1024 * 1024 * 1024 * 10 // 10GB
});
```

4. Save resume tokens frequently:

```javascript
const pipeline = [
  { $match: { 'fullDocument.status': 'active' } },
];
const changeStream = db.collection('orders').watch(pipeline);

changeStream.on('change', async (change) => {
  await saveResumeToken(change._id);
  await processOrderChange(change);
});
```

## Examples

```javascript
// Error: resume token from a change stream that has been deleted
const token = { _data: '8263...' };
const stream = db.collection('users').watch([], {
  resumeAfter: token,
});
// MongoError: resume token from a change stream that has been removed

// Fix: catch and restart without token
try {
  const stream = db.collection('users').watch([], { resumeAfter: token });
} catch (err) {
  const stream = db.collection('users').watch(); // start fresh
}
```

## Related Errors

- [Change stream error]({{< relref "/tools/mongodb/mongodb-change-stream-error" >}})
- [Replica set error]({{< relref "/tools/mongodb/mongodb-replica-set-error-v2" >}})
