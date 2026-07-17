---
title: "systemd Unit Start Failed"
description: "systemd service unit fails to start with error code."
tools: ["systemd"]
error-types: ["runtime-error"]
severities: ["error"]
tags: ["systemd", "unit", "start", "failed", "service"]
weight: 5
---

# systemd Unit Start Failed

A systemd unit start failure occurs when a service unit fails during startup. The error typically shows the exit code and the result status.

## Common Causes

- ExecStart binary is not found or not executable
- Configuration file has syntax errors
- Required files or directories are missing
- Service is running as wrong user without permissions

## How to Fix

### Check Service Status

```bash
systemctl status <service-name>
journalctl -u <service-name> -n 50
```

### Verify Service Configuration

```bash
systemctl cat <service-name>
```

### Check for Configuration Errors

```bash
nginx -t
apachectl configtest
```

### Fix File Permissions

```bash
sudo chmod +x /path/to/executable
sudo chown service-user:service-user /path/to/file
```

### Reload systemd After Changes

```bash
sudo systemctl daemon-reload
sudo systemctl restart <service-name>
```

### Check User and Group

```ini
# /etc/systemd/system/myapp.service
[Service]
User=myapp
Group=myapp
ExecStart=/usr/bin/myapp
```

## Examples

```bash
# Example 1: Missing executable
sudo systemctl start my-app
# my-app.service: Failed to execute, No such file or directory
# Fix: ensure the binary path is correct

# Example 2: Permission denied
sudo systemctl start nginx
# nginx.service: Failed to start with result 'exit-code'
# Fix: check file permissions and user/group
```

## Related Errors

- [Service Not Found]({{< relref "/tools/systemd/service-failed" >}}) — service does not exist
- [Dependency Failed]({{< relref "/tools/systemd/dependency-failed" >}}) — dependency issue
