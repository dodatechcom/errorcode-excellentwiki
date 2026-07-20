---
title: "[Solution] Linux: apt-404-not-found — apt 404 repository not found"
description: "Fix Linux apt-404-not-found errors. apt 404 repository not found with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["package-manager"]
weight: 6
---

# Linux: APT 404 Not Found Error

APT 404 not found errors occur when the package manager encounters issues during repository updates or package operations.

## Common Causes

- Repository URL unreachable or invalid
- GPG key missing or expired
- Package dependency resolution conflicts
- dpkg database corruption
- Network connectivity issues

## How to Fix

### 1. Check APT Status

```bash
sudo apt update 2>&1 | tail -20
cat /etc/apt/sources.list
ls /etc/apt/sources.list.d/
```

### 2. Fix Package Manager

```bash
sudo apt --fix-broken install
sudo dpkg --configure -a
sudo apt clean
```

### 3. Check Network

```bash
ping -c 3 archive.ubuntu.com
curl -I http://archive.ubuntu.com
```

### 4. Update Repositories

```bash
sudo apt update --allow-insecure-repositories
sudo apt upgrade
```

## Examples

```bash
$ sudo apt update
Err:1 http://archive.ubuntu.com jammy InRelease
  Could not resolve 'archive.ubuntu.com'
$ ping archive.ubuntu.com
ping: archive.ubuntu.com: Name or service not known
# DNS issue - check /etc/resolv.conf

$ sudo apt --fix-broken install
Reading package lists... Done
Building dependency tree... Done
Correcting dependencies... Done
```
