---
title: "[Solution] Linux: sysctl-parameter-error -- sysctl parameter not found"
description: "Fix Linux sysctl parameter errors. Sysctl kernel parameter not found or read-only."
os: ["linux"]
error-types: ["kernel-error"]
severities: ["error"]
---

# Linux: Sysctl Parameter Error

Sysctl parameter errors occur when kernel tunables cannot be found or written.

## Common Causes

- Parameter name misspelled or not in current kernel
- Kernel module providing parameter not loaded
- Parameter is read-only after boot
- sysctl.d configuration file has syntax errors
- Container restricting sysctl access

## How to Fix

### 1. Find Parameter

```bash
sysctl -a | grep <partial_name>
cat /proc/sys/net/ipv4/ip_forward
```

### 2. Set Parameter

```bash
sudo sysctl -w net.ipv4.ip_forward=1
echo "net.ipv4.ip_forward = 1" | sudo tee /etc/sysctl.d/99-forward.conf
sudo sysctl -p /etc/sysctl.d/99-forward.conf
```

### 3. Fix Configuration

```bash
sudo sysctl --system 2>&1 | grep -i error
```

## Examples

```bash
$ sudo sysctl -w net.ipv4.ip_forwardz=1
sysctl: unknown key 'net.ipv4.ip_forwardz'
$ sysctl -a | grep ip_forward
net.ipv4.ip_forward = 0
$ sudo sysctl -w net.ipv4.ip_forward=1
net.ipv4.ip_forward = 1
```
