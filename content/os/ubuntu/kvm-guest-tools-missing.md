---
title: "KVM Guest Tools Missing Error"
description: "Virtual machine missing virtio drivers and guest agents"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# KVM Guest Tools Missing Error

Virtual machine missing virtio drivers and guest agents

## Common Causes

- virtio drivers not installed in Windows guest
- qemu-guest-agent not installed in Linux guest
- SPICE agent not running for clipboard sharing
- Guest tools cause high CPU usage

## How to Fix

1. Install guest agent (Linux): `sudo apt-get install qemu-guest-agent`
2. Install VirtIO drivers (Windows): download from Fedora project
3. Check agent status: `virsh qemu-agent-command <vm> '{"execute":"guest-info"}'`
4. Disable unnecessary agents to reduce CPU usage

## Examples

```bash
# Install guest agent in Linux VM
sudo apt-get install qemu-guest-agent
sudo systemctl enable --now qemu-guest-agent

# Check guest agent status from host
virsh qemu-agent-command myvm '{"execute":"guest-info"}'
```
