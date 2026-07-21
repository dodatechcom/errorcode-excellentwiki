---
title: "UFW Logging Disabled or Not Working"
description: "UFW logging does not capture blocked or allowed packets"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# UFW Logging Disabled or Not Working

UFW logging does not capture blocked or allowed packets

## Common Causes

- UFW logging level set to off
- Log directory permissions prevent writing
- rsyslog not running or misconfigured
- Kernel log rate limiting dropping packets

## How to Fix

1. Check logging level: `sudo ufw status verbose`
2. Enable logging: `sudo ufw logging on` or `sudo ufw logging medium`
3. Check rsyslog: `systemctl status rsyslog`
4. Verify log directory: `ls -la /var/log/ufw.log`

## Examples

```bash
# Check current UFW status with logging
sudo ufw status verbose

# Enable logging
sudo ufw logging on

# Check UFW logs
sudo tail -f /var/log/ufw.log
```
