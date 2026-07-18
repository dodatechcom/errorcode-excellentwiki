---
title: "[Solution] Systemd Timer Unit Misconfiguration Error — How to Fix"
description: "Fix systemd timer unit misconfigurations by verifying unit file syntax, fixing OnCalendar expressions, debugging timer activation, and checking calendar syntax"
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

# Systemd Timer Unit Misconfiguration Error

This error means a systemd timer unit is misconfigured and cannot activate its associated service unit. Timers require both a `.timer` file and a matching `.service` file with the same base name.

## Why It Happens

- The `.timer` file references a `.service` file that does not exist
- `OnCalendar=` has an invalid calendar expression
- `OnBootSec=` or `OnUnitActiveSec=` is missing or zero
- The timer and service file names do not match
- `Unit=` directive in the timer points to a nonexistent service
- `Persistent=true` is used but the service does not support it
- The timer is disabled or masked
- Timer stamp files are corrupt or missing

## Common Error Messages

```
mybackup.timer: Failed to load unit "mybackup.service", skipping.
```

```
mybackup.timer: Not a valid calendar expression: ...
```

```
mybackup.service: Failed to start timer-triggered unit: no such service
```

```
systemd[1]: mybackup.timer: Timer failed with result 'failure'.
```

## How to Fix It

### 1. Verify Timer and Service Files Exist

```bash
# Check both files are present
ls -la /etc/systemd/system/mybackup.*

# Expected files:
# mybackup.timer
# mybackup.service

# Reload after any changes
sudo systemctl daemon-reload
```

### 2. Validate the Calendar Expression

```bash
# Test the OnCalendar expression
systemd-analyze calendar 'Mon *-*-* 02:00:00'

# Test common patterns
systemd-analyze calendar 'daily'
systemd-analyze calendar 'hourly'
systemd-analyze calendar '*-*-01 00:00:00'  # First of every month
systemd-analyze calendar 'Mon..Fri *-*-* 09:00:00'  # Weekdays at 9am
systemd-analyze calendar 'Mon *-*-* 02:00:00'  # Every Monday at 2am
```

### 3. Fix Timer Unit File

```ini
# /etc/systemd/system/mybackup.timer
[Unit]
Description=Daily Backup Timer

[Timer]
OnCalendar=*-*-* 02:00:00
Persistent=true
RandomizedDelaySec=600

[Install]
WantedBy=timers.target
```

```ini
# /etc/systemd/system/mybackup.service
[Unit]
Description=Daily Backup

[Service]
Type=oneshot
ExecStart=/usr/local/bin/backup.sh
User=root
```

### 4. Enable and Test the Timer

```bash
# Enable the timer
sudo systemctl enable mybackup.timer
sudo systemctl start mybackup.timer

# Check timer status
systemctl status mybackup.timer

# List all active timers
systemctl list-timers --all

# Manually trigger the service once for testing
sudo systemctl start mybackup.service
journalctl -u mybackup.service -n 20
```

### 5. Fix OnCalendar Syntax Issues

```ini
# Wrong: missing space or invalid format
OnCalendar=Mon *-*-*02:00:00
OnCalendar=*-*-* 2:00

# Right: proper format with space and seconds
OnCalendar=*-*-* 02:00:00
OnCalendar=Mon *-*-* 02:00:00

# Use aliases for common patterns
OnCalendar=daily
OnCalendar=weekly
OnCalendar=monthly
OnCalendar=hourly
```

### 6. Debug Timer Activation

```bash
# Check timer last and next trigger times
systemctl show mybackup.timer -p LastTriggerUSec,NextTriggerUSec

# Check if the timer is active
systemctl is-active mybackup.timer

# View timer-related logs
journalctl -u mybackup.timer -n 30
journalctl -u mybackup.service -n 30

# Check for stale stamp files
ls -la /var/lib/systemd/timers/
```

## Common Scenarios

- **Service file missing**: The timer works but the service file was accidentally deleted. Recreate the matching `.service` file.
- **Wrong calendar expression**: Using `02:00` instead of `02:00:00`. Always include seconds for precision.
- **Timer not firing**: The timer is enabled but the system was off at the scheduled time. Add `Persistent=true` to run missed executions on boot.

## Prevent It

- Always validate calendar expressions with `systemd-analyze calendar` before deploying
- Use `systemctl list-timers --all` to verify timers are active and their next trigger times
- Test new timers by running the service manually first with `systemctl start <service>`

## Related Pages

- [Systemd Unit Failed](/tools/systemd/systemd-unit-failed)
- [Systemd Timeout Error](/tools/systemd/systemd-timeout-error)
- [Systemd Log Error](/tools/systemd/systemd-log-error)
