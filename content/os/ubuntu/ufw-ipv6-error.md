---
title: "[Solution] Ubuntu Server: ufw-ipv6-error"
description: "Fix Ubuntu ufw-ipv6-error. UFW IPv6 rules not working or blocking IPv6 traffic."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# UFW IPv6 Error

UFW IPv6 support fails or misconfigured.

## Common Causes
- IPv6 disabled in UFW config
- IPv6 rules not specified
- Kernel IPv6 module not loaded
- UFW not processing ip6tables

## How to Fix
1. Check IPv6 in UFW config
```bash
grep IPV6 /etc/default/ufw
```
2. Enable IPv6
```bash
sudo sed -i s/IPV6=no/IPV6=yes/ /etc/default/ufw
sudo ufw reload
```
3. Add IPv6 specific rules
```bash
sudo ufw allow proto ipv6-icmp from any to any
```

## Examples
```bash
$ grep IPV6 /etc/default/ufw
IPV6=yes

$ sudo ufw status
Status: active
To                         Action      From
--                         ------      ----
22/tcp                     ALLOW       Anywhere
22/tcp (v6)                ALLOW       Anywhere (v6)
```
