---
title: "[Solution] Vagrant Insecure Base Box Warning"
description: "Fix Vagrant insecure base box warnings about default insecure keypairs being used."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["warning"]
weight: 5
---

# Vagrant Insecure Base Box Warning

A Vagrant insecure base box warning appears when a box uses the default insecure keypair for SSH authentication.

## Why This Happens

- Box ships with default insecure keys
- Box has not been customized on first boot
- Box maintainer did not regenerate keys
- Using an older or community-contributed box

## Common Error Messages

- `vagrant_insecure_key_warning`
- `vagrant_insecure_base_box`
- `vagrant_default_key_detected`
- `vagrant_ssh_insecure_key`

## How to Fix It

### Solution 1: Let Vagrant Replace Keys

Vagrant automatically replaces insecure keys on first boot:

```bash
vagrant destroy -f
vagrant up
```

### Solution 2: Generate New Keys Manually

```bash
# On the guest
ssh-keygen -f /home/vagrant/.ssh/id_rsa -N ""
cat /home/vagrant/.ssh/id_rsa.pub >> /home/vagrant/.ssh/authorized_keys
```

### Solution 3: Use Official Boxes

Official Vagrant boxes are maintained with secure keys:

```ruby
config.vm.box = "ubuntu/focal64"
```

### Solution 4: Disable Key Replacement

If you need to keep the original keys:

```ruby
Vagrant.configure("2") do |config|
  config.ssh.insert_key = false
end
```

## Common Scenarios

- **Warning on first boot:** Normal behavior, keys will be replaced
- **Warning persists:** Destroy and recreate the VM
- **Custom keys needed:** Generate and distribute your own keys

## Prevent It

- Use official Vagrant boxes when possible
- Keep boxes updated to latest versions
- Regenerate keys after importing custom boxes
