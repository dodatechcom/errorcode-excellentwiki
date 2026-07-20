---
title: "[Solution] systemd calendar timer error"
description: "Fix systemd calendar timer error. Resolve OnCalendar expression parsing and scheduling issues."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd calendar timer error

## Error Description

myapp.timer: OnCalendar= expression 'every day at 2:30' could not be parsed.

The calendar expression is not in a recognized format.

## Common Causes

Common Causes:
- Human-readable expressions are not supported
- Time format must follow systemd calendar syntax
- Missing year or date component

## How to Fix

How to Fix:
```bash
# Use systemd calendar format
systemd-analyze calendar 'Mon *-*-* 09:00:00' --iterations=3

# Common formats:
# daily          → *-*-* 00:00:00
# hourly         → *-*-* *:00:00
# Mon 09:00      → Mon *-*-* 09:00:00
# 1st of month   → *-*-01 00:00:00

sudo systemctl edit myapp.timer
```

```ini
[Timer]
OnCalendar=*-*-* 02:30:00
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