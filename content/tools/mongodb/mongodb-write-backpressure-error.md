---
title: "[Solution] MongoDB Write Backpressure Error"
description: "Fix MongoDB write backpressure error when secondaries cannot keep up with the primary's write rate"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Write Backpressure Error

A replica set secondary falls behind the primary because it cannot apply writes as fast as they arrive. The primary throttles writes or the secondary enters a recovery state.

## Common Causes

- Secondary hardware is slower than primary
- Write load exceeds secondary's I/O or CPU capacity
- Secondary is performing heavy read queries that compete with replication
- Network latency between primary and secondaries
- Large operations (bulk writes, $lookup aggregations) slow replication
- Secondary disk I/O saturation

## How to Fix

### Check Replication Lag

```javascript
rs.status().members.forEach(m => {
  if (m.stateStr === 'SECONDARY') {
    const lag = rs.status().date.getTime() - m.optDate.getTime();
    console.log(`${m.name} lag: ${lag / 1000}s`);
  }
});
```

### Prioritize Replication Traffic

```bash
# On secondary, reduce competing operations
# Set low priority for non-critical reads
mongod --setParameter diagnosticDataCollectionEnabled=false
```

### Scale Secondary Hardware

```bash
# Ensure secondary has equivalent or better I/O
# Use SSDs, increase RAM for WiredTiger cache
mongod --wiredTigerCacheSizeGB 8
```

### Reduce Write Load

```javascript
// Batch writes to reduce replication volume
const bulkOps = orders.map(order => ({
  updateOne: { filter: { _id: order._id }, update: { $set: order } }
}));
await db.collection('orders').bulkWrite(bulkOps, { ordered: false });
```

### Throttle Writes if Needed

```javascript
// Add artificial delay to spread write load
async function throttledWrite(doc, delayMs = 5) {
  await db.collection('events').insertOne(doc);
  await new Promise(r => setTimeout(r, delayMs));
}
```

## Examples

```
replSet Member <secondary:27017> is behind primary by 45 seconds.
  Replication is experiencing backpressure.

replSet Warning: primary is experiencing write backpressure.
  Secondary apply rate: 5000 ops/sec, primary rate: 12000 ops/sec.
```

## Related Errors

- [MongoDB Replication Lag]({{< relref "/tools/mongodb/mongodb-replication-lag" >}}) -- replication delay
- [MongoDB Write Concern Timeout]({{< relref "/tools/mongodb/mongodb-write-concern-timeout" >}}) -- write concern
- [MongoDB Write Error]({{< relref "/tools/mongodb/mongodb-write-error" >}}) -- write failures
