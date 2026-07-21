---
title: "[Solution] Vagrant Disk Size Error"
description: "Fix Vagrant disk size errors when the VM disk is too small or cannot be resized."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vagrant Disk Size Error

Vagrant VM runs out of disk space and cannot be resized.

```
No space left on device
```

## Common Causes

- Default disk size too small
- Disk resize not supported by provider
- VirtualBox disk format incompatible
- Partition not expanded after resize
- Snapshot preventing resize

## How to Fix

### Set Disk Size in Vagrantfile

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyhd", :id, "--resize", 40960]  # 40GB
  end
end
```

### Use vagrant-disksize Plugin

```bash
vagrant plugin install vagrant-disksize
```

```ruby
config.disksize.size = "50GB"
```

### Resize VirtualBox Disk

```bash
# Find disk file
VBoxManage showhdinfo /path/to/disk.vdi

# Resize (must destroy VM first or remove snapshots)
VBoxManage modifyhd /path/to/disk.vdi --resize 40960
```

### Expand Partition After Resize

```bash
# Inside VM
sudo growpart /dev/sda 1
sudo resize2fs /dev/sda1
# or
sudo growpart /dev/sda 1 && sudo xfs_growfs /
```

### Check Available Space

```bash
df -h
lsblk
```

## Examples

```ruby
# Disk size with provider
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.disksize.size = "40GB"
  
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "4096"
    vb.cpus = 2
  end
end
```
