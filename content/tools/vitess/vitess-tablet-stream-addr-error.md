---
title: "[Solution] Vitess Tablet Stream Address Error"
description: "Fix Vitess tablet stream address resolution errors during vreplication"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Stream Address Error

Stream address errors occur when vreplication cannot resolve the tablet address for a replication stream.

## Common Causes

- Tablet address changed after failover
- DNS resolution failing for tablet hostname
- Topo entry outdated after tablet restart
- Network firewall blocking stream connection

## How to Fix

Update stream source address:

```bash
vtctlclient MovingShardsCancel keyspace1
```

Restart vreplication stream:

```bash
vtctlclient VReplicationExec cell1-tablet-100 "UPDATE _vt.vreplication SET state='Running' WHERE id=1"
```

Check tablet address in topo:

```bash
vtctlclient GetTablet cell1-tablet-100
```

## Examples

```bash
vtctlclient ListStreams keyspace1 0
```
