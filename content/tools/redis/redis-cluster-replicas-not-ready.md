---
title: "[Solution] Redis Cluster Replicas Not Ready"
description: "How to fix Redis cluster replicas not being in sync with masters"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Replicas just started and still doing full sync
- Network latency causing replication delay
- Master overloaded with writes

## Fix

Check replica status:

```bash
redis-cli INFO replication | grep slave
```

Check replication offset:

```bash
redis-cli INFO replication | grep master_repl_offset
redis-cli INFO replication | grep slave_repl_offset
```

Monitor replication lag:

```bash
watch -n 2 'redis-cli INFO replication'
```

## Examples

```bash
# Check master-replica sync
redis-cli INFO replication

# Force replica sync
redis-cli REPLICAOF NO ONE
redis-cli REPLICAOF master-host master-port

# Check replication backlog
redis-cli INFO replication | grep backlog_active
```
