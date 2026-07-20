---
title: "[Solution] Redis Sentinel Slave Not Found Error"
description: "How to fix Sentinel slave not found errors when replica is not registered"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Replica not configured with SLAVEOF/REPLICAOF
- Sentinel cannot reach the replica
- Replica is not started

## Fix

Check registered replicas:

```bash
redis-cli -p 26379 SENTINEL replicas mymaster
```

Configure replica in sentinel.conf:

```bash
echo 'sentinel monitor mymaster 127.0.0.1 6379 2' | sudo tee -a /etc/redis/sentinel.conf
```

Add replica to Sentinel monitoring:

```bash
redis-cli -p 26379 SENTINEL set mymaster slave-priority 100
```

## Examples

```bash
# Check replica count
redis-cli -p 26379 SENTINEL replicas mymaster | grep ip

# Verify replica connection
redis-cli -h replica-host -p 6379 INFO replication

# Check Sentinel monitoring
redis-cli -p 26379 SENTINEL masters | grep -A5 name
```
