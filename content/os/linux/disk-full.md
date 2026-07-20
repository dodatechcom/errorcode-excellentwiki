---
title: "[Solution] Linux: disk-full — disk full error"
description: "Fix Linux disk-full errors. disk full error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["disk"]
weight: 10
---
# Linux: Disk Full (No Space Left on Device)

A full disk returns ENOSPC when trying to write new data. This can crash applications, prevent logins, and cause system instability.

## Common Causes

- Log files growing unchecked in /var/log/ without rotation
- Database transaction logs or binlogs accumulating without purge
- Docker images, containers, and volumes consuming disk space
- Package manager cache not cleaned (apt, yum, dnf, pacman)
- Core dump files accumulating from crashed processes
- User downloads and files filling /home

## How to Fix

### 1. Find the Full Filesystem

```bash
df -h
```

### 2. Find Largest Directories

```bash
sudo du -sh /* 2>/dev/null | sort -rh | head -10
sudo du -sh /var/* 2>/dev/null | sort -rh | head -10
```

### 3. Clean Package Cache

```bash
sudo apt clean && sudo apt autoremove --purge  # Debian/Ubuntu
sudo dnf clean all  # RHEL/Fedora
sudo pacman -Sc     # Arch
```

### 4. Clean Journal Logs

```bash
sudo journalctl --vacuum-size=200M
sudo journalctl --vacuum-time=7d
```

### 5. Find Large Files

```bash
sudo find / -xdev -type f -size +100M -exec ls -lh {} \; 2>/dev/null | sort -k5 -rh | head -20
```

### 6. Clean Docker

```bash
docker system prune -a --volumes
```

## Examples

```bash
$ df -h /
Filesystem      Size  Used Avail Use% Mounted on
/dev/sda1        50G   50G     0 100% /

$ sudo du -sh /var/log/* | sort -rh | head -3
3.2G    /var/log/journal
890M    /var/log/syslog
450M    /var/log/kern.log

$ sudo journalctl --vacuum-size=200M
Vacuuming done, freed 3.0G of archived journals
```
