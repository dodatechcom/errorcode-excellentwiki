---
title: "[Solution] Ubuntu Server: ubuntu-systemd-first-boot-error"
description: "Fix Ubuntu ubuntu-systemd-first-boot-error. systemd-first-boot fails on initial setup."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Systemd First Boot Error

systemd-first-boot fails during initial system configuration.

## Common Causes
- /etc machine-id not generated
- Locale not configured
- First boot already completed

## How to Fix
1. Check first boot status
```bash
systemd-first-boot --status
```
2. Re-run first boot
```bash
sudo systemd-firstboot --force
```
3. Generate machine-id
```bash
sudo systemd-machine-id-setup
```

## Examples
```bash
$ systemd-first-boot --status
First boot is skipped: machine-id already initialized
```