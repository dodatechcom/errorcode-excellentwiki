---
title: "[Solution] Linux: apparmor-complain-mode -- complain mode not enforcing"
description: "Fix Linux AppArmor complain mode errors. AppArmor profile in complain mode not enforcing."
os: ["linux"]
error-types: ["apparmor-error"]
severities: ["warning"]
---

# Linux: AppArmor Complain Mode

AppArmor complain mode logs violations without blocking, leaving services exposed.

## Common Causes

- Profile intentionally set to complain for testing
- aa-complain used instead of aa-enforce
- Profile auto-set to complain after load failure
- Container runtime defaulting to complain mode
- Profile not yet promoted to enforce

## How to Fix

### 1. Check Profile Mode

```bash
sudo aa-status | grep -E "enforce|complain"
cat /sys/kernel/security/apparmor/profiles | awk '{print $2}' | sort | uniq -c
```

### 2. Switch to Enforce

```bash
sudo aa-enforce /etc/apparmor.d/<profile>
sudo apparmor_parser -r /etc/apparmor.d/<profile>
```

### 3. Permanently Set Mode

```bash
echo 'profile myapp /usr/bin/myapp flags=(enforce) {' | sudo tee /etc/apparmor.d/usr.bin.myapp
sudo apparmor_parser -r /etc/apparmor.d/usr.bin.myapp
```

## Examples

```bash
$ sudo aa-status | grep complain
/usr/sbin/nginx (complain)
/usr/sbin/rsyslogd (complain)
$ sudo aa-enforce /etc/apparmor.d/usr.sbin.nginx
$ sudo aa-status | grep nginx
/usr/sbin/nginx (enforce)
```
