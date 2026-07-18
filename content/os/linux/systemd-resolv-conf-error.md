---
title: "[Solution] Linux: systemd-resolv-conf-error — /etc/resolv.conf configuration error"
description: "Fix Linux systemd-resolv-conf-error errors. /etc/resolv.conf configuration error with these solutions."
platforms: ["linux"]
severities: ["critical"]
error-types: ["network-error"]
weight: 10
---

# Linux: systemd-resolv-conf-error — /etc/resolv.conf configuration error

Fix Linux systemd-resolv-conf-error errors. This guide covers common causes, step-by-step fixes, real-world scenarios, and prevention tips.

## Common Causes

- Not symlinked properly
- Multiple managers
- Wrong DNS servers
- Loopback DNS not running

## How to Fix

### 1. Check
```bash
ls -la /etc/resolv.conf
cat /etc/resolv.conf
```

### 2. Fix Symlink
```bash
sudo rm /etc/resolv.conf
sudo ln -s /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
```

### 3. Static Config
```bash
sudo tee /etc/resolv.conf << EOF
nameserver 8.8.8.8
nameserver 1.1.1.1
search example.com
EOF
```

### 4. Configure NM
```bash
sudo tee /etc/NetworkManager/conf.d/dns.conf << EOF
[main]
dns=systemd-resolved
EOF
```

## Common Scenarios

- DNS failing
- Overwritten on reboot
- Works manually not in services

## Prevent It

- Use one DNS manager
- Point to valid servers
- Use chattr +i if needed
