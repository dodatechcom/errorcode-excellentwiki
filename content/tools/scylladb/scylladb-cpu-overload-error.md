---
title: "[Solution] ScyllaDB CPU Overload Error"
description: "How to fix ScyllaDB CPU overload errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Query too CPU-intensive
- Compaction using too many CPUs
- Shard imbalance

## How to Fix

```yaml
cpu_quota: 2
```

## Examples

```bash
nodetool tpstats | grep -i pending
```
