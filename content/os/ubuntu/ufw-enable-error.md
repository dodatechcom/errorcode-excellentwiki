---
title: "[Solution] Ubuntu Server: ufw-enable-error"
description: "Fix Ubuntu ufw-enable-error. UFW fails to enable and blocks all network traffic."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# UFW Enable Error

UFW fails to enable, sometimes blocking all traffic.

## Common Causes
- iptables backend conflict
- UFW already enabled with conflicting rules
- nftables backend not compatible
- Missing iptables kernel modules

## How to Fix
1. Check UFW status
```bash
sudo ufw status verbose
sudo ufw status numbered
```
2. Reset and re-enable
```bash
sudo ufw disable
sudo ufw reset
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow ssh
sudo ufw enable
```
3. If locked out, use console to flush iptables
```bash
sudo iptables -F
sudo iptables -X
```

## Examples
```bash
$ sudo ufw enable
ERROR: Could not set default policy. Could not determine iptables or ip6tables.

$ sudo apt install iptables
$ sudo ufw enable
Firewall is active and enabled on system startup
```
