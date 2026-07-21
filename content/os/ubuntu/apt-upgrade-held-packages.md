---
title: "[Solution] Ubuntu Server: apt-upgrade-held-packages"
description: "Fix Ubuntu apt-upgrade-held-packages. apt upgrade blocked by packages held at specific versions."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Apt Upgrade Held Packages

Certain packages are held at their current version and block the upgrade process.

## Common Causes
- System admin manually held packages
- metapackage pinning for kernel or drivers
- Third-party PPA providing conflicting version
- Package intentionally held to prevent regression

## How to Fix
1. Check which packages are held
```bash
apt-mark showhold
```
2. Unhold packages to allow upgrade
```bash
sudo apt-mark unhold <package>
sudo apt upgrade
```
3. Rehold if needed after upgrade
```bash
sudo apt-mark hold <package>
```

## Examples
```bash
$ apt-mark showhold
linux-image-generic
nvidia-driver-510

$ sudo apt-mark unhold linux-image-generic
$ sudo apt upgrade
```
