---
title: "[Solution] Linux: ssh-banner-error -- SSH banner timeout"
description: "Fix Linux SSH banner errors. SSH banner exchange timeout or protocol mismatch."
os: ["linux"]
error-types: ["ssh-error"]
severities: ["error"]
---

# Linux: SSH Banner Error

SSH banner errors occur when the initial protocol banner exchange fails.

## Common Causes

- SSH daemon not responding with protocol banner
- Non-SSH server running on port 22
- Network device injecting banner text
- TCP wrappers blocking with banner message
- SSH version incompatibility

## How to Fix

### 1. Test Banner Manually

```bash
nc -v host 22
echo "" | nc -w 5 host 22
telnet host 22
```

### 2. Check SSH Configuration

```bash
grep -i banner /etc/ssh/sshd_config
sshd -T | grep banner
```

### 3. Fix Banner Issue

```bash
sudo iptables -L -n | grep 22
echo "Banner none" | sudo tee -a /etc/ssh/sshd_config
sudo systemctl restart sshd
```

## Examples

```bash
$ nc -v host 22
SSH-2.0-OpenSSH_8.9p1 Ubuntu-3ubuntu0.1
$ nc -v host 22
SSH-2.0-OpenSSH_8.9p1
Welcome to restricted device
```
