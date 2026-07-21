---
title: "[Solution] Vagrant NFS Mount Error"
description: "Fix Vagrant NFS mount errors when NFS shared folders fail to mount."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vagrant NFS Mount Error

Vagrant NFS shared folders fail to mount in the VM.

```
Mounting NFS shared folders failed
```

## Common Causes

- NFS server not running on host
- NFS client not installed in VM
- Firewall blocking NFS ports
- /etc/exports misconfigured
- UID/GID mismatch

## How to Fix

### Configure NFS Sync

```ruby
Vagrant.configure("2") do |config|
  config.vm.synced_folder ".", "/vagrant", type: "nfs"
end
```

### Start NFS Server on Host

```bash
# macOS
sudo nfsd start

# Linux
sudo systemctl start nfs-server
sudo systemctl enable nfs-server
```

### Install NFS Client in VM

```bash
# Inside VM (Debian/Ubuntu)
sudo apt install nfs-common

# Inside VM (RHEL/CentOS)
sudo yum install nfs-utils
```

### Fix /etc/exports

```bash
# On host - add NFS export
echo '/path/to/share 192.168.56.0/24 -alldirs -maproot=0:0' | sudo tee -a /etc/exports
sudo nfsd restart
```

### Use NFS with Options

```ruby
config.vm.synced_folder ".", "/vagrant", type: "nfs",
  mount_options: ["actimeo=1", "nolock"]
```

### Fix Firewall

```bash
# macOS
sudo pfctl -ef /etc/pf.conf

# Linux
sudo ufw allow 2049/tcp
```

## Examples

```ruby
# Full NFS configuration
Vagrant.configure("2") do |config|
  config.vm.synced_folder ".", "/vagrant", type: "nfs",
    mount_options: ["actimeo=1"],
    linux__nfs_options: ["async", "subtree_check"]
end
```
