---
title: "KVM Virt-Manager Display Error"
description: "Unable to open graphical console for VM in virt-manager"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# KVM Virt-Manager Display Error

Unable to open graphical console for VM in virt-manager

## Common Causes

- QEMU guest agent not installed in VM
- SPICE/VNC server not configured correctly
- Display backend (QXL, VirtIO GPU) not available
- Missing display libraries: spice-gtk, virt-viewer

## How to Fix

1. Install viewer: `sudo apt-get install virt-viewer`
2. Check VM display config: `virsh dumpxml <vm> | grep graphics`
3. Install guest agent: `sudo apt-get install qemu-guest-agent`
4. Try connecting via SPICE: `remote-viewer spice://localhost:5900`

## Examples

```bash
# Check VM graphics settings
virsh dumpxml myvm | grep -A5 graphics

# Install virt-viewer
sudo apt-get install virt-viewer

# Connect to VM console
virt-viewer -c qemu:///system myvm
```
