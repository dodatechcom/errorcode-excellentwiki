---
title: "[Solution] Redis Sentinel Master Is Down Error"
description: "How to fix Redis Sentinel master-is-down notifications and ensure proper failover"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Master Redis process crashed
- Master node unreachable due to network issue
- Master ran out of memory and was killed

## Fix

Check Sentinel notification:

```bash
redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster
```

View master status:

```bash
redis-cli -p 26379 SENTINEL masters
```

Monitor failover progress:

```bash
tail -f /var/log/redis/sentinel.log
```

Check if new master was promoted:

```bash
redis-cli -p 26379 SENTINEL replicas mymaster
```

## Examples

```bash
# Check master status
redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster

# View failover count
redis-cli -p 26379 SENTINEL failover-count

# Check master age
redis-cli -p 26379 SENTINEL masters | grep info-refresh
```
