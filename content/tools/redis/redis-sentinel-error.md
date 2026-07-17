---
title: "Redis Sentinel Error"
description: "Redis Sentinel encounters issues with monitoring, failover, or configuration."
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
weight: 5
---

# Redis Sentinel Error

A Redis Sentinel error occurs when the Sentinel monitoring system encounters issues with failover, monitoring, or configuration. Sentinel provides high availability for Redis.

## Common Causes

- Sentinel cannot connect to Redis master
- Not enough Sentinels agree on master status
- Failover in progress or failed
- Sentinel configuration outdated

## How to Fix

### Check Sentinel Status

```bash
redis-cli -p 26379 SENTINEL master mymaster
redis-cli -p 26379 SENTINEL replicas mymaster
```

### Check Sentinel Configuration

```conf
# /etc/redis/sentinel.conf
sentinel monitor mymaster 127.0.0.1 6379 2
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 60000
```

### Check Sentinel Peers

```bash
redis-cli -p 26379 SENTINEL sentinels mymaster
```

### Force Failover

```bash
redis-cli -p 26379 SENTINEL failover mymaster
```

### Reset Sentinel

```bash
redis-cli -p 26379 SENTINEL RESET mymaster
```

### Check Sentinel Logs

```bash
tail -f /var/log/redis/sentinel.log
```

## Examples

```bash
redis-cli -p 26379 SENTINEL master mymaster
# name: mymaster
# down-after-milliseconds: 5000
# failover-timeout: 60000
```

## Related Errors

- [Cluster Error]({{< relref "/tools/redis/redis-cluster-error" >}}) — cluster issues
- [Connection Error]({{< relref "/tools/redis/redis-connection-error" >}}) — connection failure
