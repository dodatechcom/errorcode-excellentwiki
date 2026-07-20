---
title: "[Solution] Linux: resolvconf-error — resolvconf DNS error"
description: "Fix Linux resolvconf-error errors. resolvconf DNS error with these solutions."
platforms: ["linux"]
severities: ["warning"]
error-types: ["network"]
weight: 6
---
# Linux: resolvconf Error

resolvconf errors occur when the DNS resolver configuration management system fails to update /etc/resolv.conf.

## Common Causes

- resolvconf service not installed or running
- /etc/resolv.conf is a static file, not managed by resolvconf
- resolvconf package conflict with systemd-resolved
- Network interface not passing DNS information to resolvconf
- Symlink missing / broken for /etc/resolv.conf

## How to Fix

### 1. Check /etc/resolv.conf

```bash
ls -la /etc/resolv.conf
cat /etc/resolv.conf
```

### 2. Restart resolvconf

```bash
sudo systemctl restart resolvconf
sudo resolvconf -u
```

### 3. Set DNS Servers Manually

```bash
# For resolvconf-based systems
echo "nameserver 8.8.8.8" | sudo tee /etc/resolvconf/resolv.conf.d/head
sudo resolvconf -u
```

### 4. Switch to systemd-resolved

```bash
sudo systemctl enable --now systemd-resolved
sudo ln -sf /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
```

## Examples

```bash
$ ls -la /etc/resolv.conf
-rw-r--r-- 1 root root 30 Jul 20 14:30 /etc/resolv.conf

$ cat /etc/resolv.conf
nameserver 127.0.0.53

$ sudo systemctl status systemd-resolved
● systemd-resolved.service - Network Name Resolution
     Active: active (running)
```
