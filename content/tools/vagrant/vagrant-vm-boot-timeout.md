---
title: "[Solution] Vagrant VM Boot Timeout"
description: "Fix Vagrant VM boot timeout errors when the virtual machine takes too long to start."
tools: ["vagrant"]
error-types: ["tool-error"]
severities: ["error"]
weight: 5
---

# Vagrant VM Boot Timeout

A Vagrant VM boot timeout error occurs when the VM fails to start within the configured time limit.

## Why This Happens

- Insufficient host resources
- Heavy I/O on host disk
- VM configured with too much memory
- VirtualBox snapshot corruption
- BIOS/UEFI virtualization disabled

## Common Error Messages

- `vagrant_vm_boot_timeout`
- `vagrant_boot_timeout_exceeded`
- `vagrant_vm_startup_failed`
- `vagrant_virtualbox_boot_error`

## How to Fix It

### Solution 1: Increase Boot Timeout

```ruby
Vagrant.configure("2") do |config|
  config.vm.boot_timeout = 600
end
```

### Solution 2: Reduce VM Resources

```ruby
config.vm.provider "virtualbox" do |vb|
  vb.memory = "512"
  vb.cpus = 1
end
```

### Solution 3: Check Host Resources

```bash
free -h
nproc
iostat -x 1 3
```

### Solution 4: Delete Stale Snapshots

```bash
VBoxManage snapshot "VM_NAME" delete "snapshot-name"
```

## Common Scenarios

- **Slow boot on old hardware:** Increase timeout
- **Boot fails after snapshot:** Delete snapshots
- **Resource contention:** Close other VMs

## Prevent It

- Use minimal resource allocation for development
- Avoid unnecessary snapshots
- Monitor host resource usage
