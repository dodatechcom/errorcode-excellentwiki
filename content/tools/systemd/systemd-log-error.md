---
title: "[Solution] Systemd Journal Corruption or Rotation Error — How to Fix"
description: "Fix systemd journal corruption and rotation errors by verifying journal files, configuring storage limits, recovering corrupted journals, and setting retention policies"
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

# Systemd Journal Corruption or Rotation Error

This error means the systemd journal is corrupted, full, or cannot rotate log files properly. The journal daemon stores logs in binary format and corruption can occur from unclean shutdowns, disk failures, or misconfigured storage.

## Why It Happens

- The journal file was corrupted during a system crash or power loss
- Disk space for `/var/log/journal` is full
- `SystemMaxUse` is not configured and journal grows unbounded
- The journal was stored on tmpfs and lost on reboot
- `Storage=persistent` is configured but `/var/log/journal` does not exist
- Filesystem corruption affects the journal directory
- Multiple journal files have sequence gaps or overlapping timestamps

## Common Error Messages

```
Journal file /var/log/journal/.../system.journal is truncated, ignoring file.
```

```
Failed to open journal file: No such file or directory
```

```
Journal file /var/log/journal/.../system.journal: data object truncated
```

```
No journal files found to show.
```

## How to Fix It

### 1. Check Journal Status and Disk Usage

```bash
# Check journal disk usage
journalctl --disk-usage

# Check journal files
ls -lah /var/log/journal/

# Verify journal health
journalctl --verify

# Check journal configuration
cat /etc/systemd/journald.conf
```

### 2. Recover Corrupted Journal Files

```bash
# Stop the journal daemon
sudo systemctl stop systemd-journald

# Back up existing journal files
sudo cp -r /var/log/journal /var/log/journal.bak

# Remove corrupted journal files
sudo rm -f /var/log/journal/*/system.journal
sudo rm -f /var/log/journal/*/system@*.journal

# Create journal directory if missing
sudo mkdir -p /var/log/journal

# Restart the journal daemon to create fresh journals
sudo systemctl start systemd-journald

# Verify
journalctl --verify
```

### 3. Configure Journal Size Limits

```ini
# /etc/systemd/journald.conf
[Journal]
Storage=persistent
SystemMaxUse=2G
SystemMaxFileSize=128M
SystemMaxFiles=10
MaxRetentionSec=30day
MaxFileSec=1day
```

```bash
# Restart journald to apply changes
sudo systemctl restart systemd-journald
```

### 4. Manually Vacuum Old Journal Entries

```bash
# Keep only the last 500MB
sudo journalctl --vacuum-size=500M

# Keep only the last 7 days
sudo journalctl --vacuum-time=7d

# Keep only the last 10 files
sudo journalctl --vacuum-files=10
```

### 5. Fix Missing Journal Directory

```bash
# Create the persistent journal directory
sudo mkdir -p /var/log/journal
sudo systemd-tmpfiles --create --prefix /var/log/journal

# Or switch to volatile storage if persistent is not needed
# In /etc/systemd/journald.conf:
# Storage=volatile
# RuntimeMaxUse=100M
```

### 6. Use Remote Syslog as Fallback

```bash
# Forward logs to a remote syslog server
# In /etc/systemd/journald.conf:
[Journal]
ForwardToSyslog=yes

# Or use a remote journal
# In /etc/systemd/journald.conf:
[Journal]
Remote=yes
RemoteHost=syslog.example.com
RemotePort=514
```

## Common Scenarios

- **Server crashed mid-write**: The journal file was being written when the server lost power. Remove the corrupted file and let journald recreate it.
- **Disk full from journal growth**: A verbose service generates GB of logs per hour. Set `SystemMaxUse=1G` and `MaxRetentionSec=7day` to cap the size.
- **Docker container with tmpfs**: The container uses `Storage=volatile` and logs are lost on restart. Mount a volume at `/var/log/journal` or configure remote logging.

## Prevent It

- Always configure `SystemMaxUse` and `MaxRetentionSec` in `journald.conf`
- Monitor journal disk usage with `journalctl --disk-usage` and alert at 80% capacity
- Forward critical logs to a remote syslog server for permanent retention

## Related Pages

- [Systemd Log Error](/tools/systemd/systemd-log-error)
- [Systemd Mount Error](/tools/systemd/systemd-mount-error)
- [Systemd Timer Error](/tools/systemd/systemd-timer-error)
