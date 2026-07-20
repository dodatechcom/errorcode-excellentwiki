---
title: "[Solution] Redis Sentinel Quorum Not Reached Error"
description: "How to fix Sentinel quorum not reached errors during failover decisions"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Too few Sentinel instances running
- Network partition between Sentinels
- Quorum value higher than available Sentinels
- Sentinel processes unable to communicate

## Fix

Check Sentinel count:

```bash
redis-cli -p 26379 SENTINEL masters | grep num-other-sentinels
```

Adjust quorum:

```bash
redis-cli -p 26379 SENTINEL set mymaster quorum 2
```

Ensure all Sentinels are running:

```bash
for port in 26379 26380 26381; do
  redis-cli -p $port PING
done
```

Check Sentinel connectivity:

```bash
redis-cli -p 26379 SENTINEL sentinels mymaster
```

## Examples

```bash
# Check quorum
redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster

# Verify Sentinel peers
redis-cli -p 26379 SENTINEL sentinels mymaster | grep ip

# Update quorum
redis-cli -p 26379 SENTINEL set mymaster quorum 2
```
