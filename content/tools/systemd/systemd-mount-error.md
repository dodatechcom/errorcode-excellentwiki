---
title: "[Solution] Systemd Mount Unit Failed Error — How to Fix"
description: "Fix systemd mount unit failures by verifying mount paths, checking filesystem types, resolving permission issues, and debugging automount configurations"
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
comments: true
---

# Systemd Mount Unit Failed Error

This error means a systemd mount unit failed to mount a filesystem. Mount units provide a declarative way to manage mount points, but they require the filesystem, device, and mount point to exist and be accessible.

## Why It Happens

- The device or network share specified in `What=` does not exist or is unreachable
- The mount point directory does not exist on the filesystem
- The filesystem type in `Type=` is incorrect or the required kernel module is not loaded
- The mount requires credentials (NFS, CIFS) and they are missing or wrong
- Another process is already using the mount point
- The mount point is not empty
- Required kernel modules (nfs, cifs) are not loaded
- The fstab entry conflicts with the systemd mount unit

## Common Error Messages

```
mnt-data.mount: Mount process exited with code=exited status=32
Failed to mount mnt-data.mount: Mount point does not exist.
```

```
mnt-backup.mount: Failed to run 'mount' command: No such device
```

```
mnt-nfs.mount: Mount request timed out.
```

## How to Fix It

### 1. Check Mount Unit Status

```bash
# Check the mount status
systemctl status mnt-data.mount

# View mount-related logs
journalctl -u mnt-data.mount -n 30

# List all mount units
systemctl list-units --type=mount
```

### 2. Verify the Mount Point Directory Exists

```bash
# Check if the mount point exists
ls -la /mnt/data

# Create it if missing
sudo mkdir -p /mnt/data
```

### 3. Test the Mount Manually

```bash
# Test mounting manually with the same parameters
# From the mount unit:
# What=/dev/sdb1
# Where=/mnt/data
# Type=ext4

sudo mount -t ext4 /dev/sdb1 /mnt/data

# For NFS mounts
sudo mount -t nfs server:/export /mnt/nfs

# For CIFS/SMB mounts
sudo mount -t cifs //server/share /mnt/smb -o username=user,password=pass
```

### 4. Fix the Mount Unit File

```ini
# /etc/systemd/system/mnt-data.mount
[Unit]
Description=Data Volume Mount
After=blockdev@dev-disk-by\x2duuid-abc123.target

[Mount]
What=/dev/disk/by-uuid/abc123-def456
Where=/mnt/data
Type=ext4
Options=defaults,noatime

[Install]
WantedBy=multi-user.target
```

### 5. Fix NFS Mount Units

```ini
# /etc/systemd/system/mnt-nfs.mount
[Unit]
Description=NFS Share Mount
After=network-online.target
Wants=network-online.target

[Mount]
What=nfs-server:/export
Where=/mnt/nfs
Type=nfs
Options=soft,timeo=10,retrans=3

[Install]
WantedBy=multi-user.target
```

```bash
# Ensure NFS client is installed
sudo apt install nfs-common

# Load required kernel modules
sudo modprobe nfs
sudo modprobe nfsd
```

### 6. Remove Conflicting fstab Entries

```bash
# Check if there are duplicate mount entries in fstab
grep '/mnt/data' /etc/fstab

# If both fstab and a systemd mount unit exist, remove the fstab entry
# or disable the systemd mount unit
sudo systemctl disable mnt-data.mount
```

## Common Scenarios

- **NFS server temporarily down**: The mount unit fails because the NFS server is unreachable. Add `x-systemd.mount-timeout=30` and `Retry=` options.
- **USB drive not connected**: An automount unit for a USB drive fails on boot. Use an automount unit with `TimeoutIdleSec=0` so it only mounts when accessed.
- **fstab and systemd conflict**: A mount is defined in both `/etc/fstab` and a systemd unit. Remove one to avoid conflicts.

## Prevent It

- Use `systemd-analyze verify` to validate mount unit files before deploying
- Ensure mount point directories exist before defining mount units
- Use `After=network-online.target` and `Wants=network-online.target` for network mounts

## Related Pages

- [Systemd Unit Failed](/tools/systemd/systemd-unit-failed)
- [Systemd Network Error](/tools/systemd/systemd-network-error)
- [Systemd Timeout Error](/tools/systemd/systemd-timeout-error)
