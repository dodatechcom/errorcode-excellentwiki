---
title: "Multipass VM Network Error"
description: "Multipass VM cannot obtain network connection or has no internet access"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Multipass VM Network Error

Multipass VM cannot obtain network connection or has no internet access

## Common Causes

- Multipass network bridge not created
- VM network interface not configured
- DNS resolution failing inside VM
- Host firewall blocking VM traffic

## How to Fix

1. Check Multipass network: `multipass networks`
2. Restart Multipass: `sudo systemctl restart multipass`
3. Check VM IP: `multipass info <vm-name>`
4. Configure DNS in VM: `sudo nano /etc/netplan/50-cloud-init.yaml`

## Examples

```bash
# Check Multipass networks
multipass networks

# Get VM info
multipass info myvm

# Restart Multipass service
sudo systemctl restart multipass
```
