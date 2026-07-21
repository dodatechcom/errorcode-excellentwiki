---
title: "[Solution] Ubuntu Server: kvm-storage-pool-error"
description: "Fix Ubuntu kvm-storage-pool-error. KVM storage pool fails or runs out of space."
os: ["ubuntu"]
error-types: ["os-error"]
severities: ["error"]
---
# KVM Storage Pool Error

KVM storage pool encounters errors or becomes full.

## Common Causes
- Storage pool path does not exist
- Pool out of space
- File permissions wrong
- Pool not started

## How to Fix
1. Check storage pools
```bash
sudo virsh pool-list --all
```
2. Check pool info
```bash
sudo virsh pool-info default
```
3. Rebuild pool if needed
```bash
sudo virsh pool-destroy default
sudo virsh pool-build default
sudo virsh pool-start default
```

## Examples
```bash
$ sudo virsh pool-list --all
 Name    State    Autostart
--------------------------------
 default inactive no
```