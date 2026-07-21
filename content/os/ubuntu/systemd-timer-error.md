---
title: "[Solution] Ubuntu Server: system-timer-error"
description: "Fix Ubuntu system-timer-error. systemd timer fails to trigger or run its associated service."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd Timer Error

systemd timer fails to trigger or run the associated service.

## Common Causes
- Timer unit missing or misconfigured
- OnCalendar syntax incorrect
- Service unit does not exist
- Timer not enabled

## How to Fix
1. Check timer status
```bash
systemctl list-timers --all
sudo systemctl status <timer>.timer
```
2. Check timer unit file
```bash
sudo systemctl cat <timer>.timer
```
3. Verify OnCalendar syntax
```bash
systemd-analyze calendar "Mon *-*-* 09:00:00"
```

## Examples
```bash
$ systemctl list-timers
NEXT                        LEFT        LAST                        PASSED   UNIT
Mon 2023-03-20 09:00:00 UTC 5h left     n/a                         n/a      mytimer.timer

$ systemd-analyze calendar "Mon *-*-* 09:00:00"
Normalized form: Mon *-*-* 09:00:00 UTC
```
