---
title: "[Solution] ScyllaDB Compact Error"
description: "How to fix ScyllaDB compaction strategy errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Wrong compaction strategy for workload
- Compaction throughput too low
- Tombstone accumulation

## How to Fix

```cql
ALTER TABLE mytable WITH compaction = {'class': 'LeveledCompactionStrategy'};
```

## Examples

```cql
SELECT * FROM system_schema.tables WHERE keyspace_name = 'myks';
```
