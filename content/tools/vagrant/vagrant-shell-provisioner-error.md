---
title: "[Solution] Vagrant Shell Provisioner Error"
description: "Fix Vagrant shell provisioner errors when inline or path-based scripts fail."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vagrant Shell Provisioner Error

Vagrant shell provisioner fails to execute scripts in the VM.

```
The following SSH command responded with a non-zero exit status
```

## Common Causes

- Script has syntax errors
- Missing executable permission
- Script path incorrect
- Command requires sudo but not provided
- Script assumes interactive shell

## How to Fix

### Use Inline Script

```ruby
config.vm.provision "shell", inline: <<-SHELL
  apt-get update
  apt-get install -y nginx
  systemctl start nginx
SHELL
```

### Use External Script

```bash
# Make script executable
chmod +x scripts/provision.sh
```

```ruby
config.vm.provision "shell", path: "scripts/provision.sh"
```

### Handle Script Errors

```ruby
config.vm.provision "shell", inline: <<-SHELL
  set -e  # Exit on error
  apt-get update
  apt-get install -y nginx
SHELL
```

### Use Privileged Execution

```ruby
# Run as root (default)
config.vm.provision "shell", inline: "apt-get update"

# Run as vagrant user
config.vm.provision "shell", inline: "whoami", privileged: false
```

### Pass Arguments to Script

```ruby
config.vm.provision "shell", path: "scripts/setup.sh", args: ["--env", "production"]
```

## Examples

```ruby
# Complete provisioner setup
Vagrant.configure("2") do |config|
  config.vm.provision "shell", inline: <<-SHELL
    set -euxo pipefail
    export DEBIAN_FRONTEND=noninteractive
    apt-get update -qq
    apt-get install -y -qq nginx
    systemctl enable nginx
    systemctl start nginx
  SHELL
end
```
