---
title: "KVM PCI Passthrough Error"
description: "PCI device passthrough to VM fails with VFIO errors"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# KVM PCI Passthrough Error

PCI device passthrough to VM fails with VFIO errors

## Common Causes

- IOMMU not enabled in BIOS/UEFI
- Device driver not unbound from host kernel
- VFIO-PCI module not loaded
- Device ACS not supported for IOMMU grouping

## How to Fix

1. Check IOMMU: `dmesg | grep -i iommu`
2. Enable IOMMU: add `intel_iommu=on` or `amd_iommu=on` to kernel params
3. Unbind device: `echo <BDF> > /sys/bus/pci/devices/<BDF>/driver/unbind`
4. Bind to VFIO: `echo vfio-pci > /sys/bus/pci/devices/<BDF>/driver_override`

## Examples

```bash
# Check IOMMU status
dmesg | grep -i iommu

# List IOMMU groups
for g in $(find /sys/kernel/iommu_groups/* -maxdepth 0 -type d | sort -V); do
    echo "IOMMU Group ${g##*/}:"
    lspci -nns ${g##*/}:*;
done
```
