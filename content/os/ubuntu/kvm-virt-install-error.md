---
title: "Virt-Install Command Error"
description: "virt-install fails to create new virtual machine"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Virt-Install Command Error

virt-install fails to create new virtual machine

## Common Causes

- Disk image path does not exist or wrong permissions
- Insufficient disk space for virtual disk
- Network bridge not available
- ISO media not accessible or invalid

## How to Fix

1. Check disk space: `df -h /var/lib/libvirt/images/`
2. Verify ISO: `file /path/to/iso`
3. Check available networks: `virsh net-list`
4. Create disk image: `qemu-img create -f qcow2 /var/lib/libvirt/images/vm.qcow2 20G`

## Examples

```bash
# Create VM with virt-install
virt-install --name myvm \
  --ram 2048 \
  --vcpus 2 \
  --disk path=/var/lib/libvirt/images/myvm.qcow2,size=20 \
  --os-variant ubuntu22.04 \
  --network bridge=virbr0 \
  --cdrom /var/lib/libvirt/images/ubuntu-22.04.iso
```
