---
title: "[Solution] Redis NOAUTH Authentication Required"
description: "How to fix Redis NOAUTH error when commands are executed before authentication"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Client sends commands without authenticating first
- Connection pool reusing a stale connection after AUTH timeout
- `requirepass` or ACL configured but client does not send AUTH
- Multi-command pipeline sent before authentication

## How to Fix

Send AUTH command before any data commands:

```bash
redis-cli
AUTH your_password
PING
```

In application code, ensure AUTH is called on new connections:

```python
import redis
r = redis.Redis(host='localhost', port=6379, password='your_password')
r.ping()
```

Check if authentication is enabled:

```bash
redis-cli CONFIG GET requirepass
```

Disable authentication temporarily for debugging:

```bash
redis-cli CONFIG SET requirepass ""
```

## Examples

```bash
# Wrong - sends command without AUTH
redis-cli SET key value
# Error: NOAUTH Authentication required

# Correct - authenticate first
redis-cli
> AUTH mypassword
OK
> SET key value
OK
```
