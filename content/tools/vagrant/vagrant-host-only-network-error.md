---
title: "[Solution] Vagrant Host Only Network Error"
description: "Fix Vagrant host-only network errors when private network interfaces fail to create."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vagrant Host Only Network Error

Vagrant cannot create or configure host-only network interfaces.

```
Failed to create host-only network adapter
```

## Common Causes

- VirtualBox host-only adapter limit reached
- Network interface name conflict
- VirtualBox version mismatch
- IP address conflict
- NetworkManager managing the interface

## How to Fix

### Configure Host-Only Network

```ruby
Vagrant.configure("2") do |config|
  config.vm.network "private_network", ip: "192.168.56.10"
end
```

### Remove Old Interfaces

```bash
# List VirtualBox host-only networks
VBoxManage list hostonlyifs

# Remove unused interface
VBoxManage hostonlyif remove " vboxnet0"
```

### Fix IP Conflicts

```ruby
# Use unique IP for each VM
config.vm.network "private_network", ip: "192.168.56.10"

# Second VM
config.vm.network "private_network", ip: "192.168.56.11"
```

### Disable NetworkManager

```bash
# On host - add interface to NetworkManager ignore list
echo "ignore-vboxnet0" | sudo tee /etc/NetworkManager/conf.d/99-vagrant.conf
sudo systemctl restart NetworkManager
```

### Check VirtualBox Version

```bash
VBoxManage --version
# Ensure compatible with Vagrant
```

## Examples

```ruby
# Multiple private networks
Vagrant.configure("2") do |config|
  config.vm.network "private_network", ip: "192.168.56.10"
  config.vm.network "private_network", ip: "192.168.57.10"
end
```
