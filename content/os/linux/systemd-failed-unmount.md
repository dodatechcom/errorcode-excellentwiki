---
title: "[Solution] Linux: systemd-failed-unmount — Failed unmounting during shutdown"
description: "Fix Linux systemd-failed-unmount errors. Failed unmounting during shutdown with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["boot-error"]
weight: 10
---

# Linux: systemd Failed Unmount Error

systemd failed unmount errors occur when the systemd failed unmount component fails to operate correctly.

## Common Causes

- Misconfiguration in unit files or systemd configuration
- Permission or ownership issues on required paths
- Dependency failures from other systemd units
- Resource limits or system constraints reached
- SELinux or AppArmor policy blocking operations

## How to Fix

### 1. Check systemd Unit Status

```bash
sudo systemctl status systemd-failed-unmount
sudo journalctl -u systemd-failed-unmount --no-pager -n 50
```

### 2. Verify Configuration Files

```bash
ls /etc/systemd/*.conf /usr/lib/systemd/*.conf 2>/dev/null
systemctl cat systemd-failed-unmount
```

### 3. Check System Logs

```bash
sudo journalctl -xe --no-pager -n 30
sudo dmesg | tail -20
```

### 4. Restart and Re-evaluate

```bash
sudo systemctl daemon-reload
sudo systemctl restart systemd-failed-unmount
```

## Examples

```bash
$ sudo systemctl status systemd-failed-unmount
* systemd-failed-unmount.service - systemd Failed Unmount
   Loaded: loaded (/usr/lib/systemd/system/systemd-failed-unmount.service; static)
   Active: failed (Result: exit-code)

$ sudo journalctl -u systemd-failed-unmount -n 10
Jul 20 14:30:45 server systemd[failed-unmount][12345]: Failed to process configuration
Jul 20 14:30:45 server systemd[1]: systemd-failed-unmount.service: Main process exited, code=exited, status=1/FAILURE
```
