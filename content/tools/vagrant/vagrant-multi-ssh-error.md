---
title: "[Solution] Vagrant Multi SSH Error"
description: "Fix Vagrant multi-SSH errors when connecting to multiple VMs in a multi-machine environment."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Vagrant Multi SSH Error

A Vagrant multi-SSH error occurs when SSH connections to specific VMs in a multi-machine setup fail.

## Why This Happens

- VM name not specified correctly
- VM not running
- Port conflict between VMs
- SSH config not regenerated
- Multi-machine state inconsistent

## Common Error Messages

- `vagrant_multi_ssh_error`
- `vagrant_ssh_machine_not_found`
- `vagrant_ssh_machine_not_running`
- `vagrant_ssh_port_conflict`

## How to Fix It

### Solution 1: Specify Machine Name

```bash
vagrant ssh web-server
vagrant ssh db-server
```

### Solution 2: Check Machine Status

```bash
vagrant status
vagrant status web-server
```

### Solution 3: Start Specific Machine

```bash
vagrant up web-server
vagrant ssh web-server
```

### Solution 4: Configure Multi-Machine

```ruby
Vagrant.configure("2") do |config|
  config.vm.define "web" do |web|
    web.vm.box = "ubuntu/focal64"
    web.vm.network "forwarded_port", guest: 80, host: 8080
  end

  config.vm.define "db" do |db|
    db.vm.box = "ubuntu/focal64"
    db.vm.network "forwarded_port", guest: 3306, host: 33060
  end
end
```

## Common Scenarios

- **Machine not found:** Check VM names in Vagrantfile
- **Port conflict:** Use different forwarded ports
- **State mismatch:** Run vagrant status to check

## Prevent It

- Use descriptive VM names
- Allocate unique ports per VM
- Start VMs in correct order
