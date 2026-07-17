---
title: "[Solution] Linux ENXIO (errno 6) — No Such Device or Address Fix"
description: "Fix Linux ENXIO (errno 6) No Such Device or Address error. Solutions for missing device and invalid address issues."
platforms: ["linux"]
severities: ["error"]
error_types: ["os-error"]
weight: 5
---

# Linux ENXIO (errno 6) — No Such Device or Address

ENXIO (errno 6) means the requested device or address does not exist. This error occurs when you attempt to open a special device file that has no corresponding hardware driver, or when a network address cannot be resolved. It is distinct from ENOENT (errno 2) because ENXIO specifically refers to device or address references rather than general file absence.

## Common Causes

- Opening a device file for hardware that is not installed or recognized
- Attempting to access a serial port or disk device that does not exist
- Binding to a network address that is not configured on the system
- Using an invalid minor device number in an `open()` call

## How to Fix ENXIO

### 1. Verify Device Exists

Check if the device file you are trying to access actually exists:

```bash
ls -la /dev/sd* /dev/tty* /dev/video*
```

### 2. Check Loaded Kernel Modules

Confirm the kernel module for your device is loaded:

```bash
lsmod
```

Load the appropriate module if missing:

```bash
sudo modprobe <module_name>
```

### 3. Scan for Hardware Changes

Rescan the PCI bus for newly attached devices:

```bash
sudo rescan-scsi-bus
```

### 4. Verify Network Address Configuration

Ensure the network interface is up and the address is valid:

```bash
ip addr show
ping -c 1 <address>
```

## Verification

After fixing the issue, retry the operation that produced ENXIO. Verify the device is accessible:

```bash
ls -la /dev/<device_name>
```

## Related Error Codes

- [ENOENT (errno 2)](/os/linux/errno-2/) — No such file or directory
- [ENODEV (errno 19)](/os/linux/errno-19/) — No such device
- [EIO (errno 5)](/os/linux/errno-5/) — Input/output error
