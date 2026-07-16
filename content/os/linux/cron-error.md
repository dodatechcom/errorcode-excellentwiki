---
title: "[Solution] Linux CRON Error — CMD failed / Execution Error Fix"
description: "Fix Linux CRON 'CMD failed' and execution errors. Debug cron jobs, fix permissions, and resolve scheduled task failures."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["cron", "crontab", "cmd-failed", "scheduled-task", "anacron"]
weight: 5
---

# Linux: CRON - (root) CMD failed / error

The `CRON: (root) CMD failed` error means a scheduled cron job failed to execute. Cron silently runs jobs and emails output (if configured), but when the command itself fails or the environment isn't set up correctly, errors appear in system logs. Cron errors are notoriously difficult to debug because the execution environment differs from an interactive shell.

## Common Causes

- Command or script path is incorrect or missing
- Script lacks execute permissions
- Cron environment lacks PATH and other variables
- Output redirection errors
- Script depends on services or resources not available at cron time
- Crontab syntax errors (wrong field format)

## How to Fix

### 1. Check Cron Logs

```bash
# Check cron logs (Debian/Ubuntu)
grep CRON /var/log/syslog

# Check cron logs (RHEL/CentOS/Fedora)
journalctl -u crond
cat /var/log/cron

# Check for errors in the last hour
grep -i "error\|failed\|CMD" /var/log/syslog | grep CRON | tail -20
```

### 2. Fix Crontab Syntax

```bash
# Edit the crontab
crontab -e

# View the current crontab
crontab -l

# Verify crontab syntax (install cron-check if available)
# Or use crontab.guru for validation: https://crontab.guru
```

Correct cron format:

```
# ┌───── minute (0-59)
# │ ┌───── hour (0-23)
# │ │ ┌───── day of month (1-31)
# │ │ │ ┌───── month (1-12)
# │ │ │ │ ┌───── day of week (0-7, 0 and 7 = Sunday)
# │ │ │ │ │
  * * * * *  command_to_execute
```

### 3. Use Full Paths

Cron runs with a minimal environment. Always use absolute paths:

```bash
# WRONG — cron doesn't have the same PATH
* * * * * myscript.sh

# CORRECT — use full paths
* * * * * /usr/bin/python3 /home/user/scripts/myscript.sh

# Or set PATH at the top of the crontab
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
```

### 4. Set Environment Variables

Add environment variables at the top of the crontab:

```bash
crontab -e
```

```
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOME=/home/user
MAILTO=user@example.com
```

### 5. Fix Script Permissions

```bash
# Check permissions
ls -la /path/to/script.sh

# Make executable
chmod +x /path/to/script.sh

# Ensure the script owner can read and execute it
chmod 755 /path/to/script.sh
```

### 6. Redirect Output for Debugging

Add output redirection to capture errors:

```bash
# Log both stdout and stderr
* * * * * /path/to/script.sh >> /var/log/myscript.log 2>&1

# Or mail output (if mail is configured)
* * * * * /path/to/script.sh 2>&1 | mail -s "Cron Output" user@example.com

# Discard output (if you don't want emails)
* * * * * /path/to/script.sh >/dev/null 2>&1
```

### 7. Test the Command Manually

Before adding to crontab, run the exact command as the cron user:

```bash
# Run as the user who owns the crontab
sudo -u user /path/to/script.sh

# Test with minimal environment (similar to cron)
env -i HOME=/home/user PATH=/usr/bin:/bin /path/to/script.sh
```

### 8. Check for Anacron

On desktop systems, cron may not run continuously:

```bash
# Check if anacron is managing jobs
ls /etc/cron.d/

# Check anacrontab
cat /etc/anacrontab

# Ensure cron service is running
sudo systemctl status cron      # Debian/Ubuntu
sudo systemctl status crond     # RHEL/CentOS
```

### 9. Common Crontab Entries

```bash
# Run every 5 minutes
*/5 * * * * /path/to/script.sh

# Run daily at 2:30 AM
30 2 * * * /path/to/backup.sh

# Run weekly on Sunday at 3:00 AM
0 3 * * 0 /path/to/weekly-cleanup.sh

# Run monthly on the 1st at 4:00 AM
0 4 1 * * /path/to/monthly-report.sh

# Run at reboot
@reboot /path/to/startup-script.sh
```

## Examples

```bash
$ grep CRON /var/log/syslog | tail -5
Jun 15 10:00:01 server CRON[1234]: (root) CMD (/usr/local/bin/backup.sh)
Jun 15 10:00:01 server CRON[1234]: (root) CMD (ERROR: /usr/local/bin/backup.sh: No such file or directory)

$ ls -la /usr/local/bin/backup.sh
ls: cannot access '/usr/local/bin/backup.sh': No such file or directory

# Fix the path in crontab
$ crontab -e
# Change: /usr/local/bin/backup.sh → /home/admin/scripts/backup.sh
```

## Related Errors

- [Permission denied]({{< relref "/os/linux/permission-denied10" >}}) — Script lacks execute permission
- [No space left on device]({{< relref "/os/linux/no-space-left" >}}) — Disk full preventing job output
- [Failed to start X.service]({{< relref "/os/linux/systemd-failed" >}}) — systemd timer alternative
