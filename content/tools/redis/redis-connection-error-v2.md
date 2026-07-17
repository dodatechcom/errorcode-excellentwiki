---
title: "Redis - connection pool exhausted"
description: "Redis connection pool runs out of available connections, causing new requests to fail or timeout"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
tags: ["redis", "connection", "pool", "max-connections", "exhausted"]
weight: 5
---

A Redis connection pool exhausted error occurs when all connections in the pool are in use and new requests cannot acquire one. This typically happens under high concurrency or when connections are not properly returned to the pool.

## Common Causes

- Pool size too low for application concurrency
- Connection leak from unclosed connections
- Long-running blocking commands holding connections
- Network issues preventing connection return
- Client timeout shorter than Redis operation time

## How to Fix

1. Increase the connection pool size:

```javascript
// Node.js with ioredis
const Redis = require('ioredis');
const cluster = new Redis.Cluster(nodes, {
  redisOptions: {
    maxRetriesPerRequest: 3,
  },
  enableOfflineQueue: true,
  clusterRetryStrategy: (times) => Math.min(times * 100, 3000),
});

// Pool with generic-pool
const pool = require('generic-pool').createPool({
  create: () => new Redis({ host: '127.0.0.1', port: 6379 }),
  destroy: (client) => client.quit(),
  max: 20,  // increase pool size
  min: 5,
});
```

2. Monitor connection count:

```bash
redis-cli info clients
# connected_clients:15
# blocked_clients:0
```

3. Check for blocking commands:

```bash
redis-cli client list
# Look for 'cmd=blpop' or other blocking commands
```

4. Ensure connections are properly released:

```javascript
async function withRedis(operation) {
  const client = await pool.acquire();
  try {
    return await operation(client);
  } finally {
    pool.release(client); // always release
  }
}
```

5. Configure connection timeouts:

```javascript
const redis = new Redis({
  host: '127.0.0.1',
  port: 6379,
  connectTimeout: 5000,
  commandTimeout: 3000,
  maxRetriesPerRequest: 3,
});
```

## Examples

```javascript
// Error: ENOMEM: not enough memory, command not allowed
// Or: Connection pool exhausted
const Redis = require('ioredis');
const redis = new Redis({ connectionPool: { max: 5 } });
// With 10+ concurrent requests, pool exhausted

// Fix: increase pool size
const redis = new Redis({ connectionPool: { max: 50 } });
```

## Related Errors

- [Connection error]({{< relref "/tools/redis/redis-connection-error" >}})
- [Timeout error]({{< relref "/tools/redis/redis-timeout-error" >}})
