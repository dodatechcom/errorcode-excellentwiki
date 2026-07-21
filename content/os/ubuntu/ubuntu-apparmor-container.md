---
title: "Ubuntu AppArmor Container Profile Error"
description: "LXC/LXD container denied operations by AppArmor profile"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu AppArmor Container Profile Error

LXC/LXD container denied operations by AppArmor profile

## Common Causes

- Container AppArmor profile too restrictive
- Application requires capabilities blocked by profile
- Mount point not allowed by AppArmor rules
- System call filtered by seccomp profile

## How to Fix

1. Check AppArmor logs: `sudo journalctl -k | grep apparmor`
2. View container profile: `sudo cat /var/lib/lxd/security/apparmor/profiles/lxd-<container>`
3. Disable AppArmor for container: `security.apparmor=false` in container config
4. Use unconfined profile for testing

## Examples

```bash
# Check AppArmor denials for container
sudo journalctl -k | grep -i 'apparmor.*DENIED.*lxd'

# Disable AppArmor for specific container
lxc config set mycontainer security.apparmor false

# Restart container
lxc restart mycontainer
```
