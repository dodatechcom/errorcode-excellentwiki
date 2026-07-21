---
title: "Logrotate Error Handling Failed"
description: "Logrotate reports errors during rotation or compression"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Logrotate Error Handling Failed

Logrotate reports errors during rotation or compression

## Common Causes

- Log file does not exist when rotation triggered
- Compression (gzip) failed
- Permission denied on log directory
- Logrotate configuration syntax error

## How to Fix

1. Check logrotate config syntax: `logrotate -d /etc/logrotate.d/<file>`
2. Verify log files exist before rotation
3. Check permissions on log directory
4. Check disk space for compressed logs

## Examples

```bash
# Check logrotate configuration
sudo logrotate -d /etc/logrotate.d/myapp

# Verify log files exist
ls -la /var/log/myapp/

# Check logrotate state
cat /var/lib/logrotate/status | grep myapp
```
