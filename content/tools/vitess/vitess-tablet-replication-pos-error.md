---
title: "[Solution] Vitess Tablet Replication Position Error"
description: "Fix Vitess replication position errors when tablet falls behind or jumps ahead in binary log"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Replication Position Error

Replication position errors occur when the recorded position on a replica does not match what the primary expects.

## Common Causes

- Binary log on primary purged before replica caught up
- Replication position corrupted during tablet restore
- GTID executed set diverged between primary and replica
- Position reset after tablet crash recovery

## How to Fix

Check current positions:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-100 "SHOW MASTER STATUS"
vtctlclient ExecuteFetchAsDba cell1-tablet-101 "SHOW REPLICA STATUS\G"
```

Sync replica position:

```sql
STOP REPLICA;
CHANGE REPLICATION SOURCE TO SOURCE_AUTO_POSITION=1;
START REPLICA;
```

Force position reset:

```bash
vtctlclient ResetReplication -force cell1-tablet-101
vtctlclient InitReplica keyspace1/0 cell1-tablet-101
```

## Examples

```bash
vtctlclient ReplicationStatus keyspace1/0
```
