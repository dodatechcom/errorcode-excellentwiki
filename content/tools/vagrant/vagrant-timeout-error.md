---
title: "[Solution] Vagrant Timeout Error"
description: "Fix Vagrant timeout errors when operations take too long to complete."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Vagrant Timeout Error

A Vagrant timeout error occurs when an operation exceeds the configured time limit.

## Why This Happens

- VM boot takes too long
- Network timeout during provisioning
- Box download too slow
- SSH connection timeout
- Provisioner script hanging

## Common Error Messages

- `vagrant_timeout_error`
- `vagrant_boot_timeout`
- `vagrant_ssh_timeout`
- `vagrant_provision_timeout`

## How to Fix It

### Solution 1: Increase Boot Timeout

```ruby
Vagrant.configure("2") do |config|
  config.vm.boot_timeout = 600
end
```

### Solution 2: Increase SSH Timeout

```ruby
config.ssh.connect_timeout = 120
config.ssh.forward_agent = false
```

### Solution 3: Optimize Provisioning

```ruby
config.vm.provision "shell", inline: <<-SHELL
  apt-get update
  apt-get install -y nginx
SHELL
```

### Solution 4: Check VM Resources

```bash
# Ensure enough CPU and memory
free -h
nproc
```

## Common Scenarios

- **Boot timeout:** Increase boot_timeout value
- **SSH timeout:** Check VM is accessible
- **Download timeout:** Use local box file

## Prevent It

- Set appropriate timeouts for your environment
- Use fast network connections
- Monitor VM resources during provision
