---
title: "[Solution] Vagrant Provisioner Order Error"
description: "Fix Vagrant provisioner ordering errors when provisioners run in wrong sequence."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["warning"]
---

# Vagrant Provisioner Order Error

Vagrant provisioners execute in wrong order causing dependency failures.

```
Ansible playbook failed because package was not installed yet
```

## Common Causes

- Shell provisioner should run before Ansible
- Package installation order matters
- Provisioner depends on previous output
- run: "always" vs run: "once" conflict
- No explicit ordering defined

## How to Fix

### Order Provisioners Explicitly

```ruby
Vagrant.configure("2") do |config|
  # First: system setup
  config.vm.provision "shell", path: "scripts/setup.sh"
  
  # Second: install packages
  config.vm.provision "shell", path: "scripts/packages.sh"
  
  # Third: configure application
  config.vm.provision "shell", path: "scripts/configure.sh"
end
```

### Use Provisioner Flags

```ruby
# Only run specific provisioner
vagrant provision --provision-with shell

# Run in order
vagrant provision
```

### Mark Provisioners

```ruby
config.vm.provision "shell", name: "setup", path: "setup.sh"
config.vm.provision "shell", name: "packages", path: "packages.sh"
```

### Use run Option

```ruby
# Run only on first up
config.vm.provision "shell", path: "setup.sh", run: "once"

# Run always
config.vm.provision "shell", path: "config.sh", run: "always"
```

### Conditionally Run Provisioner

```ruby
config.vm.provision "shell", path: "optional.sh", run: "never"
# Run manually with: vagrant provision --provision-with shell
```

## Examples

```ruby
# Full provisioner pipeline
Vagrant.configure("2") do |config|
  config.vm.provision "shell", path: "scripts/base.sh", run: "once"
  config.vm.provision "shell", path: "scripts/docker.sh", run: "once"
  config.vm.provision "ansible" do |ansible|
    ansible.playbook = "playbook.yml"
  end
end
```
