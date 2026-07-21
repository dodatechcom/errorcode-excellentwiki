---
title: "[Solution] Ubuntu Server: dpkg-error-processing-package"
description: "Fix Ubuntu dpkg-error-processing-package. dpkg encounters errors while configuring packages."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Dpkg Error Processing Package

dpkg encounters an error while configuring or unpacking a package and halts.

## Common Causes
- Broken package dependencies
- Insufficient disk space during installation
- Conflicting files from different packages
- Post-installation script failure
- Corrupted .deb package

## How to Fix
1. Force reconfigure pending packages
```bash
sudo dpkg --configure -a
```
2. Fix broken dependencies
```bash
sudo apt --fix-broken install
```
3. Force remove problematic package
```bash
sudo dpkg --remove --force-remove-reinstreq <package>
sudo apt --fix-broken install
```

## Examples
```bash
$ sudo dpkg --configure -a
dpkg: error processing package nginx-common (--configure):
 installed nginx-common package post-installation script subprocess returned error exit status 1
```
