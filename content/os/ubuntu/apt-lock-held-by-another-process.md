---
title: "[Solution] Ubuntu Server: apt-lock-held-by-another-process"
description: "Fix Ubuntu apt-lock-held-by-another-process. Another process holds the dpkg lock preventing apt operations."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Apt Lock Held By Another Process

Another process is holding the apt/dpkg lock, preventing package operations from completing.

## Common Causes
- Automatic update running in background
- Another terminal running apt or dpkg
- Stale lock file from a crashed process
- dpkg frontend lock not released properly

## How to Fix
1. Check what process holds the lock
```bash
sudo lsof /var/lib/dpkg/lock-frontend
sudo fuser /var/lib/dpkg/lock-frontend
```
2. Kill the blocking process if safe
```bash
sudo kill -9 <PID>
```
3. Remove stale lock files
```bash
sudo rm /var/lib/dpkg/lock-frontend
sudo rm /var/lib/dpkg/lock
sudo rm /var/lib/apt/lists/lock
sudo dpkg --configure -a
```

## Examples
```bash
$ sudo apt install nginx
E: Could not get lock /var/lib/dpkg/lock-frontend (11: Resource temporarily unavailable)
E: Unable to lock the administration directory (/var/lib/dpkg/), is another process using it?
```
