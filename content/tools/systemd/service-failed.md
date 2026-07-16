---
title: "[Solution] Systemd Failed to Start — Failed to start X.service (code=exited)"
description: "Fix systemd 'Failed to start' service errors. Diagnose why a service fails to start with code=exited."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
tags: ["service-failed", "systemd", "failed", "code-exited"]
weight: 5
---

# Systemd Failed to Start — Failed to start X.service (code=exited)

This error means a systemd service failed during startup. The `code=exited` status indicates the process exited before becoming active, usually due to a configuration error, missing dependency, or permission issue.

## Common Causes

- Configuration file has syntax errors
- Required files or directories are missing
- Service is running as wrong user without needed permissions
- ExecStart binary is not found or not executable

## How to Fix

### Check Service Status and Logs

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
postgres -C config_file
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

## Examples

```bash
# Example 1: Nginx config syntax error
sudo systemctl status nginx
# nginx.service: Failed with result 'exit-code'
sudo nginx -t
# nginx: [emerg] unknown directive "listen" in /etc/nginx/conf.d/default.conf:3
# Fix: correct the typo in the config file

# Example 2: Missing executable
sudo systemctl start my-app
# my-app.service: Failed to execute, No such file or directory
# Fix: ensure the binary path in the unit file is correct
```

## Related Errors

- [Dependency Failed]({{< relref "/tools/systemd/dependency-failed" >}}) — service failed because a dependency failed
- [Upstream Error]({{< relref "/tools/nginx/upstream-error" >}}) — Nginx 502 when backend is down
