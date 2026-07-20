---
title: "[Solution] Linux: zypper-lock-error — zypper lock error"
description: "Fix Linux zypper-lock-error errors. zypper lock error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["package-manager"]
weight: 6
---

# Linux: Zypper Lock Error

Zypper lock errors occur when another package operation holds the lock.

## Common Causes

- Another zypper process running
- Previous zypper session crashed without releasing lock
- RPM database locked by another process
- Automatic update running in background
- Package kit or software center holding lock

## How to Fix

### 1. Check for Running Processes

```bash
ps aux | grep zypper
ps aux | grep rpm
```

### 2. Check Lock File

```bash
ls -la /var/run/zypper.pid
ls -la /var/lib/rpm/.rpm.lock
```

### 3. Remove Stale Lock

```bash
sudo rm -f /var/run/zypper.pid
sudo rm -f /var/lib/rpm/.rpm.lock
```

### 4. Force Kill Stuck Process

```bash
sudo kill -9 <pid>
sudo zypper --non-interactive refresh
```

## Examples

```bash
$ sudo zypper install nginx
Waiting for process 12345 to release the zypper lock...
# Another zypper process already running

$ ps aux | grep zypper
root     12345  0.0  0.0   1234  567 ?        S    Jul20  0:00 zypper dup
# Previous zypper command stuck

$ sudo kill -9 12345
$ sudo rm -f /var/run/zypper.pid
$ sudo zypper install nginx
# Now succeeds
```
