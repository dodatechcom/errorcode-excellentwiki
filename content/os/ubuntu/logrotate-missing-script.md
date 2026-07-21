---
title: "Logrotate Missing Postrotate Script"
description: "Log rotation happens but service does not receive reload signal"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Logrotate Missing Postrotate Script

Log rotation happens but service does not receive reload signal

## Common Causes

- Missing postrotate script to signal service
- Wrong service name in postrotate
- Service name changed after update
- Kill signal sent to wrong PID file

## How to Fix

1. Check logrotate config: `cat /etc/logrotate.d/<service>`
2. Add postrotate: `postrotate /usr/bin/systemctl reload <service> > /dev/null 2>&1 || true`
3. Test rotation: `sudo logrotate -d /etc/logrotate.d/<service>`
4. Verify service name matches systemctl

## Examples

```bash
# Test logrotate configuration
sudo logrotate -d /etc/logrotate.d/nginx

# Force rotation
sudo logrotate -f /etc/logrotate.d/nginx
```
