---
title: "[Solution] ScyllaDB Network Topology Strategy Error"
description: "How to fix ScyllaDB network topology replication strategy errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Datacenter name wrong in replication config
- RF per DC exceeds node count
- Strategy class incorrect

## How to Fix

Set correct replication:

```cql
ALTER KEYSPACE my_keyspace WITH replication = {
  'class': 'NetworkTopologyStrategy',
  'dc1': 3,
  'dc2': 2
};
```

## Examples

```cql
DESCRIBE KEYSPACE my_keyspace;
nodetool status
```
