---
title: "Systemd-Resolved DNS Cache Corrupt"
description: "DNS resolution fails or returns stale data due to corrupted resolved cache"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Systemd-Resolved DNS Cache Corrupt

DNS resolution fails or returns stale data due to corrupted resolved cache

## Common Causes

- resolved cache file corrupted by unclean shutdown
- Cache contains incorrect DNS responses
- DNSSEC validation failure causing cache issues
- Disk write failure during cache update

## How to Fix

1. Flush cache: `resolvectl flush-caches`
2. Check cache stats: `resolvectl statistics`
3. Restart resolved: `sudo systemctl restart systemd-resolved`
4. Check cache file: `ls -la /var/cache/systemd/`

## Examples

```bash
# Flush DNS cache
sudo resolvectl flush-caches

# Check cache statistics
resolvectl statistics

# Restart resolved
sudo systemctl restart systemd-resolved
```
