---
title: "[Solution] Vagrant Not Supported Provider Error"
description: "Fix Vagrant not supported provider errors when the requested provider is unavailable."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Vagrant Not Supported Provider Error

A Vagrant not supported provider error occurs when the requested VM provider is not installed or supported.

## Why This Happens

- Provider plugin not installed
- Provider not available on host OS
- Provider version incompatible
- Wrong provider specified
- Provider dependencies missing

## Common Error Messages

- `vagrant_provider_not_supported`
- `vagrant_provider_not_installed`
- `vagrant_provider_plugin_missing`
- `vagrant_provider_os_incompatible`

## How to Fix It

### Solution 1: Install Provider Plugin

```bash
# VirtualBox (usually built-in)
vagrant plugin install vagrant-virtualbox

# VMware
vagrant plugin install vagrant-vmware-desktop

# Hyper-V (Windows only)
# Built-in on Windows Pro/Enterprise
```

### Solution 2: Check Available Providers

```bash
vagrant status --provider=virtualbox
```

### Solution 3: Configure Provider

```ruby
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "1024"
  end
end
```

### Solution 4: Verify Provider Installation

```bash
VBoxManage --version  # For VirtualBox
vmrun list            # For VMware
```

## Common Scenarios

- **VMware not found:** Install VMware Fusion/Workstation
- **Hyper-V unavailable:** Use Windows Pro/Enterprise
- **Plugin missing:** Install required plugin

## Prevent It

- Install provider before vagrant up
- Use the --provider flag to specify
- Check provider compatibility with box
