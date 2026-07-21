---
title: "[Solution] Vagrant Box Not Found"
description: "Fix box not found errors when running vagrant up."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vagrant Box Not Found

Fix box not found errors when running vagrant up. This error occurs when Vagrant encounters virtual machine, configuration, or provider problems.

## Common Causes

- Incorrect Vagrantfile configuration
- Provider not installed or misconfigured
- Network or synced folder issues
- Virtual machine resource constraints

## How to Fix

### Solution 1: Check Vagrantfile Syntax

Validate your Vagrantfile Ruby syntax:

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.network "forwarded_port", guest: 80, host: 8080
end
```

### Solution 2: Verify Provider

```bash
# Check available providers
vagrant status

# Verify provider is installed
vagrant plugin list
```

### Solution 3: Debug with Verbose Output

```bash
vagrant up --debug
```

The `--debug` flag provides detailed logging for troubleshooting.

## Example

```ruby
# Vagrantfile example
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"
  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
    vb.cpus = 2
  end
end
```

## Related Links

- [Vagrant Documentation](https://www.vagrantup.com/docs)
- [Vagrant Troubleshooting](https://www.vagrantup.com/docs/troubleshooting)
