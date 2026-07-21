---
title: "[Solution] Vagrant Network Unreachable"
description: "Fix Vagrant network unreachable errors when the host-only or private network is not accessible."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Vagrant Network Unreachable

A Vagrant network unreachable error occurs when the host cannot reach the guest machine on configured networks.

## Why This Happens

- Host-only adapter not created
- Firewall blocking traffic
- IP address conflict
- Network interface down
- VirtualBox network driver issue

## Common Error Messages

- `vagrant_network_unreachable`
- `vagrant_host_network_unreachable`
- `vagrant_private_network_failed`
- `vagrant_network_adapter_error`

## How to Fix It

### Solution 1: Verify Network Config

```ruby
Vagrant.configure("2") do |config|
  config.vm.network "private_network", ip: "192.168.56.10"
end
```

### Solution 2: Check Adapter Status

```bash
ip addr show vboxnet0
ifconfig vboxnet0
```

### Solution 3: Recreate Network

Destroy and recreate the VM to reset networking:

```bash
vagrant destroy -f
vagrant up
```

### Solution 4: Configure Firewall

Allow traffic on the host-only interface:

```bash
# Linux
sudo iptables -I INPUT -i vboxnet0 -j ACCEPT

# macOS
sudo pfctl -f /etc/pf.conf
```

## Common Scenarios

- **Cannot ping guest:** Check adapter creation
- **Intermittent connectivity:** Check IP conflicts
- **Slow network:** Adjust VirtualBox adapter type

## Prevent It

- Use consistent IP addresses
- Avoid IP ranges used by other services
- Test connectivity after vagrant up
