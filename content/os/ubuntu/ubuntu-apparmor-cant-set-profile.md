---
title: "[Solution] Ubuntu Server: ubuntu-apparmor-cant-set-profile"
description: "Fix Ubuntu ubuntu-apparmor-cant-set-profile. Cannot set AppArmor profile mode."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu AppArmor Can't Set Profile

Cannot set or change AppArmor profile mode for a service.

## Common Causes
- Profile file not in /etc/apparmor.d/
- Profile syntax error
- AppArmor module not loaded

## How to Fix
1. Check AppArmor module
```bash
cat /sys/module/apparmor/parameters/enabled
```
2. Load module if needed
```bash
sudo modprobe apparmor
```
3. Manually parse profile
```bash
sudo apparmor_parser -r /etc/apparmor.d/<profile>
```

## Examples
```bash
$ cat /sys/module/apparmor/parameters/enabled
Y

$ sudo aa-enforce /etc/apparmor.d/usr.sbin.nginx
```