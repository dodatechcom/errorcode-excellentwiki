---
title: "[Solution] Ubuntu Server: system-run-error"
description: "Fix Ubuntu system-run-error. systemd-run fails to start a transient service or scope."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd Run Error

systemd-run fails to create and start a transient service.

## Common Causes
- Invalid unit name or option
- Service type incompatible with options
- Cgroup already exists with same name
- Permission denied for user scope

## How to Fix
1. Check systemd-run syntax
```bash
systemd-run --help | head -30
```
2. Run with debug
```bash
sudo systemd-run --unit=mytransient.service --scope /bin/true
```
3. Check scope status
```bash
systemctl list-units --type=scope
```

## Examples
```bash
$ sudo systemd-run --unit=mytest.service /bin/true
Failed to start transient scope unit: Method "StartTransientUnit" with signature "ssbba(sv)" failed: Invalid argument
```
