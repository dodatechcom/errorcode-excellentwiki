---
title: "[Solution] ScyllaDB Unavailable Exception"
description: "How to fix ScyllaDB unavailable exception errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Not enough replicas alive
- Network partition
- Consistency level cannot be met
- All replicas down for the token range

## How to Fix

Check node status:

```bash
nodetool status
```

Reduce consistency level:

```cql
CONSISTENCY ONE;
```

## Examples

```bash
nodetool status
cqlsh -e "CONSISTENCY ONE; SELECT * FROM my_table;"
```
