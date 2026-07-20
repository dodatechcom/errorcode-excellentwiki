---
title: "[Solution] Redis Connection Refused Error"
description: "How to fix Redis connection refused error when the server is not accepting connections"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Redis server is not running or has crashed
- Wrong host or port specified in the connection string
- Firewall blocking the Redis port (default: 6379)
- Redis `bind` configuration restricted to localhost
- Too many client connections already established

## How to Fix

Check if Redis is running:

```bash
redis-cli ping
```

If not running, start the server:

```bash
sudo systemctl start redis
```

Verify the bind configuration in `redis.conf`:

```bash
grep "^bind" /etc/redis/redis.conf
```

To allow remote connections, update the bind directive:

```bash
sudo sed -i 's/^bind 127.0.0.1/bind 0.0.0.0/' /etc/redis/redis.conf
sudo systemctl restart redis
```

Check if the port is listening:

```bash
ss -tlnp | grep 6379
```

Increase the max clients limit if needed:

```bash
redis-cli CONFIG SET maxclients 10000
```

## Examples

```bash
# Test connection
redis-cli -h 127.0.0.1 -p 6379 ping

# Check server status
systemctl status redis

# View active connections
redis-cli INFO clients
```
