---
title: "AppArmor Denying Write Access"
description: "AppArmor profile blocks write access to files or directories"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# AppArmor Denying Write Access

AppArmor profile blocks write access to files or directories

## Common Causes

- Profile does not include write permission for path
- Path does not match profile rule (case sensitivity)
- Directory not explicitly listed in file rules
- Symlink resolution leads to denied path

## How to Fix

1. Check denials: `sudo journalctl -k | grep apparmor`
2. Edit profile: `sudo nano /etc/apparmor.d/usr.sbin.nginx`
3. Add write rule: `/var/www/html/** rw,`
4. Reload profile: `sudo apparmor_parser -r /etc/apparmor.d/usr.sbin.nginx`

## Examples

```bash
# Check AppArmor denials
sudo journalctl -k | grep -i 'apparmor.*DENIED'

# Edit profile to allow write access
sudo nano /etc/apparmor.d/usr.sbin.nginx

# Reload modified profile
sudo apparmor_parser -r /etc/apparmor.d/usr.sbin.nginx
```
