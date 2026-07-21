---
title: "Multipass VM Launch Error"
description: "Multipass fails to create and launch a new VM instance"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Multipass VM Launch Error

Multipass fails to create and launch a new VM instance

## Common Causes

- Hypervisor (KVM, Hyper-V, VirtualBox) not available
- Insufficient disk space for VM image
- VM name already exists
- Cloud-init configuration error

## How to Fix

1. Check hypervisor: `multipass get --local.driver`
2. Check disk: `df -h /var/snap/multipass/`
3. List existing: `multipass list`
4. Try different image: `multipass launch --name myvm 22.04`

## Examples

```bash
# Check Multipass driver
multipass get --local.driver

# Launch with specific resources
multipass launch --name myvm --cpus 2 --memory 2G --disk 20G 22.04

# List existing VMs
multipass list
```
