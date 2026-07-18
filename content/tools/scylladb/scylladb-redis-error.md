---
title: "[Solution] ScyllaDB Redis Error — How to Fix"
description: "Fix ScyllaDB Redis API errors by configuring the Redis compatible interface, resolving command compatibility, and fixing connection issues"
tools: ["scylladb"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
comments: true
---

# ScyllaDB Redis Error

ScyllaDB Redis errors occur when using the Redis-compatible API, which allows Redis clients to communicate with ScyllaDB. Not all Redis commands are supported.

## Why It Happens

- Redis API is not enabled in ScyllaDB configuration
- Redis port (6379) is not accessible
- Client uses unsupported Redis commands
- Redis protocol version is incompatible
- Key naming conventions cause conflicts
- Redis authentication is not configured

## Common Error Messages

```
RedisError: Redis API is not enabled
```

```
ConnectionRefused: Cannot connect to Redis port 6379
```

```
CommandNotSupported: Command not supported by ScyllaDB
```

```
WrongNumberOfArguments: Wrong number of arguments for command
```

## How to Fix It

### 1. Enable Redis API

```yaml
# In scylla.yaml
redis_port: 6379
redis_keyspace: redis_keyspace
```

```bash
# Restart ScyllaDB
sudo systemctl restart scylla-server

# Verify Redis port is listening
ss -tlnp | grep 6379

# Test Redis connection
redis-cli -h localhost -p 6379 ping
```

### 2. Test Redis Operations

```bash
# Basic Redis operations
redis-cli -h localhost -p 6379 SET mykey "hello"
redis-cli -h localhost -p 6379 GET mykey

# Hash operations
redis-cli -h localhost -p 6379 HSET myhash field1 value1
redis-cli -h localhost -p 6379 HGET myhash field1

# List operations
redis-cli -h localhost -p 6379 LPUSH mylist "item1"
redis-cli -h localhost -p 6379 LRANGE mylist 0 -1
```

### 3. Check Supported Commands

```bash
# Supported Redis commands in ScyllaDB:
# String: SET, GET, MSET, MGET, INCR, DECR, APPEND
# Hash: HSET, HGET, HMSET, HMGET, HGETALL, HDEL
# List: LPUSH, RPUSH, LPOP, RPOP, LRANGE, LLEN
# Set: SADD, SMEMBERS, SISMEMBER, SREM
# Key: DEL, EXISTS, EXPIRE, TTL, TYPE

# Check command support
redis-cli COMMAND DOCS
```

### 4. Configure Redis Keyspace

```yaml
# In scylla.yaml
redis_keyspace: redis_data
redis_read_consistency: LOCAL_ONE
redis_write_consistency: LOCAL_QUORUM
```

```cql
-- Redis data is stored in a ScyllaDB keyspace
-- You can query it directly via CQL
DESCRIBE KEYSPACE redis_data;
SELECT * FROM redis_data.strings LIMIT 10;
```

## Common Scenarios

- **Redis client cannot connect**: Ensure `redis_port` is configured and firewall allows 6379.
- **Unsupported command error**: Check the supported command list and use alternatives.
- **Performance issues**: Use native CQL for complex queries; Redis API is for simple key-value operations.

## Prevent It

- Use Redis API only for simple key-value operations
- Monitor Redis API performance vs native CQL
- Check ScyllaDB documentation for Redis command compatibility

## Related Pages

- [ScyllaDB Connection Error](/tools/scylladb/scylladb-connection-error)
- [ScyllaDB Query Error](/tools/scylladb/scylladb-query-error)
- [ScyllaDB Auth Error](/tools/scylladb/scylladb-auth-error)
