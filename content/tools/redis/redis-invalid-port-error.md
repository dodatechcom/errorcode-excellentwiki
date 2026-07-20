---
title: "[Solution] Redis Invalid Port Error"
description: "How to fix Redis invalid port configuration errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Port number out of valid range (1-65535)
- Port already in use by another service
- Port requires root privileges (< 1024)

## Fix

Check port availability:

```bash
ss -tlnp | grep 6379
```

Use valid port range:

```bash
# Valid ports: 1-65535
# Common: 6379 (default), 6380, 6381, etc.
```

Check redis.conf:

```bash
grep "^port" /etc/redis/redis.conf
```

Test port binding:

```bash
redis-server --port 6380
```

## Examples

```bash
# Check if port is in use
ss -tlnp | grep 6379

# Start Redis on different port
redis-server --port 6380

# Check listening ports
netstat -tlnp | grep redis
```
