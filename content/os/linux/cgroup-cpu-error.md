---
title: "[Solution] Linux: cgroup-cpu-error -- cgroup CPU throttling"
description: "Fix Linux cgroup CPU throttling errors. Cgroup CPU quota limiting performance."
os: ["linux"]
error-types: ["cgroup-error"]
severities: ["error"]
---

# Linux: Cgroup CPU Error

Cgroup CPU errors occur when processes are throttled due to CPU quota.

## Common Causes

- CPU quota too restrictive for workload
- CPU period too short causing excessive throttling
- Multiple cgroups competing for CPU on same core
- cpuset not including enough CPU cores
- RT throttling preventing real-time scheduling

## How to Fix

### 1. Check CPU Throttling

```bash
cat /sys/fs/cgroup/cpu/cpu.stat
cat /sys/fs/cgroup/cpu/cpu.cfs_quota_us
cat /sys/fs/cgroup/cpu/cpu.cfs_period_us
```

### 2. Increase CPU Quota

```bash
echo 200000 | sudo tee /sys/fs/cgroup/cpu/mygroup/cpu.cfs_quota_us
sudo systemctl set-property <service> CPUQuota=200%
```

### 3. Check RT Throttle

```bash
cat /sys/fs/cgroup/cpu/cpu.rt_runtime_us
echo 950000 | sudo tee /sys/fs/cgroup/cpu/cpu.rt_runtime_us
```

## Examples

```bash
$ cat /sys/fs/cgroup/cpu/cpu.stat
nr_periods 10000
nr_throttled 8500
throttled_time 45000000000
# 85% of periods are throttled
$ cat /sys/fs/cgroup/cpu/cpu.cfs_quota_us
50000
# 50ms per 100ms period = 50% of one CPU
```
