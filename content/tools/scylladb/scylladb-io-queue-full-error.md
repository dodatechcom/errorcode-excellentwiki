---
title: "[Solution] ScyllaDB IO Queue Full Error"
description: "How to fix ScyllaDB IO queue full errors"
tools: ["scylladb"]
error-types: ["tool-error"]
severities: ["error"]
---

## Common Causes
- Disk I/O saturated
- Too many concurrent requests
- IO scheduler misconfigured

## How to Fix

```yaml
compaction_throughput_mb_per_sec: 64
```

## Examples

```bash
iostat -x 1
```
