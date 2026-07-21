---
title: "[Solution] ScyllaDB Repair Failed Error"
description: "How to fix ScyllaDB repair operation failures"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Node unreachable during repair
- Insufficient disk space for repair snapshots
- Repair timeout on large tables
- Too many concurrent repairs

## How to Fix

Run repair:

```bash
nodetool repair my_keyspace my_table
```

Check repair status:

```bash
nodetool repair_status
```

## Examples

```bash
nodetool repair my_keyspace
nodetool repair_status
nodetool repair my_keyspace my_table --full
```
