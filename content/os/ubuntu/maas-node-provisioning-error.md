---
title: "MAAS Node Provisioning Error"
description: "MAAS node fails to provision with operating system"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# MAAS Node Provisioning Error

MAAS node fails to provision with operating system

## Common Causes

- Commissioning timeout or failure
- Disk partitioning error on target node
- Network boot (PXE) not working
- Operating system image not downloaded

## How to Fix

1. Check node status: `maas admin machine read <system-id>`
2. Verify PXE: check TFTP server and DHCP
3. View commissioning logs: `maas admin machine commission <system-id>`
4. Check available images: `maas admin boot-resources read`

## Examples

```bash
# Check node status in MAAS
maas admin machine read <system-id>

# Commission node
maas admin machine commission <system-id>

# Check available boot resources
maas admin boot-resources read
```
