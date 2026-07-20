---
title: "[Solution] systemd cgroup v1 vs v2 conflict"
description: "Fix systemd cgroup v1 vs v2 conflict. Resolve incompatible cgroup controller issues between v1 and v2."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd cgroup v1 vs v2 conflict

## Error Description

The system is using mixed cgroup v1 and v2. Resource control may not work correctly.

cgroup v1 and v2 controllers are conflicting.

## Common Causes

Common Causes:
- System booted with unified cgroup hierarchy but some services expect v1
- Container runtime using different cgroup version
- Kernel boot parameter enables mixed mode

## How to Fix

How to Fix:
```bash
# Check cgroup version
stat -fc %T /sys/fs/cgroup/

# For pure cgroup v2, add to kernel cmdline:
# systemd.unified_cgroup_hierarchy=1

# Check current cgroup mount
mount | grep cgroup
```

## Examples

```bash
# Check systemd version
systemctl --version

# Verify unit file syntax
sudo systemd-analyze verify /etc/systemd/system/myapp.service

# Analyze system boot
systemd-analyze blame

# List failed units
systemctl --failed

# View service logs
journalctl -u myapp -n 50 --no-pager
```