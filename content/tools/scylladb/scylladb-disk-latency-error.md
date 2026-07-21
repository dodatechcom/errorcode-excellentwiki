---
title: "[Solution] ScyllaDB Disk Latency Error"
description: "How to fix ScyllaDB high disk latency errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Slow disk hardware
- Disk full causing write amplification
- I/O scheduler misconfiguration
- Too many concurrent disk operations

## How to Fix

Check disk latency:

```bash
iostat -x 1 5
```

## Examples

```bash
iostat -x 1 5
nodetool tablestats my_keyspace.my_table | grep -i latency
```
