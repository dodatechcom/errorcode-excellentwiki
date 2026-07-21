---
title: "Ubuntu Cgroup v2 Incompatible Error"
description: "Application requires cgroup v1 but system running cgroup v2"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Cgroup v2 Incompatible Error

Application requires cgroup v1 but system running cgroup v2

## Common Causes

- System booted with cgroup v2 (unified hierarchy)
- Application uses deprecated cgroup v1 controllers
- Docker or Podman needs cgroup v1 for certain features
- Kernel parameter not set for cgroup v1

## How to Fix

1. Check cgroup version: `stat -fc %T /sys/fs/cgroup/` (cgroup2fs for v2)
2. Boot with cgroup v1: add `systemd.unified_cgroup_hierarchy=0` to kernel params
3. Use cgroupv1 mode: `cgroupfs-mount`
4. Check Docker: `docker info | grep -i cgroup`

## Examples

```bash
# Check cgroup version
stat -fc %T /sys/fs/cgroup/

# Check Docker cgroup driver
docker info | grep -i cgroup

# Temporarily switch to cgroup v1
sudo sed -i 's/GRUB_CMDLINE_LINUX=.*/GRUB_CMDLINE_LINUX="systemd.unified_cgroup_hierarchy=0"/' /etc/default/grub
sudo update-grub && sudo reboot
```
