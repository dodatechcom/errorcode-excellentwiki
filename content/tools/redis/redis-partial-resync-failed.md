---
title: "[Solution] Redis Partial Resync Failed Error"
description: "How to fix Redis partial resynchronization failure during replication"
tools: ["redis"]
error-types: ["database-error"]
severities: ["error"]
---

## Common Causes

- Replication ID changed (master failover occurred)
- Backlog does not contain the needed offset
- Replica was disconnected too long
- Master restarted and changed replication ID

## Fix

Check replication IDs:

```bash
redis-cli INFO replication | grep master_replid
```

Force full resync:

```bash
redis-cli REPLICAOF NO ONE
redis-cli REPLICAOF master-host master-port
```

Increase backlog size:

```bash
redis-cli CONFIG SET repl-backlog-size 512mb
```

Monitor resync status:

```bash
redis-cli INFO replication | grep master_sync_in_progress
```

## Examples

```bash
# Check replication status
redis-cli INFO replication

# Force full resync
redis-cli -h replica REPLICAOF NO ONE
redis-cli -h replica REPLICAOF master 6379

# Check replid
redis-cli INFO replication | grep master_replid
```
