---
title: "[Solution] Linux: cron-environment-error -- cron environment error"
description: "Fix Linux cron environment variable errors. Cron job failing due to missing environment."
os: ["linux"]
error-types: ["cron-error"]
severities: ["error"]
---

# Linux: Cron Environment Error

Cron environment errors occur when jobs fail because cron lacks required variables.

## Common Causes

- Cron uses minimal PATH without /usr/local/bin
- HOME variable not set causing path failures
- LANG/LC_ALL not set causing locale errors
- Temporary environment variables not exported
- Shell differences between login and cron

## How to Fix

### 1. Check Cron Environment

```bash
crontab -l
echo $PATH
```

### 2. Set Environment in Crontab

```bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
HOME=/home/user
LANG=en_US.UTF-8
0 * * * * /path/to/script.sh
```

### 3. Use Full Paths

```bash
# Instead of: python script.py
# Use: /usr/bin/python3 /home/user/script.py
```

## Examples

```bash
$ crontab -l
PATH=/usr/local/bin:/usr/bin:/bin
0 * * * * python3 /home/user/script.py
# Works in terminal but fails in cron
```
