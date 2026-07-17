---
title: "Redis Cluster - MOVED/ASK redirect error"
description: "Redis Cluster client receives MOVED or ASK redirect responses because the key is on a different slot"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
tags: ["redis", "cluster", "moved", "ask", "slot", "redirect", "hash"]
weight: 5
---

A MOVED/ASK redirect error occurs in Redis Cluster when a client sends a command to the wrong node for the key's hash slot. MOVED means the slot permanently resides on another node, while ASK indicates a slot is being migrated between nodes.

## Common Causes

- Client not aware of the current slot mapping
- Client connected to a node that does not own the key's slot
- Cluster topology changed due to rebalancing
- Client-side slot cache is stale
- Hash tag not used to keep related keys on the same slot

## How to Fix

1. Use a Redis Cluster-aware client:

```javascript
// ioredis handles MOVED/ASK automatically
const Redis = require('ioredis');
const cluster = new Redis.Cluster([
  { host: 'node1', port: 6379 },
  { host: 'node2', port: 6379 },
  { host: 'node3', port: 6379 },
]);

// Operations are automatically routed
await cluster.set('user:123', 'John');
```

2. Handle MOVED/ASK in custom clients:

```javascript
async function executeCommand(node, command, args) {
  try {
    return await node.sendCommand(command, args);
  } catch (error) {
    if (error.message.includes('MOVED')) {
      const match = error.message.match(/(\d+)\s+(\S+):(\d+)/);
      if (match) {
        const newNode = { host: match[2], port: parseInt(match[3]) };
        return await executeCommand(newNode, command, args);
      }
    }
    throw error;
  }
}
```

3. Use hash tags to keep related keys on the same slot:

```bash
# All these keys go to the same slot
SET {user:123}:name "John"
SET {user:123}:email "john@example.com"
SET {user:123}:age "30"
```

4. Refresh cluster topology:

```bash
redis-cli CLUSTER SLOTS
redis-cli CLUSTER NODES
```

5. Configure cluster node timeouts:

```javascript
const cluster = new Redis.Cluster(nodes, {
  clusterRetryStrategy: (times) => Math.min(times * 100, 3000),
  enableOfflineQueue: true,
  redisOptions: { connectTimeout: 5000 },
});
```

## Examples

```bash
# Error: MOVED 3999 127.0.0.1:7002
$ redis-cli -p 7001 SET user:123 "John"
(error) MOVED 3999 127.0.0.1:7002
# Key user:123 belongs to slot 3999 on node 7002

# Fix: use cluster-aware client
const cluster = new Redis.Cluster([
  { port: 7001, host: '127.0.0.1' },
  { port: 7002, host: '127.0.0.1' },
]);
await cluster.set('user:123', 'John'); // auto-routed
```

## Related Errors

- [Sentinel error]({{< relref "/tools/redis/redis-sentinel-error" >}})
- [Connection error]({{< relref "/tools/redis/redis-connection-error" >}})
