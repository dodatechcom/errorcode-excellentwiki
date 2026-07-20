---
title: "[Solution] Linux: dpkg-error — dpkg error"
description: "Fix Linux dpkg-error errors. dpkg error with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["package-manager"]
weight: 10
---
# Linux: dpkg Error

dpkg errors occur when the Debian package manager fails to install, remove, or configure packages.

## Common Causes

- Corrupted package download or incomplete installation
- Pre/post installation script failure
- Package dependency issues or conflicts
- Filesystem full preventing package writes
- Package overwriting files from another package

## How to Fix

### 1. Fix Broken Packages

```bash
sudo dpkg --configure -a
sudo apt --fix-broken install
```

### 2. Force Package Removal

```bash
sudo dpkg --remove --force-remove-reinstreq <package>
sudo dpkg --purge --force-remove-reinstreq <package>
```

### 3. Reinstall Corrupted Package

```bash
sudo dpkg -i /var/cache/apt/archives/<package>.deb
sudo apt install --reinstall <package>
```

### 4. Check dpkg Database

```bash
sudo dpkg --audit
```

## Examples

```bash
$ sudo apt install mypackage
dpkg: error processing package mypackage (--configure):
 installed mypackage package post-installation script subprocess returned error exit status 1

$ sudo dpkg --configure -a
$ sudo apt --fix-broken install
```
