---
title: "[Solution] Ubuntu Server: ufw-block-all-traffic"
description: "Fix Ubuntu ufw-block-all-traffic. UFW rules accidentally block all traffic including SSH."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# UFW Block All Traffic

UFW configuration blocks all traffic including SSH access.

## Common Causes
- Default policy set to deny before allowing SSH
- SSH rule not added before enabling UFW
- Rule order causing SSH to be blocked
- IPv6 rules not configured

## How to Fix
1. Via console or recovery mode
```bash
sudo ufw disable
```
2. Reconfigure with SSH first
```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow 22/tcp
sudo ufw enable
```
3. Verify rules
```bash
sudo ufw status numbered
```

## Examples
```bash
$ sudo ufw status numbered
[ 1] 22/tcp    ALLOW IN    Anywhere
[ 2] 80/tcp    ALLOW IN    Anywhere
[ 3] 443/tcp   ALLOW IN    Anywhere
```
