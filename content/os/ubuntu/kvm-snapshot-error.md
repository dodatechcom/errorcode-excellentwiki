---
title: "KVM Snapshot Creation Error"
description: "Failed to create or restore VM snapshots"
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---

# KVM Snapshot Creation Error

Failed to create or restore VM snapshots

## Common Causes

- VM has snapshot-reverting disk format (qcow2 required)
- Insufficient disk space for snapshot
- VM is in inconsistent state
- Snapshot chain too deep or corrupted

## How to Fix

1. Convert disk to qcow2: `qemu-img convert -O qcow2 source.img dest.qcow2`
2. Check disk space: `df -h /var/lib/libvirt/images/`
3. List snapshots: `virsh snapshot-list <vm>`
4. Delete old snapshots: `virsh snapshot-delete <vm> <snap-name>`

## Examples

```bash
# List VM snapshots
virsh snapshot-list myvm

# Create snapshot
virsh snapshot-create-as myvm snap1 "First snapshot"

# Delete snapshot
virsh snapshot-delete myvm snap1
```
