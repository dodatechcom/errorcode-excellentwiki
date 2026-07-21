---
title: "[Solution] Vagrant Forwarded Port Error"
description: "Fix Vagrant forwarded port errors when port forwarding between host and VM fails."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vagrant Forwarded Port Error

Vagrant port forwarding fails and host cannot reach VM services.

```
Vagrant cannot forward the configured ports
```

## Common Causes

- Host port already occupied
- VM network not properly configured
- Firewall blocking port
- VirtualBox networking issue
- Port protocol mismatch

## How to Fix

### Configure Port Forwarding

```ruby
Vagrant.configure("2") do |config|
  config.vm.network "forwarded_port", guest: 80, host: 8080
  config.vm.network "forwarded_port", guest: 443, host: 8443
  config.vm.network "forwarded_port", guest: 22, host: 2222, id: "ssh"
end
```

### Check Host Port Availability

```bash
lsof -i :8080
ss -tlnp | grep 8080
```

### Use Different Port Range

```ruby
# Use high port range to avoid conflicts
config.vm.network "forwarded_port", guest: 80, host: 10080
config.vm.network "forwarded_port", guest: 443, host: 10443
```

### Disable Firewall Temporarily

```bash
# On host
sudo ufw disable
# Or allow specific port
sudo ufw allow 8080/tcp
```

### Forward UDP Ports

```ruby
config.vm.network "forwarded_port", guest: 53, host: 5353, protocol: "udp"
```

## Examples

```ruby
# Complete port forwarding setup
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  
  config.vm.network "forwarded_port", guest: 80, host: 8080, auto_correct: true
  config.vm.network "forwarded_port", guest: 443, host: 8443, auto_correct: true
  config.vm.network "forwarded_port", guest: 3306, host: 33060
  config.vm.network "forwarded_port", guest: 6379, host: 63790
end
```
