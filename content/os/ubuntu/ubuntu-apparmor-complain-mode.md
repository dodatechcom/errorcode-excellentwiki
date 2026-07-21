---
title: "Ubuntu AppArmor in Complain Mode"
description: "AppArmor profile not enforcing, only logging violations"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu AppArmor in Complain Mode

AppArmor profile not enforcing, only logging violations

## Common Causes

- Profile loaded in complain mode
- System booted with apparmor=0
- Profile set to complain with aa-complain
- Audit mode enabled instead of enforce

## How to Fix

1. Check status: `aa-status | grep <profile>`
2. Switch to enforce: `aa-enforce /etc/apparmor.d/<profile>`
3. Reload: `apparmor_parser -r /etc/apparmor.d/<profile>`
4. Check kernel params: `cat /proc/cmdline`

## Examples

```bash
# Check AppArmor status
sudo aa-status | grep -A2 'nginx'

# Switch profile to enforce
sudo aa-enforce /etc/apparmor.d/usr.sbin.nginx

# Reload AppArmor
sudo systemctl reload apparmor
```
