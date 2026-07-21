---
title: "Ubuntu Unshare Namespace Error"
description: "unshare command fails to create new Linux namespaces"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Unshare Namespace Error

unshare command fails to create new Linux namespaces

## Common Causes

- User namespace creation not allowed
- Insufficient privileges for requested namespace
- Kernel parameter restricting namespace usage
- AppArmor blocking namespace creation

## How to Fix

1. Check user namespaces: `cat /proc/sys/kernel/unprivileged_userns_clone`
2. Enable: `echo 1 | sudo tee /proc/sys/kernel/unprivileged_userns_clone`
3. Use sudo: `sudo unshare --pid --fork bash`
4. Check AppArmor: `dmesg | grep apparmor.*unshare`

## Examples

```bash
# Check user namespace setting
cat /proc/sys/kernel/unprivileged_userns_clone

# Enable user namespaces
echo 1 | sudo tee /proc/sys/kernel/unprivileged_userns_clone

# Create new PID namespace
sudo unshare --pid --fork --mount-proc bash
```
