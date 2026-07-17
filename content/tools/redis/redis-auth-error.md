---
title: "Redis Authentication Error"
description: "Redis client fails to authenticate with the Redis server."
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
tags: ["redis", "authentication", "password", "acl", "credential"]
weight: 5
---

# Redis Authentication Error

A Redis authentication error occurs when the client cannot authenticate with the Redis server. The password is incorrect or authentication is required but not provided.

## Common Causes

- Password not provided in connection
- Incorrect password
- ACL user does not have required permissions
- requirepass not configured in redis.conf

## How to Fix

### Provide Password

```bash
redis-cli -a your_password ping
```

### Set Password in redis.conf

```conf
# /etc/redis/redis.conf
requirepass your_password
```

### Authenticate in Client

```javascript
// Node.js ioredis
const redis = new Redis({ password: 'your_password' });

// Python redis-py
import redis
r = redis.Redis(password='your_password')
```

### Check ACL Users

```bash
redis-cli ACL LIST
redis-cli ACL GETUSER myuser
```

### Create ACL User

```bash
redis-cli ACL SETUSER myuser on >password ~* +@all
```

### Reset Password

```bash
redis-cli CONFIG SET requirepass new_password
```

## Examples

```bash
redis-cli ping
NOAUTH Authentication required.

redis-cli -a wrong_password ping
ERR invalid username-password pair or user is disabled.
```

## Related Errors

- [Connection Error]({{< relref "/tools/redis/redis-connection-error" >}}) — connection failure
- [Permission Error]({{< relref "/tools/redis/auth-error" >}}) — authorization error
