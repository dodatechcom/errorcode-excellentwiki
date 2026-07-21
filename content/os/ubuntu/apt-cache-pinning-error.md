---
title: "[Solution] Ubuntu Server: apt-cache-pinning-error"
description: "Fix Ubuntu apt-cache-pinning-error. APT package pinning causes unexpected version selection."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Apt Cache Pinning Error

APT pinning configuration causes unexpected package versions to be selected.

## Common Causes
- Incorrect pin priority values
- Pin priority set higher than default
- Multiple pin entries with conflicting priorities
- Pinning to origin that does not match

## How to Fix
1. Check pinning configuration
```bash
ls /etc/apt/preferences.d/
cat /etc/apt/preferences
```
2. Fix or remove problematic pins
```bash
sudo nano /etc/apt/preferences.d/<file>
```
3. View current pin priorities
```bash
apt-cache policy <package>
```

## Examples
```bash
$ apt-cache policy nginx
nginx:
  Installed: 1.18.0-0ubuntu1
  Candidate: 1.18.0-0ubuntu1
  Version table:
     1.20.0-1 1001
 *** 1.18.0-0ubuntu1 500
        500 http://archive.ubuntu.com/ubuntu focal-updates/main amd64 Packages
```
