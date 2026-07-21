---
title: "[Solution] Vagrant No Such Host Error"
description: "Fix Vagrant no such host errors when the host machine name cannot be resolved."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Vagrant No Such Host Error

A Vagrant no such host error occurs when the hostname used to connect to the VM cannot be resolved.

## Why This Happens

- DNS not configured for the VM
- /etc/hosts not updated
- Hostname not set in Vagrantfile
- Network not ready when connecting
- DNS plugin not functioning

## Common Error Messages

- `vagrant_no_such_host_error`
- `vagrant_hostname_not_found`
- `vagrant_dns_resolution_failed`
- `vagrant_host_not_resolvable`

## How to Fix It

### Solution 1: Set Hostname

```ruby
Vagrant.configure("2") do |config|
  config.vm.hostname = "my-vm.local"
end
```

### Solution 2: Update /etc/hosts

Add the VM entry manually:

```bash
echo "192.168.56.10 my-vm.local" | sudo tee -a /etc/hosts
```

### Solution 3: Use IP Address

Connect using IP instead of hostname:

```bash
vagrant ssh-config
ssh -F ssh-config default
```

### Solution 4: Install DNS Plugin

```bash
vagrant plugin install vagrant-hostmanager
```

## Common Scenarios

- **Cannot resolve hostname:** Add entry to /etc/hosts
- **SSH fails with hostname:** Use IP address
- **DNS plugin broken:** Reinstall the plugin

## Prevent It

- Configure DNS before vagrant up
- Use hostmanager for multi-VM setups
- Document hostnames for team members
