---
title: "[Solution] Ubuntu Server: dpkg-status-corruption"
description: "Fix Ubuntu dpkg-status-corruption. The dpkg status database is corrupted and unreadable."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Dpkg Status Corruption

The dpkg status database at /var/lib/dpkg/status is corrupted.

## Common Causes
- System crash or power loss during package operation
- Filesystem corruption on /var/lib/dpkg
- Disk failure or I/O error
- Manual editing of status file

## How to Fix
1. Check the status file
```bash
ls -la /var/lib/dpkg/status*
```
2. Restore from backup
```bash
sudo cp /var/lib/dpkg/status-old /var/lib/dpkg/status
```
3. If no backup, rebuild
```bash
sudo cp /var/lib/dpkg/status /var/lib/dpkg/status.corrupt
sudo touch /var/lib/dpkg/status
sudo apt update
sudo apt upgrade
```

## Examples
```bash
$ sudo dpkg --list
dpkg: warning: files list file for package 'nginx' missing; assuming package has no files currently installed
```
