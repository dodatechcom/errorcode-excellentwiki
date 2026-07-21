---
title: "[Solution] Linux: systemd-logrotate-error -- logrotate timer failure"
description: "Fix Linux systemd logrotate timer errors. Logrotate timer failed to execute or complete."
os: ["linux"]
error-types: ["systemd-error"]
severities: ["warning"]
---

# Linux: Systemd Logrotate Timer Error

Systemd logrotate timer errors occur when the automatic log rotation timer fails.

## Common Causes

- Logrotate configuration syntax errors
- Insufficient disk space for rotated logs
- Permission issues on log directories
- Missing postrotate scripts or broken pipes
- Timer unit not enabled or misconfigured

## How to Fix

### 1. Check Timer Status

```bash
systemctl status logrotate.timer
systemctl list-timers --all | grep logrotate
journalctl -u logrotate -n 30
```

### 2. Test Logrotate Manually

```bash
sudo logrotate -d /etc/logrotate.conf
sudo logrotate -f /etc/logrotate.conf
```

### 3. Fix Configuration

```bash
sudo cat /etc/logrotate.conf
sudo logrotate --debug /etc/logrotate.d/*
```

## Examples

```bash
$ systemctl status logrotate.timer
logrotate.timer - Daily rotation of log files
     Active: inactive (dead)
$ sudo logrotate -d /etc/logrotate.conf
error: skipping "/var/log/huge.log" because parent directory has insecure permissions
```
