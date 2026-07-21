---
title: "[Solution] Ubuntu Server: system-logind-error"
description: "Fix Ubuntu system-logind-error. systemd-logind session management fails."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# Systemd Logind Error

systemd-logind encounters errors managing user sessions.

## Common Causes
- /run/user directory full
- Maximum number of sessions exceeded
- polkit configuration issue
- Seat configuration missing

## How to Fix
1. Check logind status
```bash
sudo systemctl status systemd-logind
loginctl list-sessions
```
2. Check configuration
```bash
sudo nano /etc/systemd/logind.conf
# MaxSessions=256
# StopIdleSessionSec=600
```
3. Restart logind
```bash
sudo systemctl restart systemd-logind
```

## Examples
```bash
$ loginctl list-sessions
SESSION  UID USER  SEAT  TTY
      1 1000 admin seat0

$ journalctl -u systemd-logind
logind[1000]: Failed to acquire session seat: Not enough resources
```
