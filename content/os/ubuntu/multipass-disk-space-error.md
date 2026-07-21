---
title: "Multipass VM Disk Space Error"
description: "Multipass VM runs out of disk space or cannot allocate more"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# Multipass VM Disk Space Error

Multipass VM runs out of disk space or cannot allocate more

## Common Causes

- VM disk image reached maximum size
- Host filesystem does not have enough space
- VM not configured with sufficient default disk size
- Old snapshots consuming disk space

## How to Fix

1. Check VM disk usage: `multipass exec <vm> -- df -h`
2. Resize VM disk: `multipass set local.vmnet-mtu=1500` (example)
3. Delete old VMs: `multipass delete <vm-name>`
4. Free host space: `multipass purge`

## Examples

```bash
# Check VM disk usage
multipass exec myvm -- df -h

# Delete unused VMs
multipass list
multipass delete oldvm
multipass purge
```
