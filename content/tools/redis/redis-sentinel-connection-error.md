---
title: "[Solution] Redis Sentinel Connection Error"
description: "How to fix Redis Sentinel connection errors when clients cannot connect to Sentinel"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Sentinel not listening on the configured port
- Firewall blocking port 26379
- Sentinel bound to wrong interface
- Too many connections to Sentinel

## Fix

Check Sentinel port:

```bash
ss -tlnp | grep 26379
```

Verify Sentinel bind address:

```bash
grep "^bind" /etc/redis/sentinel.conf
```

Test connection:

```bash
redis-cli -h sentinel-host -p 26379 PING
```

Increase maxclients for Sentinel:

```bash
redis-cli -p 26379 CONFIG SET maxclients 10000
```

## Examples

```bash
# Test Sentinel connectivity
redis-cli -h 192.168.1.100 -p 26379 PING

# Check Sentinel clients
redis-cli -p 26379 INFO clients | grep connected_clients

# Check Sentinel config
redis-cli -p 26379 CONFIG GET port
```
