---
title: "[Solution] systemd OnCalendar parse error"
description: "Fix systemd OnCalendar parse error. Resolve timer configuration failures with invalid calendar expressions."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd OnCalendar parse error

## Error Description

myapp.timer: Failed to parse OnCalendar= expression: 'daily 2:30': Invalid format

The OnCalendar= value has invalid syntax.

## Common Causes

Common Causes:
- Invalid calendar expression format
- Missing or incorrect time specification
- Unsupported calendar keywords
- Locale-related parsing issues

## How to Fix

How to Fix:
```bash
# Valid OnCalendar= formats:
# OnCalendar=daily
# OnCalendar=*-*-* 02:30:00
# OnCalendar=Mon *-*-* 09:00:00
# OnCalendar=monthly
# OnCalendar=weekly
# OnCalendar=yearly

# Test calendar expression
systemd-analyze calendar 'daily' --iterations=3

# Edit the timer
sudo systemctl edit myapp.timer
```

```ini
[Timer]
OnCalendar=*-*-* 02:30:00
Persistent=true
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