---
title: "[Solution] Redis Socket Timeout Error"
description: "How to fix Redis socket timeout when operations exceed the configured timeout period"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Long-running blocking operations (KEYS, SORT on large datasets)
- Network congestion or packet loss
- Server under heavy CPU load
- `socket-timeout` set too low in client config
- Large value sizes exceeding network buffers

## How to Fix

Check the current timeout:

```bash
redis-cli CONFIG GET timeout
```

Increase socket timeout in client:

```python
import redis
r = redis.Redis(host='localhost', socket_timeout=30, socket_connect_timeout=10)
```

Monitor slow operations:

```bash
redis-cli SLOWLOG GET 10
```

Replace blocking commands with non-blocking alternatives:

```bash
# Instead of KEYS pattern (blocking), use SCAN
redis-cli SCAN 0 MATCH pattern:*
```

## Examples

```bash
# Check timeout config
redis-cli CONFIG GET timeout

# Monitor slow log
redis-cli SLOWLOG LEN

# Check network stats
redis-cli INFO stats | grep total_net_input_bytes
```
