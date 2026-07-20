---
title: "[Solution] systemd network mount timeout"
description: "Fix systemd network mount timeout. Resolve mount failures for network filesystems (NFS, CIFS)."
tools: ["systemd"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# systemd network mount timeout

## Error Description

mnt-nfs.mount: Mount timed out. Network server is not responding.

The network mount could not be completed within the timeout.

## Common Causes

Common Causes:
- NFS server is unreachable
- Network interface is not ready when mount is attempted
- Firewall blocking NFS/CIFS ports
- DNS resolution failed for the server hostname

## How to Fix

How to Fix:
```bash
# Ensure network is ready before mount
sudo systemctl edit mnt-nfs.mount
```

```ini
[Unit]
After=network-online.target
Wants=network-online.target

[Mount]
What=nfs-server:/export
Where=/mnt/nfs
Type=nfs
Options=soft,timeo=10,retrans=3
```

## Examples

```bash
# Check systemd version
systemctl --version

# Verify unit file syntax
sudo systemd-analyze verify /etc/systemd/system/myapp.service

# Analyze system boot
systemd-analyze blame

# List failed units
systemctl --failed

# View service logs
journalctl -u myapp -n 50 --no-pager
```