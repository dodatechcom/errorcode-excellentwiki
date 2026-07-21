---
title: "Cron Job Not Executing"
description: "Scheduled cron job does not run at expected time"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Cron Job Not Executing

Scheduled cron job does not run at expected time

## Common Causes

- Cron service not running: `systemctl status cron`
- Crontab syntax error preventing job from being scheduled
- User crontab not saved or wrong user
- Cron daemon using wrong timezone

## How to Fix

1. Check cron status: `systemctl status cron`
2. Verify crontab: `crontab -l`
3. Check cron logs: `grep CRON /var/log/syslog`
4. Ensure proper PATH in crontab

## Examples

```bash
# Check cron service
systemctl status cron

# List current user's crontab
crontab -l

# Check cron execution logs
grep CRON /var/log/syslog | tail -20
```
