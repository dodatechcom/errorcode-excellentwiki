---
title: "[Solution] Vitess Tablet Master Status Error"
description: "Fix Vitess tablet master status errors when primary tablet fails to report correct master position"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Master Status Error

Master status errors occur when the primary tablet's reported position becomes stale or inconsistent with replicas.

## Common Causes

- Primary crashed and restarted with older binary log position
- GTID gap caused by relay log corruption
- Failover promoted wrong tablet as master
- Topo server storing outdated master information

## How to Fix

Check master position:

```bash
vtctlclient ExecuteFetchAsDba cell1-tablet-100 "SHOW MASTER STATUS"
```

Force master position sync:

```bash
vtctlclient MasterPosition keyspace1/0
```

Rebuild shard master:

```bash
vtctlclient InitShardMaster -force keyspace1/0 cell1-tablet-100
```

## Examples

```bash
vtctlclient Scrap cell1-tablet-101
```
