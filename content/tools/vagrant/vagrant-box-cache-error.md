---
title: "[Solution] Vagrant Box Cache Error"
description: "Fix Vagrant box cache errors when box metadata cannot be downloaded or updated."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vagrant Box Cache Error

Vagrant cannot update or access the box cache.

```
The box could not be found or could not be downloaded
```

## Common Causes

- Vagrant cloud unreachable
- Cached box metadata corrupted
- Network proxy blocking download
- Box version constraint not met
- Disk space full

## How to Fix

### Re-download Box Metadata

```bash
# Recheck box
vagrant box update --box ubuntu/jammy64

# List cached boxes
vagrant box list
```

### Remove Corrupted Cache

```bash
# Clear Vagrant cache
rm -rf ~/.vagrant.d/boxes/ubuntu-jammy64/

# Re-add box
vagrant box add ubuntu/jammy64
```

### Set Box Version

```ruby
# Vagrantfile
Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/jammy64"
  config.vm.box_version = "3.5.2"
end
```

### Check Disk Space

```bash
df -h ~/.vagrant.d/
```

### Use Custom Box URL

```ruby
config.vm.box = "custom-box"
config.vm.box_url = "https://example.com/custom.box"
```

## Examples

```bash
# Full box refresh workflow
vagrant box update --box ubuntu/jammy64
vagrant destroy -f
vagrant up
```
