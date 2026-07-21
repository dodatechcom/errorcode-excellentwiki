---
title: "[Solution] Ubuntu Server: system-resolved-error"
description: "Fix Ubuntu system-resolved-error. systemd-resolved DNS resolution fails."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd Resolved Error

systemd-resolved fails to resolve DNS queries.

## Common Causes
- upstream DNS server unreachable
- DNSSEC validation failure
- /etc/resolv.conf not linked to stub
- Cache corruption in resolved

## How to Fix
1. Check resolved status
```bash
resolvectl status
resolvectl query google.com
```
2. Reset cache
```bash
sudo resolvectl flush-caches
```
3. Set DNS servers
```bash
sudo resolvectl dns eth0 8.8.8.8
```
4. Check resolv.conf link
```bash
ls -la /etc/resolv.conf
```

## Examples
```bash
$ resolvectl query google.com
google.com: resolve call failed: DNSSEC validation failed

$ sudo resolvectl flush-caches
$ resolvectl query google.com
google.com: 142.250.80.46
```
