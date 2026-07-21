---
title: "[Solution] ScyllaDB Keyspace Error"
description: "How to fix ScyllaDB keyspace errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Keyspace not found
- Keyspace replication factor wrong
- Keyspace strategy class wrong

## How to Fix

```cql
CREATE KEYSPACE myks WITH replication = {'class': 'NetworkTopologyStrategy', 'dc1': 3};
```

## Examples

```cql
DESCRIBE KEYSPACES;
```
