---
title: "[Solution] Ubuntu Server: ubuntu-apparmor-aa-logprof-error"
description: "Fix Ubuntu ubuntu-apparmor-aa-logprof-error. AppArmor aa-logprof fails."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu AppArmor AA Logprof Error

aa-logprof fails to update AppArmor profiles from logs.

## Common Causes
- Log file not readable
- Profile syntax prevents update
- No log entries to profile

## How to Fix
1. Check AppArmor logs
```bash
sudo journalctl -k | grep apparmor
```
2. Check profile
```bash
sudo cat /etc/apparmor.d/<profile>
```
3. Run logprof
```bash
sudo aa-logprof
```

## Examples
```bash
$ sudo aa-logprof
Reading log entries from /var/log/syslog.
```