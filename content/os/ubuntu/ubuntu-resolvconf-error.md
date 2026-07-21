---
title: "Ubuntu Resolvconf Configuration Error"
description: "DNS resolution fails due to /etc/resolv.conf misconfiguration"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Ubuntu Resolvconf Configuration Error

DNS resolution fails due to /etc/resolv.conf misconfiguration

## Common Causes

- /etc/resolv.conf is a symlink to non-existent target
- resolvconf package not installed but expected
- Nameserver entries point to wrong IPs
- search domain list causes resolution failures

## How to Fix

1. Check resolv.conf: `ls -la /etc/resolv.conf`
2. Verify nameservers: `cat /etc/resolv.conf`
3. Test: `nslookup google.com 8.8.8.8`
4. Reinstall resolvconf: `sudo apt-get install resolvconf`

## Examples

```bash
# Check resolv.conf status
ls -la /etc/resolv.conf

# Check nameservers
cat /etc/resolv.conf

# Test DNS resolution
nslookup google.com 8.8.8.8
```
