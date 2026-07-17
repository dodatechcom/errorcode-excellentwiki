---
title: "[Solution] Linux modprobe Module Not Found — Fix"
description: "Fix Linux 'modprobe: module not found' errors. Locate kernel modules, resolve dependencies, and load drivers correctly."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["modprobe", "kernel-module", "module-not-found", "driver", "insmod", "kernel"]
weight: 5
---

# Linux: modprobe: module not found

The `modprobe: FATAL: Module <name> not found` error means the kernel module you are trying to load does not exist in the module tree. This can mean the module is not built, not installed, the name is wrong, or the kernel version does not match the installed modules.

## What This Error Means

Kernel modules are kernel extensions stored in `/lib/modules/$(uname -r)/`. The `modprobe` command searches this directory tree to find and load the requested module along with its dependencies. When the module file is missing from this directory, modprobe fails. This commonly happens after kernel updates, when extra module packages aren't installed, or when building custom modules.

## Common Causes

- Module name is misspelled or case-insensitive
- Kernel module package not installed (e.g., `linux-modules-extra`)
- Kernel updated but not rebooted (module tree mismatch)
- Module not compiled (feature disabled in kernel config)
- Module loaded but under a different name
- Module built for a different kernel version
- DKMS module not rebuilt after kernel update

## How to Fix

### 1. Search for the Module

```bash
# Search for the module in the module tree
find /lib/modules/$(uname -r) -name "*<module-name>*"

# Check if the module exists with a different name
modprobe -l | grep <module-name>

# List all available modules
ls /lib/modules/$(uname -r)/kernel/drivers/
```

### 2. Install the Module Package

```bash
# Debian/Ubuntu — install kernel module extras
sudo apt install linux-modules-extra-$(uname -r)

# Install a specific module package
sudo apt install <module-package-name>

# For DKMS-managed modules (e.g., VirtualBox, ZFS)
sudo apt install dkms
sudo dkms install <module>/<version>
```

### 3. Check Kernel Version

```bash
# Check current kernel
uname -r

# Check if the module exists for a different kernel
ls /lib/modules/ | sort

# If you just updated the kernel, reboot
sudo reboot
```

### 4. Load the Module by Full Path

```bash
# Find the module file
find /lib/modules/$(uname -r) -name "*<module-name>*"

# Load it directly with insmod
sudo insmod /path/to/module.ko
```

### 5. Build the Module from Source

```bash
# Install kernel headers
sudo apt install linux-headers-$(uname -r)

# Download and build the module
git clone <module-source-url>
cd <module-source>
make
sudo make install

# Load the built module
sudo modprobe <module-name>
```

### 6. Enable the Module in Kernel Config

If compiling your own kernel:

```bash
# Check if the module is disabled
grep <MODULE_NAME> /boot/config-$(uname -r)

# Enable it as a module (=m) or built-in (=y)
```

### 7. Install Additional Hardware Drivers

```bash
# Ubuntu: check for proprietary drivers
ubuntu-drivers devices
sudo ubuntu-drivers autoinstall

# RHEL/Fedora: check for available firmware
sudo dnf install *firmware*
```

## Examples

```bash
$ sudo modprobe nvidia
modprobe: FATAL: Module nvidia not found in directory /lib/modules/5.15.0-91-generic

$ ls /lib/modules/5.15.0-91-generic/kernel/drivers/video/nvidia
ls: cannot access: No such file or directory

$ sudo apt install nvidia-driver-535
$ sudo modprobe nvidia
# Module loaded successfully
```

```bash
$ sudo modprobe vboxdrv
modprobe: FATAL: Module vboxdrv not found

$ sudo apt install virtualbox-dkms
$ sudo dkms install vboxhost/6.1.38
$ sudo modprobe vboxdrv
# Success
```

## Related Errors

- [Kernel Oops]({{< relref "/os/linux/linux-kernel-oops" >}}) — Module-triggered kernel bugs
- [Kernel tainted warning]({{< relref "/os/linux/linux-kernel-tainted" >}}) — Tainted kernel from third-party modules
- [Kernel compile error]({{< relref "/os/linux/linux-kernel-compile-error" >}}) — Building kernel modules from source
