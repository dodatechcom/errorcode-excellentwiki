---
title: "[Solution] Vagrant DNS Resolution Error"
description: "Fix Vagrant DNS resolution errors when the VM cannot resolve domain names."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vagrant DNS Resolution Error

Vagrant VM cannot resolve domain names.

```
Temporary failure in name resolution
```

## Common Causes

- DNS not configured for private network
- /etc/resolv.conf missing or wrong
- Host DNS server not accessible
- Network mode does not support DNS
- Firewall blocking DNS traffic

## How to Fix

### Configure DNS in Vagrantfile

```ruby
Vagrant.configure("2") do |config|
  config.vm.network "private_network", ip: "192.168.56.10"
  
  # Custom DNS
  config.vm.network "private_network", ip: "192.168.56.10", 
    dns: "8.8.8.8"
end
```

### Fix resolv.conf

```bash
# Inside VM
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
echo "nameserver 8.8.4.4" | sudo tee -a /etc/resolv.conf
```

### Use Public DNS Servers

```bash
# Set DNS permanently
sudo rm /etc/resolv.conf
echo "nameserver 8.8.8.8
nameserver 8.8.4.4
nameserver 1.1.1.1" | sudo tee /etc/resolv.conf
```

### Configure Network Manager

```bash
# If using NetworkManager
sudo nmcli device modify eth0 ipv4.dns "8.8.8.8 8.8.4.4"
sudo nmcli device reapply eth0
```

### Use Vagrant DNS Plugin

```bash
vagrant plugin install vagrant-dns
```

## Examples

```ruby
# Full network configuration with DNS
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.network "private_network", ip: "192.168.56.10"
  
  config.vm.provision "shell", inline: <<-SHELL
    echo "nameserver 8.8.8.8" > /etc/resolv.conf
  SHELL
end
```
