---
title: "[Solution] Linux: dpkg-corrupted — dpkg corrupted database"
description: "Fix Linux dpkg-corrupted errors. dpkg corrupted database with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["package-manager"]
weight: 10
---
# Linux: dpkg Database Corrupted

A corrupted dpkg database prevents all package management operations. This is often caused by an interrupted dpkg operation.

## Common Causes

- Power loss or system crash during dpkg operation
- Manual deletion of dpkg database files
- Running out of disk space during package installation
- Conflicting dpkg instances running simultaneously

## How to Fix

### 1. Backup Current Database

```bash
sudo cp -a /var/lib/dpkg /var/lib/dpkg.backup
```

### 2. Recover Status File

```bash
# Check if status file exists
ls -la /var/lib/dpkg/status

# Use backup if available
sudo cp /var/lib/dpkg/status-old /var/lib/dpkg/status

# Or use available
sudo cp /var/lib/dpkg/status-available /var/lib/dpkg/status
```

### 3. Rebuild Database from dpkg Info

```bash
sudo dpkg --clear-avail
sudo apt update
sudo apt --fix-broken install
```

### 4. Last Resort: Reinstall Packages

```bash
# List installed packages
dpkg --get-selections > /tmp/packages.txt
# Recreate database and reinstall
```

## Examples

```bash
$ sudo apt install vim
E: The package database or status file could not be opened
E: Could not open file /var/lib/dpkg/status - open (2: No such file or directory)

$ sudo cp /var/lib/dpkg/status-old /var/lib/dpkg/status
$ sudo apt update
```
