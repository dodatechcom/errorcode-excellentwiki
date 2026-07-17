---
title: "[Solution] Linux Kernel Compilation Failed — Fix"
description: "Fix Linux kernel compilation errors. Resolve build failures, missing dependencies, and configuration issues when compiling the kernel."
platforms: ["linux"]
severities: ["error"]
error-types: ["runtime-error"]
tags: ["kernel-compile", "build-error", "compilation", "kernel-build", "make"]
weight: 5
---

# Linux: Kernel compilation failed

Kernel compilation errors occur when building the Linux kernel from source. These failures can result from missing build dependencies, incorrect kernel configuration, toolchain issues, or source code errors.

## Common Causes

- Missing build dependencies (gcc, make, flex, bison, libssl-dev)
- Incorrect kernel configuration (.config errors)
- Outdated toolchain (compiler too old for kernel version)
- Insufficient disk space during build
- Source code patching conflicts
- Architecture mismatch (cross-compilation issues)

## How to Fix

### 1. Install Build Dependencies

```bash
# Debian/Ubuntu
sudo apt build-dep linux
sudo apt install git fakeroot build-essential ncurses-dev xz-utils libssl-dev bc flex bison libelf-dev

# RHEL/CentOS/Fedora
sudo dnf builddep kernel
sudo dnf install ncurses-devel openssl-devel elfutils-libelf-devel flex bison
```

### 2. Clean the Build Tree

```bash
# Clean object files
make clean
make mrproper    # More thorough (removes .config)

# Start fresh
make clean && make mrproper
```

### 3. Fix Configuration Errors

```bash
# Use a known good configuration
make defconfig
# or
make olddefconfig    # Accept defaults for new options

# Or copy from an existing kernel
cp /boot/config-$(uname -r) .config
make olddefconfig
```

### 4. Check Toolchain Version

```bash
# Check compiler version
gcc --version

# Check required versions for your kernel
# Kernel 5.x: GCC 5.1+
# Kernel 6.x: GCC 5.1+, Clang 11+

# Install newer compiler if needed
sudo apt install gcc-12
```

### 5. Build with Less Parallelism

```bash
# Reduce parallelism to diagnose errors
make -j1

# Or use a fraction of CPUs
make -j$(nproc --all)
```

### 6. Fix Specific Compilation Errors

```bash
# Missing header errors
sudo apt install linux-headers-$(uname -r)

# Undefined references — check module dependencies
make modules_prepare

# Symbol errors — ensure .config has all dependencies
make olddefconfig
```

### 7. Increase Disk Space

```bash
# Check available space
df -h

# Kernel build requires 10-20GB free
# Clean temporary files
make clean

# Use a different build directory
mkdir ~/kernel-build
cd ~/kernel-build
```

### 8. Use ccache for Faster Rebuilds

```bash
sudo apt install ccache
export CC="ccache gcc"
make -j$(nproc)
```

## Examples

```bash
$ make -j$(nproc)
  HOSTLD  scripts/mod/modpost
/bin/sh: 1: flex: not found
make[1]: *** [/usr/src/linux/scripts/Makefile.host:9: scripts/lexer.lex.c] Error 127
make: *** [Makefile:653: scripts] Error 2

# Missing flex — install it
$ sudo apt install flex
$ make -j$(nproc)
```

```bash
$ make olddefconfig
.config:XXXX:warning: symbol value 'm' invalid for USB_NET_AX8817X

$ make defconfig
# Configuration written to .config
$ make -j$(nproc)
Kernel: arch/x86/boot/bzImage is ready
```

## Related Errors

- [Kernel module error]({{< relref "/os/linux/linux-kernel-module-error" >}}) — Module loading failures
- [Kernel Oops]({{< relref "/os/linux/linux-kernel-oops" >}}) — Kernel runtime bugs
- [Kernel tainted warning]({{< relref "/os/linux/linux-kernel-tainted" >}}) — Tainted kernel warnings
