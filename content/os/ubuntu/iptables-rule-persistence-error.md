---
title: "[Solution] Ubuntu Server: iptables-rule-persistence-error"
description: "Fix Ubuntu iptables-rule-persistence-error. iptables rules lost after reboot."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Iptables Rule Persistence Error

iptables rules are not saved and lost after reboot.

## Common Causes
- iptables-persistent not installed
- Rules not saved to file
- Custom iptables script not in rc.local
- netfilter-persistent service not enabled

## How to Fix
1. Install persistence package
```bash
sudo apt install iptables-persistent
```
2. Save current rules
```bash
sudo netfilter-persistent save
# or
sudo iptables-save > /etc/iptables/rules.v4
sudo ip6tables-save > /etc/iptables/rules.v6
```
3. Enable service
```bash
sudo systemctl enable netfilter-persistent
```

## Examples
```bash
$ sudo iptables -L -n | head -10
Chain INPUT (policy ACCEPT)
target     prot opt source               destination
ACCEPT     tcp  --  0.0.0.0/0            0.0.0.0/0            tcp dpt:22

$ sudo netfilter-persistent save
[ ok ] Saving current rules...
```
