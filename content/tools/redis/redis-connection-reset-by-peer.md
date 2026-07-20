---
title: "[Solution] Redis Connection Reset By Peer"
description: "How to fix Redis connection reset error when the server unexpectedly closes the connection"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Redis server restarted or crashed
- `timeout` setting closing idle connections
- Server running out of memory and killing clients
- TCP keepalive not configured properly
- Firewall dropping idle connections

## How to Fix

Check if server is alive:

```bash
redis-cli PING
```

Disable connection timeout (keep connections alive):

```bash
redis-cli CONFIG SET timeout 0
```

Enable TCP keepalive:

```bash
redis-cli CONFIG SET tcp-keepalive 60
```

Check server logs for crash information:

```bash
sudo tail -100 /var/log/redis/redis-server.log
```

Increase OS file descriptor limits:

```bash
ulimit -n 65535
```

## Examples

```bash
# Monitor live connections
watch -n 1 'redis-cli INFO clients | grep connected_clients'

# Check server uptime
redis-cli INFO server | grep uptime_in_seconds

# Test connection stability
for i in {1..100}; do redis-cli PING; done
```
