---
title: "ERR Client sent AUTH but no password is set"
description: "Redis rejects an AUTH command because the server was not started with a password configured"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

This error occurs when a client sends an `AUTH` command to a Redis server that has not been configured with a password. The server rejects the authentication attempt.

## Common Causes

- Client is configured with a password but the server has none set
- Redis configuration changed and `requirepass` was removed
- Connecting to the wrong Redis instance
- Mismatch between client and server Redis versions

## How to Fix

1. Check if a password is configured:

```bash
redis-cli CONFIG GET requirepass
```

2. Set a password on the server:

```bash
redis-cli CONFIG SET requirepass "your_password_here"
```

3. Update your client connection to match:

```python
import redis
r = redis.Redis(host='localhost', port=6379, password='your_password_here')
```

4. Or connect without a password if the server does not require one:

```python
import redis
r = redis.Redis(host='localhost', port=6379)
```

## Examples

```bash
redis-cli -a mypassword PING
# (error) ERR Client sent AUTH, but no password is set. Did you mean ACL SETUSER with >password?
```

## Related Errors

- [OOM command not allowed](/tools/redis/max-memory)
