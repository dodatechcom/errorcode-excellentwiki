---
title: "Error: connect ECONNREFUSED 127.0.0.1:6379"
description: "Redis client cannot establish a connection to the Redis server"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
tags: ["connection", "network", "redis", "econnrefused"]
weight: 5
---

This error occurs when the Redis client fails to connect to the Redis server, typically because the server is not running, the port is wrong, or the host is unreachable.

## Common Causes

- Redis server is not running or crashed
- Incorrect host or port in connection configuration
- Redis bound to a different interface than expected
- Firewall blocking port 6379

## How to Fix

1. Check if Redis is running:

```bash
systemctl status redis-server
```

2. Start the service if it's stopped:

```bash
sudo systemctl start redis-server
```

3. Verify Redis is listening on the expected port:

```bash
ss -tlnp | grep 6379
```

4. Test the connection directly:

```bash
redis-cli ping
# Should return: PONG
```

5. Check `redis.conf` for the bind address:

```bash
grep "^bind" /etc/redis/redis.conf
```

## Examples

```bash
# Attempting to connect to a stopped Redis server
redis-cli -h 127.0.0.1 -p 6379
# Error: connect ECONNREFUSED 127.0.0.1:6379
```

```javascript
// Node.js with ioredis
const Redis = require('ioredis');
const redis = new Redis({ host: '127.0.0.1', port: 6379 });
// Error: connect ECONNREFUSED 127.0.0.1:6379
```

## Related Errors

- [WRONGTYPE Operation](/tools/redis/wrong-type)
