---
title: "[Solution] Linux systemd Dependency Failed for multi-user.target"
description: "Fix Linux systemd 'Dependency failed for multi-user.target' errors. Resolve service dependency chains and target failures."
platforms: ["linux"]
severities: ["error"]
error-types: ["system-error"]
weight: 5
---

# Linux: systemd — Dependency failed for multi-user.target

The `Dependency failed for multi-user.target` error means a required service or mount that `multi-user.target` depends on has failed. `multi-user.target` is the default runlevel for multi-user systems — when it fails, many services that should start at boot will not launch.

## What This Error Means

`multi-user.target` is a systemd target that represents a non-graphical, multi-user system. It is the target most servers and headless systems boot into. If any service marked with `WantedBy=multi-user.target` or required by it fails during boot, systemd may fail to reach this target, causing cascading service failures across the system.

## Common Causes

- Network mount (NFS, CIFS) failing to connect at boot
- Required network target (`network-online.target`) not reached
- Disk or filesystem errors preventing mounts
- A critical service like `sshd` or `chronyd` failing to start
- SELinux policy blocking service startup
- fstab entries with `nofail` missing or misconfigured

## How to Fix

### 1. Identify the Failed Dependency

```bash
# Show all failed units
systemctl --failed

# Check multi-user.target status
systemctl status multi-user.target

# View the full dependency tree
systemctl list-dependencies multi-user.target
```

### 2. Read Boot Logs

```bash
# View boot messages for failures
sudo journalctl -b | grep -i 'failed\|error\|dependency'

# Check what failed before multi-user.target
sudo journalctl -b -p err

# Timeline of the boot sequence
systemd-analyze blame
```

### 3. Fix the Root Cause

```bash
# If a mount failed
sudo systemctl status <mount-unit>.mount
sudo journalctl -u <mount-unit>.mount

# If network is not ready
sudo systemctl restart NetworkManager
# or
sudo systemctl restart systemd-networkd

# If sshd failed
sudo journalctl -u sshd
sudo sshd -t          # Test configuration syntax
sudo systemctl restart sshd
```

### 4. Check and Fix fstab

```bash
# Verify fstab entries mount correctly
sudo mount -a

# Check for errors
sudo fsck -n /dev/sda1

# Add nofail to non-critical mounts
sudo nano /etc/fstab
# Add 'nofail' option to prevent blocking boot
```

### 5. Relax Dependencies

```bash
# Edit a service to not block multi-user.target
sudo systemctl edit <service>.service

# Change WantedBy to weak dependency:
# [Install]
# WantedBy=multi-user.target

# Or remove After= for non-essential ordering
sudo systemctl daemon-reload
```

### 6. Mask a Non-Critical Failed Service

```bash
# Prevent a broken service from blocking boot
sudo systemctl mask <non-critical-service>.service

# Unmask later when fixed
sudo systemctl unmask <non-critical-service>.service
```

## Examples

```bash
$ systemctl --failed
  UNIT                        LOAD   ACTIVE SUB    DESCRIPTION
● remote-data.mount           loaded failed failed Remote NFS mount
● multi-user.target           loaded failed failed Multi-User System

$ sudo systemctl status remote-data.mount
● remote-data.mount - Remote NFS mount
     Active: failed (Result: exit-code)
     Where: /mnt/data
     What: nfsserver:/export/data

$ sudo mount /mnt/data
$ sudo systemctl start multi-user.target
$ systemctl status multi-user.target
● multi-user.target - Multi-User System
     Active: active since Mon 2025-07-14 10:00:00 UTC
```

## Related Errors

- [systemd failed to start]({{< relref "/os/linux/linux-systemd-failed-service-v2" >}}) — Service entry failed state
- [systemd timeout]({{< relref "/os/linux/linux-systemd-timeout-v2" >}}) — Service start timed out
- [NFS mount error]({{< relref "/os/linux/linux-nfs-mount-error" >}}) — NFS mount failures
