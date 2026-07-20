---
title: "[Solution] Redis Sentinel Replication Down Error"
description: "How to fix Redis Sentinel error when replica-serve-stale-data affects sentinel decisions"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Replica cannot reach master but is still serving
- Stale data being served to clients
- Sentinel not aware of replication state change

## Fix

Check replication state:

```bash
redis-cli -h replica-host -p 6379 INFO replication
```

Check replica-serve-stale-data:

```bash
redis-cli CONFIG GET replica-serve-stale-data
```

Disable stale data serving:

```bash
redis-cli CONFIG SET replica-serve-stale-data no
```

Monitor Sentinel detection:

```bash
redis-cli -p 26379 SENTINEL replicas mymaster | grep slave_repl_offset
```

## Examples

```bash
# Check if replica is stale
redis-cli -h replica-host -p 6379 INFO replication | grep master_link_status

# Force replica to stop serving stale data
redis-cli -h replica-host -p 6379 CONFIG SET replica-serve-stale-data no

# Check Sentinel replica monitoring
redis-cli -p 26379 SENTINEL replicas mymaster
```
