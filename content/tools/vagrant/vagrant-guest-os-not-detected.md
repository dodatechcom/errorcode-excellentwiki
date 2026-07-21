---
title: "[Solution] Vagrant Guest OS Not Detected Error"
description: "Fix Vagrant guest OS detection errors when the VM cannot determine the operating system."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vagrant Guest OS Not Detected Error

Vagrant cannot detect the guest operating system in the VM.

```
Vagrant was unable to detect an installed guest OS
```

## Common Causes

- Guest Additions not installed
- Incorrect box configuration
- Corrupted VM image
- VirtualBox version mismatch
- Custom box without proper metadata

## How to Fix

### Specify Guest Type

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.guest = :ubuntu
end
```

### Install Guest Additions

```bash
# Inside VM
sudo apt update
sudo apt install -y virtualbox-guest-utils virtualbox-guest-dkms
sudo reboot
```

### Use vagrant-vbguest Plugin

```bash
vagrant plugin install vagrant-vbguest

# Vagrantfile
config.vbguest.auto_update = true
```

### Check Box Metadata

```bash
# Verify box metadata
cat ~/.vagrant.d/boxes/ubuntu-jammy64/*/metadata.json
```

### Use Correct Base Box

```ruby
# Use official HashiCorp box
config.vm.box = "ubuntu/jammy64"
config.vm.box_version = "3.5.2"
```

## Examples

```ruby
# Full guest configuration
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.guest = :ubuntu
  
  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "2048"
  end
end
```
