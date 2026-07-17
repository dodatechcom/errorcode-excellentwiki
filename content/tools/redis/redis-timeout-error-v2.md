---
title: "Redis - command timeout"
description: "Redis client times out waiting for a response from the server during command execution"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

A Redis command timeout error occurs when the client does not receive a response from Redis within the configured timeout period. This can be caused by slow commands, server overload, or network latency.

## Common Causes

- Slow or blocking commands (KEYS, SORT, large LRANGE)
- Server CPU or memory exhaustion
- Network latency between client and server
- Command timeout set too low for the workload
- Large key operations (big hashes, lists, sets)

## How to Fix

1. Avoid blocking or slow commands:

```bash
# Bad: blocks entire server
KEYS user:*

# Good: use SCAN
SCAN 0 MATCH user:* COUNT 100

# Bad: sorting large sets
SORT large-list

# Good: use application-level sorting
```

2. Increase command timeout:

```javascript
const redis = new Redis({
  host: '127.0.0.1',
  port: 6379,
  commandTimeout: 10000, // 10 seconds
  connectTimeout: 5000,
});
```

3. Monitor slow commands:

```bash
redis-cli SLOWLOG GET 10
redis-cli --latency
```

4. Use pipeline for batch operations:

```javascript
const pipeline = redis.pipeline();
for (const item of items) {
  pipeline.hset(`item:${item.id}`, item);
}
await pipeline.exec();
```

5. Break large operations into chunks:

```bash
# Bad: large range in one call
LRANGE biglist 0 1000000

# Good: use cursor-based iteration
SSCAN bigset 0 COUNT 1000
```

6. Check server health during timeout:

```bash
redis-cli INFO stats
redis-cli INFO memory
redis-cli INFO cpu
```

## Examples

```bash
# Error: Command timed out after 5000ms
$ redis-cli --command-timeout 5
> KEYS *
# Timeout waiting for response

# Fix: use SCAN instead
> SCAN 0 COUNT 100
```

## Related Errors

- [Memory error]({{< relref "/tools/redis/redis-memory-error" >}})
- [Connection error]({{< relref "/tools/redis/redis-connection-error" >}})
