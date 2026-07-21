---
title: "[Solution] ScyllaDB Workload Prioritization Error"
description: "How to fix ScyllaDB workload prioritization and scheduling errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Scheduling groups misconfigured
- One workload starving others
- IO priority not set correctly

## How to Fix

Configure scheduling:

```yaml
scheduling_groups:
  - name: statement
    io_priority:
      read: high
      write: high
```

## Examples

```bash
nodetool tpstats | grep -i scheduling
```
