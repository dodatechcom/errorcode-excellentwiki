---
title: "MongoDB - connection pool exhausted"
description: "MongoDB connection pool runs out of available connections, causing new requests to fail or wait indefinitely"
tools: ["mongodb"]
error-types: ["database-error"]
severities: ["error"]
tags: ["mongodb", "connection", "pool", "maxpoolsize", "exhausted", "timeout"]
weight: 5
---

A MongoDB connection pool exhausted error occurs when all available connections in the pool are in use and new requests cannot acquire a connection. This typically happens under high load or when connections are not properly released.

## Common Causes

- `maxPoolSize` too low for the application's concurrency level
- Connections not being closed after use (connection leaks)
- Long-running operations holding connections unnecessarily
- Transaction locks preventing connection release
- Connection timeout set too low causing premature checkout

## How to Fix

1. Increase the connection pool size:

```javascript
const { MongoClient } = require('mongodb');
const client = new MongoClient(uri, {
  maxPoolSize: 50,        // increase from default 100
  minPoolSize: 10,
  maxIdleTimeMS: 30000,
  waitQueueTimeoutMS: 5000,
});
```

2. Monitor active connections:

```javascript
const pool = client.db().command({ connectionStatus: 1 });
console.log('Active connections:', pool.authInfo.authenticatedUsers.length);
```

3. Use connection pool metrics for debugging:

```javascript
const admin = client.db().admin();
const serverStatus = await admin.serverStatus();
console.log('Current pool:', serverStatus.connections.current);
console.log('Available:', serverStatus.connections.available);
```

4. Ensure connections are properly closed:

```javascript
// Use try-finally to guarantee cleanup
async function queryDatabase() {
  const client = new MongoClient(uri);
  try {
    await client.connect();
    const db = client.db('mydb');
    return await db.collection('users').find({}).toArray();
  } finally {
    await client.close();
  }
}
```

5. Configure timeouts to prevent pool starvation:

```javascript
const client = new MongoClient(uri, {
  maxPoolSize: 100,
  waitQueueTimeoutMS: 10000,
  serverSelectionTimeoutMS: 5000,
});
```

## Examples

```javascript
// Error: MongoDB connection pool exhausted
const client = new MongoClient(uri, { maxPoolSize: 5 });
await client.connect();
// With 10+ concurrent requests, pool is exhausted
// MongoError: Connection pool exhausted [pool size: 5, in use: 5, waiting: 5]
```

## Related Errors

- [Connection error]({{< relref "/tools/mongodb/mongodb-connection-error" >}})
- [Timeout error]({{< relref "/tools/mongodb/mongodb-timeout-error" >}})
