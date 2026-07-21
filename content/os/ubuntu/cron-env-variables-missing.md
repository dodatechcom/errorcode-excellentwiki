---
title: "Cron Missing Environment Variables"
description: "Cron job runs but environment variables are not set"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Cron Missing Environment Variables

Cron job runs but environment variables are not set

## Common Causes

- Cron uses minimal environment, not user's shell profile
- No .profile or .bashrc sourced by cron
- PATH is minimal in cron environment
- LANG and LC_* variables not exported

## How to Fix

1. Source profile in script: `. ~/.bashrc` at script start
2. Set variables explicitly in crontab
3. Use full paths in cron commands
4. Export variables in /etc/environment

## Examples

```bash
# Example crontab with environment
SHELL=/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin
MAILTO=user@example.com
0 * * * * . ~/.bashrc && /path/to/script.sh
```
