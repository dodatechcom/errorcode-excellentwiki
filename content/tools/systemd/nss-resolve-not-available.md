---
title: "[Solution] systemd nss-resolve not available"
description: "Fix systemd nss-resolve not available. Resolve name resolution failures when nss-resolve module is missing."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd nss-resolve not available

## Error Description

Name lookup using nss-resolve failed. Module not found.

The nss_resolve module is not available for name resolution.

## Common Causes

Common Causes:
- libnss_resolve is not installed
- /etc/nsswitch.conf does not include resolve
- systemd-resolved is not installed
- NSS configuration is incorrect

## How to Fix

How to Fix:
```bash
# Install systemd-resolved
sudo apt install systemd-resolved

# Check nsswitch.conf
grep hosts /etc/nsswitch.conf

# Ensure resolve is in the hosts line
# hosts: files resolve dns

# Restart resolved
sudo systemctl restart systemd-resolved
```

## Examples

```bash
# Check systemd version
systemctl --version

# Verify unit file syntax
sudo systemd-analyze verify /etc/systemd/system/myapp.service

# Analyze system boot
systemd-analyze blame

# List failed units
systemctl --failed

# View service logs
journalctl -u myapp -n 50 --no-pager
```