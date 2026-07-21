---
title: "[Solution] Vitess Tablet Lock Error"
description: "Fix Vitess tablet lock contention errors when tablets compete for shard locks during failover"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Lock Error

Tablet lock errors occur when multiple tablets try to acquire the same shard lock simultaneously during reparent or failover operations.

## Common Causes

- Multiple tablets trying to become master at the same time
- Topo server experiencing latency causing stale locks
- Network partition between tablets and topology service
- Long-running reparent operation holding the lock

## How to Fix

Check tablet status:

```bash
vtctlclient ListShards keyspace1
```

Verify topology health:

```bash
vtctlclient GetShard keyspace1/0
```

Force release stale locks:

```bash
vtctlclient InitShardMaster -force keyspace1/0 cell1-tablet-100
```

## Examples

```bash
vtctlclient TabletExternallyReparented cell1-tablet-100
```
