---
title: "[Solution] Ubuntu Server: apt-dpkg-frontend-lock"
description: "Fix Ubuntu apt-dpkg-frontend-lock. dpkg frontend lock resource unavailable during apt operations."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Dpkg Frontend Lock

dpkg cannot acquire the frontend lock because another process is running.

## Common Causes
- Automatic update in progress
- Leftover lock from crashed apt session
- Cron job running apt in background
- Another admin session performing updates

## How to Fix
1. Identify the blocking process
```bash
sudo fuser -v /var/lib/dpkg/lock-frontend
```
2. Wait for the process to finish or stop it
```bash
sudo systemctl stop unattended-upgrades
sudo kill <PID>
```
3. Remove stale locks if process is dead
```bash
sudo rm -f /var/lib/dpkg/lock-frontend
sudo rm -f /var/lib/dpkg/lock
sudo dpkg --configure -a
```

## Examples
```bash
$ sudo fuser -v /var/lib/dpkg/lock-frontend
                     USER    PID   ACCESS COMMAND
/var/lib/dpkg/lock-frontend: root   1234   F...M  apt
```
