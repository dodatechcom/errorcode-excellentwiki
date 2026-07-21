---
title: "[Solution] ScyllaDB Not Enough Nodes Error"
description: "How to fix ScyllaDB cluster not enough nodes for replication errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Replication factor higher than node count
- Nodes down reducing available replicas
- Network partition isolating nodes

## How to Fix

Check cluster status:

```bash
nodetool status
```

Reduce RF or add nodes:

```cql
ALTER KEYSPACE my_keyspace WITH replication = {'class': 'NetworkTopologyStrategy', 'dc1': 3};
```

## Examples

```bash
nodetool status
cqlsh -e "DESCRIBE KEYSPACE my_keyspace;"
```
