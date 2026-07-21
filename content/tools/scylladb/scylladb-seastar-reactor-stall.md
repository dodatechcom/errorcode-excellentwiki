---
title: "[Solution] ScyllaDB Seastar Reactor Stall Detected"
description: "How to fix ScyllaDB reactor stall errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Long-running task blocking reactor thread
- Excessive lock contention
- Large allocation in reactor context
- Sleep in reactor thread

## How to Fix

Check stall logs:

```bash
grep -i stall /var/log/scylla/scylla.log
```

## Examples

```bash
grep -i 'reactor.*stall' /var/log/scylla/scylla.log | tail -5
nodetool tpstats
```
