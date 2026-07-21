---
title: "[Solution] Linux: systemd-service-restart-loop -- service stuck in restart loop"
description: "Fix Linux systemd service restart loop errors. Service constantly crashing and restarting."
os: ["linux"]
error-types: ["systemd-error"]
severities: ["error"]
---

# Linux: Systemd Service Restart Loop

A systemd service stuck in a restart loop repeatedly crashes and restarts, exhausting resources.

## Common Causes

- Service binary crashing immediately after start
- Missing or incorrect ExecStart path
- Dependencies not available when service starts
- Incorrect environment variables or configuration
- Rate limiting exhausted due to rapid restarts

## How to Fix

### 1. Check Service Status

```bash
systemctl status <service_name> -l
journalctl -u <service_name> -n 50
```

### 2. Review Restart Configuration

```bash
systemctl cat <service_name>
# Check Restart=, RestartSec=, StartLimitBurst=
```

### 3. Fix and Reset

```bash
sudo systemctl stop <service_name>
# Fix configuration
sudo systemctl daemon-reload
sudo systemctl reset-failed <service_name>
sudo systemctl start <service_name>
```

## Examples

```bash
$ systemctl status myapp
myapp.service: Start request repeated too quickly.
myapp.service: Failed with result 'exit-code'.
$ journalctl -u myapp -n 10
Jul 20 14:00:01 server myapp[1234]: Error: config not found
Jul 20 14:00:02 server systemd[1]: myapp.service: Main process exited, code=exited
```
