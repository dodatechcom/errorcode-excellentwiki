---
title: "[Solution] Vitess Tablet Topo Lock Error"
description: "Fix Vitess topology lock errors when distributed locks conflict across tablets"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Topo Lock Error

Topology lock errors occur when tablets cannot acquire distributed locks needed for shard-level operations.

## Common Causes

- Topo server (etcd/zk) experiencing leader election
- Lock lease expired before operation completed
- Multiple vtctl clients performing conflicting operations
- Topo server disk space full causing write failures

## How to Fix

Check topo server health:

```bash
etcdctl endpoint health
```

Release stuck locks:

```bash
vtctlclient RemoveKeyspaceCell keyspace1 cell1
```

Restart topo operations:

```bash
vtctlclient RebuildVSchemaGraph cell1
```

## Examples

```bash
etcdctl get --prefix /vitess/
```
