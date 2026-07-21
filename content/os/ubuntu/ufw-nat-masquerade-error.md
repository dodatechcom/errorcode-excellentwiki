---
title: "[Solution] Ubuntu Server: ufw-nat-masquerade-error"
description: "Fix Ubuntu ufw-nat-masquerade-error. UFW NAT masquerading rules fail to work."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# UFW NAT Masquerade Error

UFW fails to apply NAT or masquerading rules for routing.

## Common Causes
- IP forwarding not enabled
- post/preceding rules in before.rules not correct
- NAT table not configured
- Missing net.ipv4.ip_forward

## How to Fix
1. Enable IP forwarding
```bash
echo net.ipv4.ip_forward=1 | sudo tee -a /etc/sysctl.conf
sudo sysctl -p
```
2. Edit UFW before rules
```bash
sudo nano /etc/ufw/before.rules
# Add NAT rules at the top:
*nat
:POSTROUTING ACCEPT [0:0]
-A POSTROUTING -s 192.168.0.0/16 -o eth0 -j MASQUERADE
COMMIT
```
3. Reload UFW
```bash
sudo ufw reload
```

## Examples
```bash
$ sudo sysctl net.ipv4.ip_forward
net.ipv4.ip_forward = 0

$ echo net.ipv4.ip_forward=1 | sudo tee -a /etc/sysctl.conf
$ sudo sysctl -p
$ sudo ufw reload
```
