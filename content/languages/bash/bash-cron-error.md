---
title: "[Solution] Bash Cron Error -- Script Execution in Cron Jobs"
description: "Fix bash cron errors when scripts run differently under cron than in terminal."
languages: ["bash"]
error-types: ["runtime-error"]
severities: ["error"]
---

# Bash Cron Error

This error occurs when scripts behave differently when executed by cron compared to manual execution.

## Common Causes

- Cron does not load user profile, so PATH is minimal
- Environment variables not set in cron context
- Relative paths failing because working directory is different
- Output redirection failing due to missing directories

## How to Fix

### Use absolute paths in cron

```bash
# WRONG: relative path
/path/to/script.sh  # works in terminal

# CORRECT: absolute path in crontab
0 * * * * /usr/bin/bash /home/user/scripts/myscript.sh
```

### Set environment in script

```bash
#!/bin/bash
export PATH="/usr/local/bin:/usr/bin:/bin"
export HOME="/home/user"

# Script logic here
```

## Examples

```bash
# In crontab
SHELL=/bin/bash
PATH=/usr/local/bin:/usr/bin:/bin
0 * * * * /home/user/scripts/backup.sh >> /var/log/backup.log 2>&1
```
