---
title: "[Solution] Vagrant VirtualBox DNS Error"
description: "Fix Vagrant VirtualBox DNS errors when the VM cannot resolve domain names."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Vagrant VirtualBox DNS Error

A Vagrant VirtualBox DNS error occurs when the VirtualBox VM cannot resolve DNS queries.

## Why This Happens

- DNS settings not passed to VM
- VirtualBox network adapter misconfigured
- Guest DNS resolver broken
- Host DNS not accessible from VM
- NetworkManager DNS conflicts

## Common Error Messages

- `vagrant_virtualbox_dns_error`
- `vagrant_dns_resolution_failed`
- `vagrant_virtualbox_dns_not_configured`
- `vagrant_guest_dns_broken`

## How to Fix It

### Solution 1: Configure DNS Manually

```ruby
Vagrant.configure("2") do |config|
  config.vm.network "private_network", ip: "192.168.56.10"

  config.vm.post_up_message = "Configure DNS in /etc/resolv.conf"
end
```

### Solution 2: Set DNS in Provisioner

```ruby
config.vm.provision "shell", inline: <<-SHELL
  echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
  echo "nameserver 8.8.4.4" | sudo tee -a /etc/resolv.conf
SHELL
```

### Solution 3: Use DNS Plugin

```bash
vagrant plugin install vagrant-dns
```

### Solution 4: Check Network Adapter

```bash
# On guest
cat /etc/resolv.conf
ping -c 1 google.com
```

## Common Scenarios

- **No DNS in VM:** Set DNS manually
- **Intermittent DNS:** Check NetworkManager
- **Slow DNS resolution:** Use faster DNS servers

## Prevent It

- Configure DNS in Vagrantfile provisioner
- Use reliable DNS servers
- Test DNS after vagrant up
