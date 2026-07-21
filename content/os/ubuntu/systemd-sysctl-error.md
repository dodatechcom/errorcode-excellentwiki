---
title: "[Solution] Ubuntu Server: system-sysctl-error"
description: "Fix Ubuntu system-sysctl-error. systemd-sysctl fails to apply kernel parameters."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd Sysctl Error

systemd-sysctl encounters errors applying kernel parameters at boot.

## Common Causes
- sysctl parameter does not exist
- Value out of allowed range
- Permission denied for parameter
- Syntax error in sysctl.d file

## How to Fix
1. Check current sysctl value
```bash
sudo sysctl <parameter>
```
2. Verify parameter exists
```bash
sudo sysctl -a | grep <parameter>
```
3. Fix sysctl.d file
```bash
sudo nano /etc/sysctl.d/99-custom.conf
sudo sysctl --system
```

## Examples
```bash
$ sudo sysctl net.ipv4.ip_forward
net.ipv4.ip_forward = 0

$ sudo sysctl -a | grep nonexistent
# (no output -- parameter does not exist)
```
