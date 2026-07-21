---
title: "Ubuntu Cgroup Namespace Error"
description: "Container or process cannot create or enter cgroup namespace"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Cgroup Namespace Error

Container or process cannot create or enter cgroup namespace

## Common Causes

- User namespace not enabled for cgroup
- insufficient privileges to create cgroup namespace
- System using cgroupv2 but application expects cgroupv1
- unshare command failing with EPERM

## How to Fix

1. Check cgroup namespace: `ls /proc/self/ns/cgroup`
2. Enable user cgroup namespace: `kernel.unprivileged_userns_clone=1`
3. Test: `unshare --cgroup echo test`
4. Check kernel config: `grep CGROUP /boot/config-$(uname -r)`

## Examples

```bash
# Check cgroup namespace
ls -la /proc/self/ns/cgroup

# Test cgroup namespace
unshare --cgroup echo 'namespace test'

# Enable user namespaces
echo 'kernel.unprivileged_userns_clone=1' | sudo tee /etc/sysctl.d/10-userns.conf
sudo sysctl -p /etc/sysctl.d/10-userns.conf
```
