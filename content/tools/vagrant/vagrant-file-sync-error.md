---
title: "[Solution] Vagrant File Sync Error"
description: "Fix Vagrant file sync errors when synced folders fail to mount or transfer files."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vagrant File Sync Error

Vagrant synced folders fail to mount or sync correctly.

```
Failed to mount folders: mount: unknown filesystem type 'vboxsf'
```

## Common Causes

- Guest Additions version mismatch
- VirtualBox shared folder module not loaded
- Incorrect mount options
- Path contains special characters
- Permission denied on mount point

## How to Fix

### Update Guest Additions

```bash
# Update VirtualBox Guest Additions
vagrant plugin install vagrant-vbguest
vagrant reload
```

### Use rsync Instead

```ruby
config.vm.synced_folder ".", "/vagrant", type: "rsync"
```

### Fix vboxsf Mount

```bash
# Inside VM
sudo modprobe vboxsf
sudo mount -t vboxsf -o uid=1000,gid=1000 default /vagrant
```

### Use NFS Sync

```ruby
config.vm.synced_folder ".", "/vagrant", type: "nfs", mount_options: ["actimeo=1"]
```

### Check Guest Additions

```bash
# Inside VM
lsmod | grep vbox
# Should show vboxsf
```

### Set Correct Permissions

```ruby
config.vm.synced_folder ".", "/vagrant", 
  owner: "vagrant", 
  group: "vagrant",
  mount_options: ["dmode=775", "fmode=664"]
```

## Examples

```ruby
# Multiple sync types
Vagrant.configure("2") do |config|
  config.vm.synced_folder ".", "/vagrant", type: "rsync"
  config.vm.synced_folder "./data", "/data", type: "virtualbox"
end
```
