---
title: "[Solution] Linux systemd Job Timeout — Service Start Fix"
description: "Fix Linux systemd 'Job <service>.service/start timed out' errors. Adjust timeout settings and resolve hanging services."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Linux: systemd — Job timed out

The `Job <service>.service/start timed out` error means systemd gave up waiting for a service to start. Services that hang during startup, require hardware that's not responding, or have long initialization times can exceed systemd's default timeout (usually 90 seconds).

## Common Causes

- Service process hangs during initialization
- Network mount or remote filesystem not responding
- Hardware device not ready (disk, network card)
- Service script performs a blocking operation
- Timeout value set too low for the service
- System overloaded during boot (too many parallel services)

## How to Fix

### 1. Check the Service Status

```bash
# View detailed service status
sudo systemctl status <service>.service

# Check if it's still running or truly hung
ps aux | grep <service>

# View logs for the timed-out service
sudo journalctl -u <service>.service
```

### 2. Increase the Service Timeout

Edit the service unit file:

```bash
sudo systemctl edit <service>.service
```

Add:

```ini
[Service]
TimeoutStartSec=300
TimeoutStopSec=120
```

Then reload and restart:

```bash
sudo systemctl daemon-reload
sudo systemctl restart <service>.service
```

### 3. Check for Hanging Mounts

```bash
# List all mounts and their state
mount | grep -E 'nfs|cifs|fuse'

# Check for unresponsive mounts
df -h 2>&1 | grep -i "stale\|timeout"

# Remount with shorter timeouts
sudo mount -o remount,soft,intr,timeo=30 /mount/point
```

### 4. Disable Services That Are Not Required

```bash
# List all enabled services
systemctl list-unit-files --state=enabled

# Disable unnecessary services
sudo systemctl disable <unnecessary-service>.service
```

### 5. Analyze Boot Time

```bash
# View boot performance overview
systemd-analyze

# View detailed service startup time
systemd-analyze blame | head -20

# View the critical chain (longest boot path)
systemd-analyze critical-chain
```

### 6. Adjust Global Timeout Defaults

```bash
# Edit the systemd config
sudo nano /etc/systemd/system.conf

# Uncomment and set:
# DefaultTimeoutStartSec=300
# DefaultTimeoutStopSec=300

# Apply changes
sudo systemctl daemon-reexec
```

### 7. Check for Failed Dependencies

```bash
# View full dependency tree
systemctl list-dependencies <service>.service

# Check each dependency
for dep in $(systemctl list-dependencies <service>.service | tail -n +2); do
  systemctl is-active "$dep" 2>/dev/null || echo "$dep is not active"
done
```

### 8. Investigate Boot-time Blocking

```bash
# Check for kernel messages during boot
dmesg | grep -E 'blocked|timeout|hung'

# Use systemd-analyze to spot long-running jobs
systemd-analyze plot > boot.svg
# View boot.svg in a browser
```

## Examples

```bash
$ sudo systemctl status network-remote.service
● network-remote.service - Remote Network Mount
     Loaded: loaded (/etc/systemd/system/network-remote.service; enabled)
     Active: failed (Result: timeout) since Thu 2025-06-15 10:00:00 UTC
    Process: 1234 ExecStart=/usr/bin/mount-nfs.sh (code=killed, signal=TERM)
   Main PID: 1234 (code=killed, signal=TERM)

$ sudo journalctl -u network-remote.service
Jun 15 10:00:00 server systemd[1]: network-remote.service: start operation timed out. Terminating.
Jun 15 10:00:00 server systemd[1]: network-remote.service: Failed with result 'timeout'.

$ systemd-analyze blame | head -5
  1min 30s network-remote.service
    12.345s postgresql.service
     5.678s networking.service
```

## Related Errors

- [systemd failed to start]({{< relref "/os/linux/systemd-failed" >}}) — Service startup failures
- [systemd dependency failed]({{< relref "/os/linux/linux-systemd-dependency" >}}) — Dependency resolution errors
- [NFS not responding]({{< relref "/os/linux/nfs-error" >}}) — Remote filesystem timeouts
