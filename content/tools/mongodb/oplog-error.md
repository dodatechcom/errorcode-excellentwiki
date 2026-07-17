---
title: "MongoDB OplogWindowTooSmall: oplog window exhausted"
description: "MongoDB secondary member falls behind primary because the oplog window is too small to keep up with write throughput"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

This error occurs when a secondary member in a replica set cannot keep up with the primary and falls out of the oplog window. The secondary must do a full initial sync to rejoin.

## Common Causes

- Write volume exceeds the secondary's replication throughput
- Oplog size is too small for the amount of write activity
- Secondary hardware is underpowered (CPU, disk I/O)
- Network latency between primary and secondary

## How to Fix

1. Check current oplog window size:

```javascript
rs.printReplicationInfo()     // primary
rs.printSecondaryReplicationInfo()  // secondaries
```

2. Resize the oplog on the primary:

```javascript
use local
db.runCommand({
  replSetResizeOplog: 1,
  size: 16 * 1024 * 1024 * 1024  // 16 GB
})
```

3. Monitor replication lag:

```javascript
rs.status().members.forEach(m => {
  print(`${m.name} lag: ${m.optimeDate - rs.status().date} ms`)
})
```

4. Upgrade secondary hardware or add more secondaries to distribute load.

## Examples

```javascript
rs.printSecondaryReplicationInfo()
// source: secondary1:27017
//   syncedTo: Thu Jul 16 2026 10:00:00 GMT+0000
//   0 secs (0 hrs) behind the primary
// source: secondary2:27017
//   syncedTo: Thu Jul 16 2026 09:00:00 GMT+0000
//   3600 secs (1 hrs) behind the primary — likely will fall out of window
```

## Related Errors

- [MongoDB WriteConcernError](/tools/mongodb/write-concern)
