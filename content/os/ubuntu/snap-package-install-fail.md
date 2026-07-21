---
title: "[Solution] Ubuntu Server: snap-package-install-fail"
description: "Fix Ubuntu snap-package-install-fail. snap package installation fails due to store or disk issues."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Snap Package Install Fail

snapd fails to install a package.

## Common Causes
- Snap store unreachable
- Insufficient disk space for snap
- snapd service not running
- Confinement issue on Ubuntu Core

## How to Fix
1. Check snapd service
```bash
sudo systemctl status snapd
snap version
```
2. Manually refresh snap store
```bash
sudo snap refresh --list
sudo snap refresh
```
3. Check disk space
```bash
df -h /var/lib/snapd
```

## Examples
```bash
$ sudo snap install nextcloud
error: access denied when trying to access the snap store

$ sudo systemctl restart snapd
```
