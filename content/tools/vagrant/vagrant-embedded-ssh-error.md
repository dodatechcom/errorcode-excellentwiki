---
title: "[Solution] Vagrant Embedded SSH Error"
description: "Fix Vagrant embedded SSH errors when Vagrant's built-in SSH client encounters issues."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Vagrant Embedded SSH Error

A Vagrant embedded SSH error occurs when Vagrant's built-in Net::SSH library fails to connect or authenticate.

## Why This Happens

- SSH key not generated
- Known hosts file conflict
- SSH agent forwarding issues
- Corrupted SSH key pair
- Incompatible SSH algorithm

## Common Error Messages

- `vagrant_embedded_ssh_error`
- `vagrant_ssh_key_not_found`
- `vagrant_ssh_known_hosts_error`
- `vagrant_ssh_algorithm_mismatch`

## How to Fix It

### Solution 1: Regenerate SSH Keys

Delete and regenerate Vagrant's SSH keys:

```bash
rm ~/.vagrant.d/insecure_private_key
vagrant up
```

### Solution 2: Configure SSH Client

Specify the SSH executable in Vagrantfile:

```ruby
Vagrant.configure("2") do |config|
  config.ssh.executable = "/usr/bin/ssh"
  config.ssh.forward_agent = false
end
```

### Solution 3: Clear Known Hosts

Remove stale entries from known_hosts:

```bash
ssh-keygen -R "[127.0.0.1]:2222"
ssh-keygen -R "[localhost]:2222"
```

### Solution 4: Use System SSH

Disable Vagrant's embedded SSH:

```bash
export VAGRANT_PREFER_SYSTEM_SPISSH=1
vagrant up
```

## Common Scenarios

- **Key not found:** Regenerate insecure key
- **Known hosts conflict:** Clear stale entries
- **Agent forwarding failed:** Disable or configure agent

## Prevent It

- Keep Vagrant and plugins updated
- Avoid manual SSH key manipulation
- Use consistent SSH configuration
