---
title: "[Solution] Vagrant Network IP Conflict Error"
description: "Fix Vagrant network IP conflicts when two VMs or networks use the same IP address."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vagrant Network IP Conflict Error

Vagrant reports IP address conflict during network configuration.

```
There is already an IP in that network
```

## Common Causes

- Two VMs using same private network IP
- Host machine using the IP range
- IP overlaps with DHCP range
- Previous VM not fully cleaned up
- Static IP in conflicting range

## How to Fix

### Assign Unique IPs

```ruby
# VM 1
Vagrant.configure("2") do |config|
  config.vm.network "private_network", ip: "192.168.56.10"
end

# VM 2
Vagrant.configure("2") do |config|
  config.vm.network "private_network", ip: "192.168.56.11"
end
```

### Check Used IPs

```bash
# List VirtualBox host-only networks
VBoxManage list hostonlyifs

# Check IP assignments
ip addr show | grep 192.168
```

### Remove Conflicting Interface

```bash
VBoxManage list hostonlyifs
VBoxManage hostonlyif remove vboxnet0
```

### Use Different IP Range

```ruby
# Use a range not used on the host
config.vm.network "private_network", ip: "10.0.0.10"
```

### Avoid DHCP Range

```ruby
# Do not use IPs in DHCP range
# Default DHCP: 192.168.56.100 - 192.168.56.200
config.vm.network "private_network", ip: "192.168.56.10"
```

## Examples

```ruby
# Multiple VMs with unique IPs
Vagrant.configure("2") do |config|
  config.vm.define "web" do |web|
    web.vm.network "private_network", ip: "192.168.56.10"
  end
  
  config.vm.define "db" do |db|
    db.vm.network "private_network", ip: "192.168.56.11"
  end
end
```
