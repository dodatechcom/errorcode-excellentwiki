---
title: "Ubuntu Cgroup Memory Limit Error"
description: "Container or process exceeds cgroup memory limit and is OOM killed"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Cgroup Memory Limit Error

Container or process exceeds cgroup memory limit and is OOM killed

## Common Causes

- Memory limit set too low for workload
- Memory leak in application
- OOM score adjustment not configured
- Swap not available within cgroup

## How to Fix

1. Check memory usage: `cat /sys/fs/cgroup/memory/<group>/memory.usage_in_bytes`
2. Increase limit: `echo <bytes> > /sys/fs/cgroup/memory/<group>/memory.limit_in_bytes`
3. Monitor with: `systemd-cgtop`
4. Adjust OOM score: `echo -1000 > /proc/<pid>/oom_score_adj`

## Examples

```bash
# Check cgroup memory usage
systemd-cgtop

# Check specific cgroup memory
cat /sys/fs/cgroup/memory/mygroup/memory.usage_in_bytes

# Set memory limit
echo 2G > /sys/fs/cgroup/memory/mygroup/memory.limit_in_bytes
```
