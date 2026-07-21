---
title: "[Solution] Ubuntu Server: ubuntu-kernel-tcp-buffer-error"
description: "Fix Ubuntu ubuntu-kernel-tcp-buffer-error. TCP buffer size too small causing packet drops."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Ubuntu Kernel TCP Buffer Error

TCP buffer size is too small causing packet drops.

## Common Causes
- TCP buffer values at defaults
- High bandwidth connection with small buffers
- vm.tcp values not tuned

## How to Fix
1. Check current TCP buffers
```bash
cat /proc/sys/net/core/rmem_max
cat /proc/sys/net/core/wmem_max
```
2. Tune buffers
```bash
sudo sysctl -w net.core.rmem_max=16777216
sudo sysctl -w net.core.wmem_max=16777216
sudo sysctl -w net.ipv4.tcp_rmem="4096 87380 16777216"
sudo sysctl -w net.ipv4.tcp_wmem="4096 65536 16777216"
```
3. Make persistent
```bash
echo 'net.core.rmem_max=16777216' | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```

## Examples
```bash
$ cat /proc/sys/net/core/rmem_max
212992
```