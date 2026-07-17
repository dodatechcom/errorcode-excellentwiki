---
title: "[Solution] macOS UTM/VMware Fusion Error"
description: "Fix virtualization errors on Mac when UTM or VMware Fusion VMs fail to start, show kernel errors, or have performance issues."
platforms: ["macos"]
severities: ["error"]
error-types: ["runtime-error"]
weight: 5
---

# macOS UTM/VMware Fusion Error Fix

VM errors include VMs failing to start, "Hypervisor Framework error," slow performance, or VMs crashing during boot. Common with UTM (QEMU-based) and VMware Fusion.

## What This Error Means

macOS virtualization uses the Hypervisor Framework. Errors can occur due to insufficient resources, permission issues, or incompatible VM configurations.

## Common Causes

- Insufficient RAM or CPU cores allocated to VM
- Virtualization not enabled in security settings
- VM disk image corrupted
- Hypervisor Framework permission denied
- macOS version incompatible with VM software version

## How to Fix

### 1. Check virtualization permissions

```bash
# System Preferences - Security & Privacy - Privacy - Hypervisor
# Ensure your VM app has permission
# Or check if virtualization is restricted
```

### 2. Verify VM resources

```bash
# Check available system resources
sysctl hw.memsize | awk '{print $2/1073741824 " GB RAM"}'
sysctl hw.ncpu
```

### 3. Reset VM preferences

```bash
# UTM: Delete VM state and reimport
# VMware: Delete .vmwarevm state files

# UTM preferences
defaults delete com.utmapp.UTM

# VMware preferences
defaults delete com.vmware.fusion
```

### 4. Check hypervisor framework

```bash
# Verify hypervisor framework is available
ls /System/Library/Frameworks/Hypervisor.framework

# Check VM logs
log show --predicate 'subsystem == "com.apple.Hypervisor"' --last 1h
```

## Related Errors

- [Parallels Error](macos-parallels-error) — Parallels Desktop issues
- [Rosetta Error](macos-rosetta-error) — Intel app translation
- [Boot Error](macos-boot-error) — system boot issues
