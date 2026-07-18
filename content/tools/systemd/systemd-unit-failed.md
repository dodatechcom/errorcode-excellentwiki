---
title: "[Solution] Systemd Unit Failed to Start Error — How to Fix"
description: "Fix systemd unit failed to start errors by checking logs, verifying dependencies, correcting unit file syntax, and resolving permission issues"
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

# Systemd Unit Failed to Start Error

This error means a systemd service unit failed to start or was stopped unexpectedly. Systemd provides detailed status information to help diagnose the root cause, including exit codes and recent log entries.

## Why It Happens

- The service binary or script does not exist at the configured path
- The working directory (`WorkingDirectory`) does not exist or is inaccessible
- The user specified in `User=` does not exist on the system
- Port conflicts prevent the service from binding to its listen address
- Required environment variables are missing or misconfigured
- A dependency service has not started yet
- The unit file has syntax errors
- The service crashes immediately on startup (segfault, unhandled exception)

## Common Error Messages

```
● myapp.service - My Application
   Loaded: loaded (/etc/systemd/system/myapp.service; enabled)
   Active: failed (Result: exit-code) since ...
   Main PID: 12345 (code=exited, status=1/FAILURE)
```

```
Job for myapp.service failed because the control process exited with error code.
```

```
systemd[1]: myapp.service: Failed with result 'exit-code'.
```

## How to Fix It

### 1. Check Service Status and Logs

```bash
# Get detailed status
systemctl status myapp.service

# View recent logs for the service
journalctl -u myapp.service -n 50 --no-pager

# Follow logs in real time during startup
journalctl -u myapp.service -f
```

### 2. Check the Exit Code

```bash
# Find the exact exit code
systemctl show myapp.service -p ExecMainStatus,ExecMainCode

# Common exit codes:
# 0   = success
# 1   = general error
# 2   = misuse of shell command
# 126 = permission denied
# 127 = command not found
# 137 = killed by SIGKILL (OOM)
# 143 = killed by SIGTERM
```

### 3. Test the ExecStart Command Manually

```bash
# Run the command as the service user
sudo -u myappuser /usr/bin/myapp --config /etc/myapp/config.yaml

# Check if the binary exists
which myapp
ls -la /usr/bin/myapp
```

### 4. Verify Unit File Syntax

```bash
# Analyze the unit file for errors
systemd-analyze verify myapp.service

# Check dependency tree
systemd-analyze dot myapp.service | dot -Tsvg > deps.svg
```

### 5. Fix Permissions

```bash
# Check file ownership and permissions
ls -la /usr/bin/myapp
ls -la /etc/myapp/

# Fix ownership
sudo chown myappuser:myappuser /etc/myapp/config.yaml
sudo chmod 640 /etc/myapp/config.yaml

# Check systemd can access the working directory
sudo -u myappuser ls /var/lib/myapp/
```

### 6. Add Restart Policy and Debug

```ini
# In /etc/systemd/system/myapp.service
[Unit]
Description=My Application
After=network.target

[Service]
Type=simple
User=myappuser
Group=myappuser
ExecStart=/usr/bin/myapp --config /etc/myapp/config.yaml
Restart=on-failure
RestartSec=5s
StandardOutput=journal
StandardError=journal
Environment=MYAPP_ENV=production

# Increase timeout for slow starts
TimeoutStartSec=60

[Install]
WantedBy=multi-user.target
```

```bash
# Reload and restart
sudo systemctl daemon-reload
sudo systemctl restart myapp.service
```

## Common Scenarios

- **Service starts but immediately fails**: The binary panics on startup. Run the ExecStart command manually to see the error output.
- **Permission denied on config file**: The service runs as `myappuser` but the config file is owned by `root:root` with `600` permissions. Change ownership or group permissions.
- **Missing shared library**: The service requires a library that is not installed. Run `ldd /usr/bin/myapp` to check for missing dependencies.

## Prevent It

- Always run `systemd-analyze verify` after editing a unit file
- Use `journalctl -u <service> -f` to monitor startup in real time
- Add `Restart=on-failure` with a reasonable `RestartSec` to handle transient errors

## Related Pages

- [Systemd Timeout Error](/tools/systemd/systemd-timeout-error)
- [Systemd Dependency Cycle](/tools/systemd/systemd-dependency-cycle)
- [Systemd Masked Unit](/tools/systemd/systemd-masked-unit)
