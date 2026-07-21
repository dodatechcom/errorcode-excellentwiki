---
title: "[Solution] ScyllaDB IO Queue Full Error"
description: "How to fix ScyllaDB IO queue full errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Too many concurrent I/O operations
- Disk saturated
- IO scheduler misconfiguration

## How to Fix

Check IO queue:

```bash
nodetool tpstats | grep -i io
```

## Examples

```bash
nodetool tpstats
iostat -x 1 5
```
