---
title: "[Solution] Linux systemd 'Failed to start X.service' — Unit Failed Fix"
description: "Fix Linux systemd 'Failed to start X.service' errors. Diagnose unit failures, check logs, and resolve service startup issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Linux: Failed to start X.service (systemd)

The error `Failed to start X.service` means systemd was unable to start a service unit. This can happen for many reasons: the service binary is missing or broken, configuration files have errors, dependencies failed to start, or the service doesn't have proper permissions. The key to diagnosing this is checking the service status and logs.

## Common Causes

- Service configuration file has syntax errors
- Service binary or script is missing or not executable
- Required dependencies (other services, network, filesystems) not available
- Permission issues preventing the service from starting
- Port already in use by another process
- Insufficient resources (memory, disk space)

## How to Fix

### 1. Check Service Status

```bash
# Check detailed status
sudo systemctl status myservice.service

# This shows the last few log lines and whether the service is active/failed
```

Example output:

```
● myservice.service - My Application
     Loaded: loaded (/etc/systemd/system/myservice.service; enabled)
     Active: failed (Result: exit-code) since Thu 2025-06-15 10:00:00 UTC
    Process: 1234 ExecStart=/usr/bin/myapp (code=exited, status=1/FAILURE)

Jun 15 10:00:00 server systemd[1]: myservice.service: Main process exited, code=exited, status=1/FAILURE
Jun 15 10:00:00 server systemd[1]: myservice.service: Failed with result 'exit-code'.
```

### 2. Check Service Logs

```bash
# View all logs for the service
sudo journalctl -u myservice.service -f

# View logs since last boot
sudo journalctl -u myservice.service -b

# View logs for a specific time range
sudo journalctl -u myservice.service --since "2025-06-15 09:00" --until "2025-06-15 10:00"

# View logs with no pager (useful for piping)
sudo journalctl -u myservice.service --no-pager | tail -50
```

### 3. Check the Service File

```bash
# View the service unit file
sudo systemctl cat myservice.service

# Check for syntax errors (systemd-analyze will validate the file)
sudo systemd-analyze verify /etc/systemd/system/myservice.service
```

Common issues in service files:

```bash
# Check if the ExecStart path exists and is executable
ls -la /usr/bin/myapp

# Check if the service user exists
id myserviceuser

# Check if the config file exists
ls -la /etc/myapp/config.yml
```

### 4. Check Dependencies

```bash
# View the dependency tree
systemctl list-dependencies myservice.service

# Check if required services are running
sudo systemctl status network.target
sudo systemctl status postgresql.service
```

If dependencies are failing, fix them first before trying to start the main service.

### 5. Fix Common Issues

```bash
# Reload systemd after changing any unit file
sudo systemctl daemon-reload

# Check if the port is already in use
sudo ss -tlnp | grep :8080

# Kill the conflicting process
sudo kill $(lsof -t -i:8080)

# Verify file permissions
ls -la /usr/bin/myapp
sudo chmod +x /usr/bin/myapp

# Start the service
sudo systemctl start myservice.service
```

### 6. Enable the Service for Boot

```bash
# Enable to start on boot
sudo systemctl enable myservice.service

# Enable and start immediately
sudo systemctl enable --now myservice.service
```

### 7. Reset Failed State

If the service is stuck in a failed state:

```bash
# Reset the failed state
sudo systemctl reset-failed myservice.service

# Try starting again
sudo systemctl start myservice.service
```

## Examples

```bash
$ sudo systemctl status nginx
● nginx.service - A high performance web server
     Active: failed (Result: exit-code) since Thu 2025-06-15 10:00:00 UTC

$ sudo journalctl -u nginx -n 20
Jun 15 10:00:00 server nginx[1234]: nginx: [emerg] bind() to 0.0.0.0:80 failed (98: Address already in use)

$ sudo ss -tlnp | grep :80
LISTEN  0  128  0.0.0.0:80  0.0.0.0:*  users:(("apache2",pid=5678,fd=4))

$ sudo systemctl stop apache2
$ sudo systemctl start nginx
$ sudo systemctl status nginx
● nginx.service - A high performance web server
     Active: active (running) since Thu 2025-06-15 10:05:00 UTC
```

## Related Errors

- [Connection refused]({{< relref "/os/linux/connection-refused7" >}}) — Service not listening after failed start
- [Permission denied]({{< relref "/os/linux/permission-denied10" >}}) — Insufficient privileges
- [GRUB errors]({{< relref "/os/linux/grub-error" >}}) — Boot-level failures
