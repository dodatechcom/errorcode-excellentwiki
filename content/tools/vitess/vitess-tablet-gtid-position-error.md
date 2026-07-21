---
title: "[Solution] Vitess Tablet GTID Position Error"
description: "Fix Vitess GTID position errors when tablet replication position becomes invalid"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet GTID Position Error

GTID position errors occur when a tablet's recorded GTID position no longer exists in the primary's binary logs.

## Common Causes

- Primary purged binary logs containing the GTID
- Replica crashed and needs GTID-based rejoin
- Errant GTID transaction on replica
- GTID mode mismatch between primary and replica

## How to Fix

Check GTID position:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-101 "SELECT @@global.gtid_executed"
```

Purge errant GTIDs:

```sql
RESET MASTER;
SET GLOBAL gtid_purged = '';
```

Reset replica with GTID:

```sql
STOP REPLICA;
RESET REPLICA;
CHANGE REPLICATION SOURCE TO SOURCE_AUTO_POSITION=1;
START REPLICA;
```

## Examples

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-101 "SHOW REPLICA STATUS\G" | grep -i gtid
```
