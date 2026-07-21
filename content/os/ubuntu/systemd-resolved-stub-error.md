---
title: "[Solution] Ubuntu Server: system-resolved-stub-error"
description: "Fix Ubuntu system-resolved-stub-error. systemd-resolved stub listener not working."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd Resolved Stub Error

systemd-resolved stub DNS listener on 127.0.0.53 fails.

## Common Causes
- resolv.conf not symlinked to stub
- Port 53 already in use by another process
- dnsmasq conflicting with resolved
- DNSMasq or bind9 occupying port 53

## How to Fix
1. Check what is on port 53
```bash
sudo ss -ulnp | grep :53
sudo lsof -i :53
```
2. Stop conflicting service
```bash
sudo systemctl stop dnsmasq
sudo systemctl disable dnsmasq
```
3. Link resolv.conf to stub
```bash
sudo ln -sf /run/systemd/resolve/stub-resolv.conf /etc/resolv.conf
sudo systemctl restart systemd-resolved
```

## Examples
```bash
$ sudo ss -ulnp | grep :53
UNCONN  0  0  127.0.0.53:53  *:*  users:(("dnsmasq",pid=1234))

$ sudo systemctl stop dnsmasq
$ sudo systemctl restart systemd-resolved
```
