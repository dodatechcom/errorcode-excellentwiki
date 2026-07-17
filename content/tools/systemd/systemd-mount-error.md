---
title: "systemd Mount Error"
description: "systemd mount unit fails to mount a filesystem."
tools: ["systemd"]
error-types: ["runtime-error"]
severities: ["error"]
weight: 5
---

# systemd Mount Error

A systemd mount error occurs when a mount unit fails to mount a filesystem. systemd manages mount points through `.mount` units that correspond to `/etc/fstab` entries.

## Common Causes

- Device or network share not available
- Mount point directory does not exist
- Filesystem type not supported
- fstab entry syntax errors
- Missing mount options

## How to Fix

### Check Mount Status

```bash
systemctl status mymount.mount
systemctl list-units --type=mount
```

### Verify Mount Configuration

```ini
# /etc/systemd/system/mymount.mount
[Unit]
Description=My Network Mount

[Mount]
What=//server/share
Where=/mnt/share
Type=cifs
Options=credentials=/etc/samba/creds,uid=1000,gid=1000

[Install]
WantedBy=multi-user.target
```

### Ensure Mount Point Exists

```bash
sudo mkdir -p /mnt/share
```

### Check Device Availability

```bash
ls -la /dev/sdb1
# Or for network mounts
ping server
```

### Fix fstab Entry

```bash
# Check fstab syntax
sudo mount -a
# This will show errors in fstab
```

### Debug Mount Issues

```bash
systemd-analyze verify mymount.mount
journalctl -u mymount.mount -n 20
```

## Examples

```bash
systemctl status data.mount
data.mount: Mount process exited with code=exited, status=32

# Fix: check device exists
ls -la /dev/sdb1
# Or check network mount
mount -t cifs //server/share /mnt/share
```

## Related Errors

- [Unit Start Failed]({{< relref "/tools/systemd/systemd-unit-error" >}}) — unit start failure
- [Dependency Failed]({{< relref "/tools/systemd/dependency-failed" >}}) — dependency issue
