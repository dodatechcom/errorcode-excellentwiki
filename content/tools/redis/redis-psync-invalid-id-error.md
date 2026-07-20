---
title: "[Solution] Redis PSYNC Invalid Replication ID Error"
description: "How to fix Redis PSYNC invalid replication ID errors during resynchronization"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Causes

- Replica has stale replication ID after master failover
- Replication ID mismatch between master and replica

## Fix

Check current replication ID:

```bash
redis-cli INFO replication | grep master_replid
```

Reset replication on replica:

```bash
redis-cli REPLICAOF NO ONE
redis-cli REPLICAOF master-host master-port
```

Verify new replication ID:

```bash
redis-cli INFO replication | grep master_replid2
```

## Examples

```bash
# Check replication IDs
redis-cli INFO replication | grep replid

# Reset and re-sync
redis-cli -h replica REPLICAOF NO ONE
sleep 2
redis-cli -h replica REPLICAOF new-master 6379

# Check sync status
redis-cli -h replica INFO replication | grep master_link_status
```
