---
title: "AppArmor Profile in Complain Mode"
description: "AppArmor security profile is not enforcing and only logging violations"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# AppArmor Profile in Complain Mode

AppArmor security profile is not enforcing and only logging violations

## Common Causes

- Profile loaded in complain mode instead of enforce
- Profile has syntax errors preventing enforcement
- System booted with apparmor=0 kernel parameter
- Profile explicitly set to complain with aa-complain

## How to Fix

1. Check profile mode: `sudo aa-status`
2. Switch to enforce: `sudo aa-enforce /etc/apparmor.d/usr.sbin.nginx`
3. Check kernel params: `cat /proc/cmdline` for apparmor settings
4. Reload profile: `sudo systemctl reload apparmor`

## Examples

```bash
# Check AppArmor status
sudo aa-status

# Switch profile to enforce mode
sudo aa-enforce /etc/apparmor.d/usr.sbin.nginx

# Reload AppArmor
sudo systemctl reload apparmor
```
