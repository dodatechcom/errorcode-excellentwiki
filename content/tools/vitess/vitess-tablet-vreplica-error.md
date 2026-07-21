---
title: "[Solution] Vitess Tablet VReplica Error"
description: "Fix Vitess vreplica errors when materialized views fail to stay synchronized"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet VReplica Error

VReplica errors occur when materialized views created via vreplication fall out of sync with the source table.

## Common Causes

- Target table schema does not match source projection
- Column added to source not present in materialized view
- Unique constraint violation during insert
- Vreplication stream stopped due to error

## How to Fix

Check materialization status:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-100 "SELECT * FROM _vt.vreplication WHERE workflow LIKE '%matview%'"
```

Drop and recreate materialized view:

```bash
vtctlclient Materialize -materialize-target=matview_orders 'CREATE TABLE matview_orders AS SELECT id, customer_id, total FROM orders'
```

Restart failed stream:

```bash
vtctlclient VReplicationExec cell1-tablet-100 "UPDATE _vt.vreplication SET state='Running', message='' WHERE workflow='matview_orders'"
```

## Examples

```bash
vtctlclient Materialize -action=lookup matview_orders
```
