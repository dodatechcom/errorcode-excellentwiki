---
title: "[Solution] Vitess Tablet Consistency Check Error"
description: "Fix Vitess consistency check errors when verifying data across primary and replicas"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Consistency Check Error

Consistency check errors occur when vtgate detects data inconsistencies between primary and replica tablets.

## Common Causes

- Replica has errant transactions
- Partial replication failure after DDL
- Data drift from direct writes to replica
- Table checksums mismatch between tablets

## How to Fix

Run consistency check:

```bash
vtctlclient ValidateVersionedKeyspace keyspace1
```

Compare table checksums:

```sql
CHECKSUM TABLE users EXTENDED;
```

Fix errant transactions:

```sql
-- On replica, reset GTID
STOP REPLICA;
RESET REPLICA;
CHANGE REPLICATION SOURCE TO SOURCE_AUTO_POSITION=1;
START REPLICA;
```

## Examples

```bash
vtctlclient ValidateKeyspace keyspace1
```
