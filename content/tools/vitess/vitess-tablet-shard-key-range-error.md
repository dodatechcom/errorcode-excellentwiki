---
title: "[Solution] Vitess Tablet Shard Key Range Error"
description: "Fix Vitess shard key range errors when routing queries to incorrect shards"
tools: ["vitess"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vitess Tablet Shard Key Range Error

Shard key range errors occur when vtgate routes queries to the wrong shard because the key range boundaries are incorrectly defined.

## Common Causes

- VSchema shard key definition does not match actual data distribution
- Key range boundaries overlap or leave gaps
- Hash-based sharding function producing unexpected distribution
- Shard split left inconsistent key ranges

## How to Fix

Check shard key ranges:

```bash
vtctlclient GetShard keyspace1/0
```

Verify VSchema routing rules:

```bash
vtctlclient GetVSchema keyspace1
```

Update VSchema with correct key column:

```bash
vtctlclient ApplyVSchema -vschema={"sharded":true,"vindexes":{"hash":{"type":"hash"}},"tables":{"users":{"column_vindexes":[{"column":"user_id","name":"hash"}]}}}
```

## Examples

```bash
vtctlclient FindTabletForShard keyspace1 -80 12345
```
