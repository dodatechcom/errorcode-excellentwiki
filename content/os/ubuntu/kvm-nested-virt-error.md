---
title: "KVM Nested Virtualization Error"
description: "Nested virtualization not working inside KVM guest"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# KVM Nested Virtualization Error

Nested virtualization not working inside KVM guest

## Common Causes

- Nested virtualization not enabled for KVM module
- CPU type does not support nested virt
- Module parameter not set for nested=1
- Guest hypervisor requires specific CPU flags

## How to Fix

1. Check: `cat /sys/module/kvm_intel/parameters/nested` (should be Y or 1)
2. Enable: `echo options kvm_intel nested=1 | sudo tee /etc/modprobe.d/kvm-intel.conf`
3. Reload module: `sudo modprobe -r kvm_intel && sudo modprobe kvm_intel`
4. Verify CPU flags: `grep -E '(vmx|svm)' /proc/cpuinfo`

## Examples

```bash
# Check nested virtualization status
cat /sys/module/kvm_intel/parameters/nested

# Enable nested virtualization
echo 'options kvm_intel nested=1' | sudo tee /etc/modprobe.d/kvm-intel.conf

# Reload KVM module
sudo modprobe -r kvm_intel && sudo modprobe kvm_intel
```
