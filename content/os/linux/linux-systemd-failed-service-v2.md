---
title: "[Solution] Linux systemd Failed to Start — Unit Entered Failed State"
description: "Fix Linux systemd 'Failed to start' errors. Resolve service failures, check unit states, and restore systemd services."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
tags: ["systemd", "failed", "service", "unit", "boot"]
weight: 5
---

# Linux: systemd — Failed to start — unit entered failed state

The `Failed to start <service>.service` or `Unit <service>.service entered failed state` error means a systemd-managed service crashed, exited with a non-zero code, or was killed during execution. systemd marks the unit as failed and may prevent dependent services from starting.

## What This Error Means

systemd tracks the state of every service unit. When a service's main process exits abnormally (non-zero exit code), is killed by a signal, or times out, systemd transitions the unit to a `failed` state. The service will not automatically restart unless configured with `Restart=` in its unit file. System logs capture the failure reason in the journal.

## Common Causes

- Application bug or misconfiguration causing immediate crash
- Missing dependencies (libraries, config files, mount points)
- Insufficient permissions to access files or sockets
- Resource limits reached (memory, file descriptors, processes)
- Conflicting services or port already in use
- Corrupted service binary or installation

## How to Fix

### 1. Check Service Status

```bash
# View detailed status and recent logs
sudo systemctl status <service>.service

# Check if the service is enabled
sudo systemctl is-enabled <service>.service
```

### 2. Read the Journal Logs

```bash
# View full logs for the service
sudo journalctl -u <service>.service -n 50 --no-pager

# Follow logs in real-time
sudo journalctl -u <service>.service -f

# View logs since last boot
sudo journalctl -u <service>.service -b
```

### 3. Check Exit Code and Reason

```bash
# Show the last exit code
systemctl show <service>.service -p ExecMainStatus,Result,ActiveState

# Common exit codes:
# 0   - success (should not fail)
# 1   - generic error
# 2   - misusage of shell command
# 126 - command invoked cannot execute
# 127 - command not found
# 137 - killed by SIGKILL (OOM)
# 143 - killed by SIGTERM (graceful stop)
```

### 4. Verify Configuration

```bash
# Check service file syntax
sudo systemd-analyze verify /etc/systemd/system/<service>.service

# Check for config file errors
sudo <service-binary> --test-config

# Verify required files exist
ls -la /etc/<service>/
```

### 5. Fix Common Issues

```bash
# If the service needs a directory
sudo mkdir -p /var/lib/<service>
sudo chown <service-user>:<service-group> /var/lib/<service>

# If the service needs a mount
sudo mount -a

# If the service needs a network
sudo systemctl start network-online.target
```

### 6. Reset and Restart

```bash
# Reset failed state
sudo systemctl reset-failed <service>.service

# Restart the service
sudo systemctl start <service>.service

# Enable on boot
sudo systemctl enable <service>.service
```

### 7. Override Resource Limits

```bash
# Increase resource limits via override
sudo systemctl edit <service>.service

# Add to [Service] section:
# [Service]
# LimitNOFILE=65536
# LimitNPROC=4096
# MemoryMax=2G

sudo systemctl daemon-reload
sudo systemctl restart <service>.service
```

## Examples

```bash
$ sudo systemctl status nginx
● nginx.service - A high performance web server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled)
     Active: failed (Result: exit-code) since Mon 2025-07-14 08:00:00 UTC
    Process: 1234 ExecStart=/usr/sbin/nginx (code=exited, status=1/FAILURE)

$ sudo journalctl -u nginx -n 10
Jul 14 08:00:00 server nginx[1234]: nginx: [emerg] bind() to 0.0.0.0:80 failed (98: Address already in use)

$ sudo lsof -i :80
COMMAND  PID  USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
apache2 1200 root    4u  IPv4  12345      0t0  TCP *:http (LISTEN)

$ sudo systemctl stop apache2
$ sudo systemctl reset-failed nginx
$ sudo systemctl start nginx
```

```bash
$ sudo systemctl status myapp
● myapp.service - My Application
     Active: failed (Result: exit-code) since Mon 2025-07-14 09:00:00 UTC
    Process: 5678 ExecStart=/usr/local/bin/myapp (code=exited, status=127/NOTFOUND)

$ sudo journalctl -u myapp -n 5
Jul 14 09:00:00 server myapp[5678]: error while loading shared libraries: libfoo.so.2: cannot open shared object file

$ sudo apt install libfoo2
$ sudo systemctl reset-failed myapp
$ sudo systemctl start myapp
```

## Related Errors

- [systemd dependency failed]({{< relref "/os/linux/linux-systemd-dependency-v2" >}}) — Dependency chain failures
- [systemd timeout]({{< relref "/os/linux/linux-systemd-timeout-v2" >}}) — Service start timed out
- [Permission denied]({{< relref "/os/linux/permission-denied10" >}}) — Permission issues
