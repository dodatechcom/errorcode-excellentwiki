---
title: "[Solution] Linux systemd Dependency Failed — Service Dependency Fix"
description: "Fix Linux systemd 'Dependency failed for <service>' errors. Resolve service dependency chains and boot-order issues."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Linux: systemd — Dependency failed for

The `Dependency failed for <service>.service` error means a required dependency of the service did not start successfully. systemd uses a dependency tree to determine the order in which services start — if a prerequisite service fails, dependent services are automatically stopped or prevented from starting.

## Common Causes

- Required network target failed (network unavailable)
- Required filesystem mount failed (disk or NFS issue)
- Another service that is a dependency failed to start
- Hardware dependency not met (device not found)
- Loop dependency between services
- `After=` or `Requires=` order misconfiguration

## How to Fix

### 1. Check the Dependency Chain

```bash
# View which dependencies failed
sudo systemctl list-dependencies <service>.service

# Show reverse dependencies (what depends on this service)
sudo systemctl list-dependencies <service>.service --reverse

# Check active/failed state of all dependencies
systemctl list-dependencies <service>.service | grep -E '\.service|\.mount|\.target' | while read dep; do
  sudo systemctl is-active "$dep" 2>/dev/null
done
```

### 2. Identify the Root Cause

```bash
# Show failed units
systemctl --failed

# Check logs of the failed dependency
sudo journalctl -u <failed-dependency>.service

# Check the dependency chain for the root failure
sudo journalctl -b | grep -i "dependency failed"
```

### 3. Fix the Failed Dependency

```bash
# If a mount dependency failed
sudo systemctl status <mount>.mount
sudo journalctl -u <mount>.mount

# Fix the mount (e.g., NFS, disk)
sudo mount -a
sudo systemctl restart <mount>.mount

# If a network target failed
sudo systemctl status NetworkManager.service
sudo systemctl restart NetworkManager
```

### 4. Modify Service Dependencies

Edit the service file:

```bash
sudo systemctl edit <service>.service
```

Change dependency types:

```ini
[Unit]
Description=My Service
# Change from Requires= to Wants= (weaker dependency)
Wants=network-online.target
After=network-online.target

# Or add a fallback
Requires=local-fs.target
After=local-fs.target
```

### 5. Remove Circular Dependencies

```bash
# Check for circular dependencies
sudo systemd-analyze verify /etc/systemd/system/*.service

# Remove the circular reference in the unit files
# Example: Service A requires B, B requires A
# Change one to Wants= instead of Requires= or remove the dependency
```

### 6. Use systemd-analyze for Boot Analysis

```bash
# View the boot chain
systemd-analyze critical-chain

# Plot the dependency graph
systemd-analyze plot > boot.svg

# Verify all unit files for syntax errors
systemd-analyze verify /etc/systemd/system/<service>.service
```

### 7. Disable the Service Temporarily

```bash
# Mask the service (prevents it from starting)
sudo systemctl mask <service>.service

# Unmask when ready
sudo systemctl unmask <service>.service
```

## Examples

```bash
$ sudo systemctl status myservice.service
● myservice.service - My Application
     Loaded: loaded (/etc/systemd/system/myservice.service; enabled)
     Active: failed (Result: dependency) since Thu 2025-06-15 10:00:00 UTC
    Process: 1234 ExecStart=/usr/bin/myapp (code=exited, status=0/SUCCESS)

$ systemctl --failed
  UNIT                        LOAD   ACTIVE SUB    DESCRIPTION
● remote-data.mount           loaded failed failed Remote data mount
● myservice.service           loaded failed failed My Application

$ sudo systemctl status remote-data.mount
● remote-data.mount - Remote data mount
     Loaded: loaded
     Active: failed (Result: exit-code)
     Where: /mnt/data
     What: nfsserver:/export/data

$ sudo mount /mnt/data
$ sudo systemctl start myservice.service
● myservice.service - My Application
     Active: active (running)
```

## Related Errors

- [systemd failed to start]({{< relref "/os/linux/systemd-failed" >}}) — Service start failures
- [systemd timeout]({{< relref "/os/linux/linux-systemd-timeout" >}}) — Service timeout issues
- [NFS mount error]({{< relref "/os/linux/linux-nfs-mount-error" >}}) — Filesystem mount failures
