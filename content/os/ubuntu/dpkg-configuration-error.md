---
title: "[Solution] Ubuntu Server: dpkg-configuration-error"
description: "Fix Ubuntu dpkg-configuration-error. dpkg configuration scripts fail during package setup."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Dpkg Configuration Error

dpkg fails while running configuration scripts for a package.

## Common Causes
- Configuration script has a bug
- Disk full during configuration
- Missing configuration file template
- Permission issue in /etc

## How to Fix
1. Check the configuration script output
```bash
sudo dpkg --configure <package> 2>&1
```
2. Edit the failing script manually
```bash
sudo nano /var/lib/dpkg/info/<package>.postinst
```
3. Reconfigure from scratch
```bash
sudo rm /var/lib/dpkg/info/<package>.*
sudo apt --reinstall install <package>
```

## Examples
```bash
$ sudo dpkg --configure tzdata
dpkg: error processing package tzdata (--configure):
 installed tzdata package post-installation script subprocess returned error exit status 1
```
