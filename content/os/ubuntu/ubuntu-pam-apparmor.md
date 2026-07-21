---
title: "Ubuntu PAM AppArmor Denial Error"
description: "PAM authentication module denied by AppArmor profile"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu PAM AppArmor Denial Error

PAM authentication module denied by AppArmor profile

## Common Causes

- AppArmor profile for PAM module not allowing required access
- PAM module trying to read files blocked by profile
- Login failing due to AppArmor denying PAM operation
- AppArmor in enforce mode blocking PAM functionality

## How to Fix

1. Check denials: `sudo journalctl -k | grep apparmor.*pam`
2. View PAM AppArmor profile: `sudo cat /etc/apparmor.d/abstractions/pam`
3. Switch to complain mode: `sudo aa-complain /etc/apparmor.d/<profile>`
4. Update PAM profile with required rules

## Examples

```bash
# Check AppArmor PAM denials
sudo journalctl -k | grep -i 'apparmor.*DENIED.*pam'

# Switch PAM profile to complain mode
sudo aa-complain /etc/apparmor.d/usr.sbin/login

# Reload AppArmor
sudo systemctl reload apparmor
```
