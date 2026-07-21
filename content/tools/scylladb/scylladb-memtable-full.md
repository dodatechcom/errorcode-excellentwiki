---
title: "[Solution] ScyllaDB Memtable Full Error"
description: "How to fix ScyllaDB memtable full errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Write throughput too high
- memtable_total_space_in_mb too low
- Flush cannot keep up with writes

## How to Fix

Increase memtable size:

```yaml
memtable_total_space_in_mb: 2048
```

## Examples

```bash
grep memtable_total_space /etc/scylla/scylla.yaml
nodetool tpstats | grep -i memtable
```
