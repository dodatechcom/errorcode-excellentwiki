---
title: "[Solution] Vagrant SSH Key Error"
description: "Fix Vagrant SSH key errors when SSH authentication to the VM fails."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
---

# Vagrant SSH Key Error

Vagrant cannot authenticate SSH connection to the VM.

```
Warning: Authentication failure. Reconnecting...
```

## Common Causes

- SSH key pair corrupted or missing
- VM not fully booted
- SSH service not running
- Key permissions wrong
- Incorrect SSH config

## How to Fix

### Regenerate SSH Keys

```bash
# Remove old keys
rm -f ~/.vagrant.d/insecure_private_key
rm -f .vagrant/machines/default/virtualbox/private_key

# Regenerate
vagrant ssh-config
```

### Check SSH Configuration

```bash
# View SSH config
vagrant ssh-config

# Test SSH manually
ssh -p 2222 -i .vagrant/machines/default/virtualbox/private_key vagrant@127.0.0.1
```

### Fix Key Permissions

```bash
chmod 600 .vagrant/machines/default/virtualbox/private_key
chmod 700 .vagrant
```

### Verify SSH Service

```bash
# Inside VM
sudo systemctl status sshd
sudo systemctl start sshd
```

### Use Password Authentication

```ruby
config.ssh.username = "vagrant"
config.ssh.password = "vagrant"
```

## Examples

```bash
# Force SSH key replacement
vagrant reload --provision

# Check if VM is accessible
ping 192.168.56.10
```
