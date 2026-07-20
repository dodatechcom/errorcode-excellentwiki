---
title: "[Solution] Redis Sentinel Down Error"
description: "How to fix Redis Sentinel down errors when sentinel process is unreachable"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Sentinel process crashed
- Port 26379 not listening
- System resource exhaustion
- Configuration error in sentinel.conf

## Fix

Check Sentinel process:

```bash
systemctl status redis-sentinel
```

Start Sentinel:

```bash
sudo systemctl start redis-sentinel
```

Check Sentinel configuration:

```bash
redis-check-sentinel /etc/redis/sentinel.conf
```

Verify Sentinel is listening:

```bash
ss -tlnp | grep 26379
```

## Examples

```bash
# Test Sentinel connection
redis-cli -p 26379 PING

# Check Sentinel ID
redis-cli -p 26379 SENTINEL myid

# View Sentinel info
redis-cli -p 26379 INFO sentinel
```
