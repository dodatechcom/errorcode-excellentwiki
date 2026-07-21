---
title: "[Solution] ScyllaDB CPU Overload Error"
description: "How to fix ScyllaDB CPU overload errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- High query throughput
- Compaction consuming CPU
- Too many concurrent requests
- Query requiring excessive computation

## How to Fix

Check CPU usage:

```bash
top -H -p $(pgrep scylla)
```

Reduce load:

```cql
-- Add LIMIT to queries
-- Reduce consistency level
```

## Examples

```bash
top -H -p $(pgrep scylla)
nodetool tpstats
```
