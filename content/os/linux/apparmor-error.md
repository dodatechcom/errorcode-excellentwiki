---
title: "[Solution] Linux: apparmor-error — AppArmor error"
description: "Fix Linux apparmor-error errors. AppArmor error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["process-error"]
weight: 8
---

# Linux: AppArmor Error

AppArmor errors occur when the Mandatory Access Control (MAC) system denies operations outside allowed profiles.

## Common Causes

- Application trying to access files outside its profile
- Profile does not have required permissions
- Profile in complain mode but needs enforce mode
- New application version needs updated profile
- Conflicting profiles for the same application

## How to Fix

### 1. Check AppArmor Status

```bash
sudo aa-status
sudo apparmor_status
```

### 2. Check Denied Operations

```bash
sudo journalctl | grep -i "apparmor\|DENIED" | tail -20
sudo ausearch -m AVC -ts recent 2>/dev/null | tail -20
```

### 3. Set Profile to Complain Mode

```bash
sudo aa-complain /path/to/profile
# Or enforce mode
sudo aa-enforce /path/to/profile
```

### 4. Update Profile

```bash
sudo aa-logprof
sudo aa-genprof /usr/bin/application
sudo systemctl reload apparmor
```

## Examples

```bash
$ sudo aa-status
apparmor module is loaded.
22 profiles are loaded.
10 profiles are in enforce mode.
12 profiles are in complain mode.

$ sudo journalctl | grep apparmor | tail -3
Jul 20 14:30:45 server kernel: audit: type=1400 apparmor="DENIED" operation="open" profile="/usr/sbin/nginx" name="/etc/shadow"
# Nginx profile needs update to access shadow file
```
