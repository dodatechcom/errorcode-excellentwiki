---
title: "[Solution] Linux: systemd-freezer-error — Cgroup freezer state error"
description: "Fix Linux systemd-freezer-error errors. Cgroup freezer state error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["runtime-error"]
weight: 10
---

# Linux: systemd-freezer-error — Cgroup freezer state error

Fix Linux systemd-freezer-error errors. This guide covers common causes, step-by-step fixes, real-world scenarios, and prevention tips.

## Common Causes

- Controller not available
- Unexpected freezer state
- Container freeze failure
- cgroup v2 migration

## How to Fix

### 1. Check Version
```bash
mount | grep cgroup
stat -f -c %T /sys/fs/cgroup/
```

### 2. Check State
```bash
cat /sys/fs/cgroup/system.slice/<unit>/cgroup.freeze
```

### 3. Unfreeze
```bash
echo 0 | sudo tee /sys/fs/cgroup/system.slice/<unit>/cgroup.freeze
```

### 4. Enable Controllers
```bash
# Add: systemd.unified_cgroup_hierarchy=1
```

## Common Scenarios

- Processes stuck frozen
- Cannot suspend/resume containers
- Freezer errors in journal

## Prevent It

- Ensure cgroup hierarchy mounted
- Use cgroup v2
- Monitor freezer state
