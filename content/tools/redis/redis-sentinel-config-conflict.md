---
title: "[Solution] Redis Sentinel Configuration Conflict"
description: "How to fix Redis Sentinel configuration conflicts between multiple sentinel instances"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Different quorum values across Sentinel configs
- Different monitor configurations
- Inconsistent down-after-milliseconds settings

## Fix

Standardize sentinel.conf across all instances:

```bash
# Copy same config to all Sentinel instances
scp /etc/redis/sentinel.conf sentinel2:/etc/redis/sentinel.conf
scp /etc/redis/sentinel.conf sentinel3:/etc/redis/sentinel.conf
```

Restart all Sentinels:

```bash
sudo systemctl restart redis-sentinel
```

Verify consistent configuration:

```bash
for port in 26379 26380 26381; do
  redis-cli -p $port SENTINEL masters
done
```

## Examples

```bash
# Compare Sentinel configurations
diff <(redis-cli -p 26379 SENTINEL masters)      <(redis-cli -p 26380 SENTINEL masters)

# Check quorum
redis-cli -p 26379 SENTINEL get-master-addr-by-name mymaster

# Verify all Sentinels see same master
for port in 26379 26380 26381; do
  echo "Sentinel $port: $(redis-cli -p $port SENTINEL get-master-addr-by-name mymaster)"
done
```
