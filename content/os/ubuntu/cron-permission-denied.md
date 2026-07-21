---
title: "Cron Permission Denied Error"
description: "User crontab cannot be modified or cron cannot execute scripts"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Cron Permission Denied Error

User crontab cannot be modified or cron cannot execute scripts

## Common Causes

- User not in /etc/cron.allow
- User listed in /etc/cron.deny
- Script being executed by cron is not executable
- Crontab file permissions incorrect

## How to Fix

1. Check cron.allow: `cat /etc/cron.allow`
2. Check cron.deny: `cat /etc/cron.deny`
3. Add user to cron.allow: `echo username | sudo tee -a /etc/cron.allow`
4. Make script executable: `chmod +x /path/to/script.sh`

## Examples

```bash
# Check cron access files
cat /etc/cron.allow
cat /etc/cron.deny

# Add user to cron.allow
echo admin | sudo tee -a /etc/cron.allow
```
