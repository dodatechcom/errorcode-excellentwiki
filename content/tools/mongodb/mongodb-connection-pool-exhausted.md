---
title: "[Solution] MongoDB Connection Pool Exhausted Error"
description: "Fix MongoDB connection pool exhausted error when all connections are in use and new requests cannot be served"
tools: ["mongodb"]
error-types: ["tool-error"]
severities: ["error"]
---

# MongoDB Connection Pool Exhausted Error

The MongoDB driver connection pool has no available connections. All connections are checked out by active operations and new requests must wait or fail.

## Common Causes

- Application holds database connections for too long inside transactions
- Connection pool size is too small for the workload
- Slow queries hold connections open, reducing available pool slots
- Connections are not properly released after use
- Background threads consume too many pool connections
- High concurrency bursts exceed pool capacity

## How to Fix

### Increase Pool Size

```javascript
const client = new MongoClient(uri, {
  maxPoolSize: 100,       // increase from default 100 if needed
  minPoolSize: 10,        // keep some connections ready
  maxIdleTimeMS: 30000,   // close idle connections
  waitQueueTimeoutMS: 5000
});
```

### Monitor Active Connections

```javascript
const admin = client.db().admin();
const stats = await admin.serverStatus();
console.log('Active connections:', stats.connections.active);
console.log('Available connections:', stats.connections.available);
console.log('Current pool:', stats.connections.current);
```

### Reduce Connection Hold Time

```javascript
// Bad: connection held for entire duration
const session = client.startSession();
await session.withTransaction(async () => {
  await slowExternalApiCall();  // holds connection while waiting
  await db.collection('orders').updateOne(..., { session });
});

// Better: do external work outside the transaction
const data = await slowExternalApiCall();  // no connection needed
const session = client.startSession();
await session.withTransaction(async () => {
  await db.collection('orders').updateOne(..., { session });
});
```

### Increase Timeout and Add Retry

```javascript
const client = new MongoClient(uri, {
  maxPoolSize: 100,
  waitQueueTimeoutMS: 10000
});
```

## Examples

```
MongoTimeoutError: Timed out after 5000ms while getting a connection from pool
  maxPoolSize: 100, open: 100, pending: 45

MongoServerError: Connection pool exhausted
  add maxPoolSize to your connection string (current: 100)
```

## Related Errors

- [MongoDB Too Many Connections]({{< relref "/tools/mongodb/mongodb-too-many-connections" >}}) -- server-side connection limit
- [MongoDB Connection Error]({{< relref "/tools/mongodb/mongodb-connection-error" >}}) -- general connection failure
- [MongoDB Operation Timed Out]({{< relref "/tools/mongodb/mongodb-operation-timed-out" >}}) -- operation timeout
