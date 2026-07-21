---
title: "MAAS DHCP Service Error"
description: "MAAS DHCP service fails to serve IP addresses to nodes"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# MAAS DHCP Service Error

MAAS DHCP service fails to serve IP addresses to nodes

## Common Causes

- MAAS DHCP configuration invalid
- DHCP range exhausted or misconfigured
- Network interface not available for DHCP
- MAAS region controller not running

## How to Fix

1. Check MAAS status: `maas status`
2. Verify DHCP config: `maas <profile> ipranges read`
3. Check network: `maas <profile> networks read`
4. Restart MAAS: `sudo systemctl restart maas-regiond`

## Examples

```bash
# Check MAAS status
maas admin status

# List DHCP ranges
maas admin ipranges read

# Check MAAS services
maas admin services read
```
