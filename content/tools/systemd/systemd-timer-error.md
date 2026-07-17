---
title: "systemd Timer Error"
description: "systemd timer unit fails to trigger or execute the associated service."
tools: ["systemd"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# systemd Timer Error

A systemd timer error occurs when a timer unit fails to trigger its associated service on schedule. Timers are systemd's replacement for cron jobs.

## Common Causes

- Timer unit file syntax errors
- Service unit referenced by timer does not exist
- Timer calendar expression is invalid
- System time or timezone issues

## How to Fix

### Check Timer Status

```bash
systemctl status mytimer.timer
systemctl list-timers --all
```

### Verify Timer Configuration

```ini
# /etc/systemd/system/mytimer.timer
[Unit]
Description=My Timer

[Timer]
OnCalendar=daily
Persistent=true

[Install]
WantedBy=timers.target
```

### Check Service Unit Exists

```bash
systemctl cat mytimer.service
# Ensure the service unit exists
```

### Validate Calendar Expression

```bash
systemd-analyze calendar "daily"
systemd-analyze calendar "Mon *-*-* 09:00:00"
systemd-analyze calendar --iterations=5 "hourly"
```

### Enable and Start Timer

```bash
sudo systemctl enable mytimer.timer
sudo systemctl start mytimer.timer
```

### Check Timer Logs

```bash
journalctl -u mytimer.service -n 20
```

## Examples

```bash
systemctl status backup.timer
backup.timer: Failed to start.

# Fix: check timer configuration
systemd-analyze verify backup.timer
```

## Related Errors

- [Unit Start Failed]({{< relref "/tools/systemd/systemd-unit-error" >}}) — service start failure
- [Service Not Found]({{< relref "/tools/systemd/service-failed" >}}) — service does not exist
