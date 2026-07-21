---
title: "Samba Browser Master Election Error"
description: "Samba cannot become or find local master browser for network browsing"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Samba Browser Master Election Error

Samba cannot become or find local master browser for network browsing

## Common Causes

- Workgroup master browser already exists on another machine
- Samba not configured as domain master browser
- NetBIOS over TCP/IP disabled or blocked by firewall
- OS level setting too low to win election

## How to Fix

1. Check master browser: `nmblookup -S <workgroup>`
2. Set OS level higher: `os level = 65` in smb.conf
3. Enable local master: `local master = yes`
4. Check firewall: ports 137, 138, 139 UDP must be open

## Examples

```bash
# Find master browser
nmblookup -S WORKGROUP

# Test name resolution
nmblookup -M WORKGROUP
```
