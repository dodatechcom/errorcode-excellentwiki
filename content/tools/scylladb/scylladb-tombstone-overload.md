---
title: "[Solution] ScyllaDB Tombstone Overload Error"
description: "How to fix ScyllaDB tombstone warning and overload errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes

- Wide partitions with many deletes
- TTL causing mass expirations
- Range deletes creating many tombstones
- Tombstone gc_grace_seconds too long

## How to Fix

Reduce tombstones:

```cql
-- Avoid deleting individual rows in wide partitions
-- Use time-based partitioning to naturally expire data
-- Set appropriate gc_grace_seconds
```

Check tombstones:

```bash
nodetool tablestats my_keyspace.my_table | grep -i tombstone
```

## Examples

```bash
nodetool tablestats my_keyspace.my_table | grep tombstone
cqlsh -e "SELECT * FROM my_table WHERE id = 1;" --CL 2>&1 | grep tombstone
```
