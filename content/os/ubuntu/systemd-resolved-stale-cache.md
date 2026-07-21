---
title: "[Solution] Ubuntu Server: system-resolved-stale-cache"
description: "Fix Ubuntu system-resolved-stale-cache. systemd-resolved serves stale DNS cache."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd Resolved Stale Cache

systemd-resolved serves outdated DNS records.

## Common Causes
- Cache not refreshed after DNS changes
- DNSSEC validation failing
- Cache too large

## How to Fix
1. Flush DNS cache
```bash
sudo resolvectl flush-caches
```
2. Check cache statistics
```bash
resolvectl statistics
```
3. Restart resolved
```bash
sudo systemctl restart systemd-resolved
```

## Examples
```bash
$ sudo resolvectl flush-caches
$ resolvectl statistics
Current Cache Size: 0
```