---
title: "[Solution] Linux systemd Job Timeout — Service Start Timed Out"
description: "Fix Linux systemd 'Job timeout' and 'start timed out' errors. Resolve service startup timeouts and hung services."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Linux: systemd — Job timeout — service start timed out

The `A dependency job for <service>.service finished as failed` or `Job <service>.service/start timed out` error means systemd gave up waiting for a service to start within its configured timeout period. The default timeout is 90 seconds for most services.

## What This Error Means

When systemd starts a service, it expects the main process to fork and report readiness within a configurable timeout (`TimeoutStartSec=`). If the service hangs during startup — for example, waiting for a disk, network, or database that never responds — systemd kills the start job and marks it as failed. This can cascade and block other services that depend on it.

## Common Causes

- Service waiting for a network resource that is unreachable
- Slow disk I/O causing startup to stall
- Deadlock in the application during initialization
- Incorrect `Type=` setting (e.g., `Type=simple` when process forks early)
- Service trying to mount a filesystem that is not available
- Resource exhaustion preventing process creation

## How to Fix

### 1. Identify the Timed-Out Service

```bash
# Show failed jobs
systemctl --failed

# View timeout details in logs
sudo journalctl -u <service>.service -n 30 --no-pager

# Search for timeout messages
sudo journalctl --since '1 hour ago' | grep -i 'timed out\|timeout'
```

### 2. Increase the Timeout

```bash
# Edit the service override
sudo systemctl edit <service>.service

# Add or modify:
# [Service]
# TimeoutStartSec=300
# TimeoutStopSec=120

sudo systemctl daemon-reload
sudo systemctl restart <service>.service
```

### 3. Check What the Service Is Waiting For

```bash
# Check if it needs a filesystem
grep -E 'Requires=|After=' /etc/systemd/system/<service>.service

# Check if it needs network
sudo systemctl is-active network-online.target

# Check if it needs a database or external service
sudo journalctl -u <service>.service | grep -i 'connect\|waiting\|unable'
```

### 4. Fix Service Type Mismatch

```bash
# If the service forks but is configured as Type=simple
sudo systemctl edit <service>.service

# Change to:
# [Service]
# Type=forking

# Or if the service signals readiness via sd_notify:
# Type=notify
```

### 5. Check Resource Constraints

```bash
# Check available memory
free -h

# Check disk I/O
iostat -x 1 3

# Check available file descriptors
cat /proc/sys/fs/file-nr

# Check process limits
ulimit -a
```

### 6. Disable Timeout (Last Resort)

```bash
# Only for services that legitimately take long to start
sudo systemctl edit <service>.service

# Add:
# [Service]
# TimeoutStartSec=0

sudo systemctl daemon-reload
```

## Examples

```bash
$ sudo systemctl status postgresql
● postgresql.service - PostgreSQL
     Active: failed (Result: timeout) since Mon 2025-07-14 08:00:00 UTC
    Process: 1234 ExecStart=/usr/lib/postgresql/15/bin/pg_ctl start (code=exited, status=0/SUCCESS)

$ sudo journalctl -u postgresql -n 10
Jul 14 07:58:30 server pg_ctl[1234]: waiting for server to start....
Jul 14 08:00:00 server systemd[1]: postgresql.service: Start operation timed out. Terminating.

$ sudo systemctl edit postgresql
# [Service]
# TimeoutStartSec=300

$ sudo systemctl daemon-reload
$ sudo systemctl restart postgresql
```

## Related Errors

- [systemd failed to start]({{< relref "/os/linux/linux-systemd-failed-service-v2" >}}) — Service entry failed state
- [systemd dependency failed]({{< relref "/os/linux/linux-systemd-dependency-v2" >}}) — Dependency chain failures
- [NFS mount error]({{< relref "/os/linux/linux-nfs-mount-error" >}}) — Filesystem mount failures
