---
title: "[Solution] Redis Sentinel Failover Aborted"
description: "How to fix Redis Sentinel failover abort errors"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Target replica too old (replication lag too high)
- Sentinel cannot reach the new master after promotion
- No healthy replica available for promotion
- Network partition during failover

## How to Fix

Check Sentinel status:

```bash
redis-cli -p 26379 SENTINEL masters
redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster
```

Check replica health:

```bash
redis-cli -p 26379 SENTINEL replicas mymaster
```

View Sentinel logs:

```bash
tail -100 /var/log/redis/sentinel.log
```

Manually trigger failover:

```bash
redis-cli -p 26379 SENTINEL failover mymaster
```

## Examples

```bash
# Check Sentinel masters
redis-cli -p 26379 SENTINEL masters

# View replica info
redis-cli -p 26379 SENTINEL replicas mymaster

# Check failover count
redis-cli -p 26379 SENTINEL failover-count
```
