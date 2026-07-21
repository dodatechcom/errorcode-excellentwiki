---
title: "[Solution] Vagrant Auto Correct Port Error"
description: "Fix Vagrant auto-correct port conflicts when forwarded ports are already in use."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Vagrant Auto Correct Port Error

Vagrant fails to auto-correct port conflicts when host ports are occupied.

```
Vagrant cannot forward the configured ports
```

## Common Causes

- Host port already in use by another process
- Multiple Vagrant VMs using same forwarded port
- Port range exhausted
- Auto-correct disabled in configuration
- Stale port mappings from crashed VM

## How to Fix

### Configure Auto-Correct

```ruby
# Vagrantfile
Vagrant.configure("2") do |config|
  config.vm.network "forwarded_port", guest: 80, host: 8080, auto_correct: true
end
```

### Find Conflicting Ports

```bash
# Check what is using the port
lsof -i :8080
netstat -tlnp | grep 8080
ss -tlnp | grep 8080
```

### Kill Conflicting Process

```bash
# Find and kill process using port
lsof -ti :8080 | xargs kill -9
```

### Use Different Port

```ruby
config.vm.network "forwarded_port", guest: 80, host: 9090
```

### Free Up Vagrant Ports

```bash
# Destroy old VMs
vagrant destroy -f old-vm

# Check running VMs
vagrant status
vagrant global-status --prune
```

## Examples

```ruby
# Multiple port forwarding with auto-correct
Vagrant.configure("2") do |config|
  config.vm.network "forwarded_port", guest: 80, host: 8080, auto_correct: true
  config.vm.network "forwarded_port", guest: 443, host: 8443, auto_correct: true
  config.vm.network "forwarded_port", guest: 3000, host: 3000, auto_correct: true
end
```
