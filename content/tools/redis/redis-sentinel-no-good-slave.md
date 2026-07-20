---
title: "[Solution] Redis Sentinel No Good Slave Error"
description: "How to fix Sentinel no good slave error during failover selection"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- All replicas are down or unreachable
- Replicas have too high replication lag
- Replica is on the same node as the master
- Replica priority set incorrectly

## Fix

Check replica status:

```bash
redis-cli -p 26379 SENTINEL replicas mymaster
```

Ensure replicas have correct priority:

```bash
redis-cli CONFIG SET replica-priority 100
```

Add more replicas:

```bash
# On new replica
redis-cli REPLICAOF master-host master-port
```

Monitor replica lag:

```bash
redis-cli INFO replication | grep master_repl_offset
```

## Examples

```bash
# Check replica count
redis-cli -p 26379 SENTINEL replicas mymaster | grep -c ip

# Verify replica priority
redis-cli CONFIG GET replica-priority

# Check replication offset
redis-cli INFO replication
```
