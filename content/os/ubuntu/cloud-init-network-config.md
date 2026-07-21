---
title: "Cloud-Init Network Configuration Error"
description: "Cloud-init fails to configure network interfaces on first boot"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Cloud-Init Network Configuration Error

Cloud-init fails to configure network interfaces on first boot

## Common Causes

- Network configuration format not supported by renderer
- Conflicting network config between cloud-init and netplan
- DHCP not available on network segment
- Static IP configuration missing required fields

## How to Fix

1. Check network config: `cat /etc/netplan/50-cloud-init.yaml`
2. View cloud-init network logs: `grep -i network /var/log/cloud-init.log`
3. Regenerate config: `sudo cloud-init clean && sudo cloud-init init`
4. Verify netplan syntax: `sudo netplan --debug generate`

## Examples

```bash
# Check cloud-init network config
cat /etc/netplan/50-cloud-init.yaml

# Check cloud-init logs for network issues
grep -i network /var/log/cloud-init.log

# Regenerate network configuration
sudo netplan generate
sudo netplan apply
```
