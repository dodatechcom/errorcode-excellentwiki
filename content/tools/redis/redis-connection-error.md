---
title: "Redis Connection Error"
description: "Redis client cannot establish a connection to the Redis server."
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
tags: ["redis", "connection", "network", "econnrefused", "timeout"]
weight: 5
---

# Redis Connection Error

A Redis connection error occurs when the client cannot connect to the Redis server. This is typically caused by the server not running, incorrect connection details, or network issues.

## Common Causes

- Redis server is not running or crashed
- Incorrect host or port in connection configuration
- Redis bound to a different interface
- Firewall blocking port 6379

## How to Fix

### Check if Redis is Running

```bash
systemctl status redis-server
```

### Start the Service

```bash
sudo systemctl start redis-server
```

### Verify Port

```bash
ss -tlnp | grep 6379
```

### Test Connection

```bash
redis-cli ping
# Should return: PONG
```

### Check Bind Address

```bash
grep "^bind" /etc/redis/redis.conf
```

### Configure Bind Address

```conf
# /etc/redis/redis.conf
bind 0.0.0.0
```

## Examples

```bash
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

- [Auth Error]({{< relref "/tools/redis/auth-error" >}}) — authentication failure
- [Timeout Error]({{< relref "/tools/redis/timeout-error" >}}) — operation timeout
