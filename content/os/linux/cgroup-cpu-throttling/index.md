---
title: "Fix Linux: cgroup-cpu-throttling -- cgroup CPU throttling in Linux"
description: "Diagnose and fix excessive cgroup CPU throttling impacting application performance."
os: ["linux"]
error-types: [["resource"]]
severities: [["warning", "info"]]
---

Cgroup CPU throttling occurs when a process group exceeds its allocated CPU quota, causing scheduling delays.

## Common Causes
- CPU quota set too low for workload
- Too many tasks sharing same cgroup
- Burst workload hitting sustained limit
- Misconfigured CPU bandwidth controller

## How to Fix
1. Check current cgroup CPU limits:
   cat /sys/fs/cgroup/cpu/cpu.cfs_quota_us
   cat /sys/fs/cgroup/cpu/cpu.cfs_period_us
2. Monitor throttling events:
   cat /sys/fs/cgroup/cpu/cpu.stat
3. Increase CPU quota if needed:
   echo 200000 > /sys/fs/cgroup/cpu/cpu.cfs_quota_us
4. Migrate heavy tasks to separate cgroup

## Examples
### Common Error Message
throttled: 12583\n
cpu.stat: nr_throttled 12583
