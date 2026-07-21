---
title: "[Solution] Vagrant NFS Server Error"
description: "Fix Vagrant NFS server errors when NFS-mounted shared folders fail to mount."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Vagrant NFS Server Error

A Vagrant NFS server error occurs when the NFS service fails to export or mount shared folders.

## Why This Happens

- NFS server not installed
- NFS service not running
- Exports file misconfigured
- Firewall blocking NFS ports
- macOS NFS daemon conflicts

## Common Error Messages

- `vagrant_nfs_server_error`
- `vagrant_nfs_export_failed`
- `vagrant_nfs_mount_failed`
- `vagrant_nfs_not_installed`

## How to Fix It

### Solution 1: Install NFS Server

```bash
# Ubuntu/Debian
sudo apt-get install nfs-kernel-server

# macOS (built-in)
sudo nfsd start
```

### Solution 2: Configure NFS Export

```ruby
Vagrant.configure("2") do |config|
  config.vm.synced_folder ".", "/vagrant", type: "nfs"
end
```

### Solution 3: Start NFS Service

```bash
# Linux
sudo systemctl start nfs-kernel-server
sudo systemctl enable nfs-kernel-server

# macOS
sudo nfsd start
```

### Solution 4: Configure Firewall

```bash
sudo ufw allow from 192.168.56.0/24 to any port nfs
```

## Common Scenarios

- **Mount timeout:** Check NFS service status
- **Permission denied:** Verify exports file
- **macOS conflict:** Restart nfsd service

## Prevent It

- Install NFS dependencies before vagrant up
- Use fixed IPs for NFS exports
- Test NFS mounts manually first
